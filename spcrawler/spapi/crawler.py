# -*- coding: utf-8 -*-
import json
import os
import requests
import urllib3
import logging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib.parse import urlparse

DEFAULT_HEADERS = {'Accept' : 'application/json; odata=verbose'}
DEFAULT_TIMEOUT = 180
CLOSED_KEYS = ['FirstUniqueAncestorSecurableObject', ]


def sprequest_full(fullurl):
    logging.info('Request %s' % (fullurl))
    resp = requests.get(fullurl, headers=DEFAULT_HEADERS, verify=False, timeout=DEFAULT_TIMEOUT)
    return json.loads(resp.text)

def sprequest(url, postfix='/_api/web'):
    logging.info('Request %s' % (url + postfix))
    resp = requests.get(url + postfix, headers=DEFAULT_HEADERS, verify=False, timeout=DEFAULT_TIMEOUT)
    return json.loads(resp.text)

def get_list(url, name):
    data = sprequest(url, postfix='/_api/web/' + name)
    if 'error' in data.keys() or 'd' not in data.keys():
        return None
    if 'results' not in data['d'].keys():
        return [data['d'],]
    objects = data['d']['results']
    return objects





def get_web(url):
    data = sprequest(url, postfix='/_api/web')
    return data

def walk(url: str):
    data = get_web(url)
    for key in data['d'].keys():
        if key != '__metadata' and isinstance(data['d'][key], dict) and '__deferred' in data['d'][key].keys():
            print(f"%s: %s" % (key, data['d'][key]['__deferred']['uri']))
    pass

def getfiles(url):
    pass

def ping(url):
    try:
        data = get_web(url)
        if 'd' in data.keys() and '__metadata' in data['d'].keys():
            print('Endpoint %s is OK' % (url))
        else:
            print('Endpoint %s JSON but no metadata available' % (url))
    except:
        print('Endpoint %s is invalid' % (url))


def dump(url: str, deep:bool = True):
    domain = urlparse(url).netloc
    datapath = os.path.join(domain, 'data')
    os.makedirs(datapath, exist_ok=True)
    data = get_web(url)
    for key in data['d'].keys():
        if os.path.exists(os.path.join(datapath, '%s.jsonl') % (key)):
            logging.info(f'%s already processed' %(key))
            continue
        if key != '__metadata' and isinstance(data['d'][key], dict) and '__deferred' in data['d'][key].keys():
            list_data = get_list(url, key)
            f = open(os.path.join(datapath, '%s.jsonl') % (key), 'w', encoding='utf8')
            if list_data is not None:
                for r in list_data:
                    f.write(json.dumps(r, ensure_ascii=False) + '\n')
                logging.info(f"%s dumped" % (key))
            else:
                logging.info(f"%s error. No access" % (key))
            f.close()
        pass
    if deep:
        for key in data['d'].keys():
            if key in CLOSED_KEYS:
                continue
            if os.path.exists(os.path.join(datapath, "%s.jsonl" % (key))):
                os.makedirs(os.path.join(datapath, key), exist_ok=True)
                f = open(os.path.join(datapath, '%s.jsonl') % (key), 'r', encoding='utf8')
                for l in f:
                    record = json.loads(l)
                    idk = None
                    if 'StringId' in record.keys():
                        idk = 'StringId'
                    elif 'Id' in record.keys():
                        idk = 'Id'
                    if idk is not None:
                        os.makedirs(os.path.join(datapath, key, str(record[idk])), exist_ok=True)
                        for lkey in record.keys():
                            if lkey != '__metadata' and isinstance(record[lkey], dict) and '__deferred' in record[lkey].keys():
                                fullkey = key + '/' + lkey
                                subfilename = os.path.join(datapath, key, record[idk], '%s.jsonl' % lkey)
                                if os.path.exists(subfilename):
                                    logging.info(f"%s already saved" % (fullkey))
                                    continue
                                list_data = sprequest_full(record[lkey]['__deferred']['uri'])
                                if list_data is not None:
                                    if 'error' in list_data.keys() or 'd' not in list_data.keys():
                                        fw = open(subfilename, 'w', encoding='utf8')
                                        fw.close()
                                        continue
                                    if 'results' not in list_data['d'].keys():
                                        objects = [list_data['d'], ]
                                    else:
                                        objects = list_data['d']['results']
                                    fw = open(subfilename, 'w', encoding='utf8')
                                    for r in objects:
                                        fw.write(json.dumps(r, ensure_ascii=False) + '\n')
                                    fw.close()
                                    logging.info(f"%s dumped" % (fullkey))
                                else:
                                    logging.info(f"%s error. No access" % (fullkey))
                f.close()




