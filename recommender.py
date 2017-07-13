# Assuming that mood and genre are continuous variables
import numpy as np

class Recommender:
    def __init__(self, default_recommendation):
        self.__default = np.array(default_recommendation)
        self.__rules = []
    
    def addRule(self, conditions, output):
        # output = [mood, tempo, genre]
        self.__rules.append([conditions, output])
    
    def getRules(self):
        return self.__rules
    
    def applyRule(self, context, rule):

        rule_subset = [val for idx, val in enumerate(rule[0]) if val != 0]
        context_subset = [context[idx] for idx, val in enumerate(rule[0]) if val != 0]
        if (rule_subset == context_subset):
            return rule[1]
        else:
            return False

    def recommend(self, context):
        recommendations = []
        for rule in self.getRules():
            rule_output = self.applyRule(context, rule)
            if (rule_output):
                recommendations.append(rule_output)
        if len(recommendations)>0:
            return np.array(recommendations).mean(axis = 0)
        else:
            return self.__default