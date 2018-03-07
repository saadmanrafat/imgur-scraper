from datetime import datetime, timedelta
from requests_html import HTMLSession

url = "https://imgur.com/gallery/hot/viral/page/{0}/hit?scrolled&set={1}"
host = "https://imgur.com"
date_format = "%d/%m/%y"


def get_viral_posts_from(date):
    """Returns the viral posts of the day

    :param date: Viral posts from date, where the date is a string.
    """
    try:
        assert datetime.today() > datetime.strptime(date, date_format)
    except AssertionError:
        raise ValueError('Invalid date')

    days_ago = datetime.today() - datetime.strptime(date, date_format) - timedelta(days=1)
    counter = 0
    r = HTMLSession().get(url.format(days_ago.days, counter))

    print(days_ago.days)

    while not r.html.find('#nomore'):
        print(' '.join(r.html.find('.images-header-main')[0].full_text.split()))
        for entries in r.html.find('.post'):
            yield {
                'title': entries.find('.hover > p')[0].full_text,
                'url': host + entries.find('.image-list-link')[0].attrs['href'],
                'points': entries.find('.point-info-points > span')[0].full_text,
                'tags': entries.find('.point-info')[0].attrs['data-gallery-tags'].rstrip()
            }
            
        counter += 1
        r = HTMLSession().get(url.format(days_ago.days, counter))
