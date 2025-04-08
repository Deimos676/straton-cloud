async def process_prompt(prompt: str) -> str:
    # Lógica temporal. Esto luego se conecta a OpenAI.
    if "hora" in prompt.lower():
        from datetime import datetime
        return f"La hora actual es {datetime.now().strftime('%H:%M:%S')}"
    
    return f"Procesando tu solicitud: '{prompt}'"
