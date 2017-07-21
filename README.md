# Ephemeral Context for Music Recommendation

[![Code Climate](https://codeclimate.com/github/pavelk2/ephemeral-context-music-recommendation/badges/gpa.svg)](https://codeclimate.com/github/pavelk2/ephemeral-context-music-recommendation)


[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

MOODS[19] = 
[action, aggressive, bouncy, bright, calming, dark, driving, eerie, epic, grooving, humorous, intense, mysterious, mystical, relaxed, somber, suspenseful, unnerving, uplifting]

GENRES[12] = 
[Alternative rock, Ambient, Classical, Country, Dance & EDM, Dancehall, Depp House, Disco, Drum & Bass, Dubstep, Electronic, Folk & Singer-Songwriter]

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
