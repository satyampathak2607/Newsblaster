import os
import requests
import threading
from bs4 import BeautifulSoup

def fetch_article(url, save_dir ="raw_articles"):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch {url} with status code {response.status_code}")
            return 
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text() for p in paragraphs if p.get_text(strip = True))
        
        file_name = url.split("/")[-1][:40].replace("?", "").replace("&", "").replace("=", "")
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        os.makedirs(save_dir, exist_ok=True)
        path = os.path.join(save_dir, file_name)
        with open(path, "w", encoding='utf-8') as file:
            file.write(text)
        
        print(f"Saved article from {url} to {path}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

def threaded_fetch(url_list, save_dir="raw_articles"):
    threads = []
    for url in url_list:
        thread = threading.Thread(target=fetch_article, args=(url, save_dir))
        thread.start()
        threads.append(thread)
     
    
    for thread in threads:
        thread.join()
