#冒泡排序
ls = [12, 15, 11, 16, 52, 84, 1, 7, 68, 58, 9, 66, 99, 8, 88]
def bubble_sort(ls):
    n = len(ls)
    print(n)
    for i in range(1,n):
        print('第{}轮的值为{}'.format(i, ls))
        status = 0
        for j in range(n-i):
            if ls[j]>ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                status = 1
        if status == 0:
            return ls
    return ls
a = bubble_sort(ls)
print(a)