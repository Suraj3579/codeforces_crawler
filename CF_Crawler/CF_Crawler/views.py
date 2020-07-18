from django.shortcuts import render


def main_page(request):
    context = {}
    return render(request, 'index.html', context)

