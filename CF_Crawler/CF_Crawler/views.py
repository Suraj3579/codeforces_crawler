from django.shortcuts import render
import urllib3
import json
from collections import Counter
from datetime import datetime
# from .forms import UserHandle
from django.http import HttpResponseRedirect


def main_page(request):
    context = {}
    return render(request, 'home.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def user_handle(request):
    # if this is a POST request we need to process the form data
    context1 = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST['input_handle']

        http = urllib3.PoolManager()
        u = http.request('GET', ('https://codeforces.com/api/user.info?handles=' + form))
        userinfo_list = json.loads(u.data.decode('utf-8'))
        status = userinfo_list['status']
        if status != 'OK':
            print("user not found")
            status = False
            userinfo_list = userinfo_list['comment']
            print("yoyo " + userinfo_list)
        else:
            print("user found")
            status = True
            userinfo_list = userinfo_list["result"]
            userinfo_list = userinfo_list[0]
            
            #---------code for anylasis page
            tag = []
            lang = []
            ABC_tag = []
            problem_rating = []
            verdicts = []
            contestids = []
            quests = []
            okquests = []
            nqos = 0  # no of successful questions in one submission
            http = urllib3.PoolManager()
            u = http.request('GET', 'https://codeforces.com/api/user.status?handle=' + form)
            user_analysis = json.loads(u.data.decode('utf-8'))
            user_analysis = user_analysis["result"]
            temp = set()
            for x in user_analysis:
                if x['id'] not in temp and x['verdict'] == 'OK':
                    temp.add(x['id'])
                    tag.extend(x['problem']['tags'])
                    lang.append(x['programmingLanguage'])
                    ABC_tag.append(x['problem']['index'][0])
                    # print(x['problem']['name'])
                    problem_rating.append(x['problem']['rating'])

            problem_rating = sorted(problem_rating)
            ABC_tag = sorted(ABC_tag)
            tagcount = Counter(tag)
            langcount = Counter(lang)
            ABC_tagcount = Counter(ABC_tag)
            problem_ratingcount = Counter(problem_rating)

            for item in user_analysis:
                verdicts.append(item["verdict"])
            for item in user_analysis:
                if (item["author"]["participantType"] == 'CONTESTANT'):
                    contestids.append(item["contestId"])
            for item in user_analysis:
                quests.append(item["problem"]["name"])
            for item in user_analysis:
                if (item["verdict"] == "OK"):
                    okquests.append(item["problem"]["name"])

            #---calendar section----------
            ok_submissions = []
            count=0
            for item in user_analysis:
                if item['verdict']=='OK':
                    ok_submissions.append(item['creationTimeSeconds'])
            dates=[]
            for item in ok_submissions:
                timestamp = datetime.fromtimestamp(item)
                dates.append(timestamp.strftime('%Y-%m-%d'))
            datecount=Counter(dates)
            datefreq=[]
            for date in datecount:
                list=[]
                list.append(date)
                list.append(datecount[date])
                datefreq.append(list)
            print(datefreq)
            #----end---------# 
            verdict_count = Counter(verdicts)
            contest_count = Counter(contestids)
            ques_count = Counter(quests)
            okques_count = Counter(okquests)
            for key in okques_count:
                if (okques_count[key] == 1):
                    nqos += 1
            noc = len(contest_count)  # no of contests participated
            ts = (len(user_analysis))  # total submissions
            ss = (verdict_count['OK'])  # successful submissions
            msqn = max(ques_count.keys(), key=(lambda k: ques_count[k]))  # name of the question with maximum submissions
            msqc = ques_count[msqn]  # max submissions per question
            data_dict = {'msqn': msqn, 'msqc': msqc, 'nqos': nqos, 'ts': ts, 'ss': ss, 'noc': noc}

            rating = []
            rtime = []
            rank = []
            http = urllib3.PoolManager()
            u = http.request('GET', 'https://codeforces.com/api/user.rating?handle=' + form)
            useranalysis3 = json.loads(u.data.decode('utf-8'))
            useranalysis3 = useranalysis3["result"]
            for item in useranalysis3:
                rating.append(item['newRating'])

            for item in useranalysis3:
                rtime.append(item['ratingUpdateTimeSeconds'])
            dtime = []
            for i in rtime:
                dtime.append(datetime.fromtimestamp(i).strftime("%d %b'%y"))
            
            print(dtime)
            context1 = {'userinfo_list': userinfo_list, 'status': status,
                        'tagcount': tagcount, 'langcount': langcount, 'ABC_tagcount': ABC_tagcount,
                        'problem_ratingcount': problem_ratingcount,
                        'dtime': dtime, 'rating': rating, 'verdict_count': verdict_count, 'data_dict': data_dict,
                        'datecount':datecount ,'ok_count': len( ok_submissions)}
            # return HttpResponseRedirect('/userhandle')
    else:
        form = UserHandle()
    return render(request, 'userinfo.html', context1)
