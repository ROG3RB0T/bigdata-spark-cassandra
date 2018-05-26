#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
from pyspark import SparkContext
#
#¿Cuál es la idea de Random Forest?
#Para decirlo de manera simple,
#promediar un conjunto de observaciones reduce la varianza.
#Por lo tanto, una forma natural de reducir la varianza y aumentar la
#precisión de predicción.
#Ejecutar /opt/spark/bin/spark-submit /home/master/ejemplos-python/arboles-decision.py
# Cargar la data en un RDD
sc = SparkContext()
data = MLUtils.loadLibSVMFile(sc, '/home/master/ejemplos-python/sample-data-arbol.txt')
# Divida los datos en conjuntos de entrenamiento y prueba (muestra de un 30% para la prueba)
(trainingData, testData) = data.randomSplit([0.7, 0.3])


# --- Point 3, 4, 5 ---
# Entrene un modelo de RandomForest
#  Empty categoricalFeaturesInfo indica que todas las características son continuas.
model = RandomForest.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={},
                                     numTrees=3, featureSubsetStrategy="auto",
                                     impurity='gini', maxDepth=4, maxBins=32)

# Evaluar el modelo en instancias de prueba y calcular el error de prueba
predictions = model.predict(testData.map(lambda x: x.features))
labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
testErr = labelsAndPredictions.filter(lambda (v, p): v != p).count() / float(testData.count())
print('Test Error = ' + str(testErr))
print('Learned classification forest model:')
print(model.toDebugString())
