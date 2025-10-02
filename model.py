import ollama 
import os

model_description = input("Enter a brief description of the model: ")
modelfile=f"""
FROM deepseek-r1:latest
SYSTEM {model_description}
PARAMETER temperature 0.6
PARAMETER top_p 0.9
MAX_TOKENS 1024
"""

assistant_name = input("Enter the name of the assistant: ")
ollama.create(model=assistant_name, modelfile=modelfile,stream=False)

msg_input = input("Ask Anything ")
res = ollama.chat(model=assistant_name,messege=[{'role':'user','content':msg_input}])
print(res)