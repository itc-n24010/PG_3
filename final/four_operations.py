ichi = int(input("1つ目の整数を入力してください>>"))
ni = int(input("2つ目の整数を入力してください>>"))

print("和：", ichi + ni)
print("差：", ichi - ni)
print("積：", ichi * ni)
if ni > 0:
    print("商：", ichi // ni)
    print("剰余：", ichi % ni)
else:
    pass