# 🤖 Personal AI Assistant

A modern AI-powered Personal Assistant built using  **LangChain**, **OpenRouter**,**LangGRaph**, **Gradio**, and **Google APIs**. The assistant can understand natural language, delegate tasks to specialized AI agents, send Gmail emails, manage Google Calendar events, and provide an intuitive chat-based interface.

---

## 🚀 Features

- 🧠 Multi-Agent Architecture using LangGraph
- 🤖 Supervisor Agent for intelligent task routing
- 📧 Gmail Integration
  - Send emails using natural language
- 📅 Google Calendar Integration
  - Create calendar events
  - Schedule meetings
- 💬 Modern Gradio Chat Interface
- ☁️ Google OAuth Authentication
- ⚡ Powered by OpenRouter LLMs
- 🛠 Modular and Scalable Architecture

---

## 🏗 Project Architecture

```
                    User
                      │
                      ▼
             Personal AI Assistant
                      │
                      ▼
              Supervisor Agent
               (LangGraph)
           ┌─────────┴─────────┐
           ▼                   ▼
     Email Agent         Calendar Agent
           │                   │
           ▼                   ▼
      Gmail API        Google Calendar API
```

---

## 📁 Project Structure

```
personal_assistant/

├── agents/
│   ├── supervisor.py
│   ├── email_agent.py
│   └── calendar_agent.py
│
├── integrations/
│   ├── auth.py
│   ├── gmail.py
│   └── google_calendar.py
│
├── tools/
│   ├── email_tools.py
│   └── calendar_tools.py
│
├── prompts/
│
├── ui/
│   └── app.py
│
├── credentials.json      # (Not included in repository)
├── token.json            # (Generated locally)
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.10+
- LangChain
- LangGraph
- OpenRouter API
- Google Gmail API
- Google Calendar API
- Google OAuth 2.0
- Gradio
- Pydantic

---


## 🔑 Google API Setup

Create a project in **Google Cloud Console**.

Enable:

- Gmail API
- Google Calendar API

Create OAuth Client Credentials.

Download the credentials file and rename it to:

```
credentials.json
```

Place it in the project root.

Run the application once to authenticate.

A `token.json` file will automatically be generated.

> **Do not upload `credentials.json` or `token.json` to GitHub.**

---

## 🔐 Environment Variables

Create a `.env` file.

```env
OPENROUTER_API_KEY=your_api_key
```

---

## ▶️ Running the Application

```bash
python ui/app.py
```

The application will launch at

```
http://127.0.0.1:7860
```

---

## 💬 Example Prompts

### Gmail

```
Send an email to john@example.com saying hello.
```

```
Draft an email informing the team about tomorrow's meeting.
```

---

### Calendar

```
Schedule a meeting tomorrow at 3 PM.
```

```
Create an event for Project Review on Friday at 2 PM.
```

---

## ✨ Current Capabilities

- Natural language understanding
- Intelligent task routing
- Gmail email sending
- Google Calendar event creation
- Chat interface
- Google OAuth authentication

---


## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hamna Bukhari**

Email: *hamnabukhari10@gmail.com*



---

⭐ If you found this project helpful, consider giving it a star.
