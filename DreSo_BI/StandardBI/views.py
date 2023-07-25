from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

@login_required(login_url='login')
def StandardBI(request):
    """
    Diese Ansicht rendert die 'BI_Scrollpage.html' Vorlage.
    Nur authentifizierte Benutzer können auf diese Ansicht zugreifen.
    """
    return render(request, 'BI_Scrollpage.html')


class CustomLoginView(LoginView):
    """
    Diese Klasse ist eine benutzerdefinierte Login-Ansicht, die die 'login.html' Vorlage rendert.
    """
    template_name = 'login.html'


