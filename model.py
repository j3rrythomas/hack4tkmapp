import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def predict():
    label_encoder = LabelEncoder()
    df = pd.read_csv('bike.csv')
    df['Gender'] = label_encoder.fit_transform(df['Gender'])
    x = df.drop(['Purchase Duke'],axis=1)
    svm_classifier = open('svm_model.joblib','rb')
    classifier = joblib.load(svm_classifier)
    x['result'] = classifier.predict(x)
    return x.to_dict(orient='records')
