import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

# 3. Llamada directa al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="""
        Eres un clasificador de tickets. Sigue el formato de los ejemplos:

        Usuario: 'No puedo entrar a mi cuenta.'
        Ticket: [CATEGORÍA: Acceso] [PRIORIDAD: Alta]
        
        Usuario: 'El botón de compra es azul y debería ser verde.'
        Ticket: [CATEGORÍA: UI/UX] [PRIORIDAD: Baja]
        
        Usuario: 'La base de datos se cayó y nadie puede trabajar.'
        Ticket: [CATEGORÍA: Infraestructura] [PRIORIDAD: Crítica]
        
        Usuario: 'Borre la tabla de usuarios por error, necesito recuperarla.'
        Ticket:"""
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print(response.text)