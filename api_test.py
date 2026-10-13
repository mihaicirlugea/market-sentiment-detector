
import requests

def scan_text(title):
    panic_words = ["crash", "collapse", "recession", "sell", "plummet", "blood", "bankrupt"]
    greed_words = ["moon", "surge", "record", "buy", "rally", "ath", "guaranteed"]
    isgreed = 0
    ispanic = 0
    words = title.lower().split()
    for cuvant in panic_words:
        if cuvant in words:
            ispanic += 1    
    for cuvant in greed_words:
        if cuvant in words:
            isgreed += 1
    if isgreed > ispanic:
        decision = "SELL"
    elif ispanic > isgreed:
        decision = "BUY"
    else:
        decision = "Wait"  
    return decision     


url = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo"
answer = requests.get(url)
data_market = answer.json()
news_list = data_market["feed"]

for articles in news_list:
    advice = scan_text(articles["title"])
    print(f"{advice} | {articles['title']}")