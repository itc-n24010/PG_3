seiza = ['山羊座', '水瓶座', '魚座', '牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座']

keyword = ['I keep ...', 'I solve ...', 'I believe ...', 'I exist.',
           'I have ...', 'I choose ...', 'I sense ...', 'I will ...',
           'I analyze ...', 'I balance ...', 'I want ...', 'I experience ...']

month = int(input('あなたの誕生月を教えてね！'))
day = int(input('あなたの誕生日を教えてね！'))

seiza=month
for i in range(1,13):
    if month == 1 and day >= 20:
        seiza += 1
    elif month == 2 and day >= 19:
        seiza += 1
    elif month == 3 and day >= 21:
        seiza += 1
    elif month == 4 and day >= 22:
        seiza += 1
    elif month == 5 and day >= 23:
