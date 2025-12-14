# 📊 ARQUITECTURA Y DIAGRAMAS - CareerGuide v2.0

## 🏗️ Arquitectura General del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    CAREERGUIDE v2.0                         │
│              Sistema de Orientación Vocacional              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────┐         ┌──────────────────────┐
│   FRONTEND (HTML)   │         │  BACKEND (FastAPI)   │
│                     │◄───────►│                      │
│ • Chatbot UI        │ HTTP    │ • API REST           │
│ • 2 Pantallas       │ JSON    │ • Rutas/Endpoints    │
│ • Responsive        │         │ • Validación         │
│ • Animaciones       │         │ • Lógica             │
└─────────────────────┘         └──────────────────────┘
         ▲                                ▲
         │                                │
         │                                │
         │                    ┌───────────┼───────────┐
         │                    ▼           ▼           ▼
         │             ┌────────────┐ ┌─────────┐ ┌──────────┐
         │             │ DATABASE   │ │ TRAINING│ │OPTIMI... │
         │             │ (SQLite)   │ │  (ML)   │ │(ML)      │
         │             └────────────┘ └─────────┘ └──────────┘
         │
         └─────────────────► http://127.0.0.1:8000

┌─────────────────────────────────────────────────────────────┐
│                    INFRAESTRUCTURA                          │
├─────────────────────────────────────────────────────────────┤
│ Python 3.8+ | FastAPI | scikit-learn | SQLite | uvicorn    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Flujo de Una Conversación

```
Usuario
   │
   ▼
┌─────────────────────────────┐
│  Abre navegador             │
│  http://127.0.0.1:8000      │
└─────────────────────────────┘
   │
   ▼
┌─────────────────────────────┐
│  Selecciona perfil:         │
│  - Estudiante               │
│  - Visitante                │
└─────────────────────────────┘
   │
   ▼
┌─────────────────────────────┐
│  Escribe mensaje/pregunta    │
│  Ej: "Me gusta programar"   │
└─────────────────────────────┘
   │
   ▼ (JavaScript POST)
┌─────────────────────────────┐
│  Backend API /chat          │
│  (routes.py)                │
└─────────────────────────────┘
   │
   ├─────────────────────┐
   │                     │
   ▼                     ▼
┌──────────────┐  ┌──────────────────┐
│ BÚSQUEDA     │  │ MODELO ML        │
│ Keywords     │  │ TF-IDF + NB      │
│              │  │                  │
│ "programar"  │  │ Predicción y     │
│ → Carrera    │  │ Confianza        │
└──────────────┘  └──────────────────┘
   │                     │
   └─────────────────────┘
           │
           ▼
   ┌───────────────────────────┐
   │ Combinar resultados       │
   │ (Mejor predicción)        │
   └───────────────────────────┘
           │
           ▼
   ┌───────────────────────────┐
   │ Generar respuesta         │
   │ personalizada con:        │
   │ • Carrera recomendada     │
   │ • Descripción             │
   │ • Habilidades             │
   │ • Campos de trabajo       │
   │ • Confianza (%)           │
   └───────────────────────────┘
           │
           ▼ (JSON Response)
   ┌───────────────────────────┐
   │ Mostrar en Chat           │
   │ (JavaScript)              │
   └───────────────────────────┘
           │
           ▼
   ┌───────────────────────────┐
   │ Registrar en BD           │
   │ (Tabla: consultas)        │
   └───────────────────────────┘
           │
           ▼
       Usuario Lee
       Respuesta Personalizada
```

---

## 📊 Arquitectura de Datos

```
┌────────────────────────────────────────────┐
│         db_vocacional.sqlite               │
├────────────────────────────────────────────┤
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │     Tabla: ENTRENAMIENTO             │ │
│  ├──────────────────────────────────────┤ │
│  │ id (PK) │ texto │ categoria          │ │
│  ├──────────────────────────────────────┤ │
│  │ 1       │ "Me gusta..." │ "Ing. Sis."│ │
│  │ 2       │ "Quiero..." │ "Admin."    │ │
│  │ ...     │ ...    │ ...              │ │
│  │ 35      │ ...    │ ...              │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │     Tabla: CONSULTAS                 │ │
│  ├──────────────────────────────────────┤ │
│  │ id │ usuario_tipo │ pregunta │ ...  │ │
│  ├──────────────────────────────────────┤ │
│  │ 1  │ "estudiante" │ "Hola"  │ ...  │ │
│  │ 2  │ "visitante"  │ "Info"  │ ...  │ │
│  │ .. │ ...          │ ...     │ ...  │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │   CAREERS (diccionario en memory)    │ │
│  ├──────────────────────────────────────┤ │
│  │ "Ingeniería de Sistemas": {          │ │
│  │   descripción: "...",                │ │
│  │   habilidades: [...],                │ │
│  │   campos: [...]                      │ │
│  │ },                                   │ │
│  │ ...8 carreras total                  │ │
│  └──────────────────────────────────────┘ │
│                                            │
└────────────────────────────────────────────┘
```

---

## 🤖 Flujo del Modelo ML

```
                    Usuario Input
                        │
                        ▼
        ┌────────────────────────────┐
        │  Preprocesamiento           │
        │  • Minúsculas               │
        │  • Tokenización             │
        └────────────────────────────┘
                        │
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
    ┌─────────────┐          ┌──────────────────┐
    │  BÚSQUEDA   │          │  TF-IDF          │
    │  KEYWORDS   │          │  VECTORIZER      │
    │             │          │                  │
    │ Palabras    │          │ Convierte        │
    │ clave por   │          │ texto a números  │
    │ carrera     │          │                  │
    │             │          │ Importancia de   │
    │ Coincidencias           palabras         │
    └─────────────┘          └──────────────────┘
         │                             │
         │             ┌───────────────┘
         │             │
         ▼             ▼
    ┌─────────────────────────────────────┐
    │  MULTINOMIAL NAIVE BAYES            │
    │  • P(Clase|Texto)                   │
    │  • Predicción: Carrera              │
    │  • Probabilidad: Confianza          │
    └─────────────────────────────────────┘
         │
         ├─────────────┐
         │             │
         ▼             ▼
    ┌─────────┐   ┌──────────┐
    │ Carrera │   │Confianza │
    │ Pred.   │   │  (0-100%)│
    └─────────┘   └──────────┘
         │             │
         └──────┬──────┘
                │
                ▼
        ┌───────────────────┐
        │ COMBINAR          │
        │ • Si match keyword│
        │   ➜ usar ese      │
        │ • Si ML alta conf │
        │   ➜ usar ML       │
        │ • Sino            │
        │   ➜ pedir más info│
        └───────────────────┘
                │
                ▼
        ┌───────────────────┐
        │ RESPUESTA FINAL   │
        │ • Carrera         │
        │ • Detalles        │
        │ • Confianza       │
        └───────────────────┘
```

---

## 🔌 Endpoints API

```
CAREERGUIDE API REST
============================

POST /chat
├─ Input: {"mensaje": "...", "tipo_usuario": "..."}
└─ Output: {
     "respuesta": "...",
     "carrera_recomendada": "...",
     "confianza": 0.92
   }

GET /carreras
├─ Input: (ninguno)
└─ Output: {
     "total": 8,
     "carreras": ["Carrera 1", "Carrera 2", ...]
   }

POST /carrera-info
├─ Input: {"carrera": "Ing. Sistemas"}
└─ Output: {
     "carrera": "Ing. Sistemas",
     "descripcion": "...",
     "habilidades": [...],
     "campos": [...]
   }

GET /sistema/estado
├─ Input: (ninguno)
└─ Output: {
     "estado": "operativo",
     "datos_entrenamiento": 35,
     "carreras_disponibles": 8,
     "modelo_listo": true
   }

POST /entrenar
├─ Input: {"texto": "...", "categoria": "..."}
└─ Output: {
     "status": "success",
     "message": "...",
     "samples": 36
   }

POST /optimizar
├─ Input: (ninguno)
└─ Output: {
     "status": "success",
     "message": "...",
     "best_params": {...},
     "best_score": 0.923
   }

PLUS: /docs (Swagger UI)
      /redoc (ReDoc)
```

---

## 🎨 Estructura Frontend

```
┌──────────────────────────────────────────┐
│          NAVEGADOR (index.html)          │
├──────────────────────────────────────────┤
│                                          │
│  ┌────────────────────────────────────┐ │
│  │     PANTALLA 1: LOBBY              │ │
│  ├────────────────────────────────────┤ │
│  │                                    │ │
│  │  🎓 CareerGuide                   │ │
│  │  Tu asesor vocacional con IA      │ │
│  │                                    │ │
│  │  ┌──────────────────────────────┐ │ │
│  │  │ [👨‍🎓 Soy Estudiante]          │ │ │
│  │  └──────────────────────────────┘ │ │
│  │                                    │ │
│  │  ┌──────────────────────────────┐ │ │
│  │  │ [👋 Soy Visitante]           │ │ │
│  │  └──────────────────────────────┘ │ │
│  │                                    │ │
│  └────────────────────────────────────┘ │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │     PANTALLA 2: CHAT               │ │
│  ├────────────────────────────────────┤ │
│  │  📚 Asesoramiento Estudiantes [<]  │ │
│  ├────────────────────────────────────┤ │
│  │                                    │ │
│  │  Bot: ¡Hola! ¿Qué te apasiona?   │ │
│  │                                    │ │
│  │                 Tú: Programación   │ │
│  │                                    │ │
│  │  Bot: 💻 **Ingeniería de Sistemas*│ │
│  │       Descripción: ...             │ │
│  │       💪 Habilidades: ...         │ │
│  │       🎯 Campos: ...              │ │
│  │       🔒 Confianza: 92%           │ │
│  │                                    │ │
│  ├────────────────────────────────────┤ │
│  │ [Escribe tu pregunta...]   [Enviar]│ │
│  └────────────────────────────────────┘ │
│                                          │
└──────────────────────────────────────────┘

    JavaScript (en index.html)
    │
    ├─ handleEnter() - Detecta Enter
    ├─ sendMessage() - Envía al backend
    ├─ addMessage() - Muestra en chat
    ├─ enterChat() - Cambia pantalla
    ├─ goBack() - Vuelve al lobby
    └─ formatBotResponse() - Formatea response
```

---

## 🔄 Ciclo de Vida del Servidor

```
1. INICIALIZACIÓN
   │
   ├─ python main.py
   │  o uvicorn main:app --reload
   │
   ▼
2. ARRANQUE
   │
   ├─ Importar módulos
   ├─ Inicializar BD
   ├─ Crear app FastAPI
   ├─ Configurar CORS
   ├─ Incluir rutas
   │
   ▼
3. ESCUCHA
   │
   ├─ Listening on http://127.0.0.1:8000
   │
   ▼
4. SOLICITUDES
   │
   ├─ Request ➜ Route ➜ Handler ➜ Response
   │
   ▼
5. CIERRE
   │
   ├─ Ctrl+C para detener
   └─ Cerrar conexiones BD
```

---

## 📊 Flujo de Entrenamiento

```
PRIMERA VEZ: python initialize_training_data.py

1. CARGA DE DATOS
   │
   ├─ Lee TRAINING_DATA (35 ejemplos)
   ├─ Inserta en tabla `entrenamiento`
   │
   ▼
2. ENTRENA MODELO
   │
   ├─ TfidfVectorizer
   │  ├─ Convierte texto a números
   │  ├─ Calcula TF-IDF
   │  └─ max_features=100, lowercase=True
   │
   ├─ MultinomialNB
   │  ├─ Entrena en datos
   │  ├─ Aprende probabilidades
   │  └─ alpha=0.1 para suavizado
   │
   ├─ Guarda en modelo_vocacional.joblib
   │
   ▼
3. OPTIMIZA MODELO (OPCIONAL)
   │
   ├─ GridSearchCV prueba combinaciones
   ├─ Encuentra mejores hiperparámetros
   ├─ Cross-validation (3 folds)
   ├─ Calcula accuracy
   │
   ▼
4. VALIDACIÓN
   │
   ├─ Comprueba modelo.joblib existe
   ├─ Comprueba BD tiene datos
   ├─ Muestra estado final
   │
   ▼
MODELO LISTO PARA USAR ✅
```

---

## 🎓 Stack Tecnológico

```
┌─────────────────────────────────────┐
│   CAREERGUIDE TECHNOLOGY STACK      │
├─────────────────────────────────────┤
│                                     │
│  LENGUAJE: Python 3.8+              │
│  ├─ Backend
│  └─ ML/Ciencia de Datos
│                                     │
│  FRAMEWORK WEB: FastAPI             │
│  ├─ API REST moderna
│  ├─ Validación automática (Pydantic)
│  ├─ Documentación automática (Swagger)
│  └─ Rápido y eficiente
│                                     │
│  ML/AI: scikit-learn                │
│  ├─ TF-IDF Vectorizer
│  ├─ Multinomial Naive Bayes
│  ├─ GridSearchCV
│  └─ Cross-validation
│                                     │
│  BASE DE DATOS: SQLite              │
│  ├─ Ligero y portable
│  ├─ No requiere servidor
│  ├─ Perfecto para desarrollo
│  └─ Escalable a PostgreSQL
│                                     │
│  SERIALIZACIÓN: joblib              │
│  ├─ Guardar modelos ML
│  ├─ Recuperar rápidamente
│  └─ Compatible con scikit-learn
│                                     │
│  DATA PROCESSING: pandas            │
│  ├─ DataFrames
│  ├─ Lectura de DB
│  └─ Manipulación de datos
│                                     │
│  SERVER: uvicorn                    │
│  ├─ ASGI server
│  ├─ Alta performance
│  └─ Soporte hot-reload
│                                     │
│  FRONTEND: HTML/CSS/JavaScript      │
│  ├─ HTML5 semántico
│  ├─ CSS3 (gradients, animations)
│  ├─ Vanilla JS (sin frameworks)
│  └─ Fetch API para comunicación
│                                     │
└─────────────────────────────────────┘
```

---

## 🚀 Deployment Posible

```
DESARROLLO (Actual)
├─ localhost:8000
├─ Servidor uvicorn
└─ BD SQLite local

PRODUCCIÓN (Futuro)
├─ Docker container
├─ Gunicorn + Uvicorn workers
├─ PostgreSQL BD
├─ Nginx reverse proxy
├─ SSL/HTTPS
├─ Load balancer
└─ Cloud (AWS, GCP, Heroku, etc)
```

---

## 📈 Escalabilidad

```
ACTUAL (1 servidor)
│
├─ 1 instancia uvicorn
├─ 1 BD SQLite
├─ ~100 usuarios concurrentes
└─ Funciona bien ✅

CRECIMIENTO 1 (Múltiples servidores)
│
├─ 3-5 instancias (Docker)
├─ PostgreSQL compartida
├─ Redis para caché
├─ Nginx load balancer
└─ ~10,000 usuarios

CRECIMIENTO 2 (Arquitectura distribuida)
│
├─ Microservicios
├─ Kubernetes orquestación
├─ Elasticsearch
├─ Message queue
└─ ~1,000,000 usuarios
```

---

## 🎯 Conclusión Visual

```
┌───────────────────────────────────────┐
│      ARQUITECTURA DE CAREERGUIDE      │
├───────────────────────────────────────┤
│                                       │
│  USUARIO                              │
│     │                                 │
│     ├─────────► FRONTEND (HTML)       │
│     │               │                 │
│     │               ├─ Chat UI        │
│     │               ├─ Animaciones    │
│     │               └─ Responsive     │
│     │                   │             │
│     └───────────────────┼─────────┐   │
│                         │         │   │
│                    JSON/HTTP      │   │
│                         │         │   │
│                         ▼         │   │
│                    BACKEND        │   │
│                    (FastAPI)      │   │
│                         │         │   │
│     ┌───────────────────┼────┐    │   │
│     │                   │    │    │   │
│     ▼                   ▼    ▼    ▼   │
│  DATABASE          TRAINING  OPTIMIZATION
│  (SQLite)          (ML)      (ML)
│     │                 │        │       │
│     ├─ Entrenamiento  ├─ TF-IDF       │
│     ├─ Consultas      ├─ Naive Bayes  │
│     └─ Historial      └─ Predicción   │
│                                       │
└───────────────────────────────────────┘

RESULTADO: Sistema completo, moderno
           y profesional para orientación
           vocacional con IA ✅
```

---

**Versión**: 2.0
**Diagrama**: Arquitectura Completa
**Estado**: ✅ Sistema Funcionando
