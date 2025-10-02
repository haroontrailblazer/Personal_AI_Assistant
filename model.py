import ollama 

model_description = input("Enter a brief description of the model: ")
modelfile=f"""
FROM deepseek-r1:latest
SYSTEM {model_description}
PARAMETER temperature 0.6
PARAMETER top_p 0.9
MAX_TOKENS 1024
"""

assistant_name = input("Enter the name of the assistant: ")
import ollama

ollama.create(
    model=assistant_name,
    template=modelfile
)

msg_input = input("Ask Anything ")
res = ollama.chat(model=assistant_name,messages=[{'role':'user','content':msg_input}])
print(res['content'])