from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime


def get_switch_news(interval):
    pc_base_url = "https://bbs.ruliweb.com"
    mobile_base_url = "https://m.ruliweb.com"
    html = urlopen(pc_base_url + "/nin/board/300004")
    bs = BeautifulSoup(html.read(), 'html.parser')
    print("get contents")

    now = datetime.datetime.now()
    threshold_date = now - datetime.timedelta(minutes=int(interval))
    list = bs.find_all("tr", {"class": "table_body"})
    result = []
    print("start parsing contents")
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
        print(link)
        result.append({
            "title": link.text,
            "url": {
                "pc": link.attrs["href"],
                "mobile": link.attrs["href"].replace(pc_base_url, mobile_base_url)
            },
            "date": target_date.strftime("%Y-%m-%d %H:%M")
        })
    print("finished parsing contents")
    return result
