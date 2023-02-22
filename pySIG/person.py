from dao import DAO
class Person(DAO):
    def __init__(self,nom,age):
        super().__init__("person")
        self.setNom(nom)
        self.age = age
    
    