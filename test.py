from imgur_scraper import get_viral_posts_from

for i, k in enumerate(get_viral_posts_from(date="27/02/18")):
    print(str(i), k)