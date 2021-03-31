#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
from argparse import ArgumentParser
from urllib.parse import urlparse, urljoin
from tqdm import tqdm
from rich import print


def do_i_run_it(url):
    valid = {"yes": True, "y": True, "ye": True,
             "": True, "no": False, "n": False}

    print('An example url looks like this: {}'.format(url))
    while True:

        print('Do I run it [Y/n] ')
        choice = input().lower()
        if choice in valid:
            return valid[choice]
        else:
            print('Please respond with y or n.\n')


backup_list = ['.backup', '.bck', '.save', '.bak', '.sav', '~', '.copy', '.old', '.orig',
               '.tmp', '.txt', '.back', '.bkp', '.bac', '.tar', '.gz', '.tar.gz', '.zip', '.rar']

parser = ArgumentParser()
parser.add_argument('url', type=str, help='URL to use')
args = parser.parse_args()

url = args.url
dictionary = {}
duplicates_links = []
parsed_url = urlparse(url)

if parsed_url.scheme != '' and parsed_url.netloc != '' and parsed_url.path != '':
    if do_i_run_it(url+backup_list[0]):
        print('Number of backup files to test: {}'.format(len(backup_list)))
        for item in tqdm(backup_list):
            link = url + item
            page = requests.get(link)
            if link not in dictionary.keys():
                dictionary[link] = page.status_code
            else:
                duplicates_links.append(link)
    else:
        print('Stopping process')
        exit(1)
else:
    print('URL is not valid. Compulsory: Scheme, Network Location, Path.')
    print('While you have {}'.format(parsed_url))
    exit(1)

at_least_one = False
for key, value in dictionary.items():
    if value != 404:
        print('link {} --> {}'.format(key, value))
        at_least_one = True

if not at_least_one:
    print('No backup files found with this URL')

if len(duplicates_links) > 0:
    print('Here are the duplicated links: {}'.format(duplicates_links))
