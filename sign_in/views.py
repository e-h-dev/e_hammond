from django.shortcuts import render


def sign_in(request):
    return render(request, 'sign_in/sign_in.html')


def sign_up(request):
    return render(request, 'sign_in/sign_up.html')


def sign_out(request):
    return render(request, 'sign_in/sign_out.html')
