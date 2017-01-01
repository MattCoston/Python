import ctypes

print("Hello World")
years = int(input("What is your age? "))

age5 = years + 5
print("You will be" , age5 , "in 5 years!\n")
age_days = age5*365
print("In 5 years you will have lived", age_days, "days!")

def SHOUT():
	print("NICE DAY TO DIE!")
	print("Just messing with you!  I am sure you will have a long life!")

SHOUT()

age_5 = "You will be " + str(age5)
def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('AGE', age_5, 0)
