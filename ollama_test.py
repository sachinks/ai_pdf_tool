import ollama

response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Summarize AI in 2 lines'}]
)

print(response['message']['content'])