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

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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
    data_h12 = unrate[0:12] # 取12个数据绘图
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


def demo_03():
    '''
    多折线绘制
    :return:
    '''
    # 加载数据（美国失业率数据）
    unrate = pd.read_csv("UNRATE.csv")

    # 将“DATE”列转化为pandas库中datetime类型
    unrate["DATE"] = pd.to_datetime(unrate["DATE"])
    # 取datatime中的月份创建新列“MONTH”
    unrate["MONTH"] = unrate["DATE"].dt.month

    fig = plt.figure(figsize=(6,3)) # 获得绘图区域，并设置区域尺寸，x轴长6（6个单位1），y轴长3（3个单位1）
    plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c="red") # 1948年数据，color="red"绘制
    plt.plot(unrate[12:24]["MONTH"], unrate[12:24]["VALUE"], c="blue") # 1949年数据，color="blue"绘制
    plt.show()

    # 多折线绘制(从1948年起，5年失业率对比)
    fig = plt.figure(figsize=(10,6))
    colors = ["red","blue","green","orange","black"]
    for i in range(5):
        start_index = i * 12
        end_index = (i+1) * 12
        label_str = str(1948 + i) # 图例标签解释说明文字
        subset = unrate[start_index:end_index] # 取出每年数据
        plt.plot(subset["MONTH"], subset["VALUE"], c=colors[i], label=label_str) # 绘制每年数据,增加图例标签
    # plt.legend(loc="upper left") # 显示图例；位置在，上方upper，左边left，右边right
    plt.legend(loc="best") # 显示图例；位置自动选择最好的
    # print(help(plt.legend)) # 查看函数文档
    plt.xticks(rotation=45)  # x轴刻度标签逆时针旋转45度，方便更好的完全显示出来
    plt.xlabel("月份")  # 增加x轴解释标签
    plt.ylabel("失业率")  # 增加y轴解释标签
    plt.title("美国每月失业率对比, 1948-1952")  # 增加图标标题
    plt.show()


def demo_04():
    '''
    绘制条形图
    :return:
    '''

    # 加载数据
    reviews = pd.read_csv("fandango_scores.csv")

    cols = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
    norm_reviews = reviews[cols]
    print(norm_reviews.loc[0])

    bar_heights = norm_reviews.ix[0, cols[1:]].values # 允许混合使用下标和名称进行选取，第0行，cols[1:]列
    print(bar_heights)

    bar_positions = np.arange(5) + 0.75 # 5列数据向右偏移0.75个距离，即最左侧偏离原点距离
    print(bar_positions)

    fig, ax = plt.subplots()
    ax.bar(bar_positions, bar_heights, 0.5) # bar为绘制条形图，参数分别为x轴数据，y轴数据，数据条宽度
    # plt.bar(bar_positions, bar_heights, 0.5) # 效果同上

    tick_positions = range(1,6)
    ax.set_xticks(tick_positions) # 指定x轴刻度显示值
    ax.set_xticklabels(cols[1:], rotation=45) # 指定x轴刻度标签显示值，并把刻度标签逆时针旋转45度

    ax.set_xlabel("各电影平台")
    ax.set_ylabel("电影评分")
    ax.set_title("各个电影平台对某个电影的评分对比")
    plt.show()


    # 水平画条形图
    fig, ax = plt.subplots()
    ax.barh(bar_positions, bar_heights, 0.5)  # bar为绘制条形图，参数分别为x轴数据，y轴数据，数据条宽度

    tick_positions = range(1, 6)
    ax.set_yticks(tick_positions)  # 指定x轴刻度显示值
    ax.set_yticklabels(cols[1:], rotation=45)  # 指定x轴刻度标签显示值，并把刻度标签逆时针旋转45度

    ax.set_ylabel("各电影平台")
    ax.set_xlabel("电影评分")
    ax.set_title("各个电影平台对某个电影的评分对比")
    plt.show()



def demo_05():
    '''
    绘制散点图
    :return:
    '''

    # 加载数据
    reviews = pd.read_csv("fandango_scores.csv")

    # fig, ax = plt.subplots()
    # # 绘制散点图
    # ax.scatter(reviews["Fandango_Ratingvalue"], reviews["RT_user_norm"])
    # ax.set_xlabel("Fandango")
    # ax.set_ylabel("Rotten Tomatoes")
    # plt.show()


    # 绘制散点图（翻转x，y坐标对比）
    fig = plt.figure(figsize=(12,6))
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    # 绘制散点图
    ax1.scatter(reviews["Fandango_Ratingvalue"], reviews["RT_user_norm"])
    ax1.set_xlabel("Fandango")
    ax1.set_ylabel("Rotten Tomatoes")
    # 绘制散点图
    ax2.scatter(reviews["RT_user_norm"], reviews["Fandango_Ratingvalue"])
    ax2.set_xlabel("Rotten Tomatoes")
    ax2.set_ylabel("Fandango")

    plt.show()



if __name__ == "__main__":
    # demo_01()
    # demo_02()
    # demo_03()
    # demo_04()
    demo_05()