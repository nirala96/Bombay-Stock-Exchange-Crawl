# Bombay Stock Exchange crawl  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Bombay_Stock_Exchange_logo.svg/1200px-Bombay_Stock_Exchange_logo.svg.png" alt="drawing" width="70"/>
Used Scrapy to Scrape details of the [BSE India](https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx?expandable=3/) and store that in CSV file.

## Framework Used
- Scrapy (Python framework)

## Output
- [BSEOutput](https://github.com/nirala96/Bombay-Stock-Exchange-Crawl/blob/main/BSEIndiaScrape/BSEOutput.csv)
  
## Output in CSV file with output

```python
scrapy crawl bsespider -o BSEOutput.csv
```

## Prerequisite
- python3
- Scrapy
- urllib
