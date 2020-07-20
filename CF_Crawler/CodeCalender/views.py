from django.shortcuts import render
import urllib3
import json




# Create your views here.


def code_calender(request):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://codeforces.com/api/contest.list?gym=false')
    # print(r.status)
    contest_list = json.loads(r.data.decode('utf-8'))
    contest_list = contest_list["result"]
    contest_list = contest_list[:10]
    string = "BEFORE"
    link_contest = "https://codeforces.com/contests/"
    #function for sorting according to start time
    def fun(e):
        return e['startTimeSeconds']
    contest_list.sort(key=fun)
    # for cont in contest_list:
    #     print(cont)
    context = {'contest_list': contest_list,'string':string,'link_contest':link_contest }
    return render(request, 'calender.html', context)

 