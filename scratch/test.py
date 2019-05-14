from bs4 import BeautifulSoup as bs

f = open("개인과제data.txt",'r',encoding = 'UTF-8')
f = f.read()
# print(f)
soup = bs(f, "lxml")
# print(soup)
# all_divs = soup.find_all("ax2102:astrtCont")
# print(all_divs)
