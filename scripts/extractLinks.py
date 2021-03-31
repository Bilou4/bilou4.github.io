#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
from argparse import ArgumentParser
from urllib.parse import urlparse, urljoin
from tqdm import tqdm
from rich import print


def get_links(url, dictionary):
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')

    for tag in soup.find_all('a'):
        link = urljoin(url, tag.get('href'))
        link = link if link[len(link)-1] != '/' else link[:-1]
        if link not in dictionary.keys():
            dictionary[link] = 1
        else:
            dictionary[link] += 1


parser = ArgumentParser()
parser.add_argument('url', type=str, help='URL to use')
parser.add_argument('--recursive', nargs='?', type=int, const=5,
                    help='Follow found links with a specified maxDepth (default: 5)')

args = parser.parse_args()
url = args.url
res = {}

parsed_url = urlparse(url)
if parsed_url.scheme != '' and parsed_url.netloc != '':
    get_links(url, res)
else:
    print('URL is not valid, try again')
    exit(1)

if args.recursive is not None:
    max_depth = args.recursive
    print('Recursive arg is set to {}, proceeding.\n'.format(max_depth))
    total = {}
    for i in tqdm(range(max_depth)):
        tmp = {}
        for link in res.keys():
            parsed_url = urlparse(link)
            if parsed_url.scheme != '' and parsed_url.netloc != '':
                get_links(link, tmp)
            else:
                print('Invalid URL: {}'.format(parsed_url))
        total.update(tmp)
    res.update(total)
else:
    print('Recursive arg is not set, proceeding.\n')

print(res)
print('\nTotal number of links found : {}'.format(sum(res.values())))

if res:  # dict is not empty
    most_present = max(res, key=res.get)
    print(
        'Most present link: {} --> {}'.format(most_present, res[most_present]))
