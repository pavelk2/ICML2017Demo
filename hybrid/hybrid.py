# Hybrid Recommender
import json
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from recommender.recommender import Recommender

with open('hybrid/hybrid_config.json') as config_file:    
    config = json.load(config_file)

RECOMMENDERS_USED = [
  {"name":"rec1", "used_features":[0]},
  {"name":"rec2", "used_features":[3,4,5]},
  {"name":"rec3", "used_features":[2,6,7]}
]
recommenders = []

for recommender in RECOMMENDERS_USED:
  rec = Recommender(config[recommender["name"]]["default"])
  for rule in config[recommender["name"]]["examples"]:
    rec.addRule(rule[0],rule[1])
  recommenders.append(rec)


def calcRecommendations(weights,context):
  indiv_recommendations = []
  for rec in recommenders:
    indiv_recommendations.append(rec.recommend(context))

  reliability_flags = getReliabilityFlags(context)
  selected_weights = np.array(reliability_flags) * weights
  balanced_weights = balanceWeights(selected_weights)
  
  # initiate empty recommendation
  hybrid = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i, recommendation in enumerate(indiv_recommendations):
    hybrid+=recommendation*balanced_weights[i]
  
  return (indiv_recommendations,hybrid,reliability_flags)

def balanceWeights(weights):
  total_weight = sum(weights)
  weights = (np.array(weights)/(total_weight*1.0)).tolist()
  
  return weights

def getReliabilityFlags(context):
  is_reliable = [1,1,1]
  for i, recommender in enumerate(RECOMMENDERS_USED):
    for feature in recommender["used_features"]:
      if context[feature] == 0:
        is_reliable[i] = 0
  
  return is_reliable

def getNotes(rec_vector):
  genre_string = getNote4Genre(rec_vector) 
  bpm = rec_vector[12]*133,
  mood = getNote4Mood(rec_vector)

  return (genre_string, bpm[0], mood)
  
def getNote4Genre(rec_vector):
  genre_string = ""
  for i in range(0, 12):
    if (rec_vector[i] > 0.66):
      genre_string+= config["genres"][i]+", "
    elif (rec_vector[i] > 0.33):
      genre_string+= "Some "+config["genres"][i]+", "
    elif (rec_vector[i] > 0):
      genre_string+= "A bit of "+config["genres"][i]+", "
  
  return genre_string

def getNote4Mood(rec_vector):
  valence = rec_vector[13]
  arousal = rec_vector[14]

  moods = pd.read_csv("hybrid/moods.csv")

  moods["similarity"] = cosine_similarity(
    moods[["valence","arousal"]],
    [[valence,arousal]])

  sorted_by_similarity = moods.sort("similarity", ascending = 0)
  top_1 = sorted_by_similarity.head(n=1)
  top_1_as_list = top_1["mood"].tolist()[0]

  return top_1_as_list



