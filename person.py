import random

class person:
 
    def __init__(self, names):
        # Select a random name
        self.name = random.choice(names)
 
        # Set information of the person by name
        self.age = random.randint(1, 95)
        self.skill_level = random.randint(1, 10)
        self.winning_count = random.randint(0, 20)
 
    def getName(self):
        return self.name
 
    def setName(self, name):
        self.name = name
 
    def getAge(self):
        return self.age
   
    def setAge(self, age):
        self.age = age
   
    def getSkillLevel(self):
        return self.skill_level
   
    def setSkillLevel(self, skillLevel):
        if (skillLevel > 10  or skillLevel < 1):
            print("Error en el nivel de habilidad")
        else:
            self.skill_level = skillLevel
   
    def getWinningCount(self):
        return self.winning_count
   
    def setWinningCount(self, winning_count):
        self.winning_count = winning_count
 
    def add_skill(self, skill):
        self.skill_level += skill
   
    def add_winning(self):
        self.winning_count += 1
   
    def play_against(self, opponent):
        skillLevelDifference = abs(self.getSkillLevel() - opponent.getSkillLevel())
        players = [self.name, opponent.getName()]

        if (skillLevelDifference <= 2):
            probabilities = [0.5, 0.5]
        
        elif (skillLevelDifference > 2 and skillLevelDifference <= 4):
            if (self.getSkillLevel() > opponent.getSkillLevel()):
                probabilities = [0.75, 0.25]
            else:
                probabilities = [0.25, 0.75]

        else:
            if (self.getSkillLevel() > opponent.getSkillLevel()):
                probabilities = [1.0, 0.0]
            else:
                probabilities = [1.0, 0.0]
        
        winner = random.choices(players, probabilities)
        
        if (self.name == winner):
                self.setWinningCount(self.getWinningCount() + 1)
                self.setSkillLevel(self.getSkillLevel() + 1)
        else:
            opponent.setWinningCount(self.getWinningCount() + 1)
            opponent.setSkillLevel(self.getSkillLevel() + 1)
                
def main():
    print("Write 10 different names separated by space")
    names = input().split(" ")
    
    # Create list of 10 people
    people = []
    for i in range(10):
        people.append(person(names[i]))
    
    # Play ->  20 iterations
    for i in range(20):
        # Select player 1 and 2
        players = random.sample(people, 2)
        players[0].play_against(players[1])
    
    # Results
    for player in people:
        print(player.getName(), player.getAge(), player.getSkillLevel(), player.getWinningCount())

main()