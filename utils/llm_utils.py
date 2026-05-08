import ollama


MODEL_NAME = "mistral"


def generate_response(prompt,
                      model=MODEL_NAME):
    """
    Send prompt to Ollama model.
    """

    try:

        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        raise Exception(f"LLM generation failed: {e}")