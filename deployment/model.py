import pandas as pd
import numpy as np

dat = pd.read_csv("C:/Users/Chetan/Desktop/deployment/SA_upsampled.csv")

type(dat)
dat.shape
dat.Reviews_fin.isna().sum()
data = dat.dropna()
data.isna().sum()
data.shape


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import sklearn.metrics as metrics
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

tfidf = TfidfVectorizer()

X = data['Reviews_fin']
y = data['sentiment']

pipeline = Pipeline([
    ('Tf-Idf', TfidfVectorizer(ngram_range=(1,2))),
    ('classifier', SVC())
])
X = data['Reviews_fin']
y = data['sentiment']
pipeline.fit(X, y)
pip_pred = pipeline.predict(X)
print(metrics.classification_report(y, pip_pred))
print("Model score ", pipeline.score(X,y))

import pickle
pickle.dump(pipeline, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
# print(model.predict("Spectacular"))          # [[4, 300, 500]]