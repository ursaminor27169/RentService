from django.shortcuts import render


def main(request):
    context = {}
    return render(request, 'rcb/main.html', context)