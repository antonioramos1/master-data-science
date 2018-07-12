# WorldCup NLP Analysis

The goal of this project is to put into practice some of the NLP tools and concepts learned during the Master while using real-world datasets, on this case I will be using Tweets posted during the Quarterfinals and Semifinals WorldCup matches.

On this notebook I will try to find out who are the most mentioned entities during these matches and try to extract any insights.

This repository contains:

 - Pulling tweets with Tweepy.
 - Entitiy analysis with Spacy, time splits every 15 minutes.
 - Sentiment analysis with TextBlob.
 
----

### Caveats:

- For simplicity, tweets are limited to English language, this introduces bias into the analysis, especially depending on the local language from the teams playing the match in question.  
- Manual work and modelling could help improve the accuracy of the entity classifier, however we are sticking to the default model from Spacy.  
- Entity analysis has been limited to only take into account those entities with a frequency > 300 mentions.  
- For simplicity, matches end times are an estimation and I do not take into account extra times or penalties.  


### Dependencies:
- Tweepy
- Spacy
- Textblob

### Outcomes:
![plot](https://i.imgur.com/iMR80GJ.png)

- Entity analysis favours certains players who appear even in matches they do not play. This could be a good indicator of the popularity of such players in social media, eg. Neymar, Mbappe.
- The bias introduced by only pulling tweets is English is very present for example in England games.
- Time splits offer another picture, ie. blunder from Muslera during the Uruguay vs France game makes other goalkeepers go viral such as Karius, or De Gea.
- Although being a secondary analysis performed with the aim to gain further practice, Sentiment analysis has been applied to the same tweets which have mixed sentiments from each of team's supporters, and it does not seem to show any clear insights apart from differences in variability and slightly better/worse sentiment rates.

### Sources:  

KSchool Master Data Science - Victor Peinado - NLP Classes  
Twitter app tokens: [https://apps.twitter.com/app/15464256](https://apps.twitter.com/app/15464256)  
Tweepy tutorial: [http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/](http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/)  
Twitter API docs: [https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets)  
Tweepy docs: [http://docs.tweepy.org/en/v3.5.0/api.html](http://docs.tweepy.org/en/v3.5.0/api.html)  
Spacy docs: [https://spacy.io/usage/linguistic-features](https://spacy.io/usage/linguistic-features)   
Interact docs: [https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)  
Textblob docs: [https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/)  
