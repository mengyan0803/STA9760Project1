import os
import sys
import pandas as pd
import numpy as np
from sodapy import Socrata
import requests
from requests import HTTPError
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from time import sleep


DATA_URL = "data.cityofnewyork.us"
DATA_ID = 'nc67-uf89'

app_token = os.environ.get("APP_TOKEN")


client = Socrata(DATA_URL, app_token)
   
client.timeout = 60


def create_and_update_index(index_name):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass
    return es

def data_formatting(datastring):
    for key, value in datastring.items():
        if 'amount' in key:
            datastring[key] = float(value)
        elif 'number' in key:
            datastring[key] = int(value)            
        elif 'date' in key:
            datastring[key] = datetime.strptime(datastring[key], '%m/%d/%Y').date()


def call_ref(datastring, es, index):
    data_formatting(datastring)
    id=datastring['summons_number']
    output = es.index(index=index, body=datastring, id=id)
    print(output['result'], 'Summons_# %s' % id)



def call_results(page_size, num_pages = None, output = None, elastic_search = None) -> dict:

 
    if not num_pages:
        num_pages = results_all // page_size + 1

    if elastic_search:
        es = create_and_update_index('bigdata1')


    try:
        for i in range(num_pages):
            records = client.get(DATA_ID, limit=page_size, offset=i*page_size)
            print(records)

            # output
            if output is not None:
                with open(output, "a") as file:
                    for j in records:
                        file.write(f"{json.dumps(j)}\n")

            # Load the data into elastic search
            if elastic_search:
                call_ref(j, es, 'bigdata1')

    except HTTPError as e:
        print(f"Evaluate the loops again!: {e}")
        raise


import argparse
ap = argparse.ArgumentParser()

if __name__ == "__main__":
    ap.add_argument("--page_size", type=int)
    ap.add_argument("--num_pages", type=int, default=None)
    ap.add_argument("--output", default=None)
    ap.add_argument("--elastic_search", type=bool, default=None)
    args = ap.parse_args()

    call_results(args.page_size, args.num_pages, args.output, args.elastic_search)
