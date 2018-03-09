Imgur Scraper
=======================================
Retrieve Imgur's viral posts from a specific date. No authentication required. Implemented using their frontend API.

Usage
================

.. code-block:: pycon

	>>> from imgur_scraper import get_viral_posts_from
	>>> for post in get_viral_posts_from(date="31/12/2015"):
	>>>     print(post)
	The most viral images from Wednesday, Dec 31 2015
	{
        'title': 'Tire went flat overnight and decided to have a little fun',
        'url': 'https://imgur.com/gallery/SIQgS',
        'points': '15,893',
	    'tags': 'funny'
	}
	… prints all 500 of them


Installation
============

.. code-block:: shell
	
	pip install imgur-scraper

Python 3.6 is required

    
