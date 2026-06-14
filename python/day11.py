# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()
"""表示不换行 第一波的时候用end=让*号连在一起形成*****
第二波再用print本身默认不换行 打印5次字符串"""      


for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()
    """九九乘法表"""