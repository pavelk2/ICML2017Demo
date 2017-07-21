
# Hybrid Recommender
from flask import  request, jsonify
import json
import math
import numpy as np
from recommender.recommender import Recommender


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
      "hybrid":vector2titles(hybrid.tolist())
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
    return 1



