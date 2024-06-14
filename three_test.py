# import ollama

# response = ollama.generate(
#     model="llama3",
#     prompt="necesito un script en python para una funcion que sume dos numeros",
#     options={"temperature": 0.1}
# )

# print(response)


from ollama import Client

client = Client()

response = client.generate(
    model="llama3",
    prompt="necesito un script en python para una funcion que sume dos numeros",
    options={"temperature": 0.1}
)

print(response)
