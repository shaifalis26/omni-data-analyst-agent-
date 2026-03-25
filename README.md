# 🤖 Omni Data Analyst Agent

[

![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)

](https://colab.research.google.com/github/shaifalis26/omni-data-analyst-agent-/blob/main/Omni_Data_Analyst_Agent.ipynb)

> Ask anything in plain English — get SQL, charts & forecasts automatically!

---

## 🎯 What It Does

Type: *"Show me monthly revenue growth"*
The agent will:
- ✅ Connect to the database
- ✅ Write its own SQL query
- ✅ Execute it automatically
- ✅ Generate a visualization
- ✅ Forecast future trends with ML

---

## 🏗 Architecture
User NL Prompt
│
▼
Claude API ──tool_call──▶ Tool Registry (MCP-style)
├─ execute_sql()  ← SQLite
├─ list_tables()  ← Schema
├─ plot_chart()   ← Matplotlib
└─ forecast()     ← Scikit-learn
---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| 🧠 Brain | Claude AI (Anthropic) — Tool Use |
| 🔌 Bridge | MCP-style Tool Registry |
| 🗄 Database | SQLite + Pandas |
| 📊 Charts | Matplotlib |
| 🔮 Forecast | Scikit-learn |
| 🖥 Frontend | Streamlit + ngrok |

---

## 🚀 How to Run

1. Open in **Google Colab** (button above)
2. Run **Cell 1** — installs packages
3. Run **Cell 2** — seeds database
4. Run **Cells 3-5** — sets up tools
5. Add your **ngrok token** in Cell 6
6. Click **Run All**
7. Open the live link → paste **Anthropic API key** → done!

---

## 💡 Example Queries

- *"Show monthly revenue as a line chart"*
- *"Which product category has highest sales?"*
- *"Forecast revenue for next 6 months"*
- *"What is the customer churn rate?"*

---

## 📁 Files

| File | Description |
|------|-------------|
| `Omni_Data_Analyst_Agent.ipynb` | Main notebook |
| `requirements.txt` | Python dependencies |
