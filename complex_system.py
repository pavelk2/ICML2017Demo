# MULTIPLE RECOMMENDERS

from recommender import Recommender

weights = [0.1,0.3,0.6]

# RECOMMENDER 1
rec1 = Recommender([10,20,30])
rules_1 =[
[[1,1,0,0,0,0,0,0],[1,1,10]],
[[1,2,0,0,0,0,0,0],[1,1,20]],
[[2,2,0,0,0,0,0,0],[1,1,30]]
]
for rule in rules_1:
    rec1.addRule(rule[0],rule[1])

# RECOMMENDER 2
rec2 = Recommender([30,20,10])
rules_2 =[
[[0,0,0,1,1,0,0,0],[10,1,1]],
[[0,0,0,1,2,0,0,0],[20,1,2]],
[[0,0,0,2,2,0,0,0],[30,1,3]]
]
for rule in rules_2:
    rec2.addRule(rule[0],rule[1])

# RECOMMENDER 3
rec3 = Recommender([1,1,1])
rules_3 =[
[[0,0,0,0,0,0,1,1],[1,1,2]],
[[0,0,0,0,0,0,1,2],[1,2,1]],
[[0,0,0,0,0,0,2,2],[2,1,1]]
]
for rule in rules_3:
    rec3.addRule(rule[0],rule[1])

# TEST CASES
test_contexts = [
    [1,2,3,4,5,6,7,8],
    [0,0,0,0,0,0,0,0],
    [9,9,3,4,5,6,7,8],
    [1,2,3,10,5,6,7,8],
    [10,2,30,4,50,6,70,8],
    [100,200,30,100,50,6,70,8],   
]

# RECOMMENDATION
for context in test_contexts:
    print("\n=========")
    print("context: ",context)
    rm_1 = rec1.recommend(context)
    rm_2 = rec2.recommend(context)
    rm_3 = rec3.recommend(context)
    print("Individual recommendations: ",rm_1,rm_2,rm_3)
    rm_final = rm_1*weights[0]+ rm_2*weights[1]+rm_3*weights[2]
    print("Final recommendation: ",rm_final)

