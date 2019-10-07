import argparse
import csv
import datetime
import json
import os

from requests_html import HTMLSession

from .utils import Convert


def get_viral_posts_from(start_date: str, end_date: str) -> json:
    """
    :param start_date: date in string
    :param end_date: date in string
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
                + " ".join(r.html.find(".images-header-main")[0].full_text.split())
            )
        while not r.html.find("#nomore"):
            for entries in r.html.find(".post"):
                yield {
                    "title": entries.find(".hover > p")[0].full_text,
                    "url": f"https://imgur.com{entries.find('.image-list-link')[0].attrs['href']}",
                    "points": entries.find(".point-info-points > span")[0].full_text,
                    "tags": entries.find(".point-info")[0].attrs["data-gallery-tags"].rstrip(),
                    "type": entries.find(".post-info")[0].full_text.strip().split()[0],
                    "views": entries.find(".post-info")[0].full_text.strip().split()[2],
                    "date": convert.from_days_ago(day_count),
                    "likes": entries.find(".arrows > .icon-upvote-outline")[0].attrs["data-up"],
                    "dislikes": entries.find(".arrows > .icon-downvote-outline")[0].attrs["data-downs"],
                }
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
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.14")
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
    results = parser.parse_args()
    start_date = results.date
    end_date = results.end_date.split(" ")[0]
    path = results.path_to_save
    to_csv = results.to_csv

    if to_csv:
        try:
            file_name = os.path.join(path, f"{start_date}_to_{end_date}_imgur_data.csv")
            with open(file_name, "x", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["title", "url", "points", "tags", "type", "views", "date"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(get_viral_posts_from(start_date, end_date))
            print(f"CSV saved in {os.path.abspath(file_name)}")
        except FileExistsError as f:
            print(f)
        except ValueError as v:
            print(v)
    else:
        for post in get_viral_posts_from(start_date, end_date):
            print(post)


if __name__ == "__main__":
    main()
