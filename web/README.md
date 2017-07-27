# ICML2017Demo

Demo for Machine Learning for Music Discovery workshop at ICML2017 https://pavelk2.github.io/ICML2017Demo

![](https://habrastorage.org/web/d69/4cd/053/d694cd0537084ab99c6dc35cf77f5f00.png)

## Survey 
Exploratory survey about causes affecting music preferences

#### Conditions

* One survey was shared on social media (https://pavelkucherbaev.typeform.com/to/WVLEi7)
* Another survey was launched on human computation platform CrowdFlower (https://pavelkucherbaev.typeform.com/to/Okk9Ni)

#### Results

* We collected 25 responses from social media (https://github.com/pavelk2/ICML2017Demo/blob/master/exploratory_survey/Music%20preferences-report.csv)
* We collected 103 responses from CrowdFlower (https://github.com/pavelk2/ICML2017Demo/blob/master/exploratory_survey/Music%20preferences%20CrowdFlower-report.csv)

## API

* Code: https://github.com/pavelk2/ephemeral-context-music-recommendation
* Hosted on Heroku: https://icml2017demo.herokuapp.com
* Request example:

```
GET /recommend?context=1,0,0,0,0,0,0,1&amp;weights=40,30,30 HTTP/1.1
Host: icml2017demo.herokuapp.com
```
