def test(a):
    del a[3]


a = [1,2,3,4,5,6,7,]
print(a)
test(a)
print(a)
