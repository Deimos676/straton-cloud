async def process_prompt(prompt: str) -> str:
    # Temporary logic. This will later connect to OpenAI.
    if "time" in prompt.lower():
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    return f"Processing your request: '{prompt}'"
