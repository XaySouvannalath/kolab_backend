

import requests
from bs4 import BeautifulSoup
import json
import scrapy

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

                follower_count = script.text[start_index:end_index]
                break
        return follower_count
    return None


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
       
        return follower_count
    return None

