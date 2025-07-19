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
File Structure
'''
JOb-Recommender/
src
├── helper.py               
├── mcp_server.py       
├── job_api.py        
├── venv     
├── app.py   
├── .env                 
├── .gitignore          
├── requirements.txt     
└── README.md            


'''

## ⚙️ Setup Instructions

### 🔑 1. Clone the Repo

```bash
git clone https://github.com/shariar26868/JOb-Recommender.git
cd JOb-Recommender
