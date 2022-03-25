from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DemandPrediction:

    def __init__(self, data_file="train_sample.csv"):
        self.data = pd.read_csv(data_file)
        

    def initialize(self):
        self.organizeData()
        self.trainModel()
        self.modelTest()

    def organizeData(self):
        self.sales = self.data["Venta_uni_hoy"].values.reshape(-1,1)
        self.demand = self.data["Demanda_uni_equil"].values.reshape(-1,1)

    def trainModel(self):
        self.model = LinearRegression()
        X_train, self.x_test, y_train, self.y_test = train_test_split(self.sales, self.demand, test_size = 0.3, random_state=42)
        
        self.model.fit(X_train, y_train)


    def modelTest(self):
        self.test = self. model.score(self.x_test, self.y_test)

