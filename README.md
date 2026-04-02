# Smart Email Auto-Responder

An AI-powered email automation workflow that monitors Gmail, 
classifies incoming emails using Gemini LLM API, and sends 
professional auto-replies automatically.

## Tech Stack
- n8n (workflow automation)
- Gemini API (email classification + reply generation)
- Gmail (trigger + auto-reply)
- Google Sheets (logging)
- Slack (notifications)
- Python (email preprocessing)

## Workflow
Gmail Trigger → Python Clean → Gemini API → Gmail Reply → Google Sheets → Slack

## Setup
1. Clone this repo
2. Copy `.env` and fill in your API keys
3. Import `n8n/workflow.json` into your n8n instance
4. Connect your Gmail, Google Sheets and Slack credentials
5. Activate the workflow
