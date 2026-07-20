from agents.supervisor import supervisor

print("🤖 Personal Assistant")
print("Type 'exit' to quit.\n")

# Store the conversation
messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add the user's message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Send the entire conversation to the agent
    response = supervisor.invoke({
        "messages": messages
    })

    # Get the assistant's reply
    assistant_message = response["messages"][-1]

    # Save the assistant's reply
    messages.append(assistant_message)

    # Print the reply
    if isinstance(assistant_message.content, list):
        print("\nAssistant:", assistant_message.content[0]["text"])
    else:
        print("\nAssistant:", assistant_message.content)

    print()