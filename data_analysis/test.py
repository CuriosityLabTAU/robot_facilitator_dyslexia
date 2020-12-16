from __future__ import division
import ast
import json
from datetime import datetime
import collections
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
import numpy as np
from os import listdir
from os.path import isfile, join, basename

def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

matplotlib.use('TkAgg')

# files
file_names = []
for s in range(1):
    try:
        path_name = './tablets/All/'
        file_names.extend([path_name + f for f in listdir(path_name) if isfile(join(path_name, f))])
    except:
        pass
print(len(file_names))

format = '%Y_%m_%d_%H_%M_%S_%f'
iter= 0
for file in file_names[1:]: # iterate on all files (except the first)
    print('k=',iter)
    iter = iter+ 1
    f = open(file, "r")
    lines = f.readlines()
    dic_message = ast.literal_eval(lines[0])
    ts_list = []
    action_up_list = []
    action_down_list = []
    action_press_list = []
    action_data_list = []
    action_spinner_list = []

# sort dictionary
    od = collections.OrderedDict(
        sorted(dic_message.items(), key=lambda t: totimestamp(datetime.strptime(t[0], '%Y_%m_%d_%H_%M_%S_%f'))))

    for k, v in od.items(): # iterate all keys and values
        # v = json.loads(v)
        #print(k)
        ts = totimestamp(datetime.strptime(k, '%Y_%m_%d_%H_%M_%S_%f')) # timestamp
        ts_list.append(totimestamp(datetime.strptime(k, '%Y_%m_%d_%H_%M_%S_%f')))
        action = ast.literal_eval(v['data'])['log']['action']
        if action == 'up':
            action_up_list.append(ts)
        elif action == 'down':
            action_down_list.append(ts)
        elif action == 'press':
            action_press_list.append(ts)
        elif action == 'data':
            action_data_list.append(ts)
        elif action == 'spinner':
            action_spinner_list.append(ts)

        print(ast.literal_eval(v['data'])['log']['action'])

    #   plt.figure()
    plt.plot(np.array(action_up_list), iter*np.ones([len(action_up_list), 1]), '.', label='up', color='red')
    plt.plot(np.array(action_down_list), iter*np.ones([len(action_down_list), 1]), '.', label='down', color='green')
    plt.plot(np.array(action_press_list), iter*np.ones([len(action_press_list), 1]), '.', label='press', color = 'purple')
    plt.plot(np.array(action_data_list), iter*np.ones([len(action_data_list), 1]), '.', label='data', color = 'yellow')
    plt.plot(np.array(action_spinner_list), iter*np.ones([len(action_spinner_list), 1]), '.', label='spinner', color='blue')

plt.legend()
plt.show()

format = '%Y_%m_%d_%H_%M_%S_%f'
filename = "2018_05_16_13_07_03_365258.log"
f = open(filename, "r")
#f = open('data_analysis/'+filename, "r")
lines = f.readlines()
dic_message = ast.literal_eval(lines[0])
#dic_message['2018_05_16_13_36_34_124697']['data']
#dic_message['2018_05_16_13_30_49_732916']['data']
datetime.strptime('2018_05_16_13_30_49_732916', '%Y_%m_%d_%H_%M_%S_%f' )



arr = json.loads(dic_message['2018_05_16_13_30_49_732916']['data'])['log']['comment']


now = datetime.utcnow()
print now
print totimestamp(now)


    # print('filename', filename)
    # for line in lines:
    #     dic_message = ast.literal_eval(line)
    #     print dic_message
#    lines_list = line.split(';')
#    source = lines_list[0]
#    timestamp = lines_list[1]
#    message = lines_list[2]
#    if source == '/log':
        # print('message', message)
#        dic_message = ast.literal_eval(message)
 #       dict[timestamp] = [source, dic_message]
#
#
# f_csv = csv.reader(open(filename), delimiter=';')
# dict = json.load(open(filename, 'r'))
od = collections.OrderedDict(sorted(dic_message.items(), key=lambda t: totimestamp(datetime.strptime(t[0], '%Y_%m_%d_%H_%M_%S_%f' ))))

ts_list = []
action_up_list = []
action_down_list = []
action_press_list = []
action_data_list = []
action_spinner_list = []


for k, v in od.items():
    # v = json.loads(v)
    print(k)
    print(totimestamp(datetime.strptime(k, '%Y_%m_%d_%H_%M_%S_%f')))
    ts = totimestamp(datetime.strptime(k, '%Y_%m_%d_%H_%M_%S_%f'))
    ts_list.append(totimestamp(datetime.strptime(k, '%Y_%m_%d_%H_%M_%S_%f')))
    action = ast.literal_eval(v['data'])['log']['action']
    if action == 'up':
        action_up_list.append(ts)
    elif action == 'down':
        action_down_list.append(ts)
    elif action == 'press':
        action_press_list.append(ts)
    elif action == 'data':
        action_data_list.append(ts)
    elif action == 'spinner':
        action_spinner_list.append(ts)

    print(ast.literal_eval(v['data'])['log']['action'])


# plt.figure()
# plt.plot(np.array(action_up_list), np.ones([len(action_up_list),1]),'.', label='up')
# plt.plot(np.array(action_down_list), np.ones([len(action_down_list),1]),'.', label='down')
# plt.plot(np.array(action_press_list), np.ones([len(action_press_list),1]),'.', label='press')
# plt.plot(np.array(action_data_list), np.ones([len(action_data_list),1]),'.', label='data')
# plt.plot(np.array(action_spinner_list), np.ones([len(action_spinner_list),1]),'.', label='spinner')
# plt.legend()
# plt.show()



