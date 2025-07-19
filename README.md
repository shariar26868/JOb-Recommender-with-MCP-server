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
## 📸 Screenshots

<img width="600" height="auto" alt="Screenshot 2025-07-20 033108" src="https://github.com/user-attachments/assets/949e2fae-c2a0-4ec1-a9d3-158370409030" />
<img width="600" height="auto" alt="Screenshot 2025-07-20 033216" src="https://github.com/user-attachments/assets/d8d9b8b1-f515-42bb-b476-bc65b64dcf60" />
<img width="600" height="auto" alt="Screenshot 2025-07-20 033327" src="https://github.com/user-attachments/assets/3e7a6fe4-cab6-4653-8347-1258cf0e9bad" />
<img width="600" height="auto" alt="Screenshot 2025-07-20 035043" src="https://github.com/user-attachments/assets/b2f3e46a-3427-4e68-85c9-6675501f97a1" />

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
│── mcp_server.py          # Modal MCP backend for job processing
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
