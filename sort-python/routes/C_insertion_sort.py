"""
插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

算法步骤

1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.post("/insertion_sort", tags=["插入排序"])
def sort(num_list: List[int]) -> List:
    num_len = len(num_list)
    # 当前位置
    cur_i = 1

    while num_len > cur_i:
        # 取后半部分第一个
        cur_num = num_list[cur_i]

        # 遍历前半部分序列插入
        insert_j = 0
        for j in range(cur_i):
            if num_list[cur_i - j - 1] < cur_num:
                insert_j = cur_i - j
                break

        if insert_j != cur_i:
            del num_list[cur_i]
            num_list.insert(insert_j, cur_num)

        cur_i += 1

    return num_list
