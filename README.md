# Imgur Scraper
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/imgur-scraper) [![Downloads](https://pepy.tech/badge/imgur-scraper)](https://pepy.tech/project/imgur-scraper) ![PyPI - License](https://img.shields.io/pypi/l/imgur-scraper)

Retrieve years of imgur.com's data. No authentication required. Implemented using their frontend API.

# Usage

```
$ imgur-scraper -h

usage: 
$ imgur-scraper [COMMAND]

Retrieve Imgur's Viral Posts

COMMAND:
  -h, --help   show this help message and exit
  --version    show program's version number and exit
  --date       date format YYYY-MM-DD (required)
  --end_date   date format YYYY-MM-DD (optional)
  --csv        flag to save the data in a csv file (defaults to False)
  --path       path to save the csv file in (defaults to the current working
               directory)

```

Enter a date range you want to scrape 

```
$ imgur-scraper --date 2017-12-25 --end_date 2018-01-25 --csv
```

# Features

Returns close to 500 data points for each date.

```javascript
{
  'title': 'I said no, my fiancé said yes. Meet Zeta', 
  'url': 'https://imgur.com/gallery/H5Xw4dh', 
  'points': '5,996', 
  'tags': 'aww,kitten,kitty', 
  'type': 'image', 
  'views': '4,363'
}
```
More attributes to be added soon, any suggestions or [feature requests](https://github.com/saadmanrafat/imgur-scraper/issues) are welcome. 

# Installation
```
$ pip install imgur-scraper
```

