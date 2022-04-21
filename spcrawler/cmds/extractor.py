import logging

import yaml
import requests
import os.path
import json
import re
from os.path import expanduser
import shutil

from ..spapi.crawler import dump, walk, ping, getfiles


class Project:
    """Sharepoint crawler"""

    def __init__(self):
        pass


    def dump(self, url):
        dump(url)
        pass

    def walk(self, url):
        walk(url)
        pass


    def getfiles(self, url):
        getfiles(url)
        pass

    def ping(self, url):
        ping(url)
        pass


