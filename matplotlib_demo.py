#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/14 09:27
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : matplotlib_demo.py
# @Software: PyCharm Community Edition


# matplotlib库学习笔记

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def demo_01():
    '''
    简单绘制一个折线图
    :return:
    '''

    # 加载数据（美国失业率数据）
    unrate = pd.read_csv("UNRATE.csv")
    print(unrate.head())
    print(unrate.dtypes)

    # 将“DATE”列转化为pandas库中datetime类型
    unrate["DATE"] = pd.to_datetime(unrate["DATE"])
    print(unrate.head())
    print(unrate.dtypes)

    # "DATE"列为x轴，"VALUE"列为y轴，绘图
    data_h12 = unrate.loc[0:12] # 取12个数据绘图
    plt.plot(data_h12["DATE"], data_h12["VALUE"]) # "DATE"列为x轴，"VALUE"列为y轴，默认为实线折现
    plt.xticks(rotation = 45) # x轴刻度标签逆时针旋转45度，方便更好的完全显示出来
    plt.xlabel("Month") # 增加x轴解释标签
    plt.ylabel("Unemployment Rate") # 增加y轴解释标签
    plt.title("Monthly Unemployment Trends, 1948") # 增加图标标题
    plt.show() # 绘图并显示


def demo_02():
    '''
    多子图绘制
    :return:
    '''
    fig = plt.figure() # 获取图形界面区域
    ax1 = fig.add_subplot(2,3,1) # 添加子图，分割为2行3列，子图位置为2*3中的第1个
    ax2 = fig.add_subplot(2,3,5) # 添加子图，分割为2行3列，子图位置为2*3中的第5个
    ax3 = fig.add_subplot(1,3,3) # 添加子图，分割为1行3列，子图位置为1*3中的第3个，相当于2*3的划分的第3,6区域合为一个大区域

    # 在子区域绘制
    ax1.plot(np.random.randint(1,5,5), np.arange(5))
    ax2.plot(np.arange(10) * 3, np.arange(10))
    ax3.plot([2,1,3,4,5], [10,8,6,4,2])

    plt.show()



if __name__ == "__main__":
    # demo_01()
    demo_02()