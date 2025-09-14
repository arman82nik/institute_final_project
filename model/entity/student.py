class Student:
    def __init__(self,id,person_id,name,family,birthday,email,gender):
        self.id = id
        self.person_id = person_id
        self.name = name
        self.family = family
        self.birthday = birthday
        self.email = email
        self.gender = gender

    def __repr__(self):
        return f"{self.__dict__}"


    def to_tuple(self):
        return tuple([self.id,self.name,self.family,self.birthday,self.email,self.gender])


