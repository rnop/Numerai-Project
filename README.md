# Numerai Tournament

This repository provides Jupyter Notebooks to implement tools for analyzing and modeling the Numerai dataset (v4.2 Rain).

### Notebooks

#### Train an XGBoost model using HyperOpt and MLFlow
This notebook provides a template to train an XGBoost regressor whose hyperparameters are tuned using Bayesian Optimization using the open-sourced HyperOpt library. MLFlow is used for model tracking to efficiently log the performance of different combinations of hyperparameter values during optimization. 

#### Local MMC Computation
A major change coming in 2024 is the re-introduction of Meta Model Contribution (MMC) as a primary performance and payout metric. Per Numerai, MMC is the **covariance** of a model's prediction with the true target. This notebook allows us to calculate how much your model contributes to the overall Meta Model Correlation to the target if Numerai increases the model's stake by a small amount. This metric encourages users to build models that are highly correlated with the target but are also less correlated with the predictions of the Meta Model.

#### Upcoming Tools
- Era Based Time Series Cross-Validation
- LightGBM + HyperOpt + MLFlow
- Update feature-target correlation analysis to v4.2
