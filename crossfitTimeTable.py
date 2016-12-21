from bs4 import BeautifulSoup
import urllib2,re, requests, os

'''
r = requests.get('https://fantasy.premierleague.com/a/team/my', auth=('singh.pavi9@hotmail.com', 'suttapride891'))
print(r.status_code)
'''

html = urllib2.urlopen("https://app.wodify.com/Schedule/PublicCalendarListView.aspx?tenant=3920").read()
soup = BeautifulSoup(html)


table = soup.find('table', attrs={'class': 'TableRecords'})
table_body = table.find('tbody')

for row in table_body.find_all("tr"):
    for stat in row.find_all("td", attrs={'class':'TableRecords_EvenLine'}):
        for text in stat:
            for spn in text.find_all("span"):
                print("SPn val:", spn)
                print("Spnm content:",spn.contents)
                for ttle in spn.find_all("title"):
                    print("title???: ", ttle.contents)
