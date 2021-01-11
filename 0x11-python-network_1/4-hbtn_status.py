"""t that fetches https://intranet.hbtn.io/status"""

import urllib.requests

if __name__ == '__main__':
    r = request.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
