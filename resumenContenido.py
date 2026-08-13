import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

# 3. Llamada directa al servicio de modelos
texto = """Cliente: Hola, tengo un problema con mi pedido. No llegó a tiempo y necesito una solución.
Agente nivel 1: Lamento escuchar eso. ¿Podría proporcionarme su número de pedido para que pueda verificarlo?
Cliente: Sí, mi número de pedido es 12345.
Agente nivel 1: Gracias por la información. Permítame revisar el estado de su pedido.
Agente nivel 1: He verificado su pedido y veo que hubo un retraso en el envío. Lamento mucho la inconveniencia.
Agente nivel 1: ¿Le gustaría que le ofrezca un reembolso o un nuevo envío sin costo adicional?
Cliente: Preferiría un nuevo envío, por favor."""

prompt = f"""Resume la conversación entre el cliente y el agente nivel 1 en cuatro puntos claves: {texto}"""

# configuración del modelo
configuracion = types.GenerateContentConfig(
    max_output_tokens=500, # Limite de tokens de salida a 500 tokens, no fuerza a modelo a usar toda esa cantidad, es un límite máximo.
    temperature=1.0 # Controla la aleatoriedad de la salida del modelo. Un valor más alto (por ejemplo, 1.0) hace que el modelo sea más creativo y diverso en sus respuestas, mientras que un valor más bajo (por ejemplo, 0.2) hace que el modelo sea más determinista y repetitivo.
)

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=configuracion
    )

except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")
# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print(response.text)
    print("-" * 30)
    print(f"Tokens de entrada (prompt): {response.usage_metadata.prompt_token_count}")
    print(f"Tokens de salida (response): {response.usage_metadata.candidates_token_count}")
    print(f"Costo de salida: ${response.usage_metadata.candidates_token_count * 0.0000015:.6f} USD")