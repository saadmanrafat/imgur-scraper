# imgur-scraper
Get Imgur's viral posts from a given date. Not authentication required. Implemented using their frontend API.

# Usage
```python
>>> from imgur_scraper import get_viral_posts_from
>>> for post in get_viral_posts_from(date="12/31/14"):
>>>     print(post)
The most viral images from Wednesday, Dec 31 2014
{
  'title': 'I will never not upvote this', 
  'url': 'https://imgur.com/gallery/rRAayxk', 
  'points': '12,481', 
  'tags': 'funny,spam,mmo,needsmorejpeg,doublenegative,repost,reposttimesamillion
}
… prints all 500 of them
```

# Installation

    
