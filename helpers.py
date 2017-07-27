from flask import request, jsonify
from hybrid.hybrid import calcRecommendations, getNotes
from soundcloud.soundcloud import getSongs

def getResponse():
    weights = getHTTPParamArray("weights")
    context = getHTTPParamArray("context")

    if (len(context) != 8 or len(weights) != 3):
        response = {"error":"context should consist exactly out of 8 features, weights should be exactly 3"}
    else:
        recommendations = calcRecommendations(weights, context)
    response = formResponse(recommendations)
    return jsonify(response)

def getHTTPParamArray(param):
  return list(map(float, request.args.get(param).split(',')))

def getRecommendationOutput(name, recommendation, flag):
  return {
        "name":name,
        "recommendation": getNotes(recommendation.tolist()),
        "is_reliable":flag
      }

def formResponse(recs):
  (ind_recommendations,hybrid, flags) = recs
  
  response = {"recommenders":[], "songs":[]}
  # response for individual recommenders
  for i, recommendation in enumerate(ind_recommendations):
    response["recommenders"].append(getRecommendationOutput("recommender_"+str(i+1),recommendation,flags[i]))
  # responses for hybrid recommender
  response["recommenders"].append(getRecommendationOutput("hybrid",hybrid,1))
  # responses with recommended tracks
  response["songs"] = getSongs(hybrid.tolist())
  
  return response
