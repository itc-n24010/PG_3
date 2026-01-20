import re

text = input("光の国からやってきた...？　>>")

#複数のパターンから選んでマッチする
ultra_regex = re.compile(r'^ウルトラ.*|^[uU][lL][tT][rR][aA]].*')
ul = ultra_regex.search(text)

if ul.group() != None:
    print(f"{ul.group()}参上！！")
else:
    print("そんなのいません！")