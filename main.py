import requests
from bs4 import BeautifulSoup

def spam(URL):
    resp = requests.get(URL)
    '''file = open("output.txt", "w")
    file.write(resp.text)'''

    soup = BeautifulSoup(resp.text, 'html.parser')
    tags = soup.find_all('tr', attrs = {"class" : "problemrow"})
    for tag in tags:
        name = tag.find('b')
        #print(name.contents[0])

        elements = tag.find_all('a')
        count = 0
        for element in elements:

            count += 1
            s = (element['href'])
            if "problems" in s:
                s = "https://www.codechef.com" + s
                #print(type(s))
                file1.write(name.contents[0] + "\t\t" + s + "\n")



if __name__ == "__main__":

    inn = int(input("press 1 for CookOff problems and 2 for Lunchtime problems\n"))
    if inn == 1:
        TYPE = "COOK"
        x = 92
        y = 118
    else:
        TYPE = "LTIME"
        x = 58
        y = 85
    file1 = open("output1.txt", "w")
    for i in range(x, y + 1):
        file1.write("\n\n"+ TYPE+str(i)+"\n")
        URL = "https://www.codechef.com/" + TYPE+ str(i) +  "A"
        spam(URL)
