#!/usr/bin/env python

import requests
import sys

LOOKUP_URL = 'https://openlibrary.org/api/books'

def init():
    print('''
 _____  _    __  __ ___   _     _ _                          
|_   _|/ \  |  \/  |_ _| | |   (_) |__  _ __ __ _ _ __ _   _ 
  | | / _ \ | |\/| || |  | |   | | '_ \| '__/ _` | '__| | | |
  | |/ ___ \| |  | || |  | |___| | |_) | | | (_| | |  | |_| |
  |_/_/   \_\_|  |_|___| |_____|_|_.__/|_|  \__,_|_|   \__, |
                                                       |___/ 
 ____                          _      
| __ )  __ _ _ __ ___ ___   __| | ___ 
|  _ \ / _` | '__/ __/ _ \ / _` |/ _ \\
| |_) | (_| | | | (_| (_) | (_| |  __/
|____/ \__,_|_|  \___\___/ \__,_|\___|
                                      
 ____                                         
|  _ \ _ __ ___   ___ ___  ___ ___  ___  _ __ 
| |_) | '__/ _ \ / __/ _ \/ __/ __|/ _ \| '__|
|  __/| | | (_) | (_|  __/\__ \__ \ (_) | |   
|_|   |_|  \___/ \___\___||___/___/\___/|_|   
    ''')

    if len(sys.argv) < 2:
        print('Usage: python process.py <barcode_scan.log>\n')
        exit()

def process():
    with open('barcode_scan.log', 'r') as f:
        for line in f.readlines()[:5]:
            isbn = line.strip()
            res = requests.get(LOOKUP_URL, params={
                'bibkeys': 'ISBN:{}'.format(isbn),
                'format': 'json'
            })
            print(res.json())

if __name__ == '__main__':
    init()
    process()
