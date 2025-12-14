from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import database
import training
import optimization

router = APIRouter()

# Modelos de datos
class TrainingData(BaseModel):
    texto: str
    categoria: str

class ChatRequest(BaseModel):
    mensaje: str
    tipo_usuario: str = "estudiante"

class CareerInfoRequest(BaseModel):
    carrera: str

# Respuestas contextuales por tipo de usuario
SYSTEM_MESSAGES = {
    "estudiante": "Soy tu asistente de orientación vocacional. Te ayudaré a descubrir la carrera perfecta según tus intereses y habilidades.",
    "visitante": "¡Bienvenido! Soy tu guía virtual para explorar las opciones de carrera disponibles. ¿En qué área te interesa trabajar?"
}

FOLLOW_UP_QUESTIONS = [
    "¿Qué te gustaría hacer en tu carrera profesional?",
    "¿Cuáles son tus principales habilidades?",
    "¿Prefieres trabajar con personas, números o tecnología?",
    "¿Te interesa el sector público, privado o emprendimiento?",
    "¿Qué problema del mundo te gustaría resolver?"
]

@router.post("/entrenar")
def endpoint_entrenar(data: TrainingData):
    """Entrena el modelo con nuevos datos."""
    database.insert_data(data.texto, data.categoria)
    result = training.train_basic_model()
    return result

@router.post("/optimizar")
def endpoint_optimizar():
    """Optimiza el modelo con mejores hiperparámetros."""
    result = optimization.train_optimized_model()
    return result

@router.post("/chat")
def endpoint_chat(request: ChatRequest):
    """
    Procesa el mensaje del usuario y proporciona recomendaciones de carrera.
    Utiliza tanto el modelo ML como búsqueda de palabras clave.
    """
    mensaje = request.mensaje.strip().lower()
    tipo_usuario = request.tipo_usuario
    
    # Registrar la consulta en la base de datos
    database.insert_consultation(tipo_usuario, request.mensaje)
    
    # Buscar carrera por palabras clave
    carrera_keywords = training.find_matching_career(mensaje)
    
    # Intentar predecir con el modelo
    pred, prob = training.predict_category(request.mensaje)
    
    # Lógica de respuesta mejorada
    if pred is None:
        respuesta = (
            "📚 El modelo aún se está entrenando. Por favor, comparte tus intereses "
            "para ayudarte mejor. ¿Qué te apasiona?"
        )
        carrera_recomendada = None
    elif carrera_keywords:
        # Usar la carrera encontrada por palabras clave (más confiable)
        respuesta = generar_respuesta_personalizada(carrera_keywords, tipo_usuario, prob)
        carrera_recomendada = carrera_keywords
    elif prob > 0.5:
        # Usar predicción del modelo si tiene alta confianza
        respuesta = generar_respuesta_personalizada(pred, tipo_usuario, prob)
        carrera_recomendada = pred
    else:
        # Baja confianza: pedir más información
        respuesta = (
            f"📖 No estoy completamente seguro de tu orientación. "
            f"Te sugiero que pienses en qué tipo de trabajo te interesa más. "
            f"¿Prefieres trabajar con tecnología, personas, números o algo creativo?"
        )
        carrera_recomendada = None
    
    # Actualizar la base de datos con la recomendación
    if carrera_recomendada:
        database.insert_consultation(tipo_usuario, request.mensaje, carrera_recomendada)
    
    return {
        "respuesta": respuesta,
        "carrera_recomendada": carrera_recomendada,
        "confianza": round(prob, 2) if prob else 0
    }

def generar_respuesta_personalizada(carrera, tipo_usuario, confianza):
    """Genera una respuesta personalizada con información de la carrera."""
    detalles = training.get_career_details(carrera)
    
    if not detalles:
        return f"Te recomiendo explorar: {carrera}"
    
    if tipo_usuario == "estudiante":
        if confianza > 0.7:
            mensaje_confianza = "✅ Basándome en tus respuestas"
        elif confianza > 0.5:
            mensaje_confianza = "📊 Parece que te encaja"
        else:
            mensaje_confianza = "💭 Podrías considerar"
        
        respuesta = (
            f"{mensaje_confianza}: **{carrera}**\n\n"
            f"📝 {detalles['descripcion']}\n\n"
            f"💪 Habilidades clave: {', '.join(detalles['habilidades'])}\n"
            f"🎯 Áreas de trabajo: {', '.join(detalles['campos'])}\n\n"
            f"¿Quieres saber más sobre esta carrera o explorar otras opciones?"
        )
    else:  # visitante
        respuesta = (
            f"🎓 Una excelente opción para ti es: **{carrera}**\n\n"
            f"📝 {detalles['descripcion']}\n"
            f"💪 Se requieren habilidades en: {', '.join(detalles['habilidades'])}\n"
            f"🌟 Campos de aplicación: {', '.join(detalles['campos'])}"
        )
    
    return respuesta

@router.get("/carreras")
def listar_carreras():
    """Retorna la lista de todas las carreras disponibles."""
    carreras = database.get_careers()
    return {
        "total": len(carreras),
        "carreras": list(carreras.keys())
    }

@router.post("/carrera-info")
def obtener_info_carrera(request: CareerInfoRequest):
    """Obtiene información detallada de una carrera específica."""
    detalles = training.get_career_details(request.carrera)
    
    if not detalles:
        return {
            "error": f"La carrera '{request.carrera}' no fue encontrada.",
            "carreras_disponibles": list(database.get_careers().keys())
        }
    
    return {
        "carrera": request.carrera,
        "descripcion": detalles['descripcion'],
        "habilidades": detalles['habilidades'],
        "campos": detalles['campos']
    }

@router.get("/sistema/estado")
def estado_sistema():
    """Retorna el estado del sistema y modelo."""
    df = database.load_data()
    return {
        "estado": "operativo",
        "datos_entrenamiento": len(df),
        "carreras_disponibles": len(database.get_careers()),
        "modelo_listo": len(df) >= 3
    }