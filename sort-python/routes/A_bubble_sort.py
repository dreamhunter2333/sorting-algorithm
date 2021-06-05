"""
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

算法步骤

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

什么时候最快：当输入的数据已经是正序时（都已经是正序了，我还要你冒泡排序有何用啊）。
什么时候最慢：当输入的数据是反序时（写一个 for 循环反序输出数据不就行了，干嘛要用你冒泡排序呢，我是闲的吗）
"""
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.post("/bubble_sort", tags=["冒泡排序"])
def sort(num_list: List[int]) -> List:
    nums_len = len(num_list)
    for i in reversed(range(nums_len)):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                num_list[j+1], num_list[j] = num_list[j], num_list[j+1]
    return num_list
