#!/usr/bin/python3
"""that takes in a URL, sends a request to the URL
and displays the body"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
