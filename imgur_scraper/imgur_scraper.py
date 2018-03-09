from .utils import Convert
from requests_html import HTMLSession

url = "https://imgur.com/gallery/hot/viral/page/{0}/hit?scrolled&set={1}"
host = "https://imgur.com"


def get_viral_posts_from(date):
    """Returns viral posts of a given date

    :param date: a string in the format 'dd/mm/yy' i.e '31/12/15'
    """

    days_ago = Convert(date).to_days_ago()
    counter = 0

    r = HTMLSession().get(url.format(days_ago, counter))

    if r.html.find('.images-header-main'):
        print(' '.join(r.html.find('.images-header-main')[0].full_text.split()))

    while not r.html.find('#nomore'):
        for entries in r.html.find('.post'):
            yield {
                'title': entries.find('.hover > p')[0].full_text,
                'url': host + entries.find('.image-list-link')[0].attrs['href'],
                'points': entries.find('.point-info-points > span')[0].full_text,
                'tags': entries.find('.point-info')[0].attrs['data-gallery-tags'].rstrip()
            }
        counter += 1
        r = HTMLSession().get(url.format(days_ago, counter))




