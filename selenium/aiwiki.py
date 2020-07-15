from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")

soup = BeautifulSoup(page, 'html.parser')

regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', attrs={'class': regex})


content = []
for li in content_lis:
    content.append(li.getText().split('\n')[0])
print(content)
see_also_section = soup.find('div', attrs={'class': 'div-col columns column-width'})
see_also_soup =  see_also_section.find_all('li')

see_also = []
for li in see_also_soup:
    a_tag = li.find('a', href=True, attrs={'title':True, 'class':False}) # find a tags that have a title and a class
    href = a_tag['href'] # get the href attribute
    text = a_tag.getText() # get the text
    see_also.append([href, text]) # append to array
print(see_also)

with open('content.txt', 'w') as f:
    for i in content:
        f.write(i+"\n")
f.close()

with open('see_also.csv', 'w') as f:
    for i in see_also:
        f.write(",".join(i)+"\n")
f.close()
