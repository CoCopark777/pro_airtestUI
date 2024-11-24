# 百位数不能为0的情况
count = 0
for i in [1, 8, 3]:  # 百位
    for j in [0, 1, 8, 3]:  # 十位
        if j!= i:
            for k in [0, 1, 8, 3]:  # 个位
                if k!= i and k!= j:
                    count += 1
                    print(str(i)+str(j)+str(k))
print("能组成", count, "个互不相同的三位数")


# 百位数能为0的情况
count = 0
for i in [0, 1, 8, 3]:  # 百位
    for j in [0, 1, 8, 3]:  # 十位
        if j!= i:
            for k in [0, 1, 8, 3]:  # 个位
                if k!= i and k!= j:
                    count += 1
                    print(str(i)+str(j)+str(k))
print("能组成", count, "个互不相同的三位数")


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}\t", end="")
    print()

#冒泡排序
def maopao(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

ab = [0,9,6,1,3,8]

print(maopao(ab))



