from django.shortcuts import render


def compare(request):
    context ={}
    return render(request, 'compare.html', context)
