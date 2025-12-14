# 🛠️ GUÍA DE DESARROLLO - CareerGuide

## Para Desarrolladores y Contribuyentes

### 📚 Estructura del Código

```python
# database.py - Gestión de datos
CAREERS = {
    "Carrera": {
        "descripcion": "...",
        "habilidades": [...],
        "campos": [...]
    }
}
# Agregar más carreras aquí

# training.py - Modelo ML
CAREER_KEYWORDS = {
    "Carrera": ["palabra1", "palabra2", ...]
}
# Agregar palabras clave para mejorar búsqueda

# routes.py - Endpoints API
@router.post("/nuevo-endpoint")
def nuevo_endpoint(request):
    # Implementar lógica
    return {"resultado": "..."}
```

---

## 🎓 Cómo Expandir el Proyecto

### 1. Agregar una Nueva Carrera

#### Paso 1: Actualizar `database.py`
```python
CAREERS = {
    # ... carreras existentes ...
    "Nueva Carrera": {
        "descripcion": "Breve descripción del campo",
        "habilidades": ["Habilidad 1", "Habilidad 2", "Habilidad 3", "Habilidad 4"],
        "campos": ["Campo 1", "Campo 2", "Campo 3", "Campo 4"]
    }
}
```

#### Paso 2: Actualizar `training.py`
```python
CAREER_KEYWORDS = {
    # ... carreras existentes ...
    "Nueva Carrera": [
        "palabra_clave1",
        "palabra_clave2",
        "palabra_clave3",
        # ... más palabras clave
    ]
}
```

#### Paso 3: Crear datos de entrenamiento
```python
# En initialize_training_data.py, agregar en TRAINING_DATA:
("Ejemplo 1 relacionado a Nueva Carrera", "Nueva Carrera"),
("Ejemplo 2 relacionado a Nueva Carrera", "Nueva Carrera"),
("Ejemplo 3 relacionado a Nueva Carrera", "Nueva Carrera"),
("Ejemplo 4 relacionado a Nueva Carrera", "Nueva Carrera"),
```

#### Paso 4: Entrenar modelo
```bash
python initialize_training_data.py
# O POST a /entrenar varias veces
```

### 2. Mejorar el Modelo ML

#### Opción A: Agregar Más Datos
```bash
# Ejecutar múltiples veces
python initialize_training_data.py
```

#### Opción B: Optimizar Hiperparámetros
```python
# En optimization.py, ajustar:
parameters = {
    'vect__max_features': [50, 100, 200, 300],  # Aumentar
    'vect__ngram_range': [(1, 1), (1, 2), (1, 3)],  # Probar trigramas
    'clf__alpha': [0.01, 0.05, 0.1, 0.5, 1.0],  # Más opciones
}
```

#### Opción C: Usar Otro Algoritmo
```python
# En training.py, reemplazar MultinomialNB con:
from sklearn.ensemble import RandomForestClassifier
# o
from sklearn.svm import SVC
# o
from sklearn.linear_model import LogisticRegression
```

### 3. Crear Nuevos Endpoints

#### Ejemplo: Endpoint para Filtrar Carreras
```python
# En routes.py
@router.get("/carreras/por-habilidad/{habilidad}")
def carreras_por_habilidad(habilidad: str):
    """Retorna carreras que requieren una habilidad específica"""
    carreras = database.get_careers()
    resultado = []
    
    for carrera, detalles in carreras.items():
        if habilidad.lower() in [h.lower() for h in detalles['habilidades']]:
            resultado.append(carrera)
    
    return {"habilidad": habilidad, "carreras": resultado}
```

#### Usar en frontend
```javascript
fetch('http://127.0.0.1:8000/carreras/por-habilidad/Programación')
    .then(r => r.json())
    .then(data => console.log(data))
```

---

## 🔧 Debugging y Testing

### Ejecutar Tests
```bash
python test_system.py
```

### Ver Logs en Tiempo Real
```bash
# En terminal donde corre uvicorn
# Los logs aparecen automáticamente
# Busca [ERROR] o [WARNING]
```

### Acceder a Documentación Interactiva
```
http://127.0.0.1:8000/docs
```

### Consultar Base de Datos
```python
import sqlite3

conn = sqlite3.connect("db_vocacional.sqlite")
cursor = conn.cursor()

# Ver todas las consultas
cursor.execute("SELECT * FROM consultas")
for row in cursor.fetchall():
    print(row)

conn.close()
```

---

## 🚀 Mejores Prácticas

### 1. Nombres de Variables
```python
# ❌ Malo
d = "Ingeniería de Sistemas"
r = modelo.predict([texto])

# ✅ Bueno
carrera_recomendada = "Ingeniería de Sistemas"
prediccion = modelo.predict([texto])
```

### 2. Funciones Pequeñas
```python
# ❌ Malo: función muy larga
def procesar_todo():
    # 100 líneas de código...

# ✅ Bueno: funciones específicas
def obtener_carrera(mensaje):
    return training.find_matching_career(mensaje)

def generar_respuesta(carrera):
    return generar_respuesta_personalizada(carrera)
```

### 3. Documentación
```python
# ✅ Bueno: docstring claro
def find_matching_career(user_input: str) -> str:
    """
    Busca la carrera más relevante basada en palabras clave.
    
    Args:
        user_input: Texto del usuario
        
    Returns:
        Nombre de la carrera más coincidente
        
    Example:
        >>> find_matching_career("Me gusta programar")
        "Ingeniería de Sistemas"
    """
```

### 4. Manejo de Errores
```python
# ✅ Bueno: manejo explícito
try:
    modelo = joblib.load(MODEL_NAME)
except FileNotFoundError:
    print("⚠️ Modelo no encontrado. Entrenando nuevo...")
    train_basic_model()
```

---

## 📊 Monitoreo en Producción

### Métricas Importantes
```python
# Registrar en logs
logging.info(f"Carrera recomendada: {carrera}")
logging.info(f"Confianza: {confianza:.2%}")
logging.warning(f"Baja confianza: {confianza:.2%}")
```

### Dashboard Simple
```python
# En routes.py
@router.get("/dashboard")
def dashboard():
    """Retorna estadísticas del sistema"""
    df = database.load_data()
    consultas = database.load_consultations()
    
    return {
        "total_consultas": len(consultas),
        "carreras_recomendadas": consultas['carrera_recomendada'].value_counts().to_dict(),
        "confianza_promedio": consultas['confianza'].mean()
    }
```

---

## 🔄 Flujo de Desarrollo

### 1. Cuando Quieras Hacer Cambios

```
1. Crea rama en git (opcional)
2. Haz cambios al código
3. Prueba localmente: python test_system.py
4. Verifica en http://127.0.0.1:8000/docs
5. Commit y push (si usas git)
```

### 2. Cuando Quieras Entrenar Nuevo Modelo

```bash
# Opción 1: Script automático
python initialize_training_data.py

# Opción 2: A través de API
curl -X POST http://127.0.0.1:8000/entrenar \
  -H "Content-Type: application/json" \
  -d '{"texto":"...", "categoria":"..."}'

# Opción 3: Optimizar
curl -X POST http://127.0.0.1:8000/optimizar
```

---

## 🐛 Errores Comunes y Soluciones

### Error: "FileNotFoundError: modelo_vocacional.joblib"
```python
# Solución:
python initialize_training_data.py
# O POST a /entrenar
```

### Error: "No module named 'fastapi'"
```bash
# Solución:
pip install fastapi uvicorn
```

### Respuestas muy genéricas
```python
# Solución: Agregar más palabras clave
CAREER_KEYWORDS["Carrera"] = [
    "palabra1", "palabra2", "palabra3",  # Agregar más
]
```

### Modelo poco preciso
```bash
# Solución 1: Entrenar con más datos
python initialize_training_data.py

# Solución 2: Optimizar modelo
curl -X POST http://127.0.0.1:8000/optimizar

# Solución 3: Cambiar algoritmo en training.py
```

---

## 📈 Optimizaciones Futuras

### Performance
- Caché de predicciones frecuentes
- Vectorización en GPU (cuML)
- API asincrónica (async/await)

### Precisión
- Ensemble de modelos
- Word embeddings (Word2Vec, BERT)
- Deep Learning (RNN, Transformers)

### Escalabilidad
- Microservicios (modelos separados)
- Load balancing
- Base de datos distribuida (NoSQL)

---

## 🧮 Matemáticas del Modelo

### TF-IDF
```
TF-IDF = TF(t,d) × IDF(t)

TF(t,d) = (Frecuencia de t en d) / (Total de palabras en d)
IDF(t) = log(Total de documentos / Documentos con t)
```

### Naive Bayes
```
P(Clase|Texto) ∝ P(Texto|Clase) × P(Clase)

Para cada palabra:
P(palabra|Clase) = (Frecuencia en clase + alpha) / (Total en clase + alpha × vocab_size)
```

---

## 📚 Recursos Útiles

### Documentación
- [FastAPI](https://fastapi.tiangolo.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Pydantic](https://pydantic-settings.readthedocs.io/)

### Tutoriales
- [Machine Learning Basics](https://www.coursera.org/)
- [Python Web Development](https://fastapi.tiangolo.com/tutorial/)

### Comunidades
- Stack Overflow
- GitHub Discussions
- Reddit r/MachineLearning

---

## ✅ Checklist para Producción

- [ ] Modelo entrenado con 100+ ejemplos
- [ ] Todas las pruebas en test_system.py pasadas
- [ ] Documentación completa
- [ ] HTTPS habilitado
- [ ] Autenticación implementada
- [ ] Rate limiting configurado
- [ ] Logs y monitoreo activos
- [ ] Backup de base de datos
- [ ] Plan de escalabilidad

---

## 🎓 Ejemplo Completo: Agregar "Música"

### 1. database.py
```python
CAREERS = {
    # ... existentes ...
    "Música": {
        "descripcion": "Formación artística y profesional en música",
        "habilidades": ["Oído musical", "Creatividad", "Disciplina", "Expresión artística"],
        "campos": ["Composición", "Interpretación", "Producción", "Docencia musical"]
    }
}
```

### 2. training.py
```python
CAREER_KEYWORDS = {
    # ... existentes ...
    "Música": [
        "música", "cantar", "tocar", "instrumento", "compositor",
        "productor", "audio", "sonido", "melodía", "ritmo",
        "orquesta", "banda", "jazz", "rock", "clásico"
    ]
}
```

### 3. initialize_training_data.py
```python
TRAINING_DATA = [
    # ... existentes ...
    ("Me encanta cantar y tocar instrumentos", "Música"),
    ("Quiero ser productor musical", "Música"),
    ("Me interesa la composición y arreglos", "Música"),
    ("Disfruto trabajar con audio y sonido", "Música"),
]
```

### 4. Probar
```bash
python initialize_training_data.py
python test_system.py
# Ir a http://127.0.0.1:8000
# Escribir: "Me gusta la música"
```

---

## 🎯 Conclusión

CareerGuide está diseñado para ser:
- **Extensible**: Fácil agregar carreras
- **Mejorable**: Fácil mejorar modelo
- **Mantenible**: Código limpio y documentado
- **Escalable**: Preparado para producción

¡Usa esta guía para contribuir y mejorar el proyecto! 🚀

---

**Versión**: 2.0
**Última actualización**: Diciembre 2025
**Mantenido por**: El equipo de desarrollo
