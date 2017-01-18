number = input()
out = []
PAT = 'PAT'
for j in xrange(number):
    inputs = raw_input()
    pat = list(set(inputs))
    index = [PAT.find(i) for i in pat]
    index_P, index_T = inputs.find('P'), inputs.find('T')
    if sum(index) is not 3 or index_T-index_P < 0:
        out.append('NO')
    elif inputs.count('P') == 1 and inputs.count('T') == 1:
        pat_P = inputs.split('P')
        pat_T = pat_P[1].split('T')
        a, b, c = pat_P[0], pat_T[0], pat_T[1]
        if b == '':
            out.append('NO')
        else:
            while b != 'A':
                b = b[:-1]
                c = c[len(a):]
            if a == c:
                out.append('YES')
            else:
                out.append('NO')
    else:
        out.append('NO')
for i in out:
    print i

