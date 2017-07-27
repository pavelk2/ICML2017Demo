# ICML2017Demo

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Demo for Machine Learning for Music Discovery workshop at ICML2017 https://icml2017demo.herokuapp.com

![](https://habrastorage.org/web/d69/4cd/053/d694cd0537084ab99c6dc35cf77f5f00.png)

## How to run locally:

```bash
git clone https://github.com/pavelk2/ICML2017Demo demo
cd demo
pip install -r requirements.txt
python app.py
```

## API

* Code: https://github.com/pavelk2/ephemeral-context-music-recommendation
* Hosted on Heroku: https://icml2017demo.herokuapp.com
* Request example:

```
GET /recommend?context=1,0,1,1,0,1,1,1&amp;weights=60,40,40 HTTP/1.1
Host: icml2017demo.herokuapp.com
```

## API usage example

#### Request

```
GET /recommend?context=1,0,0,0,0,0,0,1&amp;weights=40,30,30 HTTP/1.1
Host: icml2017demo.herokuapp.com
```
#### Response

```json
{
    "recommenders": [
        {
            "is_reliable": 1,
            "name": "recommender_1",
            "recommendation": [
                "Electronic, ",
                133,
                "Elated"
            ]
        },
        {
            "is_reliable": 0,
            "name": "recommender_2",
            "recommendation": [
                "Some Ambient, Some Folk & Singer-Songwriter, ",
                99.75,
                "Elated"
            ]
        },
        {
            "is_reliable": 1,
            "name": "recommender_3",
            "recommendation": [
                "Ambient, Electronic, ",
                119.7,
                "Fatigued"
            ]
        },
        {
            "is_reliable": 1,
            "name": "hybrid3",
            "recommendation": [
                "A bit of Ambient, Electronic, ",
                127.67999999999999,
                "Happy"
            ]
        }
    ],
    "songs": [
        {
            "arousal": 0.25,
            "bpm": 0.865,
            "genre_1": 0,
            "genre_10": 0,
            "genre_11": 1,
            "genre_12": 0,
            "genre_2": 0,
            "genre_3": 0,
            "genre_4": 0,
            "genre_5": 0,
            "genre_6": 0,
            "genre_7": 0,
            "genre_8": 0,
            "genre_9": 0,
            "id": 174720,
            "permalink_url": "http://soundcloud.com/illbilly_hitec/illbilly-hitec-ft-lady-n-why",
            "similarity": 0.974883864591345,
            "uri": "https://api.soundcloud.com/tracks/47685694",
            "valence": 0.25
        },
        {
            "arousal": 0.25,
            "bpm": 0.88,
            "genre_1": 0,
            "genre_10": 0,
            "genre_11": 1,
            "genre_12": 0,
            "genre_2": 0,
            "genre_3": 0,
            "genre_4": 0,
            "genre_5": 0,
            "genre_6": 0,
            "genre_7": 0,
            "genre_8": 0,
            "genre_9": 0,
            "id": 62149,
            "permalink_url": "http://soundcloud.com/technowagon/4-ghianda-apricots",
            "similarity": 0.9587312774139962,
            "uri": "https://api.soundcloud.com/tracks/6814739",
            "valence": 0.5
        },
        {
            "arousal": -0.25,
            "bpm": 1.203,
            "genre_1": 0,
            "genre_10": 0,
            "genre_11": 1,
            "genre_12": 0,
            "genre_2": 0,
            "genre_3": 0,
            "genre_4": 0,
            "genre_5": 0,
            "genre_6": 0,
            "genre_7": 0,
            "genre_8": 0,
            "genre_9": 0,
            "id": 260997,
            "permalink_url": "http://soundcloud.com/eqwhy/get-down-bang-feat-kash",
            "similarity": 0.9428665597107959,
            "uri": "https://api.soundcloud.com/tracks/103606276",
            "valence": 0.5
        },
        {
            "arousal": -0.25,
            "bpm": 1.203,
            "genre_1": 0,
            "genre_10": 0,
            "genre_11": 1,
            "genre_12": 0,
            "genre_2": 0,
            "genre_3": 0,
            "genre_4": 0,
            "genre_5": 0,
            "genre_6": 0,
            "genre_7": 0,
            "genre_8": 0,
            "genre_9": 0,
            "id": 261010,
            "permalink_url": "http://soundcloud.com/eqwhy/goin-crazy",
            "similarity": 0.9428665597107959,
            "uri": "https://api.soundcloud.com/tracks/103603023",
            "valence": 0.5
        },
        {
            "arousal": -0.25,
            "bpm": 1.203,
            "genre_1": 0,
            "genre_10": 0,
            "genre_11": 1,
            "genre_12": 0,
            "genre_2": 0,
            "genre_3": 0,
            "genre_4": 0,
            "genre_5": 0,
            "genre_6": 0,
            "genre_7": 0,
            "genre_8": 0,
            "genre_9": 0,
            "id": 261367,
            "permalink_url": "http://soundcloud.com/eqwhy/808-kick-drum",
            "similarity": 0.9428665597107959,
            "uri": "https://api.soundcloud.com/tracks/103877671",
            "valence": 0.5
        }
    ]
}
```

#### EPHEMERAL CONTEXT

```bash
CONTEXT_STATES = {
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

## SoundCloud

Recommendations are formed based on 1036 tracks from SoundCLoud: https://github.com/pavelk2/ICML2017Demo/blob/master/exploratory_survey/Music%20preferences-report.csv

### Music Classification

#### GENRES

```sql
update tracks_SC set genre_1 = 1 where (genre like "%alternative%" and genre like "%rock%") or (tags like "%alternative%" and tags like "%rock%")
update tracks_SC set genre_2 = 1 where (genre like "%Ambient%" and genre like "%Ambient%")
update tracks_SC set genre_3 = 1 where (genre like "%Classic%" )
update tracks_SC set genre_4 = 1 where (genre like "%Country%" )
update tracks_SC set genre_5 = 1 where (genre like "%Dance%" or genre like "%EDM%")
update tracks_SC set genre_6 = 1 where (genre like "%Dancehall%" or tags like "%Dancehall%") 
update tracks_SC set genre_7 = 1 where (genre like "%Deep%" and genre like "%House%") 
update tracks_SC set genre_8 = 1 where (genre like "%Disco%" or tags like "%Disco%" ) 
update tracks_SC set genre_9 = 1 where (genre like "%D&B%" or (genre like "%Drum%" and genre like "%bass%" )) 
update tracks_SC set genre_10 = 1 where (genre like "%dubstep%") 
update tracks_SC set genre_11 = 1 where (genre like "%Electronic%") 
update tracks_SC set genre_12 = 1 where (genre like "%Folk%" or genre like "Songwriter" or genre like "Singer") 
```

#### MOODS

```sql
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

## Survey 
Exploratory survey about causes affecting music preferences

#### Conditions

* One survey was shared on social media (https://pavelkucherbaev.typeform.com/to/WVLEi7)
* Another survey was launched on human computation platform CrowdFlower (https://pavelkucherbaev.typeform.com/to/Okk9Ni)

#### Results

* We collected 25 responses from social media (https://github.com/pavelk2/ICML2017Demo/blob/master/exploratory_survey/Music%20preferences-report.csv)
* We collected 103 responses from CrowdFlower (https://github.com/pavelk2/ICML2017Demo/blob/master/exploratory_survey/Music%20preferences%20CrowdFlower-report.csv)

