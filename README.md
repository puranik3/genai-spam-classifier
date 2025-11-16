# 📧 Spam Detector (Gemini + LangChain + Streamlit)

A lightweight, production-ready **Spam Detection App** built with:

* **Google Gemini 2.5 Flash**
* **LangChain (Pydantic Parsing)**
* **Streamlit UI**
* **Pandas for CSV batch processing**
* **Pydantic v2**
* **Python 3.11**

The app supports:

✔ **Single-message spam classification**
✔ **Batch CSV upload + classification**
✔ Strict **structured output enforcement** using `PydanticOutputParser`
✔ A clean Streamlit UI for real-time results

---

## 🚀 Features

### 🔍 **Single Message Classification**

Paste a message/email → get:

* Spam / Not Spam / Uncertain
* Risk Score (0–100)
* Reasons
* Red Flags
* Suggested Action

### 📁 **Batch Classification (CSV Upload)**

Upload a CSV file with one message per row → get:

* Auto-processed dataframe
* Label, risk score, flags, actions for each row

### 🔒 **Strict Pydantic Validation**

The output is forced into this schema:

```python
class SpamClassification(BaseModel):
    label: Literal["Spam", "Not Spam", "Uncertain"]
    reasons: List[str]
    risk_score: int            # 0 to 100
    red_flags: List[str]
    suggested_action: str
```

---

# 📦 Project Structure

```
.
├── app.py
├── config.py
├── requirements.txt
├── pipeline/
│   ├── chain.py
│   ├── wrapper.py
├── llm/
│   ├── models.py
│   ├── parser.py
│   ├── prompt_template.py
└── data/
```

---

# 🛠️ Setup Instructions (Python 3.11)

### 1️⃣ **Create a virtual environment**

```bash
python3.11 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 2️⃣ **Upgrade pip**

```bash
python3.11 -m pip install --upgrade pip
```

### 3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

> Your requirements include:
> `google-genai`, `streamlit`, `pandas`, `langchain`, `langchain-google-genai`, `pydantic`, `pyarrow`, `grpcio`

---

# 🔑 Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

The app loads it via:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

# ▶️ Running the App

Start Streamlit:

```bash
streamlit run app.py
```

This launches the web UI at:

```
http://localhost:8501
```

Use the two tabs:

* **Single Message** – paste text → get result
* **Batch CSV Upload** – upload CSV (1 column) → get table with predictions

---

# 📁 CSV Format for Batch Mode

Your CSV should look like:

```
message
"Congratulations! You won a prize"
"Your invoice is attached"
"Click here to claim your reward"
```

The app uses the **first column** automatically.

---

# ⚙️ How It Works (Internal Architecture)

### **1. Prompt Construction**

`prompt_template.py` inserts:

* system instruction
* format instructions from Pydantic parser
* the user message

### **2. LLM**

`models.py` loads Gemini:

```python
ChatGoogleGenerativeAI(model="gemini-2.5-flash")
```

### **3. PydanticOutputParser**

Enforces structured JSON.

### **4. Chain**

`prompt | llm | parser`

The output is **always a parsed Pydantic object**, not raw JSON.

---

# 🧪 Testing (Verified on Python 3.11)

This app has been tested on:

* macOS (Python 3.11 via Homebrew + Anaconda)
* Streamlit 1.47.1
* LangChain + Google GenAI 1.27.0
* Pydantic 2.11.7

---

# 📝 Troubleshooting

### ❌ *ValidationError: Field required*

Means Gemini didn’t output 100% of the schema.

Fix:

* Ensure your updated single-message prompt is applied (merged system message).

### ❌ *pip error building pandas*

Use Python **3.11**, not 3.12 or 3.13 (pandas 2.2.3 wheels unstable there).

You've already verified Python 3.11 works.

---

# ✔ Ready to Deploy

This project is fully ready for:

* local demos
* classroom training
* AI hands-on sessions
* extending into a backend service