from sys import argv

script, user_name = argv
prompt ='> '

print(f"Hi {user_name}, i'm ther {script} script.")
print("I'd like to ask you a fe questions")
print(f"do you like me {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me
you live in {lives}, Not sure where it is
and you have {computer} computer nice""")
