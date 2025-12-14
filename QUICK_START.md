# 🚀 GUÍA RÁPIDA - CareerGuide

## Inicio Rápido (3 pasos)

### Paso 1: Inicia el servidor
```bash
# En Windows PowerShell o CMD, en la carpeta del proyecto
uvicorn main:app --reload
```

Deberías ver:
```
Uvicorn running on http://127.0.0.1:8000
```

### Paso 2: Carga datos de entrenamiento (primera vez)
```bash
# En otra terminal PowerShell/CMD
python initialize_training_data.py
```

Espera el mensaje:
```
✅ Sistema listo!
```

### Paso 3: Abre el chatbot
- Ve a tu navegador
- Visita: `http://127.0.0.1:8000`
- ¡Comienza a explorar carreras!

---

## 📱 Interfaz del Chatbot

### Pantalla 1: Selecciona tu perfil
```
┌─────────────────────────────┐
│ 🎓 CareerGuide              │
│ Tu asesor vocacional con IA │
│                             │
│ [👨‍🎓 Soy Estudiante]          │
│ [👋 Soy Visitante]           │
└─────────────────────────────┘
```

### Pantalla 2: Interactúa con el chatbot
```
┌─────────────────────────────┐
│ 📚 Asesoramiento Estudiantes │ ← Salir
├─────────────────────────────┤
│ Bot: ¡Hola! ¿Qué te apasiona?
│                             │
│                    Tú: Programación
│                             │
│ Bot: Basándome en tus...   │
├─────────────────────────────┤
│ [Escribe tu pregunta...]    │
│                        [Enviar]
└─────────────────────────────┘
```

---

## 💬 Ejemplos de Preguntas

### Para Estudiantes
- "Me gusta programar"
- "¿Qué carrera me recomiendas si me interesa la salud?"
- "Soy bueno resolviendo problemas"
- "Me gustaría trabajar con números"

### Para Visitantes
- "¿Qué carreras de ingeniería existen?"
- "Quiero saber sobre negocios"
- "¿Cuál es mejor: Psicología o Educación?"
- "¿Qué necesito para ser contador?"

---

## 🔍 Carreras Disponibles

| # | Carrera | Emoji | Descripción Breve |
|---|---------|-------|-------------------|
| 1 | Ingeniería de Sistemas | 💻 | Software, programación, desarrollo |
| 2 | Administración de Empresas | 🏢 | Gestión, finanzas, negocios |
| 3 | Ingeniería Industrial | ⚙️ | Procesos, optimización, logística |
| 4 | Contabilidad | 📊 | Finanzas, auditoría, impuestos |
| 5 | Ingeniería Comercial | 💼 | Comercio, emprendimiento, ventas |
| 6 | Psicología | 🧠 | Comportamiento, salud mental |
| 7 | Enfermería | 🏥 | Salud, cuidado de pacientes |
| 8 | Educación | 📚 | Docencia, enseñanza |

---

## 🛠️ API REST (Uso Avanzado)

### Test en Postman/cURL

**Prueba el chatbot:**
```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"mensaje\": \"Me gusta programar\", \"tipo_usuario\": \"estudiante\"}"
```

**Lista todas las carreras:**
```bash
curl http://127.0.0.1:8000/carreras
```

**Obtén info de una carrera:**
```bash
curl -X POST http://127.0.0.1:8000/carrera-info \
  -H "Content-Type: application/json" \
  -d "{\"carrera\": \"Ingeniería de Sistemas\"}"
```

**Ve el estado del sistema:**
```bash
curl http://127.0.0.1:8000/sistema/estado
```

---

## 📊 Mejorando el Modelo

### Agregar más datos de entrenamiento:
```bash
# Opción 1: Usar el script
python initialize_training_data.py

# Opción 2: Usar Postman/cURL
curl -X POST http://127.0.0.1:8000/entrenar \
  -H "Content-Type: application/json" \
  -d "{\"texto\": \"Quiero ser contador\", \"categoria\": \"Contabilidad\"}"
```

### Optimizar hiperparámetros:
```bash
curl -X POST http://127.0.0.1:8000/optimizar
```

---

## ⚡ Comandos Útiles

### Ver documentación interactiva:
- URL: `http://127.0.0.1:8000/docs`
- Permite probar todos los endpoints desde el navegador

### Ver archivos de log:
```bash
# En la terminal donde corre uvicorn verás los logs
# Ctrl+C para detener el servidor
```

### Base de datos:
```bash
# Ver contenido de SQLite
# Instala: pip install sqlite3
# Luego abre: db_vocacional.sqlite con SQLite Browser
```

---

## 🐛 Troubleshooting

| Problema | Solución |
|----------|----------|
| "Error: No se conecta" | ✅ Verifica que uvicorn esté corriendo |
| "Modelo no encontrado" | ✅ Ejecuta `initialize_training_data.py` |
| "Recomendaciones vagas" | ✅ Agrega más datos con el script |
| "Puerto 8000 en uso" | ✅ Cambia en main.py: `port=8001` |

---

## 📈 Próximos Pasos

1. **Expandir carreras**: Agrega más en `database.py`
2. **Mejorar palabras clave**: Edita `CAREER_KEYWORDS` en `training.py`
3. **Entrenar más**: Ejecuta `initialize_training_data.py` varias veces
4. **Analizar datos**: Consulta `db_vocacional.sqlite`

---

## 📞 Contacto

¿Problemas? Revisa:
1. Los logs en la terminal
2. La documentación en `/docs`
3. El README.md completo

---

**¡Ahora estás listo para usar CareerGuide!** 🎓✨
