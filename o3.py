import random

class Player():
    
    score = 0

    def __init__(self, name, shoot_rate, num):
        self.name = name
        self.shoot_rate = shoot_rate
        self.num = num
        self.score = Player.score
        print(self.name + "'s shoot rate is " + str(self.shoot_rate) + '%' + '. He shoot ' + str(self.num) + ' times.')
        print()
        for i in range(0, self.num):
            print(self.name + ' shoot ' + str(i+1) + ' times')
            i += 1
            a = random.randint(0,100)
            if a <= self.shoot_rate:
                self.score = self.score + 2
                print("He got it!")
                print(self.name + " now scores " + str(self.score) + ' points.')
            else:
                print("He lost it!")
            print()

    
Curry = Player('Curry', 80, 10)
print('**************************************************')
Thompson = Player('Thompson', 50, 12)
print('**************************************************')
print('Curry finally scores '+ str(Curry.score) + ' points.')
print('**************************************************')
print('Thompson finally scores  '+ str(Thompson.score) + ' points.')

