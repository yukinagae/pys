#!/usr/bin/env python
import sys

# config map
ms = {"M01":2, "M02":5}

def may(step, pair):
    if pair[0] == '':
        return ''
    elif pair[1] != '':
        return pair[1]
    else:
        return str(int(pair[0]) + step)

def cal(step, lis):
    curried_may = lambda x: lambda y: may(x, y)
    return lis[:1] + map(curried_may(step), zip(lis[:-1], lis[1:]))

# read file
inf = open(sys.argv[1])
lines2 = inf.readlines()
lines = lines2[1::]
inf.close()

# append value
result = []
for line in lines:
    l = line.replace('\n', '').split(',')
    m = l[1]
    step = ms[m] if ms.has_key(m) else 1
    r = cal(step, l[2:6])
    result.append(','.join(l[0:2] + r) + '\n')

# write file
outf = open(sys.argv[2], 'w')
header = "#,a,b,c,d,e\n"
result.insert(0, header)
outf.writelines(result)
outf.close()
