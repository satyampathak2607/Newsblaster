import requests
from bs4 import BeautifulSoup

def multi_rss_generator(feed_urls, max_articles = 10):
    headers = {'User-Agent': 'Mozilla/5.0'}
    

    for rss_url in feed_urls:
        try:
            count = 0
            response = requests.get(rss_url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f" Failed : {rss_url} with status code {response.status_code}")
                continue
            soup = BeautifulSoup(response.content, features ='xml')
            for item in soup.find_all('item'):
                link_tag  = item.find('link')
                if link_tag and link_tag.text:
                    yield link_tag.text.strip()
                    count += 1
                    if count >= max_articles:
                        break
        except Exception as e:
            print(f"Error processing {rss_url}: {e}")

