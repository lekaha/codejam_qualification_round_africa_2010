def reverse_words(words):
    rwords = []
    for s in reversed(words):
        rwords.append(s)
    return rwords

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
        words = map(str, lines[i + 1].split(' '))
        r_words = reverse_words(words)
        s =  'Case #%d: %s\n'%(i+1, ' '.join(s for s in r_words))
        f.writelines(s)
        print '%s'%s
    f.close()
    

if __name__ == '__main__':
    main(sys.argv[1:])