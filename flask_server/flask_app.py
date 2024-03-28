from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_locations')
def get_locations():
    response = jsonify({
       'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/model_predict',methods=['POST'])
def model_predict():
    total_sqft=float(request.form['total_sqft'])
    location = request.form['location']
    beds = int(request.form['beds'])
    bath = int(request.form['bath'])
    
    response = jsonify({
        'estimated_price': util.get_prediction(location=location, sqft=total_sqft, bed=beds, bath=bath)
    })
    return response


if __name__ == "__main__":
    print("Starting BHP Server")
    util.load_saved_artifacts()
    app.run()