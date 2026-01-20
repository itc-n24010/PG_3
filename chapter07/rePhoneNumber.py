import re

text = "明日098-862-5437に電話してください。オフィスは(098)855-5437です。"

phone_number_regex = re.compile(r'(\d{3}-\d{3}-\d{4})')
mo = phone_number_regex.search(text)
print(f"電話番号が見つかりました:{mo.group()}")

phone_number_regex = re.compile(r'(\(\d{3}\)\d{3}-\d{4})')
mo = phone_number_regex.search(text)
print(f"電話番号が見つかりました:{mo.group()}")