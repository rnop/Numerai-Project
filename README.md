# Numerai Tournament
### Introduction
Numerai is a hedge fund that trades the global markets based on models created by data scientists all over the world. Numerai is unique in that it provides free high-quality financial datasets that are worth millions of dollars to any user wanting to participate in their tournament. Users are able to build their own models on this anonymized and obfuscated dataset, submit their predictions, and follow their investment performance on the live stock market. If users are confident about their models, they are able to stake on them with real money using Numerai's cryptocurrency, Numeraire (NMR).

### About this Notebook
It is much easier to run the notebook on Google Colab (Pro) because the library dependencies are much smoother. You may need to upgrade to colab pro as I have to get access to higher RAM and GPU capabilities.

The purpose of this notebook is to provide an introduction on how to approach the main Numerai tournament.

What's included:
* how to read in the Numerai data via API
* approaches to dimensionality reduction
* training an xgboost model 
* bayesian optimization techniques
* calculating predictions from the current round

### Libraries
* numpy
* pandas
* sklearn
* xgboost
* tensorflow
* bayesian-optimization
* numerapi

### Disclaimer
**This model is not guaranteed to make you money.** I am currently not staking this particular model in the tournament. This notebook only serves to provide you an introduction to the tournament and to give some of my personal input on how to tackle this data science problem. 

### One of my first models starting at round 256
* Consistent NMR payouts (none burned yet)
* Best corr placement at the top 0.8% of all models
* Best mmc placement at the top 1.3% of all models

![Image of Model1](https://github.com/rnop/nmr_tournament/blob/main/my_model1.png)

### One of my newest models in its first round (performance looks promising!)
* Consistently top 2% in corr AND mmc
* Best corr/mcc placement at top 0.0%

![Image of Model1](https://github.com/rnop/nmr_tournament/blob/main/my_model2.png)
