#!/usr/bin python3
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : Clady
# @Site    : 708
# @File    : .py
# @Software: PyCharm
import datetime

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Set the format of output
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.width', 500)
pd.set_option('display.max_colwidth', 50)
np.set_printoptions(threshold=np.inf)


# 时间转换，十进制数值转换为48位二进制
# op_data = pd.read_hdf("/home/gongjie/new/data/gongjie/csv/ad_operation_0508.h5", 'ad_operation_0508')
# op_new = pd.read_csv("/home/gongjie/new/data/gongjie/csv/ad_operation_clean.csv")
#
# ad_time = pd.DataFrame(columns=['ad_id', 'exposure_time'])
# ad = op_data.ad_id.unique()
# ad_time.ad_id = ad
# n = len(ad)
#
# for i in range(n):
#     tmp = ad_time.loc[i, 'ad_id']
#     print(tmp)
#     time = op_data[(op_data.ad_id == tmp) & (op_data.operation_type == 2) & (op_data.update_type == 4)].update_value.values[0]
#     # print(time)
#     time = time.split(',')
#     if len(set(time)) == 1:
#         if time[0]:
#             ad_time.loc[i, 'exposure_time'] = '{:048b}'.format(int(time[0]))
#             # print(time[0])
#             print(ad_time.loc[i, 'exposure_time'])
#
# ad_time.to_csv("/home/gongjie/new/data/gongjie/csv/ad_exposure_time_binary.csv")

# data = pd.read_csv("/home/gongjie/new/data/gongjie/csv/ad_exposure_time_binary.csv")

# id_special = []
# n = len(data)
# for i in range(n):
#     # print(i)
#     if data.loc[i, 'exposure_time'] is np.nan:
#         tmp = data.loc[i, 'ad_id']
#         # print(tmp)
#         id_special.append(tmp)
#
# m = len(id_special)
#
# for i in range(m):
#     tmp = id_special[i]
#     print(tmp)
#     time = op_data[(op_data.ad_id == tmp)]
#     print(time)

# train = pd.read_csv('df_train_static_feature.csv')
# train['exposure_time'] = np.empty((len(train), 0)).tolist()
#
# n = len(train)
# for i in range(n):
#     ad = train.loc[i, 'ad_id']
#     print(i)
#     tmp = data[data.ad_id == ad].exposure_time.values[0]
#     if tmp is not np.nan:
#         for j in tmp:
#             train.loc[i, 'exposure_time'].append(int(j))
#         print(train.loc[i, 'exposure_time'])
#
# train.to_csv('df_train_static_feature_new.csv')

# data = pd.read_csv('df_train_static_feature_new.csv')
# data['week'] = 0
# n = len(data)
# s = '2019-02-11'
# for i in range(n):
#     ad = data.loc[i, 'ad_id']
#     print(i)
#     tmp = data.loc[i, 'request_ymd']
#     print(tmp)
#     data.loc[i, 'week'] = ((datetime.datetime.strptime(tmp, "%Y-%m-%d").date() - datetime.datetime.strptime(s, "%Y-%m-%d").date()).days % 7) + 1
#
#     print(data.loc[i, 'week'])
#
# data.to_csv('df_train_static_feature_new1.csv')
# k = 1
# for i in range(n):
#     time = data.loc[i, 'exposure_time']
#     # print(len(time))
#     if len(time) < 147:
#         ad = data.loc[i, 'ad_id']
#         print(k)
#         k += 1
#         # print(ad)
#         week = data.loc[i, 'week']
#         tmp = op_data[
#             (op_data.ad_id == str(ad)) & (op_data.operation_type == 2) & (op_data.update_type == 4)].update_value.values[0]
#         time_new = '{:048b}'.format(int(tmp.split(',')[week-1]))
#         time = list(time)[1:-1]
#         for j in time_new:
#             time.append(int(j))
#         data.loc[i, 'exposure_time'] = str(time)
#         print(data.loc[i, 'exposure_time'])
# data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)
# data.to_csv('df_train_static_feature_new.csv')
# data.drop(['Unnamed: 0', 'Unnamed: 0.1.1'], axis=1, inplace=True)
# time_op = op_data[(op_data.operation_type == 1) & (op_data.update_type == 4)].reset_index(drop=True, inplace=False)
# n = len(time_op)
# for i in range(n):
#     ad = time_op.loc[i, 'ad_id']
#     print(ad)
#     time = time_op.loc[i, 'operation_date']
#     # print(type(time))
#     value = time_op.loc[i, 'update_value']
#     tmp = data[data.ad_id == int(ad)].reset_index(inplace=False)
#     for j in range(len(tmp)):
#         date = tmp.loc[j, 'request_ymd']
#         if datetime.datetime.strptime(date, "%Y-%m-%d") > time:
#             week = tmp.loc[j, 'week']
#             index = tmp.loc[j, 'index']
#             data.loc[index, 'exposure_time'] = str(list(map(int, '{:049b}'.format(int(value.split(',')[week-1])))))
#             print(data.loc[index, 'exposure_time'])
# data.to_csv('df_train_static_feature_new_0515.csv')

# 处理test曝光时间
# test = pd.read_hdf("/home/gongjie/new/data/gongjie/csv/test.h5", 'test')
#
# time_mark = datetime.datetime.strptime('2019-03-20 00:00:00', "%Y-%m-%d %H:%M:%S")
# index = datetime.datetime.strptime('2019-02-11', "%Y-%m-%d").date()
# print(index)
# n = len(test)
# test['week'] = 0
# for i in range(n):
#     date_op = test.loc[i, 'date']
#     # print(date_op)
#     # week
#     week = 0
#     if date_op > time_mark:
#         # print((date_op.date() - index).days)
#         week = ((date_op.date() - index).days + 1) % 7 + 1
#     else:
#         week = 4
#     test.loc[i, 'week'] = week
#     print(test.loc[i, 'week'])
#
#     # exposure_time
#     time = test.loc[i, 'exposure_time'].split(',')[week-1]
#     # print(time)
#     test.loc[i, 'exposure_time'] = str(list(map(int, '{:048b}'.format(int(time)))))
#     print(test.loc[i, 'exposure_time'])
#
# test.to_csv('test.csv')

# train = pd.read_csv('df_train_static_feature_new_0515.csv')
# train.drop(['Unnamed: 0'], axis=1, inplace=True)
# n = len(train)
# for i in range(n):
#     print(i)
#     tmp = train.loc[i, 'exposure_time']
#     train.loc[i, 'exposure_time'] = tmp[0] + tmp[4:]
#     print(train.loc[i, 'exposure_time'])
#
# train.to_csv('df_train_static_feature_0515.csv')

# 处理train的crowd
# op_data = pd.read_hdf("/home/gongjie/new/data/gongjie/csv/ad_operation_0508.h5", 'ad_operation_0508')
# op_data = pd.read_csv("/home/gongjie/new/data/gongjie/csv/ad_exposure_value.csv")
# train = pd.read_csv('df_train_static_feature_0515.csv')
# train.drop(['Unnamed: 0'], axis=1, inplace=True)
#
# train['age'] = ''
# train['gender'] = ''
# train['area'] = ''
# train['status'] = ''
# train['education'] = ''
# train['consumption_ability'] = ''
# train['device'] = ''
# train['work'] = ''
# train['connection_type'] = ''
# train['behavior'] = ''
#
# n = len(train)
# for i in range(n):
#     ad = train.loc[i, 'ad_id']
#     print(i)
#     # value = op_data[(op_data.ad_id == str(ad)) & (op_data.operation_type == 2) & (op_data.update_type == 3)].update_value.values[0]
#     value = op_data[op_data.ad_id == ad].value.values[0]
#     print(value)
#     # print(tmp)
#     if value:
#         if value == 'all':
#             train.loc[i, 'age'] = 'all'
#             train.loc[i, 'gender'] = 'all'
#             train.loc[i, 'area'] = 'all'
#             train.loc[i, 'status'] = 'all'
#             train.loc[i, 'education'] = 'all'
#             train.loc[i, 'consumption_ability'] = 'all'
#             train.loc[i, 'device'] = 'all'
#             train.loc[i, 'work'] = 'all'
#             train.loc[i, 'connection_type'] = 'all'
#             train.loc[i, 'behavior'] = 'all'
#
#             print(train.loc[i, 'age'])
#             print(train.loc[i, 'gender'])
#             print(train.loc[i, 'area'])
#             print(train.loc[i, 'status'])
#             print(train.loc[i, 'education'])
#             print(train.loc[i, 'consumption_ability'])
#             print(train.loc[i, 'device'])
#             print(train.loc[i, 'work'])
#             print(train.loc[i, 'connection_type'])
#             print(train.loc[i, 'behavior'])
#             continue
#         tmp = value.split('|')
#         for item in tmp:
#             # print(item)
#             if 'age' in item:
#                 train.loc[i, 'age'] = item[4:]
#                 print(train.loc[i, 'age'])
#                 continue
#             elif 'gender' in item:
#                 train.loc[i, 'gender'] = item[7:]
#                 print(train.loc[i, 'gender'])
#                 continue
#             elif 'area' in item:
#                 train.loc[i, 'area'] = item[5:]
#                 print(train.loc[i, 'area'])
#                 continue
#             elif 'status' in item:
#                 train.loc[i, 'status'] = item[7:]
#                 print(train.loc[i, 'status'])
#                 continue
#             elif 'education' in item:
#                 train.loc[i, 'education'] = item[10:]
#                 print(train.loc[i, 'education'])
#                 continue
#             elif 'consuptionAbility' in item:
#                 train.loc[i, 'consumption_ability'] = item[18:]
#                 print(train.loc[i, 'consumption_ability'])
#                 continue
#             elif 'device' in item:
#                 train.loc[i, 'device'] = item[7:]
#                 print(train.loc[i, 'device'])
#                 continue
#             elif 'work' in item:
#                 train.loc[i, 'work'] = item[5:]
#                 print(train.loc[i, 'work'])
#                 continue
#             elif 'connectionType' in item:
#                 train.loc[i, 'connection_type'] = item[15:]
#                 print(train.loc[i, 'connection_type'])
#                 continue
#             elif 'behavior' in item:
#                 train.loc[i, 'behavior'] = item[9:]
#                 print(train.loc[i, 'behavior'])
#                 continue
#
# train.to_csv('df_train_static_feature_new2.csv')

# data = pd.read_csv("/home/gongjie/new/data/gongjie/csv/ad_exposure_time.csv")
# data['value'] = ''
# n = len(data)
# for i in range(n):
#     print(i)
#     ad = data.loc[i, 'ad_id']
#     value = op_data[(op_data.ad_id == str(ad)) & (op_data.operation_type == 2) & (op_data.update_type == 3)].update_value.values[0]
#     data.loc[i, 'value'] = value
#     print(value)
#
# data.to_csv("/home/gongjie/new/data/gongjie/csv/ad_exposure_value.csv")

# op_data = pd.read_hdf("/home/gongjie/new/data/gongjie/csv/ad_operation_0508.h5", 'ad_operation_0508')
# data = pd.read_csv('df_train_static_feature_new2.csv')
#
# data.drop('Unnamed: 0', axis=1, inplace=True)
# time_op = op_data[(op_data.operation_type == 1) & (op_data.update_type == 3)].reset_index(drop=True, inplace=False)
# n = len(time_op)
# print(n)
# for i in range(n):
#     ad = time_op.loc[i, 'ad_id']
#     print('i: ', i)
#     time = time_op.loc[i, 'operation_date']
#     # print(type(time))
#     value = time_op.loc[i, 'update_value']
#     ad_part = data[data.ad_id == int(ad)].reset_index(inplace=False)
#     for j in range(len(ad_part)):
#         date = ad_part.loc[j, 'request_ymd']
#         if datetime.datetime.strptime(date, "%Y-%m-%d") > time:
#             index = ad_part.loc[j, 'index']
#             print(value)
#             # print(tmp)
#             if value:
#                 if value == 'all':
#                     data.loc[index, 'age'] = 'all'
#                     data.loc[index, 'gender'] = 'all'
#                     data.loc[index, 'area'] = 'all'
#                     data.loc[index, 'status'] = 'all'
#                     data.loc[index, 'education'] = 'all'
#                     data.loc[index, 'consumption_ability'] = 'all'
#                     data.loc[index, 'device'] = 'all'
#                     data.loc[index, 'work'] = 'all'
#                     data.loc[index, 'connection_type'] = 'all'
#                     data.loc[index, 'behavior'] = 'all'
#
#                     print(data.loc[index, 'age'])
#                     print(data.loc[index, 'gender'])
#                     print(data.loc[index, 'area'])
#                     print(data.loc[index, 'status'])
#                     print(data.loc[index, 'education'])
#                     print(data.loc[index, 'consumption_ability'])
#                     print(data.loc[index, 'device'])
#                     print(data.loc[index, 'work'])
#                     print(data.loc[index, 'connection_type'])
#                     print(data.loc[index, 'behavior'])
#                     continue
#                 tmp = value.split('|')
#                 for item in tmp:
#                     # print(item)
#                     if 'age' in item:
#                         data.loc[index, 'age'] = item[4:]
#                         print(data.loc[index, 'age'])
#                         continue
#                     elif 'gender' in item:
#                         data.loc[index, 'gender'] = item[7:]
#                         print(data.loc[index, 'gender'])
#                         continue
#                     elif 'area' in item:
#                         data.loc[index, 'area'] = item[5:]
#                         print(data.loc[index, 'area'])
#                         continue
#                     elif 'status' in item:
#                         data.loc[index, 'status'] = item[7:]
#                         print(data.loc[index, 'status'])
#                         continue
#                     elif 'education' in item:
#                         data.loc[index, 'education'] = item[10:]
#                         print(data.loc[index, 'education'])
#                         continue
#                     elif 'consuptionAbility' in item:
#                         data.loc[index, 'consumption_ability'] = item[18:]
#                         print(data.loc[index, 'consumption_ability'])
#                         continue
#                     elif 'device' in item:
#                         data.loc[index, 'device'] = item[7:]
#                         print(data.loc[index, 'device'])
#                         continue
#                     elif 'work' in item:
#                         data.loc[index, 'work'] = item[5:]
#                         print(data.loc[index, 'work'])
#                         continue
#                     elif 'connectionType' in item:
#                         data.loc[index, 'connection_type'] = item[15:]
#                         print(data.loc[index, 'connection_type'])
#                         continue
#                     elif 'behavior' in item:
#                         data.loc[index, 'behavior'] = item[9:]
#                         print(data.loc[index, 'behavior'])
#                         continue
#
# data.to_csv('df_train_static_feature_new2.csv')

# 处理test的crowd
# test = pd.read_csv('test.csv')
# # test.drop('Unnamed: 0', axis=1, inplace=True)
# n = len(test)
# test['age'] = ''
# test['gender'] = ''
# test['area'] = ''
# test['status'] = ''
# test['education'] = ''
# test['consumption_ability'] = ''
# test['device'] = ''
# test['work'] = ''
# test['connection_type'] = ''
# test['behavior'] = ''
#
# for i in range(n):
#     print(i)
#     # ad = test.loc[i, 'ad_id']
#     # print(ad)
#     value = test.loc[i, 'crowd']
#     print(value)
#     # print(tmp)
#     if value:
#         if value == 'all':
#             test.loc[i, 'age'] = 'all'
#             test.loc[i, 'gender'] = 'all'
#             test.loc[i, 'area'] = 'all'
#             test.loc[i, 'status'] = 'all'
#             test.loc[i, 'education'] = 'all'
#             test.loc[i, 'consumption_ability'] = 'all'
#             test.loc[i, 'device'] = 'all'
#             test.loc[i, 'work'] = 'all'
#             test.loc[i, 'connection_type'] = 'all'
#             test.loc[i, 'behavior'] = 'all'
#
#             print(test.loc[i, 'age'])
#             print(test.loc[i, 'gender'])
#             print(test.loc[i, 'area'])
#             print(test.loc[i, 'status'])
#             print(test.loc[i, 'education'])
#             print(test.loc[i, 'consumption_ability'])
#             print(test.loc[i, 'device'])
#             print(test.loc[i, 'work'])
#             print(test.loc[i, 'connection_type'])
#             print(test.loc[i, 'behavior'])
#             continue
#         tmp = value.split('|')
#         for item in tmp:
#             # print(item)
#             if 'age' in item:
#                 test.loc[i, 'age'] = item[4:]
#                 print(test.loc[i, 'age'])
#                 continue
#             elif 'gender' in item:
#                 test.loc[i, 'gender'] = item[7:]
#                 print(test.loc[i, 'gender'])
#                 continue
#             elif 'area' in item:
#                 test.loc[i, 'area'] = item[5:]
#                 print(test.loc[i, 'area'])
#                 continue
#             elif 'status' in item:
#                 test.loc[i, 'status'] = item[7:]
#                 print(test.loc[i, 'status'])
#                 continue
#             elif 'education' in item:
#                 test.loc[i, 'education'] = item[10:]
#                 print(test.loc[i, 'education'])
#                 continue
#             elif 'consuptionAbility' in item:
#                 test.loc[i, 'consumption_ability'] = item[18:]
#                 print(test.loc[i, 'consumption_ability'])
#                 continue
#             elif 'device' in item:
#                 test.loc[i, 'device'] = item[7:]
#                 print(test.loc[i, 'device'])
#                 continue
#             elif 'work' in item:
#                 test.loc[i, 'work'] = item[5:]
#                 print(test.loc[i, 'work'])
#                 continue
#             elif 'connectionType' in item:
#                 test.loc[i, 'connection_type'] = item[15:]
#                 print(test.loc[i, 'connection_type'])
#                 continue
#             elif 'behavior' in item:
#                 test.loc[i, 'behavior'] = item[9:]
#                 print(test.loc[i, 'behavior'])
#                 continue
#
# test.to_csv('test_new.csv')

# 处理crowd各个特征
# train = pd.read_csv("/home/gongjie/new/tencent_gongjie/testA/df_train_static_feature_new2.csv")
# test = pd.read_csv("/home/gongjie/new/tencent_gongjie/testA/test_new.csv")
# if data.status[0] is np.NaN:
#     print(data.status[0:50])
# print(data.status[25] == '13,9')
# s = '13,9'
# print(list(map(int, s.split(','))))
# print(data.shape)
# print(data.connection_type.value_counts())
# feature_train = pd.DataFrame(columns=['ad_id', 'status', 'education', 'connection_type'])
# feature_test = pd.DataFrame(columns=['ad_id', 'status', 'education', 'connection_type'])
#
# n_train = len(train)
# n_test = len(test)
#
# feature_train.ad_id = train.ad_id
# feature_test.ad_id = test.ad_id
# # print(feature.shape)
# feature_train['status'] = ','.join(['0' for _ in range(18)])
# feature_train['education'] = ','.join(['0' for _ in range(8)])
# feature_train['connection_type'] = ','.join(['0' for _ in range(5)])
# feature_test['status'] = ','.join(['0' for _ in range(18)])
# feature_test['education'] = ','.join(['0' for _ in range(8)])
# feature_test['connection_type'] = ','.join(['0' for _ in range(5)])
#
#
# for i in range(n_train):
#     print(i)
#     status = train.loc[i, 'status']
#     education = train.loc[i, 'education']
#     connectionType = train.loc[i, 'connection_type']
#
#     s_sta_train = ['0' for _ in range(18)]
#     s_edu_train = ['0' for _ in range(8)]
#     s_con_train = ['0' for _ in range(5)]
#
#     if status is not np.NaN:
#         print(status)
#         if status == 'all':
#             feature_train.loc[i, 'status'] = ','.join(['1' for _ in range(18)])
#         else:
#             tmp = status.split(',')
#             for j in tmp:
#                 s_sta_train[int(j)-1] = '1'
#             feature_train.loc[i, 'status'] = ','.join(s_sta_train)[::-1]
#
#     if education is not  np.NaN:
#         print(education)
#         if education == 'all':
#             feature_train.loc[i, 'education'] = ','.join(['1' for _ in range(8)])
#         else:
#             tmp = education.split(',')
#             for j in tmp:
#                 s_edu_train[int(j)-1] = '1'
#             feature_train.loc[i, 'education'] = ','.join(s_edu_train)[::-1]
#
#     if connectionType is not np.NaN:
#         print(connectionType)
#         if connectionType == 'all':
#             feature_train.loc[i, 'connection_type'] = ','.join(['1' for _ in range(5)])
#         else:
#             tmp = connectionType.split(',')
#             for j in tmp:
#                 s_con_train[int(j)-1] = '1'
#             feature_train.loc[i, 'connection_type'] = ','.join(s_con_train)[::-1]
#
#     print(feature_train.loc[i, 'status'])
#     print(feature_train.loc[i, 'education'])
#     print(feature_train.loc[i, 'connection_type'])
#
# for i in range(n_test):
#     status = test.loc[i, 'status']
#     education = test.loc[i, 'education']
#     connectionType = test.loc[i, 'connection_type']
#
#     s_sta_test = ['0' for _ in range(18)]
#     s_edu_test = ['0' for _ in range(8)]
#     s_con_test = ['0' for _ in range(5)]
#
#     if status is not np.NaN:
#         if status == 'all':
#             feature_test.loc[i, 'status'] = ','.join(['1' for _ in range(18)])
#         else:
#             tmp = status.split(',')
#             for j in tmp:
#                 s_sta_test[int(j)-1] = '1'
#             feature_test.loc[i, 'status'] = ','.join(s_sta_test)[::-1]
#
#     if education is not np.NaN:
#         if education == 'all':
#             feature_test.loc[i, 'education'] = ','.join(['1' for _ in range(8)])
#         else:
#             tmp = education.split(',')
#             for j in tmp:
#                 s_edu_test[int(j)-1] = '1'
#             feature_test.loc[i, 'education'] = ','.join(s_edu_test)[::-1]
#
#     if connectionType is not np.NaN:
#         if connectionType == 'all':
#             feature_test.loc[i, 'connection_type'] = ','.join(['1' for _ in range(5)])
#         else:
#             tmp = connectionType.split(',')
#             for j in tmp:
#                 s_con_test[int(j)-1] = '1'
#             feature_test.loc[i, 'connection_type'] = ','.join(s_con_test)[::-1]
#
#     print(feature_test.loc[i, 'status'])
#     print(feature_test.loc[i, 'education'])
#     print(feature_test.loc[i, 'connection_type'])
#
# feature_train.to_csv('feature_train.csv')
# feature_test.to_csv('feature_test.csv')

# feature_test = pd.read_csv('feature_test.csv')
# feature_train = pd.read_csv('feature_train.csv')
#
# n_train = len(feature_train)
# n_test = len(feature_test)
#
# for i in range(n_train):
#     sta = feature_train.loc[i, 'status']
#     edu = feature_train.loc[i, 'education']
#     con = feature_train.loc[i, 'connection_type']
#
#     feature_train.loc[i, 'status'] = sta[::-1]
#     feature_train.loc[i, 'education'] = edu[::-1]
#     feature_train.loc[i, 'connection_type'] = con[::-1]
#
# for i in range(n_test):
#     sta = feature_test.loc[i, 'status']
#     edu = feature_test.loc[i, 'education']
#     con = feature_test.loc[i, 'connection_type']
#
#     feature_test.loc[i, 'status'] = sta[::-1]
#     feature_test.loc[i, 'education'] = edu[::-1]
#     feature_test.loc[i, 'connection_type'] = con[::-1]
#
# feature_train.to_csv('feature_train.csv', index=False)
# feature_test.to_csv('feature_test.csv', index=False)

# train = pd.read_csv("/home/gongjie/new/tencent_gongjie/testA/df_train_static_feature_new2.csv")
#
# print(len(train.age.value_counts()))
# print(train.age.value_counts()[:10])
# print(len(train.area.value_counts()))
# print(train.area.value_counts()[:10])
# print(len(train.behavior.value_counts()))
# print(train.behavior.value_counts()[:10])

