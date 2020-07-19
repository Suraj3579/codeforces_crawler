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
    contest_list = contest_list[:100]
    # for cont in contest_list:
    #     print(cont)
    context = {'contest_list': contest_list}
    return render(request, 'calender.html', context)

