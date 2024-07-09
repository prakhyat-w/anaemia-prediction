from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'This model uses Random Forest Classifier to check if someone has anaemia based on blood data. Enter required data for prediction.'
    })

@app.route('/predict/', methods = ['GET','POST'])
def prediction():
    if request.method == 'POST':
        data = request.json
        
        red = data.get('red')
        green = data.get('green')
        blue = data.get('blue')
        hb = data.get('hb')
        M = data.get('M')

        result= util.prediction(red,green,blue,hb,M)
        print(result)
        result_data = {
            'result': result
        }
        print(result)
        return jsonify(result_data), 200
    else:
        return 'Predict through Streamlit UI'

if __name__ == '__main__':
    app.run(debug= True)