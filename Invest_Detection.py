print("Title for news:")
news =input().lower().split()

panic_words = ["crash", "collapse", "recession", "sell", "plummet", "blood", "bankrupt"]
greed_words = ["moon", "surge", "record", "buy", "rally", "ath", "guaranteed"]
isgreed = 0
ispanic = 0

for cuvant in  panic_words:
    if cuvant in news:
        ispanic += 1
    
for cuvant in greed_words:
    if cuvant in news:
        isgreed += 1
    
if isgreed > ispanic:
    print("Greed detected \n")
    print("SELL")
elif ispanic > isgreed:
    print("Panic detected \n")
    print("BUY")
else:
    print("No market signal")
    print("Wait") 