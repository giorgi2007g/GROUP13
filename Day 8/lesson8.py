#  მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, 
#  თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე მაგ შემთხვევაში დაპრინტეთ,თქვენ დაგიფინანსდებათ სწავლა.
# თუ მიღებული ქულა მეტია 70 - ზე და  ნაკლებია 80 - ზე მაგ შემთხვევაში
#  დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული 
# ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე მაგ შემთხვევაში დაპრინტეთ,თქვენ დაგიფინანსდებათ სწავლა 500 
# ლარტით,ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე,მაგ შემტხვევაში დაპრინტეთ, 
# ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი


# Request user input and convert it to an integer
score = int(input("testshi migebuli qula?: "))

if score > 90 and score < 100:
    print("tqven srulad dagipinansebt swavlas")

elif score > 70 and score < 90:
    print("swavla dagipinansdebat 1500 larit")

elif score > 40 and score < 70:
    print("swavla dagipinansdebat 500 larit")

elif score > 0 and score < 40:
    print("ar dagipinansdebat")

else:
    print("araswori qula")