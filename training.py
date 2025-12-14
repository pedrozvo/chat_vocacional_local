import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from database import load_data, CAREERS
import re

MODEL_NAME = "modelo_vocacional.joblib"

# Palabras clave relacionadas con cada carrera para mejor recomendación
CAREER_KEYWORDS = {
    "Ingeniería de Sistemas": ["programación", "software", "código", "web", "apps", "python", "javascript", "desarrollo", "sistemas", "datos", "base datos"],
    "Administración de Empresas": ["administración", "empresas", "negocios", "gerencia", "recursos humanos", "finanzas", "marketing", "empresa"],
    "Ingeniería Industrial": ["procesos", "producción", "optimización", "eficiencia", "calidad", "logística", "fabricación"],
    "Contabilidad": ["contabilidad", "contador", "auditoría", "impuestos", "balance", "cuentas", "finanzas"],
    "Ingeniería Comercial": ["comercio", "negocios", "internacional", "emprendimiento", "ventas", "comerciante"],
    "Psicología": ["psicología", "comportamiento", "salud mental", "emociones", "personas", "consejería", "terapia"],
    "Enfermería": ["enfermería", "salud", "hospital", "cuidado", "pacientes", "medicina", "sanitario"],
    "Educación": ["educación", "docencia", "enseñanza", "maestro", "profesor", "estudiantes", "enseñar"]
}

def train_basic_model():
    """
    Entrena un modelo Naive Bayes mejorado y lo guarda.
    Retorna un diccionario con el estado.
    """
    df = load_data()
    
    # Validación mínima de datos
    if len(df) < 3:
        return {"status": "error", "message": "Insuficientes datos (mínimo 3)."}

    # Pipeline mejorado: TF-IDF -> Naive Bayes
    model = make_pipeline(TfidfVectorizer(max_features=100, lowercase=True, stop_words='spanish'), 
                         MultinomialNB(alpha=0.1))
    
    # Entrenar
    model.fit(df['texto'], df['categoria'])
    
    # Guardar
    joblib.dump(model, MODEL_NAME)
    
    return {
        "status": "success", 
        "message": "Modelo Entrenado Correctamente", 
        "samples": len(df)
    }

def predict_category(text):
    """Carga el modelo y predice la carrera más relevante."""
    try:
        model = joblib.load(MODEL_NAME)
        pred = model.predict([text])[0]
        prob = model.predict_proba([text]).max()
        return pred, prob
    except FileNotFoundError:
        return None, 0.0

def find_matching_career(user_input):
    """Busca la carrera más relevante basada en palabras clave del usuario."""
    user_input_lower = user_input.lower()
    best_match = None
    best_count = 0
    
    for career, keywords in CAREER_KEYWORDS.items():
        match_count = sum(1 for keyword in keywords if keyword in user_input_lower)
        if match_count > best_count:
            best_count = match_count
            best_match = career
    
    return best_match

def get_career_details(career_name):
    """Retorna los detalles de una carrera específica."""
    return CAREERS.get(career_name, None)