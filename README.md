# iSagha Gold Price Scraper

A simple Python script that scrapes live gold prices in Egypt from [iSagha Market](https://market.isagha.com/prices) and exports them to a CSV file.

## Features

- Scrapes prices for 24K, 21K, and 18K gold (buy price, sell price, and price direction: up/down)
- Automatically exports results to a CSV file encoded in UTF-8 with BOM, so Arabic text displays correctly in Excel

## Requirements

```bash
pip install requests beautifulsoup4 lxml
```

## Usage

```bash
python isagha-gold-price-scraper.py
```

This generates a `golds_prices.csv` file containing the price data.

## Data fields (in Arabic, as they appear on the source site)

| Field          | Description                                      |
|----------------|---------------------------------------------------|
| العيار         | Gold purity (24K / 21K / 18K)                     |
| سعر البيع      | The price at which the dealer sells               |
| سعر الشراء     | The price at which the dealer buys                |
| الحالة         | Price direction since the last update (up/down)   |


is project is for educational and personal use only. Data source: iSagha Market.
