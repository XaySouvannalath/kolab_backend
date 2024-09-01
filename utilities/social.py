

from fastapi import HTTPException
import requests
from bs4 import BeautifulSoup
import json
import scrapy



def get_tiktok_follower_ranking(followers):
    if isinstance(followers,int):
        if followers < 1000:
            return "Less than Nano"
        elif 1000 <= followers < 30000:
            return "Nano"
        elif 30000 <= followers < 100000:
            return "Micro"
        elif 100000 <= followers < 500000:
            return "Mid-Tier"
        elif 500000 <= followers < 1000000:
            return "Macro"
        elif followers > 1000001:
            return "Mega"
        else:
            return "-"
    else:
        return "-"


def get_facebook_follower_ranking(followers):
    print(type(followers))
    print(followers)
    if isinstance(followers,int):  
            if followers < 1000:
                return "Less than Nano"
            elif 1000 <= followers < 10000:
                return "Nano"
            elif 10000 <= followers < 50000:
                return "Micro"
            elif 50000 <= followers < 100000:
                return "Mid-Tier"
            elif 100000 <= followers < 500000:
                return "Macro"
            elif followers > 500001:
                return "Mega"
            else:
                return "-"
    else:
        return "-"

    
 

def get_tiktok_followers(username):
    url = f"https://www.tiktok.com/@{username}"
    
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        follower_count = None
        for script in soup.find_all('script'):
            if 'followerCount' in script.text:
                start_index = script.text.find('"followerCount":') + len('"followerCount":')
                end_index = script.text.find(',', start_index)

                follower_count = int(script.text[start_index:end_index])
                break
        return {
            "followers": follower_count,
            "ranking": get_tiktok_follower_ranking(follower_count)
        }
    return {
        "details": "User not found"
    }


def get_facebook_followers(username):
    url = f"https://www.facebook.com/{username}"
    
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    # print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the follower count
        follower_count = None
       
        return {
            "followers": follower_count,
            "ranking": get_facebook_follower_ranking(follower_count)
        }
    return None



def get_youtube_followers(username):
    
    YOUR_API_KEY = "AIzaSyAPr6ti4hBb_9yYuYZPwCC8VfKUFqqVo3o"
    #     # Sample text
    # text = username

    # # Extract the word after the '@' sign
    # word_after_at = text.split('@')[1]

    # # Print the result
    # print(word_after_at)

    url =f"https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2Cstatistics&forHandle={username}&key={YOUR_API_KEY}"
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    data = response.json()
    
    
    
    if "items" not in data or len(data["items"]) == 0:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    result = {
        "followers": data["items"][0]["statistics"]["subscriberCount"],
        "view_count": data["items"][0]["statistics"]["viewCount"],
        "ranking": get_tiktok_follower_ranking(int(data["items"][0]["statistics"]["subscriberCount"]))
        
    }
    
    return result
    
    




