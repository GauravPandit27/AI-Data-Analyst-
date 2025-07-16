
# 🤖 AI Data Analyst – No-Code, Beginner-Friendly Data Insights

Turn raw spreadsheets into simple, clear insights using **AI** – no data science skills needed.

![AI Analyst Banner](https://img.shields.io/badge/Made%20With-Streamlit-blue?style=for-the-badge)
![LLM Powered](https://img.shields.io/badge/LLM-LLaMA3%208B-Groq-orange?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

---

## ✨ What It Does

Upload one or more **CSV** or **Excel** files and let the AI:

* ✅ Understand what the data is about
* ✅ Describe each column in plain English
* ✅ Spot missing or weird values
* ✅ Share **real-world observations** like trends, top performers, or outliers
* ✅ Suggest **practical business decisions** from the data

> Ideal for beginners, business owners, or non-tech teams who want **smart summaries** from complex datasets.

---

## 📦 Features

* **Multiple File Uploads**
* **Automatic EDA** (Preview, Stats, Histograms, Correlations)
* **LLM-Powered Interpretation** (via Groq + LLaMA3-8B)
* **Beginner-Friendly Insights**
* **Plain Language Explanations**
* **Beautiful Streamlit UI**

---

## 🚀 Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-demo-link-if-hosted)

---

## 🛠️ Tech Stack

| Component       | Tech                        |
| --------------- | --------------------------- |
| Frontend        | Streamlit                   |
| Backend / LLM   | Groq API + LLaMA3-8B        |
| Data Processing | Pandas, Matplotlib, Seaborn |
| File Support    | CSV, Excel (.xlsx)          |

---

## 📂 Folder Structure

```
├── app.py                   # Main Streamlit app
├── constants.py             # API key for Groq
├── requirements.txt         # Dependencies
└── README.md                # This file
```

---

## 🔐 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/ai-data-analyst.git
cd ai-data-analyst
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your Groq API key**
   In `constants.py`, add your Groq key:

```python
groq_key = "your_groq_api_key_here"
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## 🧠 Sample Prompt Used

The LLM is prompted as:

> “You are the world’s smartest and most beginner-friendly data scientist. The user doesn't understand technical terms...”

Then it's asked to:

* Describe the dataset
* Explain each column
* Spot issues
* Give 3–5 real insights
* Suggest how it can be used for decisions

---

## 📌 Use Case Ideas

* 📈 Startup founders reviewing sales logs
* 🏪 Retail owners analyzing store data
* 🧑‍🏫 Educators tracking student performance
* 💸 Finance folks reviewing expenses
* 🤓 Students learning how AI understands data

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Built with 💡 by [Gaurav Pandit](https://linkedin.com/in/gaurav-pandit-gp07) — empowering non-tech users with AI superpowers.

---

Want a badge-ready cover image or project card for LinkedIn too? Just say the word.
