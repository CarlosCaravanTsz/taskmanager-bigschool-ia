# TaskManager BigSchool IA

## Descripción

TaskManager BigSchool IA es una aplicación de consola para la gestión de tareas, que permite agregar, listar, completar y eliminar tareas. Además, integra inteligencia artificial (OpenAI) para desglosar tareas complejas en subtareas simples y accionables, facilitando la organización y el seguimiento de actividades.

## Características

- **Gestión de tareas**: Añade, lista, completa y elimina tareas fácilmente desde la terminal.
- **Desglose inteligente de tareas**: Utiliza la API de OpenAI para dividir tareas complejas en subtareas simples.
- **Persistencia**: Las tareas se guardan automáticamente en un archivo `tasks.json`.
- **Interfaz sencilla**: Menú interactivo por consola.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias:
	```
	pip install -r requirements.txt
	```
3. Crea un archivo `.env` en la raíz del proyecto y agrega tu clave de API de OpenAI:
	```
	OPENAI_API_KEY=tu_clave_aqui
	```

## Uso

Ejecuta la aplicación principal:
```
python main.py
```
Sigue las instrucciones del menú para gestionar tus tareas.

## Estructura del Proyecto

- `main.py`: Interfaz principal de usuario.
- `task_manager.py`: Lógica de gestión y persistencia de tareas.
- `ai_service.py`: Integración con OpenAI para desglosar tareas.
- `tasks.json`: Archivo donde se almacenan las tareas.
- `test_ai_service.py`: Pruebas para la integración de IA.
- `pyproject.toml`: Configuración del proyecto.
- `README.md`: Este archivo.

## Contribución

¡Las contribuciones son bienvenidas! Por favor, abre un issue o pull request para sugerencias o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT.
