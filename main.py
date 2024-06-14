from langchain_community.llms import Ollama

llm = Ollama(
    model="llama3"
)  # assuming you have Ollama installed and have llama3 model pulled with `ollama pull llama3 `

llm.invoke("Tell me a joke")



# query = "Tell me a joke"

# for chunks in llm.stream(query):
#     print(chunks)

# query = "¿Cuál es el clima hoy?"

# response = llm.stream(query)


# for chunks in response:
#     print(chunks)

# for chunks in llm.stream(query):
#     print(chunks)