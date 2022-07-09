# Analysis of german rental data

## 1. Installations

| Library    | Version | Link                                                 |
| ---------- | ------- | ---------------------------------------------------- |
| Python     | 3.9.0   | https://www.python.org/downloads/release/python-390/ |
| pandas     | 1.4.2   | https://pandas.pydata.org/                           |
| seaborn    | 0.11.2  | https://seaborn.pydata.org/                          |
| numpy      | 1.22.4  | https://numpy.org/                                   |
| matplotlib | 3.5.2   | https://matplotlib.org/                              |

## 2. Project Motivation:

This project takes a look at the developement of rental prices over 3 years. Whereas rantal prices where fetched at 4 specific points of time (September 2018, May 2019, October 2019, Februar 2020) from https://immobilienscout24.de/. The dataset was available on [Kaggle](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany). The was analyzed folowing the crisp dm process.

In this project the following questions are tried being answered:

- Did price to rent change over time ?
- Is there a difference in the rent on different areas ?
- Does living space, number of rooms, picture count, or year contructed have a correlation with the base rent ?
- Does the latter change in different regions Hamburg, - Berlin, Münich, Bavaria, Bavaria without Münich ?

## 3. File Descriptions

- **immo_data.csv** contains the raw rental data with in a csv format.The dataset contains data from immscout24 it container data from: 2018-09-22, 2019-05-10 and 2019-10-08.
  The data set contains most of the important properties, such as living area size, the rent, both base rent as well as total rent (if applicable), the location (street and house number, if available, ZIP code and state), type of energy etc. It also has two variables containing longer free text descriptions: description with a text describing the offer and facilities describing all available facilities, newest renovation etc. The date column was added to give the time of scraping.

- **rental.ipynb** contains the jypyther notebook

- **helper.py** contains helper methods which help to keep the code in the juyptjer notbook clean and readable

## 4. How to Interact with your project:

First you need to install python and the libraries mentioned above. In a next step you need to run the jupyther notebook to take a look at the results

## 5. Results

Also in the this dataset it could be seen that the prices have increased over time. 
Looking at the second question. It can be seen that when analyzing the whole dataset. There is no clear correlation to the base rent visible. Whatsever when looking at larger cities the correlation to livingspace is clear. An Exception can be oberved when looking at Munich. One hyothesis is that maybe there are much less offers for appartment in Munich and there the data is biased.
