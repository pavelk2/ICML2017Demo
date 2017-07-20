import os
from flask import Flask, render_template, request, jsonify
from hybrid.hybrid import rec1, rec2, rec3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
  weights = list(map(float, request.args.get('weights').split(',')))
  context = list(map(int, request.args.get('context').split(',')))
  if (len(context) != 8 or len(weights) != 3):
    response = {"error":"context should consist exactly out of 8 features, weights should be exactly 3"}
  else:
    rm_1 = rec1.recommend(context)
    rm_2 = rec2.recommend(context)
    rm_3 = rec3.recommend(context)
    rm_hybrid = rm_1*weights[0]+ rm_2*weights[1]+rm_3*weights[2]
    response = {
      "rec1":rm_1.tolist(),
      "rec2":rm_2.tolist(),
      "rec3":rm_3.tolist(),
      "hybrid":rm_hybrid.tolist()
    }
  return jsonify(response)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
