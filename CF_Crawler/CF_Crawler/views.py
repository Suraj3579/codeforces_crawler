from django.shortcuts import render
import urllib3
import json
from .forms import UserHandle
from django.http import HttpResponseRedirect


def main_page(request):
    context = {}
    return render(request, 'index.html', context)


def user_handle(request):
    # if this is a POST request we need to process the form data
    context1 = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST['input_handle']

        http = urllib3.PoolManager()
        u = http.request('GET', ('https://codeforces.com/api/user.info?handles='+form))
        userinfo_list = json.loads(u.data.decode('utf-8'))
        userinfo_list = userinfo_list["result"]
        userinfo_list = userinfo_list[0]
        print(userinfo_list)
        context1 = {'userinfo_list': userinfo_list}
        # return HttpResponseRedirect('/userhandle')
    else:
        print("not found")
        form = UserHandle()
    return render(request, 'userinfo.html', context1)
