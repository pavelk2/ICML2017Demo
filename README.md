# Ephemeral Context for Music Recommendation

[![Code Climate](https://codeclimate.com/github/pavelk2/ephemeral-context-music-recommendation/badges/gpa.svg)](https://codeclimate.com/github/pavelk2/ephemeral-context-music-recommendation)


[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

MOODS[19] = 
[action, aggressive, bouncy, bright, calming, dark, driving, eerie, epic, grooving, humorous, intense, mysterious, mystical, relaxed, somber, suspenseful, unnerving, uplifting]

GENRES[12] = 
[0 Alternative rock, 1 Ambient, 2 Classical, 3 Country, 4 Dance & EDM, 5 Dancehall, 6 Deep House, 7 Disco, 8 Drum & Bass, 9 Dubstep, 10 Electronic, 11 Folk & Singer-Songwriter]

### EPHEMERAL CONTEXT

```bash
CONTEXT_DICTIONARY = {
    "activity":["undefined","jogging", "walking", "cycling", "driving", "sleeping"],
    "speed": ["undefined","slow","moderate","fast"],
    "social": ["undefined","alone", "family", "friends", "colleagues"],
    "location": ["undefined","park","downtown","home","work"],
    "weather": ["undefined","sunny", "rainy", "heavy rain", "cloudy", "thunderstorm"],
    "daytime": ["undefined","early morning","morning","noon","afternoon","evening","night","late night"],
    "physical condition": ["undefined","relaxed", "tired", "energized"],
    "mood": ["undefined","angry", "excited", "happy", "nervous", "calm", "pleased", "bored", "relaxed", "sad", "sleepy", "peaceful"]
}

# jogging fast alone in downtown under heavy rain at night being tired and angry
CONTEXT_EXAMPLE = [1,3,1,2,3,6,2,1]
```

### GET CODE:

```bash
git clone https://github.com/pavelk2/ephemeral-context-music-recommendation ICML
cd ICML
```

### SEE HOW SIMPLE RECOMMENDER WORKS:

```bash
python simple_system.py
```

OUTPUT:

```bash
# [mood, tempo, genre]
[ 50.5  50.5  50.5]
[2 4 6]
[ 9.  9.  9.]
[ 10.  10.  10.]
[ 100.  100.  100.]
[2 4 6]
```

### SEE HOW COMPLEX RECOMMENDER WORKS:

```bash
python complex_system.py
```

OUTPUT:

```bash
# RECOMMENDATION FORMAT: [mood, tempo, genre]
=========
('context: ', [1, 2, 3, 4, 5, 6, 7, 8])
('Individual recommendations: ', array([  1.,   1.,  20.]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 9.7,  6.7,  5.6]))

=========
('context: ', [0, 0, 0, 0, 0, 0, 0, 0])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))

=========
('context: ', [9, 9, 3, 4, 5, 6, 7, 8])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))

=========
('context: ', [1, 2, 3, 10, 5, 6, 7, 8])
('Individual recommendations: ', array([  1.,   1.,  20.]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 9.7,  6.7,  5.6]))

=========
('context: ', [10, 2, 30, 4, 50, 6, 70, 8])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))

=========
('context: ', [100, 200, 30, 100, 50, 6, 70, 8])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))
```

## Music Sources

* http://docs.mdlrs.apiary.io/
* http://musimap.com
* http://developers.musicshake.com/docs/songlist


## GISTS 

#### GENRES

```
-- update tracks_vec set genre_1 = 1 where (genre like "%alternative%" and genre like "%rock%") or (tags like "%alternative%" and tags like "%rock%")
-- update tracks_vec set genre_2 = 1 where (genre like "%Ambient%" and genre like "%Ambient%")
-- update tracks_vec set genre_3 = 1 where (genre like "%Classic%" )
-- update tracks_vec set genre_4 = 1 where (genre like "%Country%" )
-- update tracks_vec set genre_5 = 1 where (genre like "%Dance%" or genre like "%EDM%")
-- update tracks_vec set genre_6 = 1 where (genre like "%Dancehall%" or tags like "%Dancehall%") 
-- update tracks_vec set genre_7 = 1 where (genre like "%Deep%" and genre like "%House%") 
-- update tracks_vec set genre_8 = 1 where (genre like "%Disco%" or tags like "%Disco%" ) 
-- update tracks_vec set genre_9 = 1 where (genre like "%D&B%" or (genre like "%Drum%" and genre like "%bass%" )) 
-- update tracks_vec set genre_10 = 1 where (genre like "%dubstep%") 
-- update tracks_vec set genre_11 = 1 where (genre like "%Electronic%") 
-- update tracks_vec set genre_12 = 1 where (genre like "%Folk%" or genre like "Songwriter" or genre like "Singer") 
```

#### MOODS
```
-- Valence
-- positive
update tracks_SC set valence = 4 where (tags like "%happy%" or tags like "%content%") or (description like "%happy%" or description like "%content%");
update tracks_SC set valence = 3 where (tags like "%elated%" or tags like "%serene%") or (description like "%elated%" or description like "%serene%");
update tracks_SC set valence = 2 where (tags like "%excit%" or tags like "%relax%") or (description like "%excit%" or description like "%relax%") ;
update tracks_SC set valence = 1 where (tags like "%alert%" or tags like "%calm%") or (description like "%alert%" or description like "%calm%");
-- negative
update tracks_SC set valence = -1 where (tags like "%tense%" or tags like "%fatig%") or (description like "%tense%" or description like "%fatig%");
update tracks_SC set valence = -2 where (tags like "%nerv%" or tags like "%letharg%") or (description like "%nerv%" or description like "%letharg%");
update tracks_SC set valence = -3 where (tags like "%stress%" or tags like "%depress%") or (description like "%stress%" or description like "%depress%");
update tracks_SC set valence = -4 where (tags like "%upset%" or tags like "%sad%") or (description like "%upset%" or description like "%sad%");

-- Arousal
-- positive
update tracks_SC set arousal = 4 where (tags like "%tense%" or tags like "%alert%") or (description like "%tense%" or description like "%alert%");
update tracks_SC set arousal = 3 where (tags like "%nerv%" or tags like "%excit%") or (description like "%nerv%" or description like "%excit%");
update tracks_SC set arousal = 2 where (tags like "%stress%" or tags like "%elated%") or (description like "%stress%" or description like "%elated%");
update tracks_SC set arousal = 1 where (tags like "%upset%" or tags like "%happy%") or (description like "%upset%" or description like "%happy%");
-- negative
update tracks_SC set arousal = -1 where (tags like "%sad%" or tags like "%content%") or (description like "%sad%" or description like "%content%");
update tracks_SC set arousal = -2 where (tags like "%depress%" or tags like "%serene%") or (description like "%depress%" or description like "%serene%");
update tracks_SC set arousal = -3 where (tags like "%letharg%" or tags like "%relax%") or (description like "%letharg%" or description like "%relax%");
update tracks_SC set arousal = -4 where (tags like "%fatig%" or tags like "%calm%") or (description like "%fatig%" or description like "%calm%");

```
