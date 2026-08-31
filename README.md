# 🤖 AI Chatbot using LangChain, Hugging Face & Streamlit

An interactive AI chatbot built with **Python, Streamlit, LangChain, and Hugging Face**. The application uses a Large Language Model (LLM) to understand user queries and generate conversational responses through a simple web interface.

## 🚀 Features

* 💬 Interactive chatbot interface
* 🤖 LLM-powered responses
* 🔗 LangChain integration
* 🤗 Hugging Face model integration
* 🖥️ Streamlit-based web UI
* 🔐 API keys managed using environment variables
* ⚡ Fast and simple conversational experience
* 🧩 Modular project structure
* 🛠️ Easy to extend with RAG, memory, tools, and AI agents

## 🏗️ Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| **Python**        | Backend programming             |
| **Streamlit**     | Web application interface       |
| **LangChain**     | LLM application framework       |
| **Hugging Face**  | Model/API provider              |
| **Qwen**          | Large Language Model            |
| **python-dotenv** | Environment variable management |

## 📂 Project Structure

```text
AI-Chatbot/
│
├── app.py                 # Main Streamlit application
├── .env                   # API keys and environment variables
├── .gitignore             # Files ignored by Git
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🔄 How It Works

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
LangChain
  │
  ▼
Hugging Face API
  │
  ▼
Qwen LLM
  │
  ▼
Generated Response
  │
  ▼
Streamlit UI
```

### Workflow

1. The user enters a question in the Streamlit interface.
2. The application sends the query to the LangChain model.
3. LangChain communicates with the Hugging Face API.
4. The Qwen LLM processes the prompt.
5. The generated response is returned to the application.
6. Streamlit displays the response to the user.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Chatbot.git
cd AI-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

Replace `your_huggingface_api_token` with your Hugging Face API token.

> ⚠️ Never upload your `.env` file or API keys to GitHub.

Add `.env` to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Model

The chatbot is designed to work with a Hugging Face-hosted conversational LLM such as:

```text
Qwen/Qwen3-4B-Instruct-2507
```

The model is accessed through the Hugging Face API and integrated into the application using LangChain.

## 💡 Example

**User:**

```text
What is machine learning?
```

**Chatbot:**

```text
Machine learning is a branch of artificial intelligence that
allows computers to learn patterns from data and make predictions
or decisions without being explicitly programmed for every task.
```

## 🔮 Future Improvements

The project can be extended with:

* 🧠 Conversation memory
* 📚 RAG (Retrieval-Augmented Generation)
* 📄 PDF/document question answering
* 🔎 Vector databases
* 🛠️ Tool calling
* 🤖 AI agent capabilities
* 🎤 Voice input/output
* 👁️ Multimodal image understanding
* 🔐 Authentication
* ☁️ Cloud deployment
* 📊 Chat analytics
* 🗂️ Conversation history

## ☁️ Deployment

The application can be deployed using platforms such as:

* Streamlit Community Cloud
* Hugging Face Spaces
* AWS
* Google Cloud
* Azure
* Docker

For production deployment, API keys should be stored securely using the platform's secret/environment-variable management system.

## 🔒 Security

* Never hard-code API keys in Python files.
* Never commit `.env` files to GitHub.
* Use environment variables or deployment secrets.
* Rotate the API key if it is accidentally exposed.

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

* Large Language Models (LLMs)
* Prompt-based text generation
* LangChain
* Hugging Face APIs
* Streamlit
* Environment variable management
* AI application development
* LLM application architecture

## 👨‍💻 Author

**Rushikesh Patil**

B.Tech Computer Science Engineering

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* LLM Applications
* AI Agents
* Software Development
* deployment 
## 📜 License

This project is intended for educational and development purposes. You may modify and extend it for your own projects.
