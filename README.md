# Machine Learning

My hands-on notebooks from learning machine learning, written as I go. I'm moving from RPA development into AI engineering, and this repo is where the practice code lives.

Each folder is one concept: a small dataset, a Jupyter notebook, and the results it produced.

![Linear regression on home prices](assets/linear_regression_plot.png)

## What's inside

### Supervised ML: Regression

| Notebook | What it does | Result |
|---|---|---|
| [Linear Regression](Regression/Linear%20Regression/linear_regression_single_variable.ipynb) | Predicts home price (₹ lakhs) from area alone with `y = mx + b` | `y = 0.0517·area + 18.05`; 2000 sq ft → ₹121.4L |
| [Multiple Linear Regression](Regression/Multiple%20Linear%20Regression/linear_regression_multiple_variables.ipynb) | Adds bedrooms as a second feature, then works out the prediction by hand with `m1·x1 + m2·x2 + b` to confirm it matches `model.predict()` | 1500 sq ft, 3 BHK → ₹106.83L (both ways) |
| [Train Test Split](Regression/Train%20Test%20Split/train_test.ipynb) | Uses the UCI Auto MPG dataset (398 cars, 7 features) to predict fuel efficiency. Fills missing horsepower values with the mean, splits the data 80/20 and evaluates on the test set | R² = **0.85**, MSE = 8.2 |
| [One Hot Encoding](Regression/One%20hot%20Encoding/one_hot_encoding.ipynb) | Converts the text `locality` column to numbers using `pd.get_dummies(drop_first=True)` to avoid the dummy-variable trap, then trains and tests the model | R² = **0.86**; same house costs ~₹48L more in Banjara Hills than in Mankhal |

### Exercises

| Notebook | What it does |
|---|---|
| [Exercise 1: Weather](Excercises/Excercise%201/assignment.ipynb) | Predicts daily temperature from hours of sunlight (single variable), then from sunlight + humidity (multiple variables) |

## Key concepts

- **Linear regression** fits a line (or a plane, with more features) through the data. `model.predict()` simply plugs new values into the learned equation.
- **Cost function:** MSE is the standard choice for linear regression. It's differentiable everywhere and penalises large errors more heavily, which works well with gradient descent.
- **Gradient descent** finds the best slope and intercept step by step, instead of trying every possible combination.
- **Train/test split:** a model is judged on data it hasn't seen. `random_state` keeps the split reproducible.
- **Evaluation metrics:** MAE, MSE and R². R² is the easiest to read: 1.0 is a perfect fit and 0 means the model is no better than predicting the average.
- **Encoding:** label encoding for ordered categories, one-hot encoding for unordered ones. Dropping one dummy column avoids multicollinearity.
- **Overfitting vs underfitting** (high variance vs high bias). L1 (Lasso) and L2 (Ridge) regularization help control overfitting.

## Tech stack

Python 3.13 · pandas · scikit-learn · Jupyter

## Run it locally

```bash
git clone https://github.com/hauntedguest/machine-learning.git
cd machine-learning
python -m venv .venv && source .venv/bin/activate
pip install pandas scikit-learn jupyter
jupyter notebook
```

Open a notebook from inside its own folder so the relative CSV paths resolve. The Train Test Split notebook downloads the Auto MPG dataset from the UCI repository, so it needs an internet connection.

## Roadmap

- [x] Regression: linear, multiple, train/test split, metrics, one-hot encoding
- [ ] Classification
- [ ] Unsupervised learning
- [ ] Moving on to LLM engineering: RAG and agents

Learning path: [Codebasics AI Engineering & Data Science Bootcamp](https://codebasics.io).
