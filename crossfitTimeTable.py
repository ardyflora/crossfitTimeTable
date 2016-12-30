from bs4 import BeautifulSoup
import urllib2,re, requests, os

'''
r = requests.get('https://fantasy.premierleague.com/a/team/my', auth=('singh.pavi9@hotmail.com', 'suttapride891'))
print(r.status_code)
'''

html = urllib2.urlopen("https://app.wodify.com/Schedule/PublicCalendarListView.aspx?tenant=3920").read()
soup = BeautifulSoup(html,"lxml")



table = soup.find('table', attrs={'class': 'TableRecords'})
table_body = table.find('tbody')

FinalData = []

for row in table_body.find_all("tr"):
    for stat in row.find_all("td", attrs={'class':['TableRecords_EvenLine', 'TableRecords_OddLine']}):
        dictContent ={}
        for spn in stat.find_all("span"):
            if spn.has_attr("title"):
                if 'Olympic Weightlifting' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                            dictContent["Title"] = str(spn["title"])
                elif 'CrossFit' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        dictContent["Title"] = str(spn["title"])
                elif 'Open Gym' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        dictContent["Title"] = str(spn["title"])
                elif 'Athletic Conditioning' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        dictContent["Title"] = str(spn["title"])
        if len(dictContent) >0:
            FinalData.append(dictContent)


print("THe final data is:", FinalData)


'''               
            elif spn.has_attr("class"):
                if 'h3' in spn["class"]:
                    print(spn.contents)
            elif spn.has_attr("style"):
                print(spn.text)

                '''

