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
                       'response':[],
                       'answer1':[],
                       'answer2':[],
                       'm_0':[],
                       'm_1':[],
                       'm_2':[],
                       'm_3':[],
                       'm_4':[],
                       'm_5':[],
                       'm_6':[],
                       'm_7':[],
                       'm_8':[],
                       'm_9':[],
                       'm_10':[],
                       'm_11':[],
                       'm_12':[],
                       'm_13':[],
                       'm_14':[],
                       'm_15':[],
                       'm_16':[],
                       'm_17':[],
                       'm_other':[],
                       'm_none':[],
                       'm_correct': []
                       }

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('googlesheet_jsons/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('googlesheet_jsons/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'single1!B3:Z'
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
            dyslexia_single['answer1'].append(row[2])
            dyslexia_single['answer2'].append(row[3])
            dyslexia_single['m_0'].append(row[4])
            dyslexia_single['m_1'].append(row[5])
            dyslexia_single['m_2'].append(row[6])
            dyslexia_single['m_3'].append(row[7])
            dyslexia_single['m_4'].append(row[8])
            dyslexia_single['m_5'].append(row[9])
            dyslexia_single['m_6'].append(row[10])
            dyslexia_single['m_7'].append(row[11])
            dyslexia_single['m_8'].append(row[12])
            dyslexia_single['m_9'].append(row[13])
            dyslexia_single['m_10'].append(row[14])
            dyslexia_single['m_11'].append(row[15])
            dyslexia_single['m_12'].append(row[16])
            dyslexia_single['m_13'].append(row[17])
            dyslexia_single['m_14'].append(row[18])
            dyslexia_single['m_15'].append(row[19])
            dyslexia_single['m_16'].append(row[20])
            dyslexia_single['m_17'].append(row[21])
            dyslexia_single['m_other'].append(row[22])
            dyslexia_single['m_none'].append(row[23])
            dyslexia_single['m_correct'].append(row[24])
    print(dyslexia_single)

    # Write JSON file
    with io.open('googlesheet_jsons/dyslexia_single.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_single,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('googlesheet_jsons/dyslexia_single.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_single == data_loaded)


def get_tefel_task ():
    dyslexia_tefel = {'word': [],
                      'response': [],
                      'answer1': [],
                      'm_0': [],
                      'm_1': [],
                      'm_2': [],
                      'm_3': [],
                      'm_4': [],
                      'm_5': [],
                      'm_6': [],
                      'm_7': [],
                      'm_8': [],
                      'm_9': [],
                      'm_10': [],
                      'm_11': [],
                      'm_12': [],
                      'm_13': [],
                      'm_14': [],
                      'm_15': [],
                      'm_16': [],
                      'm_17': [],
                      'm_other': [],
                      'm_none': [],
                      'm_correct':[]
                      }

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('googlesheet_jsons/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('googlesheet_jsons/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'tefel1!B3:Y'
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
            dyslexia_tefel['answer1'].append(row[2])
            dyslexia_tefel['m_0'].append(row[3])
            dyslexia_tefel['m_1'].append(row[4])
            dyslexia_tefel['m_2'].append(row[5])
            dyslexia_tefel['m_3'].append(row[6])
            dyslexia_tefel['m_4'].append(row[7])
            dyslexia_tefel['m_5'].append(row[8])
            dyslexia_tefel['m_6'].append(row[9])
            dyslexia_tefel['m_7'].append(row[10])
            dyslexia_tefel['m_8'].append(row[11])
            dyslexia_tefel['m_9'].append(row[12])
            dyslexia_tefel['m_10'].append(row[13])
            dyslexia_tefel['m_11'].append(row[14])
            dyslexia_tefel['m_12'].append(row[15])
            dyslexia_tefel['m_13'].append(row[16])
            dyslexia_tefel['m_14'].append(row[17])
            dyslexia_tefel['m_15'].append(row[18])
            dyslexia_tefel['m_16'].append(row[19])
            dyslexia_tefel['m_17'].append(row[20])
            dyslexia_tefel['m_other'].append(row[21])
            dyslexia_tefel['m_none'].append(row[22])
            dyslexia_tefel['m_correct'].append(row[23])

    print(dyslexia_tefel)

    # Write JSON file
    with io.open('googlesheet_jsons/dyslexia_tefel.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_tefel,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('googlesheet_jsons/dyslexia_tefel.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_tefel == data_loaded)

def get_single_mistakes ():
    dyslexia_single_mistakes = {'mistakes':[],
                       'initials':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('googlesheet_jsons/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('googlesheet_jsons/client_secret.json', SCOPES)
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
    with io.open('googlesheet_jsons/dyslexia_single_mistakes.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_single_mistakes,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('googlesheet_jsons/dyslexia_single_mistakes.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_single_mistakes == data_loaded)

def get_tefel_mistakes ():
    dyslexia_tefel_mistakes = {'mistakes':[],
                       'initials':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('googlesheet_jsons/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('googlesheet_jsons/client_secret.json', SCOPES)
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
    with io.open('googlesheet_jsons/dyslexia_tefel_mistakes.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_tefel_mistakes,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('googlesheet_jsons/dyslexia_tefel_mistakes.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_tefel_mistakes == data_loaded)

def get_dyslexia_types ():
    dyslexia_types = {'dyslexia_types':[],
                      'feedback':[]}

    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('googlesheet_jsons/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('googlesheet_jsons/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1xtlwZ2EGO18lPJCNV2IWpvhSFblzFLyyHdka01mAdIs'
    RANGE_NAME = 'dyslexia_types!A2:B'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('mistake, initial:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s' % (row[0]))
            dyslexia_types['dyslexia_types'].append(row[0])
            dyslexia_types['feedback'].append(row[1])

    print(dyslexia_types)

    # Write JSON file
    with io.open('googlesheet_jsons/dyslexia_types.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(dyslexia_types,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

    # Read JSON file
    with open('googlesheet_jsons/dyslexia_types.json') as data_file:
        data_loaded = json.load(data_file)

    print(dyslexia_types == data_loaded)

get_single_task()
get_tefel_task()
get_single_mistakes()
get_tefel_mistakes()
get_dyslexia_types()