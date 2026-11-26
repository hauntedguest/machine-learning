# AI & Machine Learning

My complete AI/ML learning repository, from math and statistics through machine learning, deep learning and NLP, to Generative AI and agentic systems.

I'm an automation engineer (RPA) moving into AI engineering. Everything here is hands-on: each topic has a notebook, the dataset it uses, and the results it produced. I'm following the [Codebasics AI Engineering & Data Science Bootcamp](https://codebasics.io) and adding my own notes and experiments along the way.

![Linear regression on home prices](assets/linear_regression_plot.png)

## Progress

| # | Module | Status | Highlights |
|---|---|---|---|
| 01 | [Math & Statistics](01-math-and-statistics) | ✅ Done | Probability, distributions, hypothesis testing, A/B testing |
| 02 | [Machine Learning](02-machine-learning) | 🟡 In progress | **Regression ✅** · **Classification 🟡** · Ensembles · Unsupervised · ML lifecycle |
| 03 | [Deep Learning](03-deep-learning) | ⏳ Not started | PyTorch, CNNs, transfer learning, RNN/LSTM, Transformers |
| 04 | [NLP](04-nlp) | ⏳ Not started | Text preprocessing, TF-IDF, embeddings, spaCy, Hugging Face, BERT |
| 05 | [Gen AI & Agentic AI](05-gen-ai-and-agentic-ai) | ⏳ Not started | LLMs, RAG, LangChain, LangGraph, CrewAI, MCP, AI agents |
| ⭐ | [Projects](projects) | ⏳ Not started | End-to-end, deployed projects for each module |

## Latest work

### Classification

| Notebook | What it does | Result |
|---|---|---|
| [Logistic regression (binary)](02-machine-learning/02-classification/01-Logistic-Regression) | Predicts whether someone owns a car from their monthly salary, then recalculates the probability by hand with the sigmoid function to confirm it matches `predict_proba()` | Accuracy **0.89** (8 of 9 test rows) |
| [Multiclass logistic regression](02-machine-learning/02-classification/02-Multi-Class-Classification) | Classifies iris flowers into 3 species from sepal and petal measurements, with a classification report and confusion matrix heatmap | Accuracy **0.98** on 45 test flowers |
| [Support Vector Machine](02-machine-learning/02-classification/03-SVM) | Classifies 900 raisins (Kecimen vs Besni) from 7 shape features, comparing RBF and linear kernels with and without `StandardScaler`, then wraps scaler + SVM in a `Pipeline` | RBF accuracy 0.83 → **0.88** with scaling |
| [Naive Bayes spam classifier](02-machine-learning/02-classification/04-Naive-Bayes-SMS%20Spam%20Classifier) | Classifies 5,572 SMS messages as spam or ham using `CountVectorizer` word counts and `MultinomialNB`, then rebuilds it as a two-step `Pipeline` | Accuracy **0.99**, spam F1 0.97 |
| [Decision tree](02-machine-learning/02-classification/05-%20Decision%20Tree) | Predicts whether a salary is above 100k from company, job and degree (16 rows), comparing gini and entropy and printing the tree with `export_text` | Same tree with both criteria (no test split, the dataset is tiny) |

### Regression

| Notebook | What it does | Result |
|---|---|---|
| [Linear regression](02-machine-learning/01-regression/01-linear-regression) | Predicts home price from area with `y = mx + b` | `price = 0.0517·area + 18.05` |
| [Multiple linear regression](02-machine-learning/01-regression/02-multiple-linear-regression) | Adds bedrooms as a feature, then recalculates the prediction by hand to confirm it matches `model.predict()` | ₹106.83L both ways |
| [Train-test split & metrics](02-machine-learning/01-regression/03-train-test-split) | Predicts car fuel efficiency on the UCI Auto MPG dataset (398 cars), with missing-value handling and an 80/20 split | **R² = 0.85**, MSE = 8.2 |
| [One-hot encoding](02-machine-learning/01-regression/04-one-hot-encoding) | Encodes a text `locality` column with `drop_first=True` to avoid multicollinearity | **R² = 0.86** on test data |
| [L1 & L2 regularization](02-machine-learning/01-regression/05-L1-L2-Regularisation) | Compares plain linear regression with Lasso (L1) and Ridge (L2) on a dataset with 150 features and only 150 training rows, a setup that encourages overfitting | R² **0.74 → 0.99** (Lasso), 0.95 (Ridge) |
| [Exercise: weather](02-machine-learning/01-regression/exercises/01-weather-temperature) | Predicts daily temperature from sunlight hours, then from sunlight + humidity | |

See the [Machine Learning module](02-machine-learning) for the full topic list and notes.

## Repository structure

```
├── 01-math-and-statistics/
├── 02-machine-learning/
│   ├── 01-regression/
│   │   ├── 01-linear-regression/
│   │   ├── 02-multiple-linear-regression/
│   │   ├── 03-train-test-split/
│   │   ├── 04-one-hot-encoding/
│   │   ├── 05-L1-L2-Regularisation/
│   │   └── exercises/
│   └── 02-classification/
│       ├── 01-Logistic-Regression/
│       ├── 02-Multi-Class-Classification/
│       ├── 03-SVM/
│       ├── 04-Naive-Bayes-SMS Spam Classifier/
│       └── 05- Decision Tree/
├── 03-deep-learning/
├── 04-nlp/
├── 05-gen-ai-and-agentic-ai/
├── projects/
└── assets/
```

Each module folder has its own README with the topics it covers and a checklist of my progress. Inside a module, every topic gets its own folder with the notebook and its data.

## Tech stack

**Used so far:** Python · pandas · scikit-learn · Matplotlib · Seaborn · Jupyter

**Coming up in this repo:**

| Area | Tools |
|---|---|
| Data & math | NumPy |
| Machine learning | XGBoost, MLflow |
| Deep learning | PyTorch, Optuna |
| NLP | spaCy, Hugging Face Transformers |
| Gen AI & agents | LangChain, LangGraph, CrewAI, ChromaDB, MCP, Amazon Bedrock AgentCore |
| Apps & deployment | Streamlit, FastAPI |

## Run it locally

```bash
git clone https://github.com/hauntedguest/machine-learning.git
cd machine-learning
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open each notebook from its own folder so the relative data paths resolve. Some notebooks download public datasets (for example UCI Auto MPG), so they need an internet connection.

## Connect

I post what I learn on [LinkedIn](https://www.linkedin.com/in/pranav-gupta-264438228/). Feedback and suggestions are welcome; feel free to open an issue.
