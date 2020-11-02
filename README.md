[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-orange)](https://fair-software.eu)

# PuReGoMe

[PuReGoMe](https://www.esciencecenter.nl/projects/puregome/) is a research project of [Utrecht University](https://www.uu.nl/en/research/intelligent-software-systems/intelligent-systems) and the [Netherlands eScience Center](https://www.esciencecenter.nl/). We analyze Dutch social media messages to assess the opinion of the public towards the COVID-19 pandemic mesasures taken by the Dutch government.

## Data

PuReGome uses three data sources for social media analysis. Our main data source are Dutch tweets from [Twitter](https://twitter.com/). We use Dutch posts from [Reddit](https://www.reddit.com/) and comments from [Nu.nl](https://www.nu.nl) as sources of verfication of the results obtained by the tweet analysis.

After a month has ended, the data from the month are collected. Here are the steps taken for each data source, starting with Twitter:

1. the tweets are taken from the crawler of [twiqs.nl](http://twiqs.nl). They are stored in json format in hourly files. (this data set is not publically available)
2. the tweets are extracted from the json files and and stored in csv files (six columns: id\_str, in\_reply\_to\_status\_id\_str, user, verified, text, location). The conversion is performed by the script [query-text.py](/puregome/queries/blob/master/query-text.py)
3. duplicate tweets are removed from from the csv files produced in step 2 by the script [text-unique.py](/puregome/scripts/blob/master/text-unique.py)

(it would be useful to combine steps 2 and 3 in the future)

Reddit:

1. Run the script [get\_subreddit\_ids.py](/puregome/scripts/blob/master/get_subreddit_py) to automatically retrieve the subreddits of the Dutch corona reddits
2. Manually expand the list of ids of the subreddit [Megathread Coronavirus COVID-19 in Nederland](https://www.reddit.com/r/thenetherlands/search?q=Megathread+Coronavirus+COVID-19+in+Nederland&restrict_sr=on&sort=new&t=all)
3. Run the script [coronamessagesnl.py](/puregome/scripts/blob/master/coronamessagesnl.py) to automatically retrieve the posts in the found subreddits
4. ...

Nu.nl:

1. Run code blocks 1, 3 and 4 of the notebook [selenium-test.ipynb](/puregome/notebooks/blob/master/selenium-test.ipynb), after updating the name of the file in URLFILE in code block 4
2. Restart the notebook and run code blocks 1 and 6, after updating the name of the file in URLFILE in code block 6 to the same value as under code block 4. This takes many hours to complete
3. The notebook can be copied and several copies can be run in parallel
4. ...

## Publications

Shihan Wang, Marijn Schraagen, Erik Tjong Kim Sang and Mehdi Dastani, [Public Sentiment on Governmental COVID-19 Measures in Dutch Social Media](https://openreview.net/forum?id=37zyB5yuPXi). In: Workshop on NLP for COVID-19 (Part 2) at EMNLP 2020
(NLP-COVID19-EMNLP), 20 November 2020.

Shihan Wang, Marijn Schraagen, Erik Tjong Kim Sang and Mehdi Dastani, [Dutch General Public Reaction on Governmental COVID-19 Measures and Announcements in Twitter Data](https://arxiv.org/abs/2006.07283). Preprint report on arXiv.org, 29 September 2020.

Nienke Vergunst, [Researchers use social media data to analyse public sentiment about Coronavirus measures](https://www.uu.nl/en/news/researchers-use-social-media-data-to-analyse-public-sentiment-about-coronavirus-measures). University of Utrecht news message, 11 May 2020.

