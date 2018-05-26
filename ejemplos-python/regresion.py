#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#La regresión es construir un modelo que pueda ajustar los datos de entrenamiento
#de la forma más cercana.
#Normalmente utilizamos el error cuadrático medio (MSE)
#como la medida de la calidad de ajuste y la función objetivo
#cuando estimamos los parámetros.

Los métodos que generalmente usamos para hacer la regresión en Spark MLlib son linearRegressionWithSGD
#Ejecutar /opt/spark/bin/spark-submit /home/master/ejemplos-python/regresion.py

from pyspark import SparkContext
sc = SparkContext("local", "Mi App")
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD
from pyspark.mllib.evaluation import RegressionMetrics

# Cargar y parsear la data
def parsePoint(line):
    values = [float(x) for x in line.replace(',', ' ').split(' ')]
    return LabeledPoint(values[0], values[1:])

data = sc.textFile("/home/master/ejemplos-python/lpsa.data")
parsedData = data.map(parsePoint)


# Divide la data en 2 set, de entrenamiento y pruebas
# Aquí he establecido la semilla para que pueda reproducir el resultado
(trainingData, testData) = parsedData.randomSplit([0.7, 0.3], seed=100)
# contruir el modelo
model = LinearRegressionWithSGD.train(trainingData)
# evaluar el modelo y entrenar
# --- Point 1 ---
Preds = testData.map(lambda p: (float(model.predict(p.features)), p.label))
MSE = Preds.map(lambda (v, p): (v - p)**2).reduce(lambda x, y: x + y) / Preds.count()
print("Mean Squared Error = " + str(MSE))
print("\n")
# --- Point 2 ---
# Más acerca del modelo y evaluar el analisis de regresión
# Instanciar el objeto
metrics = RegressionMetrics(Preds)
# Squared Error
print("MSE = %s" % metrics.meanSquaredError)
print("RMSE = %s" % metrics.rootMeanSquaredError)
# R-squared
print("R-squared = %s" % metrics.r2)
# Mean absolute error
print("MAE = %s" % metrics.meanAbsoluteError)
# Explained variance
print("Explained variance = %s" % metrics.explainedVariance)
