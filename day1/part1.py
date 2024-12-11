#from typing import List
import heapq
from collections import defaultdict

def read_file(filename):
    res = []
    with open(filename, mode='r') as f:
        lines = f.readlines()
        res.extend(lines)
    return res

def part1(filename):
    first_list = []
    second_list = []
    with open(filename, mode='r') as f:
        lines = f.readlines()
        for l in lines:
            first, *_, second = l.strip("\n").split(" ")
            heapq.heappush(first_list,first)
            heapq.heappush(second_list,second)

    sum = 0
    for _ in range(len(first_list)):
        breakpoint()
        tmp_first = int(heapq.heappop(first_list))
        tmp_second = int(heapq.heappop(second_list))
        diff = abs(tmp_first - tmp_second)
        sum += diff

    return sum

def part2(filename):
    first_list = []
    second_list = defaultdict(int)
    with open(filename, mode='r') as f:
        lines = f.readlines()
        for l in lines:
            first, *_, second = l.strip("\n").split(" ")
            first_list.append(first)
            second_list[int(second)] += 1

    similarity = 0
    for i in first_list:
        tmp = second_list[int(i)] * int(i)
        similarity += tmp

    return similarity


if __name__ == '__main__':
    sum = part1('input')
    print(f'Part1: {sum}')
    similarity = part2('input')
    print(f'Part2: {similarity}')
