from agents.supervisor import supervisor

response = supervisor.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Schedule a meeting with Sarah on Friday at 2 PM."
            }
        ]
    }
)

last_message = response["messages"][-1]

if isinstance(last_message.content, list):
    print(last_message.content[0]["text"])
else:
    print(last_message.content)