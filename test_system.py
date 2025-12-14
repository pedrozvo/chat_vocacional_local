"""
Script de prueba para validar que CareerGuide está funcionando correctamente.
Ejecutar después de que el servidor uvicorn esté corriendo.
"""

import requests
import json
from time import sleep

API_BASE = "http://127.0.0.1:8000"

def print_header(title):
    """Imprime un encabezado"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def test_server_connection():
    """Prueba la conexión con el servidor"""
    print_header("1. PRUEBA DE CONEXIÓN")
    try:
        response = requests.get(API_BASE, timeout=2)
        print("✅ Servidor conectado correctamente")
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        print("   Asegúrate de ejecutar: uvicorn main:app --reload")
        return False

def test_system_status():
    """Obtiene el estado del sistema"""
    print_header("2. ESTADO DEL SISTEMA")
    try:
        response = requests.get(f"{API_BASE}/sistema/estado")
        if response.ok:
            status = response.json()
            print(f"Estado: {status['estado']}")
            print(f"Datos de entrenamiento: {status['datos_entrenamiento']}")
            print(f"Carreras disponibles: {status['carreras_disponibles']}")
            print(f"Modelo listo: {'✅ Sí' if status['modelo_listo'] else '⚠️ No (necesita datos)'}")
            
            if not status['modelo_listo']:
                print("\n💡 Sugerencia: Ejecuta 'python initialize_training_data.py'")
            return status
        else:
            print(f"❌ Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_list_careers():
    """Lista todas las carreras disponibles"""
    print_header("3. CARRERAS DISPONIBLES")
    try:
        response = requests.get(f"{API_BASE}/carreras")
        if response.ok:
            data = response.json()
            print(f"Total de carreras: {data['total']}\n")
            for i, carrera in enumerate(data['carreras'], 1):
                print(f"  {i}. {carrera}")
            return data['carreras']
        else:
            print(f"❌ Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_chat(message, user_type="estudiante"):
    """Prueba el endpoint de chat"""
    print_header(f"4. PRUEBA DE CHAT ({user_type})")
    print(f"Mensaje: '{message}'")
    print()
    
    try:
        response = requests.post(
            f"{API_BASE}/chat",
            json={
                "mensaje": message,
                "tipo_usuario": user_type
            }
        )
        if response.ok:
            data = response.json()
            print(f"Respuesta del Bot:")
            print(f"{data['respuesta']}")
            print(f"\nCarrera Recomendada: {data.get('carrera_recomendada', 'Ninguna')}")
            print(f"Confianza: {data.get('confianza', 0):.2%}")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_career_info(career_name):
    """Obtiene información detallada de una carrera"""
    print_header(f"5. INFORMACIÓN DE CARRERA: {career_name}")
    
    try:
        response = requests.post(
            f"{API_BASE}/carrera-info",
            json={"carrera": career_name}
        )
        if response.ok:
            data = response.json()
            if "error" in data:
                print(f"❌ {data['error']}")
                return False
            else:
                print(f"Descripción: {data['descripcion']}\n")
                print(f"Habilidades requeridas:")
                for skill in data['habilidades']:
                    print(f"  • {skill}")
                print(f"\nCampos de trabajo:")
                for field in data['campos']:
                    print(f"  • {field}")
                return True
        else:
            print(f"❌ Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_training():
    """Prueba el endpoint de entrenamiento"""
    print_header("6. PRUEBA DE ENTRENAMIENTO")
    
    test_data = {
        "texto": "Me gusta crear software y programar en Python",
        "categoria": "Ingeniería de Sistemas"
    }
    
    print(f"Agregando: '{test_data['texto']}'")
    print(f"Categoría: {test_data['categoria']}\n")
    
    try:
        response = requests.post(
            f"{API_BASE}/entrenar",
            json=test_data
        )
        if response.ok:
            result = response.json()
            print(f"✅ Estado: {result['status']}")
            print(f"Mensaje: {result['message']}")
            print(f"Muestras entrenadas: {result['samples']}")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║          🧪 PRUEBAS DE CAREERGUIDE - SISTEMA IA           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    results = {
        "Conexión": False,
        "Estado": False,
        "Carreras": False,
        "Chat": False,
        "Info Carrera": False,
        "Entrenamiento": False
    }
    
    # Test 1: Conexión
    if not test_server_connection():
        print("\n❌ No se puede continuar sin conexión al servidor")
        return
    results["Conexión"] = True
    
    # Test 2: Estado
    status = test_system_status()
    results["Estado"] = status is not None
    
    # Test 3: Lista de carreras
    careers = test_list_careers()
    results["Carreras"] = careers is not None
    
    # Test 4: Chat
    if careers:
        results["Chat"] = test_chat("Me interesa programar y el desarrollo de software")
    
    # Test 5: Información de carrera
    if careers:
        results["Info Carrera"] = test_career_info(careers[0])
    
    # Test 6: Entrenamiento
    results["Entrenamiento"] = test_training()
    
    # Resumen final
    print_header("RESUMEN DE PRUEBAS")
    total_tests = len(results)
    passed_tests = sum(1 for v in results.values() if v)
    
    for test_name, result in results.items():
        status = "✅ PASÓ" if result else "❌ FALLÓ"
        print(f"{status} - {test_name}")
    
    print(f"\nResultado: {passed_tests}/{total_tests} pruebas pasadas")
    
    if passed_tests == total_tests:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        print("✨ CareerGuide está listo para usarse")
    elif passed_tests > total_tests // 2:
        print("\n⚠️  ALGUNAS PRUEBAS FALLARON")
        print("💡 Ejecuta 'python initialize_training_data.py' para cargar datos iniciales")
    else:
        print("\n❌ HAY PROBLEMAS SERIOS")
        print("Revisa los errores arriba")
    
    print("\n🌐 Accede a: http://127.0.0.1:8000")
    print("📚 Documentación interactiva: http://127.0.0.1:8000/docs\n")

if __name__ == "__main__":
    try:
        run_all_tests()
    except KeyboardInterrupt:
        print("\n\n⚠️  Pruebas interrumpidas por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
