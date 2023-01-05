# FarmEasy🌾

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

---

## What is FarmEasy🌾?
A vast majority of the Indian farmers believe in depending on their intuition to decide which crop to sow in a particular season. They find comfort in simply following the ancestral farming patterns and norms without realizing the fact that crop output is circumstantial, depending heavily on the present-day weather and soil conditions.

However, a single farmer cannot be expected to take into account all the innumerable factors that contribute to crop growth before reaching a consensus about which one to grow.

> FarmEasy🌾 solves this problem by using a combination of analytics and machine learning so that the farmers can make a more informed decision.

---

## Project Architecture🏗️

---

## Project Structure📁

---

## Data📊
The dataset used for this project is taken from the [Kaggle](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset) website. The dataset contains 2200 rows and 8 columns. The dataset contains the following columns:
- N - ratio of Nitrogen content in soil
- P - ratio of Phosphorous content in soil
- K - ratio of Potassium content in soil
- temperature - temperature in degree Celsius
- humidity - relative humidity in %
- ph - ph value of the soil
- rainfall - rainfall in mm
- label - crop type

![data](/assets/data.PNG)

---

## Machine Learning🤖

The machine learning model is built using the following steps:
1. Load the dataset
2. Applying one-hot encoding to the label column
3. Split the dataset into training and testing sets
4. Apply feature scaling to the dataset
5. Apply different classification algorithms like KNN, SVM, Random Forest and Naive Bayes
6. Perform ensemble learning using Voting Classifier 
7. Save the model

> The accuracy of the model is **99.27%**.

---

## Backend🔧


---

## Frontend🖥️

---

## Project Demo🎥

---

## Project Screenshots📸

---

## How to run the project locally?🤔
- Clone the repository
```bash
git clone https://github.com/abhikalparya/FarmEasy.git
```
- Install the dependencies
```bash
pip install -r requirements.txt
```
- Run the app
```bash
python app.py
```

