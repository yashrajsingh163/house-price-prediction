from flask import Flask, request, jsonify
from matplotlib.pyplot import title
import pickle

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to  fddf  dsgflearning model APIs!" 


@app.route('/houseprice', methods=["POST"])
def add_guide():
    model = pickle.load(open('house_price','rb'))
    bedroom = request.json['bedroom']
    bathrooms = request.json['bathrooms']
    sqft_living = request.json['sqft_living']
    sqft_lot = request.json['sqft_lot']
    floors = request.json['floors']
    waterfront = request.json['waterfront']
    view = request.json['view']
    condition = request.json['condition']
    sqft_above = request.json['sqft_above']
    sqft_basement = request.json['sqft_basement']
    yr_built = request.json['yr_built']
    yr_renovated = request.json['yr_renovated']
    city = request.json['city']

    data = [
    bedroom ,
    bathrooms ,
    sqft_living ,
    sqft_lot ,
    floors ,
    waterfront ,
    view,
    condition,
    sqft_above ,
    sqft_basement,
    yr_built,
    yr_renovated,
    city
    ]
    format_float = "{:.2f}".format(model.predict([data])[0])
    return jsonify({
        "price":format_float
    })

