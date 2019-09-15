# Imgur Scraper
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/imgur-scraper) [![Downloads](https://pepy.tech/badge/imgur-scraper)](https://pepy.tech/project/imgur-scraper) ![PyPI - License](https://img.shields.io/pypi/l/imgur-scraper)

Retrieve Imgur's viral posts from a specific date. No authentication required. Implemented using their frontend API.

# Usage

[![asciicast](https://asciinema.org/a/268419.svg)](https://asciinema.org/a/268419)

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

