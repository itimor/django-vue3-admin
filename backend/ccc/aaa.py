# -*- coding: utf-8 -*-
# author: itimor

import json
import re
import requests


def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        pass


url = "https://ip.useragentinfo.com/jsonp"
payload = {"ip": "18.163.183.134"}
res = requests.get(url, params=payload)
print(res.text)
print(loads_jsonp(res.text))
