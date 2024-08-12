user_input = input("do you want boolean ? ")
print(f"you enterd: {user_input} of type {type(user_input)}")

user_answer = user_input.lower() == "true"
user_answer = user_input.lower() == 'false'

print(f"the boolean value of your answer is: {user_answer}")