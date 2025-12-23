import os
import zipfile
import shutil
import pymupdf
import pandas as pd
import streamlit as st

from typing import TypedDict, Optional, List
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="AI Resume Analyzer",page_icon=" ",layout="wide")

st.title("AI Resume Analyzer")
st.write("Upload a ZIP file containing resumes (PDF)")

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("gemini")

model = ChatGoogleGenerativeAI( model="gemini-2.5-flash-lite",temperature=0.2)

class DataFormat(TypedDict):
    name: str
    summary: str
    experience: Optional[int]
    projects: List[str]
    skills: List[str]
    links: List[str]

structured_model = model.with_structured_output(DataFormat)

TEMP_DIR = "temp_resumes"
os.makedirs(TEMP_DIR, exist_ok=True)

uploaded_zip = st.file_uploader("Upload Resume ZIP File",type=["zip"])

if uploaded_zip:

    shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True)

    zip_path = os.path.join(TEMP_DIR, uploaded_zip.name)

    with open(zip_path, "wb") as f:
        f.write(uploaded_zip.read())

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(TEMP_DIR)

    st.success("ZIP extracted successfully")

    results = []

    with st.spinner("Processing resumes..."):
        for root, dirs, files in os.walk(TEMP_DIR):
            for file in files:
                if file.lower().endswith(".pdf"):
                    file_path = os.path.join(root, file)

                    doc = pymupdf.open(file_path)
                    text = ""

                    for page in doc:
                        text += page.get_text()

                    response = structured_model.invoke(
                        f"""
                        Extract the following from the resume:
                        - Name
                        - Professional summary
                        - Total years of experience (number only)
                        - Projects (project names or short descriptions as a list)
                        - Skills
                        - Any links (LinkedIn, GitHub, Portfolio)

                        Resume text:
                        {text}
                        """
                    )

                    response["file_name"] = file
                    results.append(response)

    st.success(f"Processed {len(results)} resumes")

    if results:
        df = pd.DataFrame(results)

        st.subheader("Extracted Resume Data")
        st.dataframe(df, use_container_width=True)

        csv_data = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="resume_output.csv",
            mime="text/csv"
        )