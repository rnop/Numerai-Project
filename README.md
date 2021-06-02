# Numerai Tournament
### Introduction
Numerai is a hedge fund that trades the global markets based on models created by data scientists all over the world. Numerai is unique in that it provides free high-quality financial datasets that are worth millions of dollars to any user wanting to participate in their tournament. Users are able to build their own models on this anonymized and obfuscated dataset, submit their predictions, and follow their investment performance on the live stock market. If users are confident about their models, they are able to stake on them with real money using Numerai's cryptocurrency, Numeraire (NMR).

### My Numerai Models
I started building and submitting models at round 255 so I am relatively new to the Numerai tournament. I have three main models for the tournament that are all named after my cat Winston. 

**Model 1: SirWinstonPurchill** 
<br>https://numer.ai/sirwinstonpurrchill
* 2 Gold Medals (Top 1% in CORR and MMC)

![](numerai_goldmedals.png)

**Model 2: Unnamed**
* This is currently my best model in the tournament. Not making this public because of staking and anonymity. 
* I expect this model to jump the leaderboard after 20 rounds

![](model2.png)

**Model 3: Clowder** 
* This is an ensembled model from multiple models I created for the tournament. 
<br>https://numer.ai/clowder


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
