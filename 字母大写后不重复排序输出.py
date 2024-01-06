string = input("请输入一个英文字符串: ")  # 获取输入字符串

# 初始化字母列表
letters = []

# 遍历输入字符串
for i in string:
    if i.isalpha() and i.upper() not in letters:  # 如果当前字符是字母且未出现在列表中
        letters.append(i.upper())  # 将大写字母加入列表

# 使用sorted函数对列表进行升序排序
sorted_letters = sorted(letters)

print(sorted_letters)  # 输出排序后的列表
