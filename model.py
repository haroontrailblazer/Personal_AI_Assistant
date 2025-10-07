import ollama

model_description = input("Enter a brief description of the model: ")
assistant_name = input("Enter a name for the model: ")
ollama.create(
    model=assistant_name,
    from_="deepseek-r1:latest",
    system=model_description,
    parameters={"temperature": 0.2, "top_p": 0.5},
    stream=False
)

msg_input = input("Ask Anything ")
res = ollama.chat(model=assistant_name,messages=[{'role':'user','content':msg_input}])
print(res['messege']['content'])