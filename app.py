import os
from flask import Flask
from flask_cors import CORS, cross_origin


from helpers import getResponse
from soundcloud.soundcloud import getSongs

app = Flask(__name__, static_url_path="", static_folder="web")
CORS(app)

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
  return getResponse()
    

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
