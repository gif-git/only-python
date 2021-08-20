user_name = input("Please type your name ? ")
pwd = input("Please type you password ? ")

t = ('*' * len(pwd))

print(f"Hi {user_name}, your password is {t} and it\'s {len(pwd)} letters long")
