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
    start, end = Convert(start_date, end_date).to_days_ago()
    for days_ago in reversed(range(end, start + 1)):
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
                    "tags": entries.find(".point-info")[0]
                    .attrs["data-gallery-tags"]
                    .rstrip(),
                }
            counter += 1
            r = HTMLSession().get(
                f"https://imgur.com/gallery/hot/viral/page/{days_ago}/hit?scrolled&set={counter}"
            )


def main():
    parser = argparse.ArgumentParser(
        prog="imgur-scraper",
        usage="\n$ imgur-scraper [COMMAND]",
        description="Retrieve Imgur's Viral Posts",
    )
    parser._optionals.title = "COMMAND"
    parser.add_argument(
        "--date",
        action="store",
        dest="date",
        type=str,
        metavar="",
        help="Format YYYY-MM-DD (required)",
        required=True,
    )
    parser.add_argument(
        "--end_date",
        action="store",
        dest="end_date",
        type=str,
        metavar="",
        help="Format YYYY-MM-DD (optional)",
        default=str(datetime.datetime.utcnow()),
    )
    parser.add_argument(
        "--csv",
        action="store_true",
        dest="to_csv",
        help="Format to Save Data In (defaults to False)",
    )
    parser.add_argument(
        "--path",
        action="store",
        default=".",
        metavar="",
        type=str,
        dest="path_to_save",
        help="Path where in to the file csv file, i.e. ../somefoler/. \
            (Defaults to the path from where the script is called.)",
    )
    results = parser.parse_args()
    start_date = results.date
    end_date = results.end_date.split(" ")[0]
    path = results.path_to_save
    to_csv = results.to_csv

    if to_csv:
        try:
            path = os.path.join(path, f"{start_date}_to_{end_date}_imgur_data.csv")
            with open(path, "x", newline="") as csvfile:
                fieldnames = ["title", "url", "points", "tags"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(get_viral_posts_from(start_date, end_date))
        except FileExistsError:
            print("File Already Exists.")


if __name__ == "__main__":
    main()
