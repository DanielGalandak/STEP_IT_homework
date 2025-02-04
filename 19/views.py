from django.shortcuts import render

def matches(a, b):
    return a == b

def signup_form(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            password_repeat = request.POST['password_repeat']
        except KeyError:
            return render(request, 'signup/signup_failed.html', {"error": "Vyplňte všechna pole!"})

        if not matches(password, password_repeat):
            return render(request, 'signup/signup_failed.html', {"error": "Hesla se neshodují!"})

        return render(request, 'signup/signup_success.html', {"email": email})

    return render(request, 'signup/form.html')

