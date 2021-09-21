# Numerai Tournament (updated for the 1k+ feature release) 
## Introduction
Numerai is a hedge fund that trades the global markets based on models created by data scientists all over the world. Numerai is unique in that it provides free high-quality financial datasets that are worth millions of dollars to any user wanting to participate in their tournament. Users are able to build their own models on this anonymized and obfuscated dataset, submit their predictions, and follow their investment performance on the live stock market. If users are confident about their models, they are able to stake on them with real money using Numerai's cryptocurrency, Numeraire (NMR).

### About this Notebook
The purpose of this notebook is to provide an introduction on how to approach the main Numerai tournament using Google Colab Pro. Pro version is needed for the extra VRAM!

Alot of the code is taken from example scripts from Numerai's official GitHub here: https://github.com/numerai/example-scripts

What's included:
* how to read in the new Numerai data via API
* train a lightgbm model
* calculating predictions from the current round
* submit live rounds via API

### Libraries
* numpy
* pandas
* matplotlib
* seaborn
* lightgbm
* numerapi

### Disclaimer
**This model is not guaranteed to make you money.** I am currently not staking this particular model in the tournament. This notebook only serves to provide you an introduction to the tournament and to give some of my personal input on how to tackle this data science problem. 
