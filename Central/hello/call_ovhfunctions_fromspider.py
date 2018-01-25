# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 06:28:14 2018

@author: Cyril
"""

#   curl -XPOST -s 'https://exec.functions.ovh/f/gxiaaacfkvbc4/hellopy?token=MVqONcvD55pUItKcp9Fz'

#https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
import requests
#res = requests.get('https://exec.functions.ovh/f/gxiaaacfkvbc4/hellopy?token=MVqONcvD55pUItKcp9Fz')
res = requests.get('https://exec.functions.ovh/f/gxiaaacfkvbc4/hellopy?token=MVqONcvD55pUItKcp9Fz')


print(res.text)


#https://docs.ovh.com/gb/en/functions/global-doc-ovh-functions/#python-dependencies
#https://pkgs.alpinelinux.org/package/edge/testing/armhf/opencv
