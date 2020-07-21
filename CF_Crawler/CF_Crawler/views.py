from django.shortcuts import render
import urllib3
import json
from collections import Counter
#from .forms import UserHandle
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
        status=userinfo_list['status']
        if status == 'OK':
            print("user found")
            status = True
            userinfo_list = userinfo_list["result"]
            userinfo_list = userinfo_list[0]
        else:
            print("user not found")
            status = False
            userinfo_list = userinfo_list['comment']
            print("yoyo "+userinfo_list)
        
        tag=[]
        lang=[]
        http = urllib3.PoolManager()
        u = http.request('GET', 'https://codeforces.com/api/user.status?handle='+ form)
        useranalysis = json.loads(u.data.decode('utf-8'))
        useranalysis = useranalysis["result"]
        for item in useranalysis:
            tag.extend(item['problem']['tags'])

        tagcount=Counter(tag)

        for item in useranalysis:
            lang.append(item['programmingLanguage'])    

        langcount=Counter(lang)
        
        context1 = {'userinfo_list': userinfo_list, 'status': status,'tagcount':tagcount,'langcount':langcount}
        # return HttpResponseRedirect('/userhandle')
    else:
        form = UserHandle()
    return render(request, 'userinfo.html', context1)
