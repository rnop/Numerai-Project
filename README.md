# Numerai Tournament (updated for the 1k+ feature release) 
## Introduction
Numerai is a global hedge fund that trades the stock market based on crowd-sourced knowledge of data scientists all over the world. They provide expensive, high-quality financial datasets for free to participants in their data science tournament who build and train models and submit their predictions to Numerai every round. If participants are confident about the predictive power of their models, they can stake them with cryptocurrency ($NMR) and potentially earn money for correct predictions during live trading rounds.   

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
