# 🎮 Mini AI Agent

A lightweight AI agent built with Python that can interact with the local environment through tools such as file management and command execution.

The project is designed as a small, extensible agent framework that can receive a user request, reason about the required actions, execute available tools, and return the results through an AI model.

## ✨ Features

- 🤖 AI-powered agent loop
- 🛠️ Tool/function calling
- 📁 Read and write files
- 📋 List files and directories
- 💻 Execute terminal commands
- 🔄 Multi-step task execution
- 🔐 Environment-based API key configuration
- 🧩 Modular project structure
- ⚡ Dependency management with `uv`

## 📁 Project Structure

```text
.
├── main.py
├── src/
│   └── ...
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── .python-version
└── README.md
```

## 🚀 Requirements

- Python 3.12+
- An OpenRouter API key
- [uv](https://docs.astral.sh/uv/) for dependency management

## ⚙️ Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd <project-directory>
```

Install the project dependencies:

```bash
uv sync
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

> Never commit your `.env` file or expose your API key publicly.

## ▶️ Running the Agent

Run the application with:

```bash
uv run main.py
```

The agent will start an interactive session and prompt you for a request.

Example:

```text
Hi! How can I assist you today?
> Create a new Python file called hello.py
```

The agent can then determine which available tools are required to complete the task.

## 🧰 Available Tools

The agent can interact with the local environment through tools such as:

| Tool | Description |
|------|-------------|
| `list_files` | Lists files and directories |
| `read_files` | Reads the contents of a file |
| `write_files` | Creates or modifies files |
| `run_command` | Executes terminal commands |

Additional tools can be added as the project evolves.

## 🏗️ Architecture

The agent follows a simple tool-calling workflow:

```text
User Request
     │
     ▼
┌─────────────┐
│     Agent   │
└──────┬──────┘
       │
       ▼
   AI Model
       │
       ├─── Final Response
       │
       └─── Tool Call
              │
              ▼
        Execute Function
              │
              ▼
        Tool Result
              │
              └──────────► AI Model
```

The agent continues this cycle until the model produces a final response or the configured iteration limit is reached.

## 🔐 Security

This project provides tools capable of interacting with the local filesystem and executing terminal commands.

**Do not run the agent with untrusted instructions or unrestricted system privileges.**

In particular, `run_command` can potentially execute arbitrary commands depending on its implementation. Consider restricting allowed commands and filesystem access before using the agent in a production environment.

## 🧪 Development

Install dependencies and synchronize the development environment with:

```bash
uv sync
```

Run the application:

```bash
uv run main.py
```

Before committing changes, verify that:

- The application starts correctly.
- Tool calls execute as expected.
- Tool results are returned to the model.
- The agent stops correctly after completing a task.
- Errors are handled without causing infinite tool-call loops.

## 🛣️ Future Improvements

Possible improvements include:

- Better conversation memory
- More robust tool-call validation
- Tool execution timeouts
- Command allowlists
- Improved error recovery
- Automated tests
- Streaming responses
- Multiple AI model support
- Richer terminal output
- Persistent conversation history

## 📄 License

This project is provided for educational and development purposes. Add an appropriate license here if you plan to distribute the project publicly.

---

Built with **Python**, **OpenRouter**, and **uv**.