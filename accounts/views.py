from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils.http import urlencode
from .models import User
from .helper import get_token, get_profile
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
    auth_uri = settings.OAUTH['AUTHORIZE_URI']
    client_id = settings.OAUTH['CLIENT_ID']

    get = {
        'response_type': 'code',
        'client_id': client_id,
    }

    auth_url = auth_uri + '?' + urlencode(get)

    return render(request, 'login.html', {
        'auth_url': auth_url,
        })


def passport(request):
    try:
        code = request.GET['code']
    except:
        return HttpResponse('invalid code')
    
    data = get_token(code=code)

    if data.has_key('error'):
        return HttpResponse(data)

    profile =  get_profile(data['access_token'])

    user = User.objects.filter(username=profile['username'])
    if user:
        user = user[0]
    else:
        user = User.objects.create_user(
            username = profile['username'],
            access_token = data['access_token'],
            refresh_token = data['refresh_token'],
            )
    user = auth.authenticate(username=profile['username'], password='innlym')
    auth.login(request, user)

    return render(request, 'profile.html', {'profile': profile})


@login_required
def profile(request):
    user = request.user
    profile =  get_profile(str(user.access_token))
    if not profile:
        data = get_token(refresh_token=str(user.refresh_token))
        user.access_token = data['access_token']
        user.refresh_token = data['refresh_token']
        user.save()
        profile = get_profile(data['access_token'])

    return render(request, 'profile.html', {'profile': profile})

    

