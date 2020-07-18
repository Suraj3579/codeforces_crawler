from django.shortcuts import render


# Create your views here.


def code_calender(request):
    # contest_list =
    # context = {'contest_list': contest_list}
    context = {}
    return render(request, 'calender.html', context)
