import sqlite3
import pandas as pd

DB_NAME = "db_vocacional.sqlite"

# Carreras disponibles con sus descripciones
CAREERS = {
    "Ingeniería de Sistemas": {
        "descripcion": "Desarrollo de software, programación y gestión de sistemas informáticos",
        "habilidades": ["Lógica", "Programación", "Resolución de problemas", "Análisis"],
        "campos": ["Software", "Web", "Apps", "Bases de datos"]
    },
    "Administración de Empresas": {
        "descripcion": "Gestión empresarial, finanzas y recursos humanos",
        "habilidades": ["Liderazgo", "Análisis financiero", "Comunicación", "Organización"],
        "campos": ["Finanzas", "RH", "Marketing", "Negocios"]
    },
    "Ingeniería Industrial": {
        "descripcion": "Optimización de procesos, producción y eficiencia empresarial",
        "habilidades": ["Optimización", "Análisis", "Matemáticas", "Liderazgo"],
        "campos": ["Producción", "Logística", "Calidad", "Consultoría"]
    },
    "Contabilidad": {
        "descripcion": "Gestión contable, auditoría y finanzas",
        "habilidades": ["Precisión", "Análisis numérico", "Organización", "Ética"],
        "campos": ["Auditoría", "Impuestos", "Finanzas", "Gobierno"]
    },
    "Ingeniería Comercial": {
        "descripcion": "Negocios, comercio internacional y emprendimiento",
        "habilidades": ["Negociación", "Comercio", "Análisis", "Comunicación"],
        "campos": ["Comercio", "Negocios", "Emprendimiento", "Logística"]
    },
    "Psicología": {
        "descripcion": "Estudio del comportamiento humano y salud mental",
        "habilidades": ["Empatía", "Escucha activa", "Análisis", "Comunicación"],
        "campos": ["Clínica", "RH", "Educativa", "Organizacional"]
    },
    "Enfermería": {
        "descripcion": "Cuidado de la salud y atención sanitaria",
        "habilidades": ["Empatía", "Responsabilidad", "Trabajo en equipo", "Precisión"],
        "campos": ["Hospitales", "Clínicas", "Salud pública", "Cuidado domiciliario"]
    },
    "Educación": {
        "descripcion": "Formación y enseñanza educativa",
        "habilidades": ["Paciencia", "Comunicación", "Empatía", "Creatividad"],
        "campos": ["Docencia", "Capacitación", "Diseño curricular", "Educación digital"]
    }
}

def init_db():
    """Inicializa la base de datos si no existe."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entrenamiento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            categoria TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_tipo TEXT NOT NULL,
            pregunta TEXT NOT NULL,
            carrera_recomendada TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(texto: str, categoria: str):
    """Guarda un nuevo ejemplo."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entrenamiento (texto, categoria) VALUES (?, ?)", (texto, categoria))
    conn.commit()
    conn.close()

def insert_consultation(usuario_tipo: str, pregunta: str, carrera_recomendada: str = None):
    """Registra una consulta del usuario."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO consultas (usuario_tipo, pregunta, carrera_recomendada) VALUES (?, ?, ?)",
        (usuario_tipo, pregunta, carrera_recomendada)
    )
    conn.commit()
    conn.close()

def load_data():
    """Carga todos los datos en un DataFrame."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT texto, categoria FROM entrenamiento", conn)
    conn.close()
    return df

def get_careers():
    """Retorna el diccionario de carreras disponibles."""
    return CAREERS