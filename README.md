# Imgur Scraper
[![Downloads](https://pepy.tech/badge/imgur-scraper)](https://pepy.tech/project/imgur-scraper) 

Retrieve Imgur's viral posts from a specific date. No authentication required. Implemented using their frontend API.

# Usage
```
$ imgur-scraper [COMMAND]

Retrieve Imgur's Viral Posts

COMMAND:
  -h, --help   show this help message and exit
  --date       Format YYYY-MM-DD (required)
  --end_date   Format YYYY-MM-DD (optional)
  --csv        Format to Save Data In (defaults to False)
  --path       Path where in to the file csv file, i.e. ../somefoler/.
               (Defaults to the path from where the script is called.)

```

# Installation
```
$ pip install imgur-scraper
```

Python 3.6 is required
