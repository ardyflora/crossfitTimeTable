from bs4 import BeautifulSoup
import urllib2,re, requests, os


from prettytable import PrettyTable
x = PrettyTable()


html = urllib2.urlopen("https://app.wodify.com/Schedule/PublicCalendarListView.aspx?tenant=3920").read()
soup = BeautifulSoup(html,"lxml")


table = soup.find('table', attrs={'class': 'TableRecords'})
table_body = table.find('tbody')

FinalData = []
FinalData2 = []

for row in table_body.find_all("tr"):
    for stat in row.find_all("td", attrs={'class':['TableRecords_EvenLine', 'TableRecords_OddLine']}):
        dictContent ={}
        dict2Content = {}
        z={}
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
                        dict2Content["Title"] = str(spn["title"])
                elif 'CrossFit' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        x.add_row([str(spn["title"]),""])
                        dict2Content["Title"] = str(spn["title"])
                elif 'Open Gym' in spn["title"]:
                    if re.match(r'^[0-9]', spn["title"][0]):
                        x.add_row([str(spn["title"]),""])
                        dict2Content["Title"] = str(spn["title"])
                elif 'Athletic Conditioning' in spn["title"]:
                    x.add_row([str(spn["title"]),""])
                    if re.match(r'^[0-9]', spn["title"][0]):
                        dict2Content["Title"] = str(spn["title"])
        if len(dictContent) >0:
            FinalData.append(dictContent)
        if len(dict2Content)>0:
            FinalData2.append(dict2Content)
        print("Final data val:", FinalData)
        print("Final data 2val:", FinalData2)
        if len(FinalData2) >0:
            z = dict(FinalData + FinalData2)


print("the val of z: ",z)
print("THe final data is:", FinalData)
print("THe final data 2 is:", FinalData2)

'''               
            elif spn.has_attr("class"):
                if 'h3' in spn["class"]:
                    print(spn.contents)
            elif spn.has_attr("style"):
                print(spn.text)

                '''

