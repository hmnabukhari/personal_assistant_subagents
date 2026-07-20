from agents.supervisor import supervisor

print("🤖 Personal Assistant")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = supervisor.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        }
    )

    last_message = response["messages"][-1]

    if isinstance(last_message.content, list):
        print("\nAssistant:", last_message.content[0]["text"])
    else:
        print("\nAssistant:", last_message.content)

    print()