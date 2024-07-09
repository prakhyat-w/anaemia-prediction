import pickle

with open ('Anaemia prediction new','rb') as f:
    model = pickle.load(f)

def prediction (red,green,blue,hb,M):
    result = model.predict([[red,green,blue,hb,M]])
    return str(result[0])