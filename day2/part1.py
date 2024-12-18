import copy

def read_file(filename):
    res = []
    with open(filename, mode='r') as f:
        lines = f.readlines()
        res.extend(lines)
    return res

def check_gen_tolerate(ls, f):
    # get the unsafe value
    res_ls = [ f(*i) for i in zip(ls, ls[1:]) ]

    # If count of False is 1 or less than ok
    tolerate = res_ls.count(False)
    
    if tolerate == 1:
        tmp = brute_force(ls, f)
        return tmp

    if tolerate == 0:
        return True

    return False

def check_gen(ls, f):
    # get the unsafe value
    return all(f(*i) for i in zip(ls, ls[1:]))

def brute_force(ls, f):
    # try remove each level
    for _, i in enumerate(ls): 
        tmp_ls = copy.copy(ls)
        tmp_ls = tmp_ls[:i] + tmp_ls[i+1:]
        res = check_gen(tmp_ls,f)
        if res:
            print(tmp_ls)
            return True

    return False
    

def check_monotonicity(ls):
    # increase
    increasing = all(x<y for x, y in zip(ls, ls[1:]))
    # decrease
    decreasing = all(x>y for x, y in zip(ls, ls[1:]))
    monotonic = increasing or decreasing
    return monotonic

def check_relative_diff(ls):
    # all diff by 
    relative_diff = all(abs(x-y) <= 3 and abs(x-y) >= 1 for x, y in zip(ls, ls[1:]))
    return relative_diff
    

def part1(filename):
    res = 0
    with open(filename, mode='r') as f:
        lines = f.readlines()
        for l in lines:
            monotonic, diff = 0, 0
            tmp_ls = l.strip("\n").split(" ")
            my_ls = list(map(int, tmp_ls))
            monotonic = check_monotonicity(my_ls)
            diff = check_relative_diff(my_ls)

            if monotonic and diff:
                #print(my_ls)
                res += 1

    return res


def part2(filename):
    res = 0
    inc_f = lambda x, y: x < y
    dec_f = lambda x, y: x > y
    diff_f = lambda x, y: abs(x-y) <= 3 and abs(x-y) >= 1
    with open(filename, mode='r') as f:
        lines = f.readlines()
        for l in lines:
            mono, diff = 0, 0
            tmp_ls = l.strip("\n").split(" ")
            my_ls = list(map(int, tmp_ls))
            inc = check_gen(my_ls, inc_f)
            dec = check_gen(my_ls, dec_f)
            diff = check_gen(my_ls, diff_f)

            mono = inc or dec

            if mono and diff:
                #print(my_ls)
                res += 1
            elif mono:
                # check


    return res

if __name__ == '__main__':
    level = part1('input')
    print(f'Part1: {level}')
    tolerate = part2('input')
    print(f'Part2: {tolerate}')
