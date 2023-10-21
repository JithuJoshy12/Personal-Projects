import random
import time

print('welcome to Jithus Fortune Teller \n')

question = input('Would you like to know your future? \n')
color = input('pick a color')
print('your color choice is important as I will chose your future based on it', color)
time.sleep(2)

fortune =['You Will Be Single For The Rest Of Your Life', 'You Will Die By Cancer When You Reach 30', 'You Will Be Homeless And Unloved'
, 'You Will Be Married To A Model!', 'The Boogie Monster Will Eat You At your Wedding']
print(random.choice(fortune))