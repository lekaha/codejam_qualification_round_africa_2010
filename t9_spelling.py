tp_dict = {
    'a':'2', 'b':'22', 'c':'222',
    'd':'3', 'e':'33', 'f':'333',
    'g':'4', 'h':'44', 'i':'444',
    'j':'5', 'k':'55', 'l':'555',
    'm':'6', 'n':'66', 'o':'666',
    'p':'7', 'q':'77', 'r':'777', 's':'7777',
    't':'8', 'u':'88', 'v':'888',
    'w':'9', 'x':'99', 'y':'999', 'z':'9999',
    ' ':'0'
}

def t9(input_str):
    last = None
    output = ''
    for c in input_str:
        if last and tp_dict[c][0] == tp_dict[last][0]:
            output += ' '
        output += tp_dict[c]
        last = c
    return output


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
    print int(lines[0]) == (len(lines) - 1)
    for i in xrange(int(lines[0])):
        types = t9(lines[i + 1])
        s =  'Case #%d: %s\n'%(i+1, types)
        f.writelines(s)
        print '%s'%s
    f.close()
    

if __name__ == '__main__':
    main(sys.argv[1:])


