
# Hybrid Recommender
from flask import  request, jsonify
import json
import math
import numpy as np
import os
import MySQLdb
from urllib.parse import urlparse
from recommender.recommender import Recommender

database =  urlparse(os.environ['CLEARDB_DATABASE_URL'])
print(database)

with open('hybrid/hybrid_config.json') as config_file:    
    config = json.load(config_file)

# RECOMMENDER 1
rec1 = Recommender(config["rec1"]["default"])
for rule in config["rec1"]["examples"]:
    rec1.addRule(rule[0],rule[1])


# RECOMMENDER 2
rec2 = Recommender(config["rec2"]["default"])
for rule in config["rec2"]["examples"]:
    rec2.addRule(rule[0],rule[1])


# RECOMMENDER 3
rec3 = Recommender(config["rec3"]["default"])
for rule in config["rec3"]["examples"]:
    rec3.addRule(rule[0],rule[1])

def calcRecommendations(weights,context):
  rm_1 = rec1.recommend(context)
  rm_2 = rec2.recommend(context)
  rm_3 = rec3.recommend(context)


  total_weight = sum(weights)
  weights = (np.array(weights)/(total_weight*1.0)).tolist()
  hybrid = rm_1*weights[0]+ rm_2*weights[1]+rm_3*weights[2]

  return (rm_1,rm_2,rm_3,hybrid)

def formResponse(recommendations):
  (rm_1,rm_2,rm_3,hybrid) = recommendations
  print(rm_1)
  print(hybrid)

  
  hybrid_rec = vector2titles(hybrid.tolist())
  mood = hybrid_rec[0]
  tempo = hybrid_rec[1]
  genre = hybrid_rec[2]
  
  return {
      "individual":[
        {
          "name":"recommender_1",
          "recommendation" : vector2titles(rm_1.tolist())
        },{
          "name":"recommender_2",
          "recommendation" : vector2titles(rm_2.tolist())
        },{
          "name":"recommender_3",
          "recommendation" : vector2titles(rm_3.tolist())
        }
      ],
      "hybrid":hybrid_rec,
      "songs" : getSongs(mood, tempo, genre)
    }
def getHTTPParamArray(param):
  return list(map(float, request.args.get(param).split(',')))

def getRecommendations():
    weights = getHTTPParamArray("weights")
    context = getHTTPParamArray("context")
    if (len(context) != 8 or len(weights) != 3):
        response = {"error":"context should consist exactly out of 8 features, weights should be exactly 3"}
    else:
        recommendations = calcRecommendations(weights, context)
    response = formResponse(recommendations)
    return jsonify(response)

def vector2titles(recommendation_vector):
    return [config["moods"][int(recommendation_vector[0])],int(recommendation_vector[1]),config["genres"][int(recommendation_vector[2])]]

def getSongs(mood,tempo,genre):
    db = MySQLdb.connect(host=database.hostname,
                user=database.username,
                passwd=database.password,
                db="heroku_843cf1933fb9599")
    cur = db.cursor()
    print(tempo,genre)
    query = "select uri from tracks1 where bpm > ("+str(tempo)+"-10) and bpm < ("+str(tempo)+"+10) and genre like '%"+genre+"%' order by playback_count desc limit 5"
    print(query)

    cur.execute(query)
    songs = []
    for (track_uri,) in cur:
        songs.append(track_uri)
    db.close()
    return songs



