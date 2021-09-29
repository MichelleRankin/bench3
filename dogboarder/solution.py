class DogBoarder:
    def __init__(self, total_slots, daily_rate):
        self.total_slots = total_slots
        self.daily_rate = daily_rate
        self.dogs = []


    def board(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        self.dogs.append 
        self.slots_occupied += slots_occupied
        



    def dog_in_list(self, name, breed, owner):
            for dog in self.dogs:
                if self.name == name and self.breed == breed and self.owner == owner:
                    return True
                
    def pick_up(self, name, breed, owner):
            if self.dog_in_list() == True:
                for dog in self.dogs:
                    if self.name == name and self.breed == breed and self.owner == owner:
                        self.dogs.remove(dog)
                        self.slots_occupied - 1
            else:
                raise(ValueError)


    def slots_occupied(self):
        if self.slots_occupied == self.total_slots:
            return True
        return False

    def is_full(self):
        if self.slots_occupied() == self.total_slots:
            return True
        return False


class dog(DogBoarder):
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    
