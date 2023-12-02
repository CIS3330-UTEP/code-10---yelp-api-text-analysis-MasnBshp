from yelpapi import YelpAPI
import pandas as pd


api_key = "8rq-4mCFLe1sPa-EB-6b0Q8U-0ziCFJ1yf4kaZzwetlAN5I30frlr365PneCR3mM5oTRVGyLnWArxNKnISv4Amu7ZNJvHkgJfHRzu5AdfNjydWmb9mhq14Muo4NMZXYx"
yelp_api = YelpAPI(api_key)
search_term = "tacos"
location_term = "El Paso, TX"
search_results = yelp_api.search_query(term=search_term,location=location_term,sort_by='rating',limit=20)

for business in search_results['businesses']:
    print('\n')
    print(business)

id_for_reviews = 'little-habana-el-paso'


reviews_response = yelp_api.reviews_query(id=id_for_reviews)

for review in reviews_response['reviews']:
    print(review)
    #Getting the lis of information from Yelp but as a dataframe
result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df)

result_df.to_csv('api_result.csv',index=False)




# url = f"https://api.yelp.com/v3/businesses/search?location={location_term}&term={search_term}&sort_by={sort_by}&limit={limit}"
# headers = {"accept": "application/json", "Authorization": 
#            "Bearer 8rq-4mCFLe1sPa-EB-6b0Q8U-0ziCFJ1yf4kaZzwetlAN5I30frlr365PneCR3mM5oTRVGyLnWArxNKnISv4Amu7ZNJvHkgJfHRzu5AdfNjydWmb9mhq14Muo4NMZXYx"}

# response = requests.get(url, headers=headers)
# response_json = json.loads(response.text)

# print(response_json['businesses'])


# search_results = yelp_api.search_query(term=search_term,location=location_term,sort_by='rating',limit=20)
 
# print(search_results)

# # for business in search_results['businesses']:
# #     print('\n')
# #     print(business)
# print("\n")
# id_for_reviews = 'little-habana-el-paso'

#reviews_response = yelp_api.reviews_query(id=id_for_reviews)

# for review in reviews_response['reviews']:
#     print(review)
    #Getting the lis of information from Yelp but as a dataframe
# result_df = pd.DataFrame.from_dict(search_results['businesses'])
# print(result_df)

# result_df.to_csv('api_result.csv',index=False)

