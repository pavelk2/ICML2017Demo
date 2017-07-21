from flask import  request, jsonify
from hybrid.hybrid import rec1, rec2, rec3

def calcRecommendations(weights,context):
  rm_1 = rec1.recommend(context)
  rm_2 = rec2.recommend(context)
  rm_3 = rec3.recommend(context)
  hybrid = rm_1*weights[0]+ rm_2*weights[1]+rm_3*weights[2]

  return (rm_1,rm_2,rm_3,hybrid)

def formResponse(recommendations):
  (rm_1,rm_2,rm_3,hybrid) = recommendations
  return {
      "individual":[
        {
          "name":"recommender_1",
          "recommendation" : rm_1.tolist()
        },{
          "name":"recommender_2",
          "recommendation" : rm_2.tolist()
        },{
          "name":"recommender_3",
          "recommendation" : rm_3.tolist()
        }
      ],
      "hybrid":hybrid.tolist()
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