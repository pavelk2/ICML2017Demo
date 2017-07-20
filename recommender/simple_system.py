# ONE RECOMMENDER ONLY

from recommender import Recommender

# [mood, tempo, genre]
default_recommendation = [2,4,6]

rec = Recommender(default_recommendation)

#[
#   [
#       [activity,speed,social,location, weather, daytime, physcondition, mood],
#       [mood, tempo, genre]
#   ],...
#]
rules =[
[[1,2,3,4,5,6,7,8],[1,1,1]],
[[9,9,0,0,0,0,0,0],[9,9,9]],
[[1,2,3,10,5,6,7,8],[10,10,10]],
[[0,2,0,4,0,6,0,8],[100,100,100]]
]

# teach our Recommender
for rule in rules:
    rec.addRule(rule[0],rule[1])

# cases of contexts to test the recommender
test_contexts = [
    [1,2,3,4,5,6,7,8],
    [0,0,0,0,0,0,0,0],
    [9,9,3,4,5,6,7,8],
    [1,2,3,10,5,6,7,8],
    [10,2,30,4,50,6,70,8],
    [100,200,30,100,50,6,70,8],   
]

# for each context we print recommendations as [mood, tempo, genre]
for context in test_contexts:
    print(rec.recommend(context))
    