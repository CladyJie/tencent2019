#!/usr/bin python3
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : Clady
# @Site    : 708
# @File    : .py
# @Software: PyCharm

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Set the format of output
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.width', 500)
pd.set_option('display.max_colwidth', 100)
np.set_printoptions(threshold=np.inf)


# 将十进制时间数值转为二进制，再转为字符串
# data = pd.read_hdf("/home/gongjie/new/data/gongjie/csv/ad_operation_0508.h5", 'ad_operation_0508')
# num = len(data)
# for i in range(num):
#     if data.iloc[i, 3] == 4:
#         print(i)
#         day_time = data.iloc[i, 4].split(',')
#         s = ''
#         for j in range(len(day_time)):
#             period = '{:049b}'.format(int(day_time[j]))[::-1]
#             #print(period)
#             valid_num = []
#             flag = False
#             begin = 0
#             end = 0
#
#             for k in range(49):
#                 index = int(period[k])
#                 # print(index)
#                 if not flag:
#                     if index:
#                         flag = not flag
#                         begin = k/2
#                         end = begin + 0.5
#                 else:
#                     if index:
#                         end += 0.5
#                     else:
#                         flag = not flag
#                         valid_num.append([begin, end])
#
#             #print(valid_num)
#             n = len(valid_num)
#
#             for p in range(n):
#
#                 begin = valid_num[p][0]
#                 end = valid_num[p][1]
#
#                 tmp = int(begin)
#                 if tmp == begin:
#                     s += '{:02d}'.format(tmp) + ':00-'
#                 else:
#                     s += '{:02d}'.format(tmp) + ':30-'
#                 tmp = int(end)
#                 if tmp == end:
#                     s += '{:02d}'.format(tmp) + ':00'
#                 else:
#                     s += '{:02d}'.format(tmp) + ':30'
#
#                 if p < n-1:
#                     s += ','
#
#             if j < 6:
#                 s += ';'
#         data.iloc[i, 4] = s
#         print(s)
#
# data.to_hdf("/home/gongjie/new/data/gongjie/csv/ad_operation_time_transfer_new.h5",'ad_operation_time_transfer_new')


# 时区转换：+8h
# import csv
# out = open("/home/gongjie/new/data/fuyu/total_log_clean_new.csv",'a', newline='')
# csv_write = csv.writer(out,dialect='excel')
# line = 'Unnamed: 0,request_id,request_date,location_id,user_id,ad_id,size,price,pctr,quality_ecpm,total_ecpm,request_ymd'.split(',')
# csv_write.writerow(line)
# with open("/home/gongjie/new/data/fuyu/total_log_clean_0510.csv") as f:
#
#     line = f.readline()
#     while True:
#         line = f.readline().strip('\n')
#         if line:
#             # print(line)
#             line = line.split(',')
#             tmp = line[2]
#             # if tmp == 'request_date':
#             #     csv_write.writerow(line)
#             #     continue
#             # print(tmp)
#             data_old = datetime.datetime.strptime(tmp, "%Y-%m-%d %H:%M:%S")
#     # print(tmp)
#
#             date_new = (data_old + datetime.timedelta(hours=8))
#             line[2] = date_new.strftime('%Y-%m-%d %H:%M:%S')
#             print(line[2])
#             line[11] = date_new.strftime('%Y-%m-%d')
#             # print(line[11])
#             csv_write.writerow(line)
#         else:
#             break
# out.close()