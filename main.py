from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import router

# 1. Inicializar DB al arrancar
init_db()

# 2. Crear App
app = FastAPI(title="Chatbot Modular MLOps")

# 3. Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Incluir las rutas de la API
app.include_router(router)

# 5. Servir el Frontend (HTML) en la raíz "/"
@app.get("/", response_class=HTMLResponse)
def read_root():
    # Lee el archivo index.html y lo devuelve como respuesta web
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Error: No se encontró el archivo index.html</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)