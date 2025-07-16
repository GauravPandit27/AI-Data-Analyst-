import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from langchain_groq import ChatGroq
from constants import groq_key  # Make sure this has your Groq API key

# 🔐 Initialize LLM
llm = ChatGroq(api_key=groq_key, model_name="llama3-8b-8192")

# 🎯 Streamlit Config
st.set_page_config(page_title="AI Data Analyst (Beginner Friendly)", layout="wide")
st.title("🤖 AI-Powered Data Analysis for Everyone")
st.markdown("Upload one or more CSV/Excel files and get clear, friendly insights — no data science knowledge needed!")

# 📁 Upload Files
uploaded_files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.divider()
        st.header(f"📄 File: `{file.name}`")

        # 🧾 Load file
        try:
            df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
        except Exception as e:
            st.error(f"❌ Failed to load {file.name}: {e}")
            continue

        # 🔍 Preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        # 📌 Basic Summary
        st.subheader("📌 Quick Stats (FYI)")
        st.write(df.describe())

        # 📉 Histograms
        st.subheader("📉 Data Distributions (Histograms)")
        numeric_cols = df.select_dtypes(include="number").columns
        for col in numeric_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col].dropna(), kde=True, ax=ax)
            ax.set_title(f"{col} - Value Distribution")
            st.pyplot(fig)

        # 🔗 Correlation Heatmap
        if len(numeric_cols) > 1:
            st.subheader("🔗 Correlation Between Numbers")
            fig, ax = plt.subplots(figsize=(10, 6))
            corr = df[numeric_cols].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

        # 🧠 LLM Analysis - Layman-Friendly Prompt
        st.subheader("🧠 Friendly AI Analysis")
        sample = df.head(100).to_csv(index=False)

        user_prompt = f"""
You are the world’s smartest and most beginner-friendly data scientist.

The person you're helping does **not** understand technical terms, so:
- Speak clearly and in plain English
- Use bullet points
- Give real business insight — not just stats

Here’s a sample from a dataset called **{file.name}** (CSV format):

{sample}

Please do the following in order:

1. 📘 Tell what this dataset is about (guess from column names & values)
2. 🔤 Describe what each column means in everyday terms
3. 🧼 Mention if there are missing or strange values
4. 📊 Give 3–5 interesting observations or patterns you noticed
   - Look for things like trends over time (sales going up or down), best-selling products, top-performing regions/managers, or big outliers
   - If there's a date column, check if things are improving or declining over time
5. 💡 Explain how this data can help in making decisions
   - Like how to improve sales, manage inventory, or reward high performers

Make your explanation simple, practical, and friendly — as if you're talking to a business owner, not a data scientist.

Avoid words like "skewness", "variance", "standard deviation", or "correlation" unless you explain them.
"""

        with st.spinner("🤔 AI is thinking in plain English..."):
            try:
                response = llm.invoke(user_prompt)
                st.markdown(response.content)
            except Exception as e:
                st.error(f"❌ LLM failed: {e}")
