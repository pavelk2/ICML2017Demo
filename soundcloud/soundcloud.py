import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

feature_space = [
            "genre_1",
            "genre_2",
            "genre_3",
            "genre_4",
            "genre_5",
            "genre_6",
            "genre_7",
            "genre_8",
            "genre_9",
            "genre_10",
            "genre_11",
            "genre_12",
            "bpm",
            "valence",
            "arousal"]

def getSongs(recommendation_vector):

    soundcloud_tracks = pd.read_csv("soundcloud/tracks.csv")

    soundcloud_tracks["similarity"] = cosine_similarity(
        soundcloud_tracks[feature_space],
        [recommendation_vector])
    sorted_by_similarity = soundcloud_tracks.sort("similarity", ascending = 0)
    top_5 = sorted_by_similarity.head(n=5)
    top_5_as_list = top_5.T.to_dict().values()
    print(top_5_as_list)
    
    return top_5_as_list

#recommendation_vector = [0,1,0,0,0,0,0,0,0,0,0,0,70,2,0]
    
    
