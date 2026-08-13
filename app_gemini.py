import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")

    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents="Preséntate brevemente como un asistente de IA configurado para apoyar el curso de 'Desarrollo de aplicaciones con IA.'"
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")

if __name__ == "__main__":
 ejecutar_consulta()