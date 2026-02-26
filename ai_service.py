from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(task):
  
  if not client.api_key:
    return ["Error: OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."]
  try:
    prompt = f"""Desglosa la isguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
    
    Tarea: {task.description}
    
    Formato de respuesta:
    - Subtarea 1
    - Subtarea 2
    - Subtarea 3
    
    Responde solo con la lista de subtareas, una por linea, empezando cada linea con un guion
    """
    
    params = {
      "model": "gpt-5",
      "messages": [
        {"role": "system", "content": "Eres un asistente que ayuda a desglosar tareas complejas en subtareas simples y accionables."},
        {"role": "user", "content": prompt}
      ],
      # "max_completion_tokens": 300,
      "verbosity": "medium",
      "reasoning_effort": "minimal"
    }
    
    response = client.chat.completions.create(**params)
    content = [line.strip() for line in response.choices[0].message.content.split('\n') if line.strip()]
    
  except Exception as e:
    return [f"Error: {str(e)}"]