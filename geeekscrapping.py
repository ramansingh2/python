from bs4 import BeautifulSoup
import requests
import csv
page=requests.get("https://coreyms.com/")
soup=BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
# print(soup.find_all('p'))
# print(soup.p)
csv_file=open('corewyscrapping.csv','w')
csv_writer=csv.writer(csv_file)

csv_writer.writerow(['headline','summary','vid_link'])





for article in soup.find_all('article'):

    # print(article.prettify())
    headline=article.h2.a.text
    # print(headline)

    summary=article.find('div',class_="entry-content").p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except Exception as e:
        yt_link=None
    print(yt_link)

    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()