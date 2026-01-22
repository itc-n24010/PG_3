#あいさつに関する情報
def aisatsu(name, jikantai):
    if jikantai == 1:
        print(f"{name}さん、おはようございます!")
    elif jikantai == 2:
        print(f"{name}さん、こんにちは!")
    elif jikantai == 3:
        print(f"{name}さん、こんばんは!")
    else:
        print(f"{name}さん、おやすみなさい...")

#プログラム実行
name = input("名前をここに入力して下さい >>")
print("朝：1 昼：2 晩：3 寝る前：4")
jikan = int(input("時間帯を入力してください >>"))
aisatsu(name,jikan)