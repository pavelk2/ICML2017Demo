# Hybrid Recommender
import json
from recommender.recommender import Recommender

with open('hybrid/hybrid_config.json') as config_file:    
    config = json.load(config_file)
print (config)

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
