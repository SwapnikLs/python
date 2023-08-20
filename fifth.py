Email=input("What is your email address?: ").strip()
user_name=Email[:Email.index("@")]
domain=Email[Email.index("@")+1:]
output="your username is {} and your domain is {}".format(user_name,domain)
print(output)

