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

### 🔍 Job Search Form
![Search Form](https://raw.githubusercontent.com/user-attachments/assets/949e2fae-c2a0-4ec1-a9d3-158370409030)

### 📋 Result View - Cards
![Result Cards](https://raw.githubusercontent.com/user-attachments/assets/3e7a6fe4-cab6-4653-8347-1258cf0e9bad)

### 🧠 Summary Section
![Summary Output](https://raw.githubusercontent.com/user-attachments/assets/d8d9b8b1-f515-42bb-b476-bc65b64dcf60)

### ⚙️ Modal Job Summary
![Modal Backend](https://raw.githubusercontent.com/user-attachments/assets/313fb872-1f32-4ade-b942-064754c632a0)

### ✅ Success Log / Console
![Log Output](https://raw.githubusercontent.com/user-attachments/assets/b2f3e46a-3427-4e68-85c9-6675501f97a1)


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
