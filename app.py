import os
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

from hybrid.hybrid import getRecommendations

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
  return getRecommendations()

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
