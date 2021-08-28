from bs4 import BeautifulSoup
import requests
import telegram
from testdeal.models import MyDeal
from datetime import datetime, timedelta
response = requests.get(
    "https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1&divpage=68")

soup = BeautifulSoup(response.text, "html.parser")
# BOT_TOKEN = "1969113519:AAHdUsEnOE6Vof6HIyZV1Uhi9sqCE6QD4AA"
#
# bot = telegram.Bot(token=BOT_TOKEN)

def run():
    row, _ = MyDeal.objects.filter(created_at__lte=datetime.now()-timedelta(seconds=1)).delete()
    print(row,"deals deleted")
    for item in soup.find_all("tr", {'class': ["list1", "list0"]}):
        try:
                image = item.find("img", class_="thumb_border").get("src")[2:]
                image = "http://" + image
                enroll = item.find("nobr",class_="eng list_vspace").text
                title = item.find("font", class_="list_title").text
                title = title.strip()
                link = item.find("font", class_="list_title").parent.get("href")
                link = "https://www.ppomppu.co.kr/zboard/" + link
                reply_count = item.find("span", class_="list_comment2").text
                reply_count = int(reply_count)
                up_count = item.find_all("td")[-2].text

                up_count = up_count.split("-")[0]
                up_count = int(up_count)


                if (MyDeal.objects.filter(link__iexact=link).count() ==0) :
                    MyDeal(image_url=image, title=title, link=link,reply_count=reply_count,up_count=up_count,enroll=enroll).save()

                        # bot.sendMessage(-1001523717670, '{}{} {}'.format(image,title, link))
        except Exception as e:
                continue





