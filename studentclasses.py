class students:
    def __init__(self,name,age,nationality,hair_color):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.hair_color = hair_color
    def birthyear(self):
        birthyear = 2024-self.age
        #print('The birthyear of '+str(self.name)+' is '+str(birthyear))
        return birthyear




Jessica = students("Jessica",12,'Canadian','ginger')
Jack = students('Jack',14,'American','black')
print(Jack.birthyear())
print(Jessica.birthyear())
#birthyear(Jessica)