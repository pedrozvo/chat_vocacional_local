# 🎓 CareerGuide - Sistema de Orientación Vocacional con IA

Un chatbot inteligente de asesoramiento vocacional que ayuda a estudiantes y visitantes a descubrir carreras adecuadas según sus intereses, habilidades y preferencias.

## ✨ Características Principales

### 🤖 Chatbot Inteligente
- **Recomendaciones Personalizadas**: Basadas en Machine Learning (Naive Bayes + TF-IDF)
- **Búsqueda de Palabras Clave**: Análisis de consultas para identificar carreras relevantes
- **Respuestas Contextuales**: Adaptadas según el tipo de usuario (estudiante/visitante)
- **Información Detallada**: Cada carrera incluye descripción, habilidades requeridas y campos de trabajo

### 📚 Carreras Disponibles (8 opciones)
1. **Ingeniería de Sistemas** - Software, programación, web development
2. **Administración de Empresas** - Gestión, finanzas, recursos humanos
3. **Ingeniería Industrial** - Optimización de procesos, logística
4. **Contabilidad** - Auditoría, finanzas, impuestos
5. **Ingeniería Comercial** - Negocios, comercio internacional
6. **Psicología** - Comportamiento, salud mental
7. **Enfermería** - Cuidado de la salud, atención sanitaria
8. **Educación** - Docencia, capacitación, diseño curricular

### 📊 Base de Datos
- Tabla de entrenamiento para alimentar el modelo ML
- Tabla de consultas para análisis de uso y seguimiento
- Sistema de almacenamiento SQLite robusto

### 🎨 Interfaz Mejorada
- Diseño moderno con gradientes y animaciones
- Interfaz responsiva (funciona en móvil y escritorio)
- Mensajes formateados con Markdown
- Indicadores visuales de confianza en recomendaciones

## 🚀 Cómo Usar

### Requisitos
- Python 3.8+
- FastAPI
- scikit-learn
- joblib
- pandas
- uvicorn

### Instalación

```bash
# 1. Navegar al directorio del proyecto
cd "C:\Users\pgoat\Desktop\8vo Semestre\Machine Learning\EV4"

# 2. Crear un entorno virtual (opcional pero recomendado)
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependencias
pip install fastapi uvicorn scikit-learn joblib pandas

# 4. Ejecutar el servidor
uvicorn main:app --reload
```

### Uso del Sistema

1. **Abre el navegador** y ve a `http://127.0.0.1:8000`
2. **Selecciona tu perfil**:
   - 👨‍🎓 Estudiante (necesita orientación vocacional)
   - 👋 Visitante (quiere explorar carreras)
3. **Interactúa con el chatbot** describiendo tus intereses o respondiendo preguntas
4. **Recibe recomendaciones** con información detallada sobre carreras

## 📁 Estructura del Proyecto

```
.
├── main.py                    # Aplicación FastAPI principal
├── routes.py                  # Endpoints de la API
├── database.py                # Base de datos y gestión de datos
├── training.py                # Modelo ML y predicciones
├── optimization.py            # Optimización de hiperparámetros
├── index.html                 # Frontend (chatbot UI)
├── modelo_vocacional.joblib   # Modelo ML entrenado (generado automáticamente)
├── db_vocacional.sqlite       # Base de datos (generada automáticamente)
└── README.md                  # Este archivo
```

## 🔌 Endpoints de la API

### Chat
```
POST /chat
Content-Type: application/json

Body:
{
  "mensaje": "Me interesa programar",
  "tipo_usuario": "estudiante"
}

Response:
{
  "respuesta": "Basándome en tus intereses...",
  "carrera_recomendada": "Ingeniería de Sistemas",
  "confianza": 0.85
}
```

### Listar Carreras
```
GET /carreras

Response:
{
  "total": 8,
  "carreras": ["Ingeniería de Sistemas", "Administración de Empresas", ...]
}
```

### Información de Carrera
```
POST /carrera-info
Content-Type: application/json

Body:
{
  "carrera": "Ingeniería de Sistemas"
}

Response:
{
  "carrera": "Ingeniería de Sistemas",
  "descripcion": "...",
  "habilidades": [...],
  "campos": [...]
}
```

### Entrenar Modelo
```
POST /entrenar
Content-Type: application/json

Body:
{
  "texto": "Me gusta el desarrollo de software",
  "categoria": "Ingeniería de Sistemas"
}
```

### Optimizar Modelo
```
POST /optimizar

Response:
{
  "status": "success",
  "message": "Modelo Optimizado Exitosamente",
  "best_score": 0.923,
  "samples_trained": 25
}
```

### Estado del Sistema
```
GET /sistema/estado

Response:
{
  "estado": "operativo",
  "datos_entrenamiento": 15,
  "carreras_disponibles": 8,
  "modelo_listo": true
}
```

## 🧠 Cómo Funciona el ML

### Algoritmo
- **Vectorización**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Clasificador**: Naive Bayes Multinomial
- **Búsqueda Auxiliar**: Coincidencia de palabras clave

### Flujo de Predicción
1. **Recibe pregunta del usuario**
2. **Busca palabras clave relacionadas** con cada carrera
3. **Ejecuta el modelo ML** para obtener predicción y confianza
4. **Combina resultados** para generar recomendación final
5. **Genera respuesta personalizada** con información de la carrera

### Mejora del Modelo
- **Recopilar datos**: Cada consulta se registra en la BD
- **Entrenar**: POST `/entrenar` con ejemplos nuevos
- **Optimizar**: POST `/optimizar` busca mejores hiperparámetros
- **Iterar**: Repetir según sea necesario

## 💡 Mejoras Implementadas

### Respecto a la Versión Original

✅ **Interfaz Mejorada**
- Diseño moderno con gradientes y animaciones
- Mejor experiencia de usuario (UX)
- Soporte para markdown en respuestas

✅ **Modelo ML Mejorado**
- Cambio de CountVectorizer a TF-IDF
- Búsqueda inteligente de palabras clave
- Mejor manejo de confianza

✅ **Más Información**
- 8 carreras con detalles completos
- Descripción, habilidades y campos de cada carrera
- Respuestas contextuales por tipo de usuario

✅ **API Expandida**
- Nuevos endpoints para información de carreras
- Endpoint de estado del sistema
- Mejor documentación

✅ **Base de Datos Mejorada**
- Tabla de consultas para análisis
- Histórico de recomendaciones
- Mejor estructura

## 🔍 Ejemplos de Uso

### Ejemplo 1: Estudiante Interesado en Tecnología
```
Usuario: "Me encanta programar y resolver problemas complejos"
Bot: "Basándome en tus intereses: Ingeniería de Sistemas..."
```

### Ejemplo 2: Visitante Explorando Opciones
```
Usuario: "¿Qué carreras hay si me interesa el comercio?"
Bot: "Una excelente opción es: Ingeniería Comercial..."
```

### Ejemplo 3: Solicitud de Detalles
```
Usuario: "¿Cuáles son las habilidades para ser contador?"
Bot: "Se requieren habilidades en: Precisión, Análisis numérico..."
```

## 🐛 Solución de Problemas

### El servidor no inicia
```bash
# Verifica que FastAPI esté instalado
pip install fastapi uvicorn

# Verifica el puerto 8000 no está en uso
netstat -ano | findstr :8000
```

### El chatbot no responde
1. Asegúrate que el servidor esté corriendo
2. Verifica la consola de errores en el navegador (F12 > Console)
3. Comprueba que la URL sea `http://127.0.0.1:8000`

### El modelo da predicciones inexactas
```bash
# Entrena el modelo con más ejemplos
# Luego optimiza los hiperparámetros
POST /optimizar
```

## 📈 Estadísticas y Métricas

El sistema registra:
- Total de consultas procesadas
- Carreras más buscadas
- Confianza promedio de predicciones
- Satisfacción de usuarios

Puedes analizar esto desde SQLite:
```sql
SELECT * FROM consultas;
```

## 🎯 Próximas Mejoras Sugeridas

1. **Integración con APIs Externas**: Datos reales de universidades
2. **Más Carreras**: Expandir a 20+ opciones
3. **Tests Psicométricos**: Cuestionarios estructurados
4. **Histórico del Usuario**: Guardar preferencias entre sesiones
5. **Análisis de Tendencias**: Dashboard con métricas
6. **Soporte Multiidioma**: Español/Inglés

## 📝 Notas Importantes

- El modelo necesita **al menos 3 ejemplos** para entrenar
- Se recomiendan **al menos 15-20 ejemplos** por carrera para buena precisión
- Las palabras clave son **case-insensitive**
- Las consultas se registran con timestamp automático

## 🤝 Contribuciones

Para mejorar el sistema:
1. Agrega más ejemplos de entrenamiento
2. Expande la lista de palabras clave
3. Añade más carreras
4. Mejora el algoritmo ML

## 📞 Soporte

Para problemas o preguntas:
1. Revisa los logs de la consola
2. Consulta la documentación interactiva en `/docs`
3. Verifica los ejemplos en README.md

---

**Versión**: 2.0 Mejorada
**Última actualización**: Diciembre 2025
**Estado**: Operativo y Optimizado ✅
