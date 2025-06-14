from rss_generator import multi_rss_generator
from scrapper import threaded_fetch
from summarizer import parallel_summarize
def main():
    rss_feeds = [
        "https://www.firstpost.com/commonfeeds/v1/mfp/rss/india.xml",
        "https://feeds.feedburner.com/ndtvnews-india-news",
        "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
    ]


    urls = list(multi_rss_generator(rss_feeds, max_articles=3))

    print(" Streaming article URLs:")
    for i, url in enumerate(urls):
        print(f"[{i+1}] {url}")


    threaded_fetch(urls)
    parallel_summarize()

if __name__ == "__main__":
    main()


