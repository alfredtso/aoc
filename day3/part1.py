import re
import logging

logger = logging.getLogger(__name__)


def part1(input_file):
    res = 0
    with open(f'{input_file}') as f:
        lines = f.readlines()
        for l in lines:
            tmp = part1_line(l)
            res += tmp

    return res

def part2(input_file):
    # split by "don't"
    deduct = 0
    with open(input_file, mode='r') as f:
        lines = f.readlines()
        for l in lines:
            tmp = part2_line(l)
            deduct += tmp

    return deduct

def deduct():
    with open('input') as f:
        data = f.read()
    res = 0
    deduct = False
    ans = re.compile(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))')
    for i, j, k in ans.findall(data):
        if i == "don't()":
            deduct = True
        elif i == "do()":
            deduct = False
        else:
            if deduct:
                res += int(j) * int(k)
    return res


def part1_line(line):
    """
    >>> line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+(mul(11,8)undo()?mul(8,5))"
    >>> part1_line(line)
    161
    """
    valid_mul = re.compile(r'mul\(([0-9]+),([0-9]+)\)')
    res = 0
    gen_match = valid_mul.finditer(line)
    match_ls = list(gen_match)
    tmp_res = [ int(i.group(1)) * int(i.group(2)) for i in match_ls ]
    res += sum(tmp_res)

    return res

def part2_line(line):
    """
    >>> line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+(mul(11,8)undo()?mul(8,5))"
    >>> part2_line(line)
    113
    """
    deduct = 0
    tmp = split_by_dont(line)
    _, *rest = tmp
    for r in rest:
        first, *_ = split_by_do(r)
        bw_sum, tmp_ls = between_sum(first)
        deduct += bw_sum

    return deduct

def split_by_do(line):
    dont = re.compile(r'do\(\)')
    res = dont.split(line) 
    return res


def split_by_dont(line):
    dont = re.compile(r'don\'t\(\)')
    res = dont.split(line) 
    return res
    
def between_sum(line: str):
    # mul matching group
    fre = re.compile(r'(mul\(([0-9]+),([0-9]+)\))+')
    gen_mul = fre.finditer(line)
    list_mul = list(gen_mul)
    #breakpoint()
    res = [ int(x.group(2)) * int(x.group(3)) for x in list_mul ]
    #breakpoint()
    list_mul = [ x[0] for x in list_mul ]
    return sum(res), list_mul


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    res = part1('input')
    print(f'Result: {res}')
    dec = deduct()
    print(f'going to deduct: {dec}, Result: {res - dec}')
