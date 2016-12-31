from bs4 import BeautifulSoup
import urllib2,re, requests, os


from prettytable import PrettyTable
x = PrettyTable()


'''
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide",1295, 1158259, 600.5])

print x.get_string(fields=["City name", "Population"])

'''

html = urllib2.urlopen("https://app.wodify.com/Schedule/PublicCalendarListView.aspx?tenant=3920").read()
soup = BeautifulSoup(html,"lxml")



table = soup.find('table', attrs={'class': 'TableRecords'})
table_body = table.find('tbody')

FinalData = []

for row in table_body.find_all("tr"):
    for stat in row.find_all("td", attrs={'class':['TableRecords_EvenLine', 'TableRecords_OddLine']}):
        dictContent ={}
        dict2Content = {}
        for spn in stat.find_all("span"):
            if spn.has_attr("class"):
                    if 'h3' in spn["class"]:
                        x.field_names = [str(spn.contents[0]), str(spn.contents[2])]
                        print x.get_string()
                        dictContent["Day"] = str(spn.contents[0])
                        dictContent["Date"] = str(spn.contents[2])
            elif spn.has_attr("title"):
                if 'Olympic Weightlifting' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        x.add_row([str(spn["title"]),""])
                        dictContent["Title"] = str(spn["title"])
                elif 'CrossFit' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        x.add_row([str(spn["title"]),""])
                        dictContent["Title"] = str(spn["title"])
                elif 'Open Gym' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        x.add_row([str(spn["title"]),""])
                        dictContent["Title"] = str(spn["title"])
                elif 'Athletic Conditioning' in spn["title"]:
                    x.add_row([str(spn["title"]),""])
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

