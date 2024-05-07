import sys
import os
import http.cookiejar
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


class HTTPManager:
    def __init__(self):
        self.cookie_filename = 'cookies.txt'
        self.cookie_jar = http.cookiejar.MozillaCookieJar(self.cookie_filename)
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPRedirectHandler(),
            urllib.request.HTTPHandler(debuglevel=0),
            urllib.request.HTTPSHandler(debuglevel=0),
            urllib.request.HTTPCookieProcessor(self.cookie_jar)
        )

    def load_page(self, url, data=None):
        try:
            if data is not None:
                response = self.opener.open(url, data)
            else:
                response = self.opener.open(url)
            return ''.join([line.decode('utf-8') for line in response.readlines()])
        except Exception as err:
            print('[Notice] Exception hit')
            print(err)
            sys.exit(0)

    def login(self, token):
        html = self.load_page('https://www.linkedin.com/checkpoint/lg/login')
        soup = BeautifulSoup(html, 'html.parser')

        csrf = soup.find('input', {'name': 'csrfToken'}).get('value')
        login_csrf_param = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

        login_data = urllib.parse.urlencode({
            'csrfToken': csrf,
            'loginCsrfParam': login_csrf_param
        }).encode('utf-8')

        self.load_page('https://www.linkedin.com/checkpoint/lg/login-submit', login_data)

        try:
            cookie = token
            jsessionid = ''
            for ck in self.cookie_jar:
                if ck.name == 'JSESSIONID':
                    jsessionid = ck.value
        except Exception as err:
            print(err)
            sys.exit(0)

        self.cookie_jar.save()
        os.remove(self.cookie_filename)

        return cookie, csrf

    def authenticate(self, token):
        try:
            session, csrf = self.login(token)
            if not session:
                sys.exit('[!] Unable to login to LinkedIn.com')
            print('[*] Obtained new session: %s' % session)
            sessions = dict(li_at=session, JSESSIONID=csrf)
        except Exception as e:
            sys.exit('[!] Could not authenticate to LinkedIn. %s' % e)
        return sessions
