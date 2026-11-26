# 02 · Machine Learning

Supervised and unsupervised machine learning with scikit-learn, from the math behind linear regression to ensembles, model evaluation and the full ML project lifecycle.

✅ = done · 📓 = has a notebook in this repo

## 1. Regression ✅

| Topic | Status | Notebook |
|---|---|---|
| Introduction to ML · supervised vs unsupervised · classification vs regression | ✅ | |
| Simple linear regression | ✅ | 📓 [01-linear-regression](01-regression/01-linear-regression) |
| Multiple linear regression | ✅ | 📓 [02-multiple-linear-regression](01-regression/02-multiple-linear-regression) |
| Cost function (MAE, MSE) | ✅ | |
| Derivatives, partial derivatives, chain rule | ✅ | |
| Gradient descent | ✅ | |
| Model evaluation: train-test split, MSE, MAE, R² | ✅ | 📓 [03-train-test-split](01-regression/03-train-test-split) |
| Data preprocessing: one-hot encoding | ✅ | 📓 [04-one-hot-encoding](01-regression/04-one-hot-encoding) |
| Polynomial regression | ✅ | |
| Overfitting and underfitting | ✅ | |
| L1 and L2 regularization (Lasso, Ridge) | ✅ | 📓 [05-L1-L2-Regularisation](01-regression/05-L1-L2-Regularisation) |
| Bias-variance trade-off | ✅ | |
| Exercise: weather temperature prediction | ✅ | 📓 [exercises/01-weather-temperature](01-regression/exercises/01-weather-temperature) |

### Key takeaways

- `model.predict()` just plugs new inputs into the learned equation `y = m1·x1 + m2·x2 + … + b`. I verified this by hand.
- MSE is the usual cost function for linear regression. It's differentiable everywhere and penalises large errors more heavily. MAE is the better choice when the data has many outliers.
- Gradient descent finds the best `m` and `b` step by step instead of trying every combination. Learning rate and epochs control how it converges.
- Always evaluate on data the model hasn't seen. `random_state` keeps the split reproducible.
- One-hot encode nominal categories and drop one dummy column. If you know N−1 of the columns you already know the last one, which causes multicollinearity.
- High bias leads to underfitting and high variance leads to overfitting. Regularization (Ridge/Lasso) helps control overfitting. With 150 features and only 150 training rows, plain linear regression scored R² 0.74 on test data, while Lasso scored 0.99 and Ridge 0.95.
- Memory trick for bias-variance, **BUVO**: high **B**ias → **U**nderfitting, high **V**ariance → **O**verfitting.
- Fix underfitting with more relevant features, a more complex model or less regularization. Fix overfitting with more data, fewer features or more regularization.
- Ridge (L2) shrinks coefficients towards zero. Lasso (L1) can shrink some to exactly zero, which removes features that don't help.

## 2. Classification

- [ ] Logistic regression: binary classification
- [ ] Model evaluation: accuracy, precision, recall, F1 score, confusion matrix
- [ ] Logistic regression: multiclass classification
- [ ] Cost function: log loss
- [ ] Support Vector Machine (SVM)
- [ ] Data preprocessing: scaling
- [ ] scikit-learn pipelines
- [ ] Naive Bayes
- [ ] Decision tree
- [ ] Handling class imbalance

## 3. Ensemble learning

- [ ] Introduction to ensemble learning
- [ ] Majority voting, average and weighted average
- [ ] Bagging and Random Forest
- [ ] Boosting: AdaBoost
- [ ] Gradient Boosting
- [ ] XGBoost

## 4. Model evaluation and tuning

- [ ] ROC curve and AUC
- [ ] Cost-benefit analysis using ROC
- [ ] K-fold and stratified K-fold cross-validation
- [ ] Hyperparameter tuning
- [ ] Variance Inflation Factor (VIF)

## 5. Unsupervised learning

- [ ] K-means clustering

## 6. ML project lifecycle

- [ ] 10 stages of an AI project lifecycle
- [ ] Requirements and scope of work (SOW)
- [ ] Data collection, data cleaning and EDA
- [ ] Feature engineering
- [ ] Model selection, training and fine-tuning
- [ ] Model deployment
- [ ] Monitoring and feedback with MLOps

## Projects for this module

- [ ] Healthcare premium prediction (regression)
- [ ] Beverage price range prediction (classification)

See [projects](../projects).
