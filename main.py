
email = input("Enter you email:")

username = email[:email.index("@")]
domain = email[email.index("@"): + 1:]

print(f"your username is {username} and your domain  is{domain}")