AI Resume Analyzer – Bulk Resume Parsing & CSV Export
📌 Project Description

Organizations receive resumes in large volumes and in multiple formats, making manual screening slow and inconsistent. This project provides an AI-powered resume analysis system that automatically processes bulk resumes from ZIP files and converts them into structured, analysis-ready data.

Using LangChain and Large Language Models, the system extracts key candidate details and exports them as a CSV file through an intuitive Streamlit interface.

🔍 Core Capabilities

Upload a ZIP file containing multiple resumes

Automatically process PDF and DOCX formats

Extract structured candidate information using LLMs

Enforce consistent output using predefined schemas

Generate a downloadable CSV for easy review

🧠 Why This Project

Manual resume screening is time-consuming and error-prone

Resume layouts vary widely across candidates

Inconsistent data makes filtering and comparison difficult

HR teams need scalable, standardized resume insights

This solution demonstrates how LLMs can bring structure and reliability to real-world HR workflows.

⚙️ System Workflow

User uploads a ZIP file of resumes

Files are extracted and text is parsed

LangChain prompts guide the LLM to extract fixed fields

Structured outputs are validated against a schema

All records are consolidated into a CSV file

📑 Extracted Information

Candidate Name

Email & Phone

Technical Skills

Education Details

Work Experience Summary

LinkedIn URL

GitHub URL

🛠 Technology Stack

Python – Core implementation

Streamlit – User interface

LangChain – Prompt orchestration & structured output

LLMs – Resume intelligence

Pandas – Data aggregation & CSV export

PyPDF2 / python-docx – Resume text extraction

▶️ Getting Started
Install Dependencies
``` bash
pip install -r requirements.txt
```
Launch Application
``` bash
streamlit run app.py
```

Upload a ZIP file containing resumes and download the generated CSV after processing.

📊 Output Format

The system produces a single CSV file with structured candidate data, suitable for:

Resume filtering

Candidate comparison

ATS integration

Analytics workflows

🚀 Applications

Automated Resume Screening

HR Data Pipelines

Campus Recruitment Systems

AI-assisted Hiring Tools

🎓 Skills Demonstrated

LLM-based information extraction

Schema-driven structured outputs

Prompt engineering for reliability

Building production-ready AI applications

✅ Conclusion

This project demonstrates how LangChain and Large Language Models can be effectively used to automate bulk resume analysis and transform unstructured documents into structured, reliable data. By enforcing schema-based outputs and providing CSV exports through a Streamlit interface, the system delivers a scalable, accurate, and efficient solution for modern resume screening and HR automation workflows.
