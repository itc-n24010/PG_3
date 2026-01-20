# 数当てゲーム
import random
secret_number = random.randint(1, 20)
print('1から10までの数を当ててください。')
score = 5
game = 1

while True:
    print(f'*** GAME{game} ***')
    secret_number = random.randint(1, 10)
    #10回開く
    for guesses_taken in range(1, 11):
        guess = int(input("数を入力してください(0は終了)->"))
        if guess == 0:
            break
        if guess < secret_number:
            print('あなたの推定値は小さいです。')
            score -= 1
        elif guess > secret_number:
            print('あなたの推定値は大きいです。')
            score -= 1
        else:
            print("なんと！正解です！")
            score += 10
            game += 1
            break

    print(f'正解は{secret_number}でした！')
    print(f'得点は{score}でした！')