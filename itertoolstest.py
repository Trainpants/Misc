import itertools

a = ["1","2","3"]
c = itertools.product(a,repeat=2)
b = itertools.product(range(3,10),repeat=3)
for i in c:
    string = "".join(i)
    print(string)

#returns:
#('A', 'A')
#('A', 'B')
#('A', 'C')
#('B', 'A')
#('B', 'B')
#('B', 'C')
#('C', 'A')
#('C', 'B')
#('C', 'C')