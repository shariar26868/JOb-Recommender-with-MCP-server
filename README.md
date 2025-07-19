# 💼 AI Job Recommender

An intelligent job-finding assistant that scrapes job listings and recommends the best matches based on your skills and preferences — powered by OpenAI, Apify, and Groq.

---

## 🚀 Features

- 🔍 Scrapes job listings automatically using **Apify**
- 💡 Smart matching and summarization with **Groq**
- ⚙️ Fast backend processing via `mcp_server.py` using **Modal's MCP** system
- 📄 Extracts useful data: Job title, link, company, skills, and responsibilities
- 🌐 Streamlit Web App Interface
- 🔒 Uses `.env` file for all API keys

---

## 🧰 Tech Stack

- `Python 3.10+`
- `Streamlit`
- `OpenAI API` (for summarization)
- `Apify API` (for job scraping)
- `Groq API` (optional GPT-4 alternative)
- `Modal MCP` (`mcp_server.py`) for backend job processing
- `.env` for key management

---
```text
JOb-Recommender/
├── src/
│   ├── helper.py           # Functions for PDF extraction and Groq API calls
│   ├── job_api.py         # Apify LinkedIn job scraping logic
│   └── mcp_server.py      # Modal MCP backend for job processing
├── .env                   # Environment variables (API keys) - NOT tracked by Git
├── .gitignore             # Git ignore rules (excludes venv/, .env, etc.)
├── app.py                 # Streamlit web app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
---

## ⚙️ Setup Instructions

### 🔑 1. Clone the Repo

```bash
git clone https://github.com/shariar26868/JOb-Recommender.git
cd JOb-Recommender
