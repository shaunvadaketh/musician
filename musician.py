class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bam", "Tsk", "BOOM"])
    
    def count(self):
        print("One, Two, Three, Four!")

class Band(object):
    def __init__(self, members):
        self.members = members
    
    def fire_member(self, member):
        self.members.remove(member)
        print ("Now your band consists of:{1} ".format(self.members))


if __name__ == '__main__':
    
    bassist = Bassist()
    guitarist = Guitarist()
    drummer = Drummer()
    
    band = Band([bassist, guitarist, drummer])
    
    
    