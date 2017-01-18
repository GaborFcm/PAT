# PAT test
# 1002
c = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
a = raw_input()
b = sum(map(int, a))
d = map(int, str(b))
for i in d:
    print c[i],
