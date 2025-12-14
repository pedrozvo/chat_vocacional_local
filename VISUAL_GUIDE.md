# 🎨 GUÍA VISUAL - CareerGuide v2.0

## 🖼️ Lo Que Vas a Ver

### PANTALLA 1: BIENVENIDA

```
╔════════════════════════════════════════╗
║                                        ║
║           🎓 CareerGuide               ║
║      Tu asesor vocacional con IA       ║
║                                        ║
║  Por favor, selecciona tu perfil:      ║
║                                        ║
║  ┌──────────────────────────────────┐  ║
║  │  👨‍🎓 Soy Estudiante               │  ║
║  │  Necesito orientación vocacional │  ║
║  └──────────────────────────────────┘  ║
║                                        ║
║  ┌──────────────────────────────────┐  ║
║  │  👋 Soy Visitante                │  ║
║  │  Quiero explorar carreras        │  ║
║  └──────────────────────────────────┘  ║
║                                        ║
║  ✨ Responde nuestras preguntas para   ║
║  recibir recomendaciones personalizadas║
║                                        ║
╚════════════════════════════════════════╝
```

### PANTALLA 2: CHAT

```
╔════════════════════════════════════════╗
║  📚 Asesoramiento para Estudiantes [←] ║
╠════════════════════════════════════════╣
║                                        ║
║ Bot: ¡Hola! 👋                        ║
║ Soy tu asistente de orientación       ║
║ vocacional. Voy a ayudarte a          ║
║ descubrir qué carrera se adapta       ║
║ mejor a tus habilidades e intereses.  ║
║                                        ║
║ ¿Cuéntame, qué te apasiona o en       ║
║ qué áreas tienes fortaleza?           ║
║                                        ║
║                                        ║
║              Tú: Me gusta programar    ║
║                                        ║
║                                        ║
║ Bot: 💻 Ingeniería de Sistemas        ║
║                                        ║
║ 📝 Descripción: Desarrollo de         ║
║ software, programación y gestión      ║
║ de sistemas informáticos              ║
║                                        ║
║ 💪 Habilidades requeridas:            ║
║ • Lógica                              ║
║ • Programación                        ║
║ • Resolución de problemas             ║
║ • Análisis                            ║
║                                        ║
║ 🎯 Campos de aplicación:              ║
║ • Software • Web • Apps • BD          ║
║                                        ║
║ 🔒 Confianza: 92% ✅                  ║
║                                        ║
║ ¿Te gustaría conocer más sobre        ║
║ alguna carrera específica o           ║
║ explorar otras opciones?              ║
║                                        ║
╠════════════════════════════════════════╣
║ [Escribe tu pregunta aquí...] [Enviar]║
╚════════════════════════════════════════╝
```

---

## 🎨 Elementos Visuales

### Colores
```
Primario:    Azul (#667eea)
Secundario:  Púrpura (#764ba2)
Fondo:       Blanco (#ffffff)
Texto:       Gris oscuro (#333333)

Gradiente Principal:
┌─────────────────────┐
│ 🟦 Azul             │ (#667eea)
│ ░░░░░░░░░░░░░░░░░░░│ (gradual)
│ 🟪 Púrpura          │ (#764ba2)
└─────────────────────┘
```

### Iconos Emoji
```
🎓 Educación
💻 Tecnología
🏢 Empresa
⚙️ Industria
📊 Números
💼 Negocios
🧠 Mente
🏥 Salud
📚 Educación
```

### Animaciones
```
✨ Fade-in: Mensajes aparecen suavemente
↓ Slide-in: Elementos entran desde arriba
🔄 Hover: Botones reaccionan al pasar mouse
⚡ Active: Botones se activan al hacer click
```

---

## 📱 Responsive Design

### En Móvil
```
┌─────────────┐
│ 🎓CareerGde │  Título ajustado
├─────────────┤
│ Bot: Hola   │  100% ancho
│             │
│ Tú: Pregunta│  Scroll vertical
│             │  Messages apilados
│ Bot: Resp...│
├─────────────┤
│[Escribe...] │  Input y botón
│[Enviar]     │  apilados
└─────────────┘
```

### En Tablet
```
┌──────────────────┐
│ 📚 Asesoramiento │
├──────────────────┤
│ Bot: Mensaje     │
│                  │
│      Tú: Mensaje │
│                  │
│ Bot: Respuesta   │
├──────────────────┤
│[Escrita...] [Env]│
└──────────────────┘
```

### En Desktop (1920px)
```
┌────────────────────────────────┐
│   📚 Asesoramiento Vocacional   │
├────────────────────────────────┤
│                                │
│ Bot: Bienvenido a CareerGuide  │
│                                │
│                Tú: Hola        │
│                                │
│ Bot: Respuesta detallada con   │
│ información de carrera         │
│                                │
├────────────────────────────────┤
│ [Escribe tu pregunta....] [Env]│
└────────────────────────────────┘
```

---

## 🎬 Flujo Visual

```
USUARIO ABRE NAVEGADOR
           ↓
      ┌─────────┐
      │ LOBBY   │
      │ 🎓      │
      │[Est][Vis]
      └────┬────┘
           ↓ (Click)
      ┌─────────┐
      │CHAT     │
      │Bot: Hi  │
      │[Input]  │
      └────┬────┘
           ↓ (Escribe mensaje)
           ↓ (Click Enviar)
      ┌─────────────────────┐
      │ Backend procesa     │
      │ • Busca keywords    │
      │ • Ejecuta ML        │
      │ • Genera respuesta  │
      └────┬────────────────┘
           ↓ (JSON response)
      ┌─────────────────────┐
      │ Muestra respuesta   │
      │ • Carrera           │
      │ • Detalles          │
      │ • Confianza         │
      └────┬────────────────┘
           ↓
    USUARIO LEE RESPUESTA
```

---

## 💡 Indicadores Visuales

### Confianza de Predicción
```
100% █████████████ Verde ✅ (Muy seguro)
 92% ██████████░░ Verde ✅ (Seguro)
 70% ███████░░░░░ Amarillo ⚠️ (Moderado)
 50% █████░░░░░░░ Amarillo ⚠️ (Incierto)
 30% ███░░░░░░░░░ Rojo ❌ (Poco seguro)
```

### Tipos de Mensaje
```
🤖 Bot message      │ Gris claro, izquierda
────────────────────┼─────────────────────
👤 User message     │ Azul, derecha
────────────────────┼─────────────────────
⚠️ Error message    │ Rojo, centro
────────────────────┼─────────────────────
ℹ️ System message   │ Azul claro, centro
```

---

## 🔔 Estados de Interfaz

### Cargando
```
[Escribe tu pregunta...]
                     [⏳ Enviar] (desactivado)
```

### Listo
```
[Escribe tu pregunta...]
                     [✓ Enviar] (activo)
```

### Error
```
[Escribe tu pregunta...]
                     [✓ Enviar] (activo)

❌ Error de conexión. Revisa tu internet.
```

### Procesando
```
Bot: ⏳ Procesando tu pregunta...
```

---

## 🎯 Elementos Interactivos

### Botones
```
ESTADO NORMAL:
┌──────────────────┐
│  👨‍🎓 Soy Estudiante │
└──────────────────┘

ESTADO HOVER:
┌──────────────────┐
│  👨‍🎓 Soy Estudiante │ (Más brillante)
└──────────────────┘

ESTADO CLICK:
┌──────────────────┐
│  👨‍🎓 Soy Estudiante │ (Presionado)
└──────────────────┘
```

### Input Text
```
NORMAL:
┌────────────────────────┐
│ Escribe tu pregunta... │
└────────────────────────┘

ENFOCADO:
┌────────────────────────┐
│ Escribe tu pregunta... │ (Outline azul)
└────────────────────────┘

ESCRITO:
┌────────────────────────┐
│ Me gusta programar     │ (Con texto)
└────────────────────────┘
```

---

## 📊 Estructura Visual de Mensaje Bot

```
┌─────────────────────────────────────────┐
│                                         │
│ Bot: 💻 **Ingeniería de Sistemas**     │
│                                         │
│ 📝 Descripción:                        │
│ Desarrollo de software, programación y │
│ gestión de sistemas informáticos      │
│                                         │
│ 💪 Habilidades requeridas:             │
│ • Lógica                               │
│ • Programación                         │
│ • Resolución de problemas              │
│ • Análisis                             │
│                                         │
│ 🎯 Campos de aplicación:               │
│ • Software • Web • Apps • BD          │
│                                         │
│ 🔒 Confianza: 92%                     │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🌈 Paleta de Colores Completa

```
Primario
████ #667eea (Azul)

Secundario
████ #764ba2 (Púrpura)

Acentos
████ #f093fb (Rosa)
████ #f5576c (Rojo)
████ #50e3c2 (Turquesa)

Neutral
████ #ffffff (Blanco)
████ #f4f4f9 (Gris muy claro)
████ #e0e0e0 (Gris claro)
████ #999999 (Gris medio)
████ #666666 (Gris oscuro)
████ #333333 (Gris muy oscuro)

Feedback
████ #4caf50 (Verde - éxito)
████ #ff9800 (Naranja - advertencia)
████ #f44336 (Rojo - error)
████ #2196f3 (Azul - información)
```

---

## 🎭 Pantallas Alternativas

### Cuando Modelo No Está Entrenado
```
╔════════════════════════════════════╗
║  📚 Asesoramiento para Estudiantes  ║
╠════════════════════════════════════╣
║                                    ║
║ Bot: ⚠️ El modelo aún no ha sido   ║
║ entrenado. Por favor, comparte     ║
║ tus intereses para ayudarte mejor. ║
║ ¿Qué te apasiona?                  ║
║                                    ║
│ [Escribe tu pregunta...]    [Enviar]
╚════════════════════════════════════╝
```

### Cuando No Hay Conexión
```
╔════════════════════════════════════╗
║  📚 Asesoramiento para Estudiantes  ║
╠════════════════════════════════════╣
║                                    ║
║ ❌ Error: No pude conectar con     ║
║ el servidor. Verifica que el       ║
║ backend (pantalla negra) está      ║
║ corriendo: uvicorn main:app ...    ║
║                                    ║
│ [Escribe tu pregunta...]    [Enviar]
╚════════════════════════════════════╝
```

---

## 🎬 Transiciones Visuales

### Cambio de Pantalla
```
LOBBY                CHAT
┌─────────┐         ┌─────────┐
│ 🎓      │ ──────► │ 📚 Chat │
│ [Est]   │ FADE   │ [Msg]   │
│ [Vis]   │ (200ms)│ [Input] │
└─────────┘         └─────────┘
```

### Entrada de Mensaje
```
           ▼ (Aparece)
    ┌──────────────┐
    │ Bot: Nuevo   │
    │ mensaje      │ SLIDE-IN (300ms)
    │ llega        │
    └──────────────┘
```

### Auto-scroll
```
┌─────────────────────┐
│ Mensaje antiguo      │
├─────────────────────┤
│ Mensaje antiguo      │
├─────────────────────┤
│ Nuevo mensaje ◄──┐  │
│                  │ SCROLL AUTO
│ (Siempre visible)│  │
└─────────────────────┘
```

---

## 🎨 Conclusión Visual

Tu interfaz es:
- ✅ **Moderna**: Gradientes y animaciones
- ✅ **Profesional**: Colores coordinados
- ✅ **Intuitiva**: Flujo claro
- ✅ **Responsive**: En cualquier dispositivo
- ✅ **Accesible**: Buena legibilidad
- ✅ **Atractiva**: Elemento emoji personalizan

**¡Una interfaz de nivel profesional!** 🚀

---

**Versión**: 2.0
**Tipo**: Guía Visual
**Estado**: ✅ Completado
