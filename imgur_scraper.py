from requests_html import HTMLSession

url = "https://imgur.com/gallery/hot/viral/page/{0}/hit?scrolled&set={1}"
host = "https://imgur.com"


def get_viral_posts(day=1):
    """Returns the viral posts of the day

    :param day: Viral posts from x days ago.

    """
    counter = 0
    
    r = HTMLSession().get(url.format(day, counter))
    print('Scraping ', url.format(day, counter))
    while not r.html.find('#nomore'):

        for entries in r.html.find('.post'):
            yield {
                'title': entries.find('.hover > p')[0].full_text,
                'url': host + entries.find('.image-list-link')[0].attrs['href'],
                'points': entries.find('.point-info-points > span')[0].full_text,
                'tags': entries.find('.point-info')[0].attrs['data-gallery-tags'].rstrip()
            }
            
        counter += 1
        r = HTMLSession().get(url.format(day, counter))