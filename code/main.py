#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Auther :liuyuqi.gov@msn.cn
@Time :2018/7/4 15:55
@File :main.py
'''
import os,sys
import numpy as np,pandas as pd
import matplotlib.pyplot as plt

# 数据预览
import pandas as pd
import matplotlib.pyplot as plt
from configparser import ConfigParser

# step1: 数据参数初始化

cf = ConfigParser()
config_path = "../conf/config.ini"
section_name = "data_file_name"
cf.read(config_path)

app_interference = cf.get(section_name, "app_interference")
app_resources = cf.get(section_name, "app_resources")
instance_deploy = cf.get(section_name, "instance_deploy")
machine_resources = cf.get(section_name, "machine_resources")

#Wij矩阵表示第i个instance实例部署到j主机上
Wij_size = np.zeros((68219, 6000))
Wij = np.zeros_like(Wij_size)

def getWij():
    # inst_26195, app_147, machine_1149
    df3=pd.read_csv("../data/instance.csv", header=None,names=list(["instanceid", "appid", "machineid","disk"]))
    df2 = pd.read_csv(machine_resources, header=None, names=list(
        ["machineid", "cpu", "mem", "disk", "P", "M", "PM"]), encoding="utf-8")
    for i in range(0,68219):
            if df3[i]["machineid"]==None:
                pass
            else:
                # Wij[i][j]=
                pass


if __name__ == '__main__':
    pass