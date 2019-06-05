# scraper-script

## Starting crawler
```scrapy crawl clothing -a tag="tag" -o plik.json ```

"tag" - specify what you want to search, first word must be a thing, f.e. "kurtka zimowa", "bluza z kapturem" - -a tag needed

plik.json - file where scrapped things will be stored - -o flag needed

```sudo docker run -p 8050:8050 scrapinghub/splash```

needed to run Splash

### Results structure

```{ClothesName: { "image": imageURL, "price": PRICE, "url": URL}} ```

ClothesName - string with the name of clothes, f.e "Nike Nightgazer"

imageURL - string with url to image

price - string with price(zł or PLN) - "XX,XX zł/PLN"

url - string with url to shop
