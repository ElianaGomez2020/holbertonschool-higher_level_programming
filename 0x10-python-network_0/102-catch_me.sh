#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
