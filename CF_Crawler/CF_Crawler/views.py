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
        form = UserHandle(request.POST)

        # check whether it's valid:
        if form.is_valid():
            text = form.cleaned_data['user_handle']
            # process the data in form.cleaned_data as required
            # ...
            http = urllib3.PoolManager()
            u = http.request('GET', 'https://codeforces.com/api/user.info?handles={0}'.format(text))
            userinfo_list = json.loads(u.data.decode('utf-8'))
            userinfo_list = userinfo_list["result"]
            userinfo_list = userinfo_list["0"]
            print(userinfo_list)
            context1 = {'userinfo_list': userinfo_list}
            # return HttpResponseRedirect('/userhandle')
    else:
        form = UserHandle()

    return render(request, 'userinfo.html', context1)
