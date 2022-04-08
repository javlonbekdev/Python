#1-5savol
class Shaxs():
    shaxs_soni = 0
    def __init__(self,ism,fami,yosh, km):
        self.ism = ism
        self.fami = fami
        self.yosh = yosh
        self.__km = km
        Shaxs.shaxs_soni += 1
    def get_dis(self):
        return self.__km
    @classmethod
    def get_son(cls):
        return cls.shaxs_soni
    def get_info(self):
        return f"{self.ism} {self.fami} {self.yosh} yoshda "

shaxs1 = Shaxs('Javlonbek', 'Muhammad', 21, 5)
shaxs2 = Shaxs('Islomjon', 'Meliboyev', 24, 10)
print(shaxs1.get_son())