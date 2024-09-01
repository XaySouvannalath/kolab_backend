from apify_client import ApifyClient


# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_j1CvTdGSt1GlW8RNa1s5K6YWoWRWvb4z77dp")


def get_fb_user_timeline():
    
# Prepare the Actor input
    run_input = {
        "startUrls": [{ "url": "https://www.facebook.com/zuck" }],
        "resultsLimit": 20,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("KoJrdxJCTtpon81KY").call(run_input=run_input)

    result =[]
    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        # print(item)
        result.append(item)
        
    return result
        