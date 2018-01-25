# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 18:17:02 2017

@author: Cyril
"""


import requests
res = requests.get('https://stackoverflow.com/questions/26000336')

url     = 'http://192.168.1.19/virb'
payload = {'command' : 'status'}#payload = { 'key' : 'val' }
headers = {}
res = requests.post(url, data=payload, headers=headers)


#{"command":"livePreview","streamType": <stream_type> }
payload = {'command' : 'livePreview', 'streamType' : 'rtp' }#payload = { 'key' : 'val' }
headers = {}
res = requests.post(url, data=payload, headers=headers)
print(res.url)



#{"command":"status"}
payload = {'command' : 'status'}#payload = { 'key' : 'val' }
headers = {}
res = requests.post(url, data=payload, headers=headers)
print(res)
from pprint import pprint


