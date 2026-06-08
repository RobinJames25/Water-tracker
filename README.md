# 💧 Neuron Water Tracker

An AI-powered hydration tracking application that helps users monitor 
their daily water intake and receive intelligent feedback powered by 
a Large Language Model (LLM) agent.

## 🚀 Features
- 🤖 AI Agent powered by Groq (LLaMA 3.3) via LangChain
- 📊 Interactive dashboard built with Streamlit
- 🗄️ PostgreSQL database hosted on Neon
- 📈 Visual water intake history with charts
- 🔐 Secure environment variable management

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| AI Agent | LangChain + Groq (LLaMA 3.3-70b) |
| Frontend | Streamlit |
| Backend | Python, FastAPI |
| Database | PostgreSQL (Neon) |
| ORM | SQLAlchemy + psycopg2 |
| Environment | Conda, python-dotenv |

## ⚙️ Setup
1. Clone the repository
2. Create a conda environment: `conda create --name water-tracker python=3.11`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `secrets.toml.example` to `secrets.toml` and fill in your credentials
5. Run the app: `streamlit run dashboard.py`

## 🌐 Live Demo
[View on Streamlit Cloud](https://your-app-url.streamlit.app)
