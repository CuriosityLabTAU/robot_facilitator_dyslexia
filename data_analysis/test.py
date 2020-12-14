import ast
import json
from datetime import datetime
import collections

format = '%Y_%m_%d_%H_%M_%S_%f'
filename = "2018_05_16_13_07_03_365258.log"
f = open(filename, "r")
lines = f.readlines()
dic_message = ast.literal_eval(lines[0])
dic_message['2018_05_16_13_36_34_124697']['data']
dic_message['2018_05_16_13_30_49_732916']['data']
datetime.strptime('2018_05_16_13_30_49_732916', '%Y_%m_%d_%H_%M_%S_%f' )

arr = json.loads(dic_message['2018_05_16_13_30_49_732916']['data'])['log']['comment']

print('filename', filename)
for line in lines:
    dic_message = ast.literal_eval(line)
    print dic_message
#    lines_list = line.split(';')
#    source = lines_list[0]
#    timestamp = lines_list[1]
#    message = lines_list[2]
#    if source == '/log':
        # print('message', message)
        dic_message = ast.literal_eval(message)
        dict[timestamp] = [source, dic_message]
#
#
# f_csv = csv.reader(open(filename), delimiter=';')
# dict = json.load(open(filename, 'r'))
od = collections.OrderedDict(sorted(dict.items(), key=lambda t: int(t[0].toordinal)))