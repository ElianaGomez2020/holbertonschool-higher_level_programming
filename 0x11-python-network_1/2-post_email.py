#!/usr/bin/python3
"""takes in a URL and an email, sends
    a POST request to the passed URL"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}
    dat = urllib.parse.urlencode(value)
    dat = dat.encode('ascii')
    obj_req = urllib.request.Request(url, dat)
    with urllib.request.urlopen(obj_req) as file_req:
        content = file_req.read()
        print(content.decode('utf-8'))
