# Conexion con la API de Gemini

Ejemplo en Python para conectarse a la API de Google Gemini usando el SDK oficial `google-genai` y una clave almacenada en variables de entorno.

## Requisitos

- Python 3.10 o una version posterior.
- Una clave de API de Gemini creada desde [Google AI Studio](https://aistudio.google.com/apikey).

## Instalacion

1. Clona el repositorio y entra en su carpeta:

   ```bash
   git clone https://github.com/ChrlyDev/conexion-gemini-python.git
   cd conexion-gemini-python
   ```

2. Crea y activa un entorno virtual:

   En Windows PowerShell:

   ```powershell
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```

   En macOS o Linux:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Configuracion de la clave

1. Copia `.env.example` como `.env`.
2. Reemplaza el valor de `GEMINI_API_KEY` por tu clave real:

   ```env
   GEMINI_API_KEY=tu_clave_real
   ```

El archivo `.env` esta excluido por `.gitignore`. Nunca publiques claves de API en el repositorio ni las incluyas directamente en el codigo.

## Ejecucion

Con el entorno virtual activo, ejecuta:

```bash
python app_gemini.py
```

El programa enviara una consulta al modelo `gemini-3.1-flash-lite` e imprimira la respuesta en la terminal.

Tambien se incluye `app_text.py`, un ejemplo de clasificacion de tickets:

```bash
python app_text.py
```

## Estructura principal

```text
.
|-- app_gemini.py       # Consulta basica a Gemini
|-- app_text.py         # Clasificacion de tickets con Gemini
|-- requirements.txt    # Dependencias del proyecto
|-- .env.example        # Plantilla de configuracion
`-- README.md           # Instrucciones de uso
```

## Publicar en GitHub

Desde la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Agrega conexion inicial con la API de Gemini"
git branch -M main
git remote add origin https://github.com/ChrlyDev/conexion-gemini-python.git
git push -u origin main
```

Crea antes un repositorio vacio con el nombre `conexion-gemini-python` en tu cuenta de GitHub. No selecciones la opcion de agregar README, `.gitignore` o licencia, porque estos archivos ya estan incluidos localmente.

## Seguridad

La clave de API es una credencial privada. Si una clave real se compartio o se incluyo en un repositorio, revocala desde Google AI Studio y genera una nueva antes de continuar.
