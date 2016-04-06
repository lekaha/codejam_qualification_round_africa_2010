def find_two_sum(target, nums):
    check = {}
    for i,num in enumerate(nums):
        if num not in check:
            check[target-num]=i
        else:
            return [min(i,check[num]),max(i,check[num])]


def load_input(filename = None):
    if not filename:
        return
    line_buffer = None
    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer

import sys  

def main(argv):
    if not argv:
        return
    filename = argv[0]
    lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')
    print int(lines[0]) == (len(lines) - 1) * 3
    for i in xrange(int(lines[0])):
        target  = int(lines[i * 3 + 1])
        nums = map(int, lines[i * 3 + 3].split(' '))
        two_nums = find_two_sum(target, nums)
        s =  'Case #%d: %s\n'%(i+1, ' '.join(str(s + 1) for s in two_nums))
        f.writelines(s)
        print '%s'%s
    f.close()
    

if __name__ == '__main__':
    main(sys.argv[1:])