
from yelpapi import YelpAPI
import pandas as pd
import requests
import urllib.parse
import json

api_key = "8rq-4mCFLe1sPa-EB-6b0Q8U-0ziCFJ1yf4kaZzwetlAN5I30frlr365PneCR3mM5oTRVGyLnWArxNKnISv4Amu7ZNJvHkgJfHRzu5AdfNjydWmb9mhq14Muo4NMZXYx"
yelp_api = YelpAPI(api_key)


search_term = "Chinese"
location_term = "El Paso, TX"
search_results = yelp_api.search_query(term=search_term,location=location_term,sort_by='rating',limit=20)
sort_by = "rating"

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df)

id_for_reviews = 'noodles-and-dumplings-el-paso-6'
review_response = yelp_api.reviews_query(id=id_for_reviews)
#print(review_response)




result_df = pd.DataFrame.from_dict(review_response['reviews'])
print(result_df)

for review in review_response['reviews']:
    print("\n")
    print(review['text'])



result_df.to_csv('George_Dieter_Noodles_Dumplings_result.csv',index=False)



from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()
review1 = open('George_Dieter_Noodles_Dumplings_result.csv')

for review in review1:
    sentiment_score = vader.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')