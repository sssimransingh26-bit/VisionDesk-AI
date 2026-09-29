# 🦺 VisionDesk AI

### AI-Powered Visual Data Analytics and Business Intelligence Platform

VisionDesk AI is a multimodal workplace safety intelligence platform that combines **computer vision, document intelligence, RAG, LLMs, and analytics** to help monitor PPE compliance and provide safety-related insights.

The system can analyze construction-site images/videos, retrieve relevant safety rules from uploaded documents, answer questions using retrieved knowledge, track compliance history, and generate safety reports.

---

## 🚀 Key Features

### 👷 PPE Detection

* Detects PPE equipment using **YOLOv8**
* Supports image and video analysis
* Identifies PPE violations such as missing helmets, goggles, gloves, etc.
* Displays confidence scores and detection results
* Generates a compliance summary

### 📄 Document Intelligence

* Supports PDF, TXT, and DOCX documents
* Extracts and cleans document text
* Splits documents into searchable chunks
* Stores document embeddings in **ChromaDB**
* Performs semantic search over safety manuals and reports

### 🤖 AI Safety Assistant

* Uses **LangGraph** to orchestrate the AI workflow
* Retrieves relevant safety documents before answering
* Uses **Gemini** for natural-language responses
* Can combine document knowledge with PPE detection results
* Provides document/source references in responses

### 📊 Safety Dashboard

* Tracks analyzed images and videos
* Displays compliance rate
* Shows total violations
* Visualizes violations by type
* Shows violation trends over time
* Collects user feedback on AI responses

### 📋 Automated Reports

* Generates safety compliance summaries
* Creates downloadable PDF reports
* Provides violation statistics
* Allows scan data to be downloaded as CSV

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │    Streamlit UI      │
                    │      app.py          │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ YOLOv8     │  │ Document    │  │ LangGraph   │
       │ PPE        │  │ Processing  │  │ AI Agent    │
       │ Detection  │  │ + ChromaDB  │  │             │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              │                ▼                ▼
              │         Safety Knowledge    Gemini LLM
              │              Base
              │                                 │
              └──────────────┬──────────────────┘
                             ▼
                    ┌──────────────────┐
                    │ Storage + Report │
                    │ Dashboard / PDF  │
                    └──────────────────┘
```

---

## 🛠️ Tech Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Frontend / Dashboard | Streamlit             |
| Programming Language | Python                |
| Computer Vision      | YOLOv8, OpenCV        |
| Image Processing     | Pillow, NumPy         |
| Document Processing  | PyPDF, python-docx    |
| Embeddings           | Sentence Transformers |
| Vector Database      | ChromaDB              |
| AI / LLM             | Google Gemini         |
| Agent Workflow       | LangGraph             |
| Data Storage         | CSV / Pandas          |
| PDF Reports          | FPDF                  |
| Version Control      | Git & GitHub          |

---

## 📁 Project Structure

```text
VisionDesk-AI/
│
├── app.py                    # Streamlit dashboard
├── vision.py                 # PPE detection and video processing
├── agent.py                  # LangGraph AI agent
├── knowledge_base.py         # ChromaDB knowledge base
├── llm.py                    # Gemini integration
├── storage.py                # Scan and feedback storage
├── report.py                 # PDF report generation
├── evaluate.py               # Retrieval evaluation
│
├── src/
│   └── rag/
│       ├── documents.py      # Document loading, cleaning and chunking
│       └── vector_store.py   # Vector store utilities
│
├── data/
│   ├── safety_manual.pdf
│   └── sample_safety_manual.txt
│
├── best.pt                   # Trained YOLOv8 model
├── requirements.txt
├── ppe_training.ipynb
├── README.md
└── .gitignore
```

---

## 🔄 Project Milestones

### Milestone 1 — Computer Vision

Implemented PPE detection using a trained YOLOv8 model.

The system detects PPE-related classes and identifies violations based on classes beginning with `no_`.

---

### Milestone 2 — Document Intelligence & RAG

Implemented:

```text
Document
   ↓
Text Extraction
   ↓
Text Cleaning
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Semantic Retrieval
```

The retrieval system was evaluated using 10 safety-related questions and achieved:

**100% retrieval accuracy** on the project evaluation set.

---

Milestone 3 — LLM + Agentic RAG

Implemented a LangGraph workflow:

Question
   ↓
Retrieve relevant documents
   ↓
Combine document + vision context
   ↓
Gemini
   ↓
Safety Answer

The agent is designed to answer using retrieved safety documents and can incorporate PPE detection findings.
---
Milestone 4 — Dashboard & Business Intelligence

Implemented:

Scan history
Compliance KPIs
Violation analytics
User feedback tracking
PDF report generation
CSV export
Streamlit dashboard
Integrated image/video detection
Document upload and search
AI safety assistant
---
⚙️ Installation
1. Clone the repository
git clone https://github.com/sssimransingh26-bit/VisionDesk-AI.git
cd VisionDesk-AI
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure Gemini

Create a .env file:

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.8-flash

Do not commit your .env file to GitHub.

5. Run the application
streamlit run app.py
---
📊 Retrieval Evaluation

Run:

python evaluate.py

The evaluation tests the semantic retrieval system against predefined workplace safety questions.

Current project evaluation:

Retrieval accuracy: 100%
Target: 85%
---
🔐 Security

Sensitive credentials are excluded using .gitignore.

The following are intentionally not committed:

.env
venv/
chroma_db/
logs/
runs/
output/
__pycache__/
---
🎯 Project Goal

VisionDesk AI aims to connect visual workplace observations with organizational safety knowledge.

Instead of treating computer vision, documents, and AI as separate systems, the platform combines them into one workflow:

See → Retrieve → Reason → Analyze → Report
---
👩‍💻 Author

Simran Singh

