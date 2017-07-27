import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from hybrid.hybrid import calcRecommendations, getNotes
from soundcloud.soundcloud import getSongs

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

def getHTTPParamArray(param):
  return list(map(float, request.args.get(param).split(',')))

def formResponse(recommendations):
  (rm_1,rm_2,rm_3,hybrid, flags) = recommendations
  
  return {
      "recommenders":[
        {
          "name":"hybrid",
          "recommendation" : getNotes(hybrid.tolist()),
          "is_reliable": 1
        },
        {
          "name":"recommender_1",
          "recommendation" : getNotes(rm_1.tolist()),
          "is_reliable": flags[0]
        },{
          "name":"recommender_2",
          "recommendation" : getNotes(rm_2.tolist()),
          "is_reliable": flags[1]
        },{
          "name":"recommender_3",
          "recommendation" : getNotes(rm_3.tolist()),
          "is_reliable": flags[2]
        }
      ],
      "songs" : getSongs(hybrid.tolist())
    }

@app.route('/recommend', methods=['GET'])
def recommend():
    weights = getHTTPParamArray("weights")
    context = getHTTPParamArray("context")

    if (len(context) != 8 or len(weights) != 3):
        response = {"error":"context should consist exactly out of 8 features, weights should be exactly 3"}
    else:
        recommendations = calcRecommendations(weights, context)
    response = formResponse(recommendations)
    return jsonify(response)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

# ==================

