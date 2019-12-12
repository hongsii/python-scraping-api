from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime


def get_switch_news(minutes):
    html = urlopen("https://bbs.ruliweb.com/nin/board/300004")
    bs = BeautifulSoup(html.read(), 'html.parser')

    now = datetime.datetime.now()
    threshold_date = now - datetime.timedelta(minutes=int(minutes))
    list = bs.find_all("tr", {"class": "table_body"})
    result = []
    for news in list:
        time = news.find("td", {"class": "time"}).text.strip()
        if ":" not in time:
            continue

        target_date = datetime.datetime.strptime(time, '%H:%M').replace(
            year=now.year, month=now.month, day=now.day
        )
        if threshold_date > target_date:
            continue

        link = news.find("a", {"class": "deco"})
        result.append({
            "title": link.text,
            "url": link.attrs["href"]
        })
    return result
