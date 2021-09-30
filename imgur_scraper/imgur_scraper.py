import argparse
import csv
import datetime
import json
import os
import re

from requests_html import HTMLSession

from .utils import Convert


def get_more_details_of_post(post_url: str) -> json:
    """
    :param post_url: the url of an imgur post
    :return: Details like Virality-score, username etc in JSON format
    """
    details = {}
    try:
        request = HTMLSession().get(post_url)

        # some times, request isn't properly made, hence call again.
        if len(request.html.find('script')) < 18:
            request = HTMLSession().get(post_url)

            return details
            # handle when its not there at all

        regex = 'item: ({.+} )'  # regex to isolate the `item` dict.
        # 18th script tag has the `item` dict. this is tested on more than 1500 links.
        matched = re.search(regex, request.html.find(
            'script')[18].text).group(0)
        item = json.loads(matched[5:])

        details['username'] = item['account_url']
        details['comment_count'] = item['comment_count']
        details['downs'] = item['downs']
        details['ups'] = item['ups']
        details['points'] = item['points']
        details['score'] = item['score']
        details['timestamp'] = item['timestamp']
        details['views'] = item['views']
        details['favorite_count'] = item['favorite_count']
        details['hot_datetime'] = item['hot_datetime']
        details['nsfw'] = item['nsfw']
        details['platform'] = 'Not Detected' if item['platform'] == None else item['platform']
        details['virality'] = item['virality']
    except Exception as e:
        print(e)

    return details


def get_viral_posts_from(start_date: str, end_date: str, provide_details: bool) -> json:
    """
    :param start_date: date in string
    :param end_date: date in string
    :param provide_details: boolean value to get more details of a post
    :return: Imgur's viral content of the specified period in JSON Format
    """
    convert = Convert(start_date, end_date)
    start, end = convert.to_days_ago()
    for days_ago in reversed(range(end, start + 1)):
        day_count = 0
        counter = 0
        r = HTMLSession().get(
            f"https://imgur.com/gallery/hot/viral/page/{days_ago}/hit?scrolled&set={counter}"
        )
        if r.html.find(".images-header-main"):
            print(
                "Grabbing "
                + " ".join(r.html.find(".images-header-main")
                           [0].full_text.split())
            )
        while not r.html.find("#nomore"):
            for entries in r.html.find(".post"):
                less_details = {
                    "title": entries.find(".hover > p")[0].full_text,
                    "url": f"https://imgur.com{entries.find('.image-list-link')[0].attrs['href']}",
                    "points": entries.find(".point-info-points > span")[0].full_text,
                    "tags": entries.find(".point-info")[0].attrs["data-gallery-tags"].rstrip(),
                    "type": entries.find(".post-info")[0].full_text.strip().split()[0],
                    "views": entries.find(".post-info")[0].full_text.strip().split()[2],
                    "date": convert.from_days_ago(day_count),
                }
                if provide_details:
                    more_details = get_more_details_of_post(
                        f"https://imgur.com{entries.find('.image-list-link')[0].attrs['href']}")
                    yield dict(more_details, **less_details)
                else:
                    yield less_details
            counter += 1
            r = HTMLSession().get(
                f"https://imgur.com/gallery/hot/viral/page/{days_ago}/hit?scrolled&set={counter}"
            )
        day_count += 1


def main():
    parser = argparse.ArgumentParser(
        prog="imgur-scraper",
        usage="\n$ imgur-scraper [COMMAND]",
        description="Retrieve Imgur's Viral Posts",
    )
    parser._optionals.title = "COMMAND"
    parser.add_argument("--version", action="version",
                        version="%(prog)s 0.1.14")
    parser.add_argument(
        "--date",
        action="store",
        dest="date",
        type=str,
        metavar="",
        help="date format YYYY-MM-DD (required)",
        required=True,
    )
    parser.add_argument(
        "--end_date",
        action="store",
        dest="end_date",
        type=str,
        metavar="",
        help="date format YYYY-MM-DD (optional)",
        default=str(datetime.datetime.utcnow()),
    )
    parser.add_argument(
        "--csv",
        action="store_true",
        dest="to_csv",
        help="flag to save the data in a csv file (defaults to False)",
    )
    parser.add_argument(
        "--path",
        action="store",
        default=".",
        metavar="",
        type=str,
        dest="path_to_save",
        help="path to save the csv file in \
            (defaults to the current working directory)",
    )
    parser.add_argument(
        "--details",
        action="store_true",
        dest="provide_details",
        help="flag to get more details about a post, like: username, virality etc"
        # TODO: describe better
    )
    results = parser.parse_args()
    start_date = results.date
    end_date = results.end_date.split(" ")[0]
    path = results.path_to_save
    to_csv = results.to_csv
    provide_details = results.provide_details

    if to_csv:
        try:
            file_name = os.path.join(
                path, f"{start_date}_to_{end_date}_imgur_data.csv")
            with open(file_name, "x", newline="", encoding="utf-8") as csvfile:
                if provide_details:
                    fieldnames = ["title", "url", "points", "tags", "type", "views", "date", "username", "comment_count", "downs",
                                  "ups", "points", "score", "timestamp", "views", "favorite_count", "hot_datetime", "nsfw", "platform", "virality"]
                else:
                    fieldnames = ["title", "url", "points",
                                  "tags", "type", "views", "date"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(get_viral_posts_from(
                    start_date, end_date, provide_details))
            print(f"CSV saved in {os.path.abspath(file_name)}")
        except FileExistsError as f:
            print(f)
        except ValueError as v:
            print(v)
    else:
        for post in get_viral_posts_from(start_date, end_date, provide_details):
            print(post)


if __name__ == "__main__":
    main()
