# Script para Cargar Datos de Entrenamiento Iniciales
# Ejecutar este script una sola vez para llenar la base de datos con ejemplos

import sqlite3
import requests
import json

DB_NAME = "db_vocacional.sqlite"
API_BASE = "http://127.0.0.1:8000"

# Datos de ejemplo para entrenar el modelo
TRAINING_DATA = [
    # Ingeniería de Sistemas
    ("Me gusta programar y crear aplicaciones web", "Ingeniería de Sistemas"),
    ("Quiero trabajar con Python y bases de datos", "Ingeniería de Sistemas"),
    ("Me interesa el desarrollo de software", "Ingeniería de Sistemas"),
    ("Disfruto resolviendo problemas lógicos con código", "Ingeniería de Sistemas"),
    ("Quiero ser desarrollador de aplicaciones", "Ingeniería de Sistemas"),
    
    # Administración de Empresas
    ("Me interesa la gestión empresarial y los negocios", "Administración de Empresas"),
    ("Quiero trabajar en recursos humanos", "Administración de Empresas"),
    ("Me fascina el análisis financiero", "Administración de Empresas"),
    ("Deseo emprender mi propio negocio", "Administración de Empresas"),
    ("Me interesa el marketing y la estrategia comercial", "Administración de Empresas"),
    
    # Ingeniería Industrial
    ("Me gusta optimizar procesos y mejorar eficiencia", "Ingeniería Industrial"),
    ("Quiero trabajar en producción y manufactura", "Ingeniería Industrial"),
    ("Me interesa la logística y la cadena de suministro", "Ingeniería Industrial"),
    ("Disfruto análisis de calidad y mejora continua", "Ingeniería Industrial"),
    
    # Contabilidad
    ("Me fascinan los números y la contabilidad", "Contabilidad"),
    ("Quiero ser contador o auditor", "Contabilidad"),
    ("Me interesa la gestión fiscal e impuestos", "Contabilidad"),
    ("Disfruto trabajar con balances y estados financieros", "Contabilidad"),
    
    # Ingeniería Comercial
    ("Me interesa el comercio internacional", "Ingeniería Comercial"),
    ("Quiero trabajar en negocios y emprendimiento", "Ingeniería Comercial"),
    ("Me fascina la negociación comercial", "Ingeniería Comercial"),
    ("Deseo expandir empresas a nuevos mercados", "Ingeniería Comercial"),
    
    # Psicología
    ("Me interesa entender el comportamiento humano", "Psicología"),
    ("Quiero ayudar a las personas con sus problemas", "Psicología"),
    ("Me fascina la salud mental y el bienestar", "Psicología"),
    ("Disfruto trabajar en orientación y consejería", "Psicología"),
    
    # Enfermería
    ("Me gustaría cuidar de la salud de las personas", "Enfermería"),
    ("Quiero trabajar en un hospital o clínica", "Enfermería"),
    ("Me interesa la atención al paciente", "Enfermería"),
    ("Disfruto trabajar en equipo sanitario", "Enfermería"),
    
    # Educación
    ("Me apasiona enseñar y transmitir conocimiento", "Educación"),
    ("Quiero ser profesor o educador", "Educación"),
    ("Me interesa diseñar programas educativos", "Educación"),
    ("Disfruto trabajar con estudiantes y jóvenes", "Educación"),
]

def insert_training_data():
    """Inserta datos de entrenamiento inicial en la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    for texto, categoria in TRAINING_DATA:
        cursor.execute(
            "INSERT INTO entrenamiento (texto, categoria) VALUES (?, ?)",
            (texto, categoria)
        )
    
    conn.commit()
    conn.close()
    print(f"✅ Insertados {len(TRAINING_DATA)} ejemplos de entrenamiento")

def train_model_via_api():
    """Entrena el modelo a través de la API"""
    try:
        response = requests.post(
            f"{API_BASE}/entrenar",
            json={
                "texto": "Datos de entrenamiento inicial",
                "categoria": "Sistema"
            }
        )
        if response.ok:
            result = response.json()
            print(f"✅ Modelo entrenado: {result}")
        else:
            print(f"❌ Error al entrenar: {response.status_code}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def optimize_model_via_api():
    """Optimiza el modelo a través de la API"""
    try:
        response = requests.post(f"{API_BASE}/optimizar")
        if response.ok:
            result = response.json()
            print(f"✅ Modelo optimizado: {result}")
        else:
            print(f"❌ Error al optimizar: {response.status_code}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def get_system_status():
    """Obtiene el estado del sistema"""
    try:
        response = requests.get(f"{API_BASE}/sistema/estado")
        if response.ok:
            status = response.json()
            print("\n📊 Estado del Sistema:")
            print(f"  Estado: {status['estado']}")
            print(f"  Datos de entrenamiento: {status['datos_entrenamiento']}")
            print(f"  Carreras disponibles: {status['carreras_disponibles']}")
            print(f"  Modelo listo: {'✅ Sí' if status['modelo_listo'] else '❌ No'}")
        else:
            print(f"❌ Error al obtener estado: {response.status_code}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    print("🚀 Inicializando datos de entrenamiento...\n")
    
    try:
        insert_training_data()
        print("\n⏳ Entrenando modelo...")
        train_model_via_api()
        
        print("\n⏳ Optimizando modelo...")
        optimize_model_via_api()
        
        get_system_status()
        
        print("\n✅ ¡Sistema listo! Puedes acceder a http://127.0.0.1:8000")
    except Exception as e:
        print(f"\n❌ Error: {e}")
