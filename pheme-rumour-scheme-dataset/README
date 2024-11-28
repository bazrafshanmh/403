======================================
PHEME dataset of social media rumours:

Journalism use case
======================================

This directory contains the PHEME rumour dataset collected and annotated within the journalism use case of the project. These rumours are associated with 9 different breaking news. It was created for the analysis of social media rumours, and contains Twitter conversations which are initiated by a rumourous tweet; the conversations include tweets responding to those rumourous tweets. These tweets have been annotated for support, certainty, and evidentiality.

The code we used for the collection of conversations from Twitter is available on GitHub: https://github.com/azubiaga/pheme-twitter-conversation-collection

Please, refer to the papers below for further details on the datasets.

Data Structure
==============

The dataset contains 330 conversational threads (297 in English, and 33 in German), with a folder for each thread, and structured as follows:

 * source-tweets: This folder contains a json file with the source tweet.

 * reactions: This folder contains the json files for all the tweets that participated in the conversations by replying.

 * url-content: This folder contains the content of the web pages pointed to from the tweets.

 * structure.json: This file provides the structure of the conversation, making it easier to determine what each tweets children tweets are and to reconstruct the conversations by putting together the source tweet and the replies.

 * retweets.json: This file contains the tweets that retweeted the source tweet.

 * who-follows-whom.dat: This file contains the users, within the thread, who are following someone else. Each row contains two IDs, representing that the user with the first ID follows the user with the second ID. Note that following is not reciprocal, and therefore if two users mutually follow each other it'll be represented in two rows, A B and B A.

 * annotation.json: This files includes the manual annotations at the thread level, which is especially useful for rumours, and contains the following fields:
  ** is_rumour: which is rumour or non-rumour.
  ** category: which is the title that describes the rumourous story, and can be used to group with other rumours within the same story.
  ** misinformation: 0 or 1. It determines if the story was later proven false, in which case is set to 1, and otherwise is set to 0.
  ** true: 0 or 1. It determines if the story was later confirmed to be true, in which case is set to 1, and otherwise is set to 0.
  ** is_turnaround: 0 or 1. A thread is marked as a turnaround if it represents a shift in the rumourous story, either by confirming in the case of a true story, or debunking in the case of a false story.
  ** links: when available, this contains a list of links that covered the rumourous story, which includes the URL of the link, the type of media (social media, news media or blog), and whether it is positioned against, for or observing the rumour.

Annotations
===========

The annotations performed at the tweet level for the 4,842 tweets within these 330 conversations can be found in two files:
 * annotations/en-scheme-annotations.json (for the English threads)
 * annotations/de-scheme-annotations.json (for the German threads)

Each line contains a tweet, with its event, threadid and tweetid identifiers, as well as the annotations for support, certainty, and evidentiality.

Annotation process and references:
==================================

For more details on the annotation process, please refer to the following papers (please, consider citing them if you make use of this dataset for your research):

 * Arkaitz Zubiaga, Maria Liakata, Rob Procter, Kalina Bontcheva, Peter Tolmie. Crowdsourcing the Annotation of Rumourous Conversations in Social Media. WWW Companion. 2015.
   http://www.zubiaga.org/publications/files/www2015-crowdsourcing.pdf

 * Arkaitz Zubiaga, Maria Liakata, Rob Procter, Geraldine Wong Sak Hoi, Peter Tolmie. Analysing How People Orient to and Spread Rumours in Social Media by Looking at Conversational Threads. PLoS ONE 11(3): e0150989. 2016. http://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0150989

Acknowledgment:
===============

The development of this dataset has been supported by the PHEME FP7 project (grant No. 611233).

Contact:
========

If you encounter any problems while using this dataset or having any questions, feel free to email me: a.zubiaga@warwick.ac.uk
