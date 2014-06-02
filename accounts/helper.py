import pycurl, cStringIO
import simplejson as json
from django.utils.http import urlencode
from django.conf import settings

def  get_token(code=None, refresh_token=None):
    post_data = {
        'client_id': settings.OAUTH['CLIENT_ID'],
        'client_secret': settings.OAUTH['CLIENT_SECRET'],
    }
    if code:
        post_data.update({
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.OAUTH['REDIRECT_URI'],
        })
    else:
        post_data.update({
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        })
    c = pycurl.Curl()
    buf = cStringIO.StringIO()
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.setopt(c.POST, 1)
    c.setopt(c.POSTFIELDS, urlencode(post_data))
    c.setopt(c.URL, settings.OAUTH['TOKEN_URI'])
    c.perform()
    if json.loads(buf.getvalue()).has_key('error'):
        raise
    return json.loads(buf.getvalue())

def get_profile(token):
    c = pycurl.Curl()
    buf = cStringIO.StringIO()
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.setopt(c.URL, settings.OAUTH['API_URI'])
    c.setopt(c.HTTPHEADER, ['Authorization: Bearer ' + token])
    c.perform()
    return buf.getvalue() and json.loads(buf.getvalue())
