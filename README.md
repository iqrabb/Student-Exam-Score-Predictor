# Student Exam Score Predictor

A Streamlit application that estimates a student's exam score from five user-provided learning and study-related inputs. The app loads a saved regression model and displays its predicted score with a simple performance-band message.

> **Project type:** Educational machine-learning demonstration. The prediction is an estimate, not a guaranteed exam result or a validated measure of a student's ability.

## Features

- Streamlit interface with a responsive two-column input form.
- Inputs for learning mode, subject, study hours, retention score, and focus level.
- Converts categorical inputs to numeric values before inference.
- Loads a saved model with Joblib.
- Displays a predicted exam score and a simple score-band message.

## Technology

- Python
- Streamlit
- Pandas
- Joblib
- scikit-learn and NumPy (listed in the project dependencies)

The application loads the serialized model file `student_exam_predictor.pkl`. The current repository does not include the training code needed to independently confirm the estimator configuration.

## How it works

1. The user selects a learning mode and subject.
2. The user enters study hours, retention score, and focus level.
3. The app maps the two categorical inputs to numeric values.
4. It creates a one-row Pandas DataFrame with the five model input features.
5. The saved model predicts an exam score.
6. The app displays the estimate and a simple message based on the predicted score.

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/iqrabb/Student-Exam-Score-Predictor.git
cd Student-Exam-Score-Predictor
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

The app expects `student_exam_predictor.pkl` in the repository root. Only load Joblib/pickle artifacts from trusted sources because deserialization can execute arbitrary code.

## Input features

| Feature | Values |
|---|---|
| Learning mode | Offline or Online |
| Subject | English, History, Math, Programming, or Science |
| Study hours | 1.0–8.0 hours |
| Retention score | 40–100 |
| Focus level | 40–100 |

## Repository contents

- `app.py` — Streamlit interface, input encoding, and prediction display.
- `student_exam_predictor.pkl` — serialized model artifact.
- `requirements.txt` — Python dependencies.
- `README.md` — project documentation.

## Evaluation and reproducibility

The repository currently contains the app and saved model, but not the dataset, model-training script, or evaluation notebook. As a result, model training and reported performance cannot be reproduced from the committed files alone. The previous README also mentioned a Streamlit Cloud deployment but did not provide a verifiable public app URL, so no live deployment is claimed here.

To strengthen this project, add the dataset source and license, a reproducible training pipeline, a held-out test evaluation, and metrics such as MAE, RMSE, and R². Include a clear explanation of the target score scale and how the model was validated.

## Limitations

- A predicted score is only as reliable as the data and model used to train it.
- The app does not show a prediction interval or uncertainty estimate.
- The performance messages are simple thresholds in the UI, not independently validated educational assessments.
- Do not use this tool to make consequential decisions about a student's academic progression.

---

Developed as an educational demonstration of regression-model inference and Streamlit application development.
