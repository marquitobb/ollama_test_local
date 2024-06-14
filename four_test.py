from langchain.chains import LLMChain
from langchain.llms import Ollama


# Crear un objeto de modelo LLaMA3 utilizando Ollama
llama_model = Ollama.load_model("llama3")

# Definir la cadena de lenguaje en LangChain
llama_chain = LLMChain(
    llm=llama_model,
    input="Tu entrada de texto aquí",
    output="Tu salida de texto esperada aquí"
)

# Ejecutar la cadena de lenguaje
respuesta = llama_chain.run("Tu pregunta o entrada aquí")
print(respuesta)
