#-*- coding=utf-8 -*-
'''
***********直接插入排序***********
'''


# 直接插入排序
def insertSort(a, n):
    for i in xrange(1, n):
        if a[i] < a[i - 1]:  # 若第i个元素大于i-1元素，直接插入。小于的话，移动有序表后插入
            j = i - 1
            x = a[i]  # 复制为哨兵，即存储待排序元素
            a[i] = a[i - 1]  # 先后移一个元素
            while x < a[j] and j >= 0:  # 查找在有序表的插入位置, 保证变量J不能小于0
                a[j + 1] = a[j]  #不断将大的数字后移到不可以移动为止
                j -= 1
            a[j + 1] = x
        print i, a


'''
***********希尔排序***********
'''


#希尔插入排序
def shellInsertSort(a, n, dk):
    for i in xrange(dk, n):
        if a[i] < a[i - dk]:  #若第i个元素大于i-1元素，直接插入。小于的话，移动有序表后插入
            j = i - dk
            x = a[i]  #复制为哨兵，即存储待排序元素
            a[i] = a[i - dk]  #首先后移一个元素
            while x < a[j] and j >= 0:  #查找在有序表的插入位置
                a[j + dk] = a[j]
                j -= dk  #元素后移
            a[j + dk] = x  #插入到正确位置
    print dk, a


#希尔排序
#先按增量d（n/2,n为要排序数的个数进行希尔排序
def shellSort(a, n):
    dk = n / 2
    while dk >= 1:
        shellInsertSort(a, n, dk)
        dk = dk / 2


'''
***********简单选择排序***********
'''


#选择最小值索引
def selectMinKey(a, n, i):
    k = i
    for x in xrange(i + 1, n):
        if a[k] > a[x]:
            k = x
    return k


#简单选择排序
def selectSort(a, n):
    for i in xrange(0, n):
        key = selectMinKey(a, n, i)
        if key != i:
            tmp = a[i]
            a[i] = a[key]
            a[key] = tmp
    print a


'''
***********堆排序***********
'''


# 已知a[s…m]除了a[s] 外均满足堆的定义
# 调整a[s],使其成为大顶堆.即将对第s个结点为根的子树筛选,
#
# @param a是待调整的堆数组
# @param s是待调整的数组元素的位置
# @param n是数组的长度
def heapAdjust(a, s, n):
    tmp = a[s]
    c = 2 * s + 1  #左孩子结点的位置。(i+1 为当前调整结点的右孩子结点的位置)
    while c < n:
        if c + 1 < n and a[c] < a[c + 1]:  #如果右孩子大于左孩子(找到比当前待调整结点大的孩子结点)
            c += 1
        if a[s] < a[c]:  #如果较大的子结点大于父结点
            a[s] = a[c]  #如果较大的子结点大于父结点
            s = c  #如果较大的子结点大于父结点
            c = 2 * s + 1
        else:  #如果较大的子结点大于父结点
            break
        a[s] = tmp  #如果较大的子结点大于父结点
    print a[0:n]


# 初始堆进行调整
# 将H[0..length-1]建成堆
# 调整完之后第一个元素是序列的最小的元素
def buildingHeap(a, n):
    #最后一个有孩子的节点的位置 i=  (length -1) / 2
    for i in sorted(range(0, (n - 1) / 2), reverse=True):
        heapAdjust(a, i, n)


#堆排序算法
def heapSort(a, n):
    #初始堆
    buildingHeap(a, n)
    #从最后一个元素开始对序列进行调整
    for i in sorted(range(1, n), reverse=True):
        #交换堆顶元素H[0]和堆中最后一个元素
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp
        #每次交换堆顶元素和堆中最后一个元素之后，都要对堆进行调整
        heapAdjust(a, 0, i)
    print a


'''
***********冒泡排序***********
'''


#传统冒泡
def bubbleSort(a, n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
    print a


#改进版1
def bubbleSort1(a, n):
    i = n - 1  #初始时,最后位置保持不变
    while i > 0:
        pos = 0  #每趟开始时,无记录交换
        for j in range(0, i):
            if a[j] > a[j + 1]:
                pos = j  #记录交换的位置
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
        i = pos  #为下一趟排序作准备
    print a


#改进版2
def bubbleSort2(a, n):
    low = 0
    high = n - 1  #设置变量的初始值
    tmp = 0
    j = 0
    while low < high:
        for j in range(low, high):  #设置变量的初始值
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
        high -= 1  #修改high值, 前移一位
        for j in sorted(range(low, high), reverse=True):  #反向冒泡,找到最小者
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
        low += 1  #修改low值,后移一位
    print a


a = [3, 1, 5, 7, 2, 4, 9, 6, 10, 8]
n = len(a)
bubbleSort2(a, n)