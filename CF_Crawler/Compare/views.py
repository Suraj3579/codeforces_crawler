from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import Counter
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
import requests


@login_required(login_url='loginpage')
def compare(request):
    context = {}
    return render(request, 'compare.html', context)


@login_required(login_url='loginpage')
def compare_analysis(request):
    # if this is a POST request we need to process the form data
    context1 = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST['input_handle1']
        form1 = request.POST['input_handle2']

        u = requests.get(('https://codeforces.com/api/user.info?handles=' + form))
        userinfo_list = u.json()
        status = userinfo_list['status']
        u1 = requests.get(('https://codeforces.com/api/user.info?handles=' + form1))
        userinfo_list1 = u1.json()
        status1 = userinfo_list1['status']        
        if (status == 'FAILED' or status1 == 'FAILED'):
            status = False
            userinfo_list = userinfo_list['comment']
            status1 = False
            userinfo_list1 = userinfo_list1['comment']
            #print("yoyo " + userinfo_list1)

        else:
            # print("user found")
            status = True
            userinfo_list = userinfo_list["result"]
            userinfo_list = userinfo_list[0]

            status1 = True
            userinfo_list1 = userinfo_list1["result"]
            userinfo_list1 = userinfo_list1[0]

            # ---------code for anylasis page
            tag = []
            lang = []
            ABC_tag = []
            problem_rating = []
            verdicts = []
            contestids = []
            quests = []
            okquests = []
            nqos = 0  # no of successful questions in one submission

            u = requests.get('https://codeforces.com/api/user.status?handle=' + form)
            user_analysis = u.json()
            user_analysis = user_analysis["result"]
            temp = set()
            for x in user_analysis:
                if x['id'] not in temp and x['verdict'] == 'OK' and 'rating' in x['problem']:
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

            # ---calendar section----------
            ok_submissions = []
            count = 0
            for item in user_analysis:
                if item['verdict'] == 'OK':
                    ok_submissions.append(item['creationTimeSeconds'])
            dates = []
            for item in ok_submissions:
                timestamp = datetime.fromtimestamp(item)
                dates.append(timestamp.strftime('%Y-%m-%d'))
            datecount = Counter(dates)
            datefreq = []
            for date in datecount:
                list = []
                list.append(date)
                list.append(datecount[date])
                datefreq.append(list)
            # print(datefreq)
            # ----end---------#

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
            msqn = max(ques_count.keys(),
                       key=(lambda k: ques_count[k]))  # name of the question with maximum submissions
            msqc = ques_count[msqn]  # max submissions per question
            data_dict = {'msqn': msqn, 'msqc': msqc, 'nqos': nqos, 'ts': ts, 'ss': ss, 'noc': noc}

            rating = []
            rtime = []
            rank = []

            u = requests.get('https://codeforces.com/api/user.rating?handle=' + form)
            useranalysis3 = u.json()
            useranalysis3 = useranalysis3["result"]
            for item in useranalysis3:
                rating.append(item['newRating'])

            for item in useranalysis3:
                rtime.append(item['ratingUpdateTimeSeconds'])
            dtime = []
            for i in rtime:
                dtime.append(i*1000)

            nlist=[]
            for i in range(len(dtime)):
                templist=[]
                templist.append(dtime[i])
                templist.append(rating[i])
                nlist.append(templist)

            #print(nlist)


            # ---------code for anylasis page
            tag1 = []
            lang1 = []
            ABC_tag1 = []
            problem_rating1 = []
            verdicts1 = []
            contestids1= []
            quests1 = []
            okquests1 = []
            nqos1 = 0  # no of successful questions in one submission

            u1 = requests.get('https://codeforces.com/api/user.status?handle=' + form1)
            user_analysis1 = u1.json()
            user_analysis1 = user_analysis1["result"]
            temp1 = set()
            for x in user_analysis1:
                if x['id'] not in temp1 and x['verdict'] == 'OK' and 'rating' in x['problem']:
                    temp1.add(x['id'])
                    tag1.extend(x['problem']['tags'])
                    lang1.append(x['programmingLanguage'])
                    ABC_tag1.append(x['problem']['index'][0])
                    # print(x['problem']['name'])
                    problem_rating1.append(x['problem']['rating'])

            problem_rating1 = sorted(problem_rating1)
            ABC_tag1 = sorted(ABC_tag1)
            tagcount1 = Counter(tag1)
            langcount1 = Counter(lang1)
            ABC_tagcount1 = Counter(ABC_tag1)
            problem_ratingcount1 = Counter(problem_rating1)

            for item in user_analysis1:
                verdicts1.append(item["verdict"])
            for item in user_analysis1:
                if (item["author"]["participantType"] == 'CONTESTANT'):
                    contestids1.append(item["contestId"])
            for item in user_analysis1:
                quests1.append(item["problem"]["name"])
            for item in user_analysis1:
                if (item["verdict"] == "OK"):
                    okquests1.append(item["problem"]["name"])

            # ---calendar section----------
            ok_submissions1 = []
            count1 = 0
            for item in user_analysis1:
                if item['verdict'] == 'OK':
                    ok_submissions1.append(item['creationTimeSeconds'])
            dates1 = []
            for item in ok_submissions1:
                timestamp = datetime.fromtimestamp(item)
                dates1.append(timestamp.strftime('%Y-%m-%d'))
            datecount1 = Counter(dates)
            datefreq1 = []
            for date in datecount1:
                list1 = []
                list1.append(date)
                list1.append(datecount1[date])
                datefreq1.append(list1)
            # print(datefreq)
            # ----end---------#

            verdict_count1 = Counter(verdicts1)
            contest_count1 = Counter(contestids1)
            ques_count1 = Counter(quests1)
            okques_count1 = Counter(okquests1)
            for key in okques_count1:
                if (okques_count1[key] == 1):
                    nqos1 += 1
            noc1 = len(contest_count1)  # no of contests participated
            ts1 = (len(user_analysis1))  # total submissions
            ss1 = (verdict_count1['OK'])  # successful submissions
            msqn1 = max(ques_count1.keys(),
                       key=(lambda k: ques_count1[k]))  # name of the question with maximum submissions
            msqc1 = ques_count1[msqn1]  # max submissions per question
            data_dict1 = {'msqn1': msqn1, 'msqc1': msqc1, 'nqos1': nqos1, 'ts1': ts1, 'ss1': ss1, 'noc1': noc1}

            rating1 = []
            rtime1 = []
            rank1 = []

            u1 = requests.get('https://codeforces.com/api/user.rating?handle=' + form1)
            useranalysis1 = u1.json()
            useranalysis1 = useranalysis1["result"]
            for item in useranalysis1:
                rating1.append(item['newRating'])

            for item in useranalysis1:
                rtime1.append(item['ratingUpdateTimeSeconds'])
            dtime1 = []
            for i in rtime1:
                dtime1.append(i*1000)

            nlist1=[]
            for i in range(len(dtime1)):
                templist1=[]
                templist1.append(dtime1[i])
                templist1.append(rating1[i])
                nlist1.append(templist1)

            #print(nlist)
            context1 = {'userinfo_list1': userinfo_list1, 'status1': status1,
                        'tagcount1': tagcount1, 'langcount1': langcount1, 'ABC_tagcount1': ABC_tagcount1,
                        'problem_ratingcount1': problem_ratingcount1,
                        'dtime1': dtime1, 'rating1': rating1, 'verdict_count1': verdict_count1, 'data_dict1': data_dict1,
                        'userinfo_list': userinfo_list, 'status': status,
                        'tagcount': tagcount, 'langcount': langcount, 'ABC_tagcount': ABC_tagcount,
                        'problem_ratingcount': problem_ratingcount,
                        'dtime': dtime, 'rating': rating, 'verdict_count': verdict_count, 'data_dict': data_dict,'datecount': datecount, 'ok_count': len(ok_submissions), 'datecount1': datecount1, 'ok_count1': len(ok_submissions1), 'nlist':nlist, 'nlist1':nlist1
                        }
            # return HttpResponseRedirect('/userhandle')
    else:
        form = UserHandle()
    return render(request, 'compare_analysis.html', context1)


