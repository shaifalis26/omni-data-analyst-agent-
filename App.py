import streamlit as st
import sqlite3
import pandas as pd
import anthropic
import json
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from PIL import Image
from io import BytesIO

# ── Page Config ──────────────────────────
st.set_page_config(
    page_title="Omni Data Analyst",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Omni Data Analyst Agent")
st.caption("Natural language → SQL → Charts → Forecasts")

# ── Sidebar ──────────────────────────────
with st.sidebar:
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        placeholder="sk-ant-..."
    )
    st.markdown("### 💡 Try asking:")
    st.markdown("- Show monthly revenue as a line chart")
    st.markdown("- Which product has highest sales?")
    st.markdown("- Forecast revenue for next 6 months")
    st.markdown("- What is the customer churn rate?")

# ── Main Input ────────────────────────────
query = st.text_area(
    "Ask anything about your data",
    height=100,
    placeholder="e.g. Show me monthly revenue growth..."
)

if st.button("🚀 Analyze", type="primary"):
    if not api_key:
        st.error("Please enter your Anthropic API key!")
    else:
        st.info("Running in Google Colab-see notebook for full execution !")
