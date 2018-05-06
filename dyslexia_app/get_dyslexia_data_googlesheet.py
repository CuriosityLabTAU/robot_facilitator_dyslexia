"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
In this

"""
from __future__ import print_function
#from apiclient.discovery import build #bad
#sudo pip install --upgrade google-api-python-client
from googleapiclient.discovery import build #good
from httplib2 import Http
from oauth2client import file, client, tools
# -*- coding: utf-8 -*-
import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def get_single_task ():
    dyslexia_single = {'word':[],
                       'response':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'single!A2:B'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('word, response:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
            dyslexia_single['word'].append(row[0])
            dyslexia_single['response'].append(row[1])

    print(dyslexia_single)

    # Write JSON file
    with io.open('dyslexia_single.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_single,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('dyslexia_single.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_single == data_loaded)


def get_tefel_task ():
    dyslexia_tefel = {'word':[],
                       'response':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'tefel!A2:B'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('word, response:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
            dyslexia_tefel['word'].append(row[0])
            dyslexia_tefel['response'].append(row[1])

    print(dyslexia_tefel)

    # Write JSON file
    with io.open('dyslexia_tefel.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_tefel,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('dyslexia_tefel.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_tefel == data_loaded)

def get_single_mistakes ():
    dyslexia_single_mistakes = {'mistakes':[],
                       'initials':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'single_mistakes!A1:B'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('mistake, initial:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
            dyslexia_single_mistakes['mistakes'].append(row[0])
            dyslexia_single_mistakes['initials'].append(row[1])

    print(dyslexia_single_mistakes)

    # Write JSON file
    with io.open('dyslexia_single_mistakes.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_single_mistakes,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('dyslexia_single_mistakes.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_single_mistakes == data_loaded)

def get_tefel_mistakes ():
    dyslexia_tefel_mistakes = {'mistakes':[],
                       'initials':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'tefel_mistakes!A1:B'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('mistake, initial:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
            dyslexia_tefel_mistakes['mistakes'].append(row[0])
            dyslexia_tefel_mistakes['initials'].append(row[1])

    print(dyslexia_tefel_mistakes)

    # Write JSON file
    with io.open('dyslexia_tefel_mistakes.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_tefel_mistakes,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('dyslexia_tefel_mistakes.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_tefel_mistakes == data_loaded)

def get_dyslexia_types ():
    dyslexia_types = {'dyslexia_types':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'dyslexia_types!A'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('mistake, initial:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
            dyslexia_types['dyslexia_types'].append(row[0])

    print(dyslexia_types)

    # Write JSON file
    with io.open('dyslexia_types.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_types,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('dyslexia_types.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_types == data_loaded)

get_single_task()
get_tefel_task()
get_single_mistakes()
get_tefel_mistakes()
get_dyslexia_types()