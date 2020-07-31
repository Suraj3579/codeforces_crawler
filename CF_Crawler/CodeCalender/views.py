from django.shortcuts import render
import urllib3
import json
####
from bs4 import BeautifulSoup
import requests


def code_calender(request):
    # http = urllib3.PoolManager()
    r = requests.get('https://codeforces.com/api/contest.list?gym=false')

    # print(r.status)
    contest_list = r.json()
    contest_list = contest_list["result"]
    contest_list = contest_list[:10]
    string = "BEFORE"
    link_contest = "https://codeforces.com/contests/"

    # function for sorting according to start time
    def fun(e):
        return e['startTimeSeconds']

    contest_list.sort(key=fun)
    # for cont in contest_list:
    #     print(cont)

    soup = requests.get(
        'https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests#future-contests')
    soup = BeautifulSoup(soup.content, 'html')
    soup = soup.find(id='future-contests')
    soup = soup.next_sibling.next_sibling
    soup = soup.find_all('td')
    result = []
    links = []
    for tag in soup:
        # print (tag.text)
        result.extend(tag.stripped_strings)
        link = tag.find('a')
        if link is not None:
            link = link.get('href')
            links.append(link)
    chef_contest_list = []
    count = len(links)
    # print (count)
    for i in range(count):
        lis = [links[0]]
        links.pop(0)
        result.pop(0)
        for j in range(3):
            lis.append(result[0])
            result.pop(0)
        result.pop(0), result.pop(0)
        chef_contest_list.append(lis)

    # print(chef_contest_list)
    chef_link = "https://www.codechef.com"
    context = {'contest_list': contest_list, 'string': string, 'link_contest': link_contest,
               'chef_contest_list': chef_contest_list,
               'chef_link': chef_link}
    return render(request, 'calender.html', context)
