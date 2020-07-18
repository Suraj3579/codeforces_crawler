from django.shortcuts import render


def main_page(request):
    context = {}
    return render(request, 'index.html', context)


def code_calender(request):
    context = {}
    return render(request, 'calender.html', context)
