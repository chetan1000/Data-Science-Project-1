import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import warnings
# from gevent.pywsgi import WSGIServer

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def top_new():

  user_review = input("Hey there!! Your words please...")
  output = model.predict([user_review])
  
  return render_template('index.html', prediction_text='YOUR REVIEW IS POSITIVE' if output==1 else 'YOUR REVIEW IS NEGATIVE')

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict(data)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()