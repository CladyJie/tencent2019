#!/usr/bin python3
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : Clady
# @Site    : 708
# @File    : .py
# @Software: PyCharm

import csv
out = open('update_testB.csv','a', newline='')
csv_write = csv.writer(out,dialect='excel')
title = 'sample_id,ad_id,date,size,industry_id,commodity_type,commodity_id,account_id,exposure_time,crowd,price'.split(',')
csv_write.writerow(title)
i = 0
with open("/home/gongjie/new/data/gongjie/raw/update_Btest_sample.dat") as f:
    while True:
        i += 1
        line=f.readline().strip('\n')
        if line:
            csv_write.writerow(line.split('\t'))
        else:
            break
        if i % 50 == 0:
            print('writing...')
print ("write over")
out.close()