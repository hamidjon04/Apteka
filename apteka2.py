class Dori:
    def __init__(self, bolim, name, srok, narx):
        self.bolim = bolim
        self.name = name
        self.srok = srok
        self.narx = narx


class Apteka:
    def __init__(self):
        self.dorilar = dict()
        self.__summa = 1000000
        self.nomi = "Najot Pharm"
        self.location = "Chilonzor"
        self.tel = +998777075544


    def add(self, dori:Dori, miqdor):
        if dori.srok.split(".")[1] > "2024":
            if dori.bolim not in self.dorilar:
                self.dorilar[dori.bolim] = dict()
                self.dorilar[dori.bolim][dori.name] = dict()
                self.dorilar[dori.bolim][dori.name]["srok"] = dori.srok
                self.dorilar[dori.bolim][dori.name]["narx"] = dori.narx
                self.dorilar[dori.bolim][dori.name]["miqdor"] = miqdor
            elif dori.bolim in self.dorilar and dori.name not in self.dorilar[dori.bolim]:
                self.dorilar[dori.bolim][dori.name] = dict()
                self.dorilar[dori.bolim][dori.name]["srok"] = dori.srok
                self.dorilar[dori.bolim][dori.name]["narx"] = dori.narx
                self.dorilar[dori.bolim][dori.name]["miqdor"] = miqdor
            else: 
                self.dorilar[dori.bolim][dori.name]["miqdor"] += miqdor
        else:
            print(f"{dori.name} dorining muddati tugagan!!!")

    def sotmoq(self, dori_name, miqdor):
        sotildi = 0
        for i in self.dorilar:
            if dori_name in self.dorilar[i]:
                if miqdor <= self.dorilar[i][dori_name]["miqdor"]:
                    self.dorilar[i][dori_name]["miqdor"] -= miqdor
                    self.__summa += miqdor * self.dorilar[i][dori_name]["narx"]
                    sotildi = 2
                else:
                    sotildi = 1
                break
        if sotildi == 0:
            print("Bizda bu dori mavjud emas!")
        elif sotildi == 1:
            print(f"Siz so'ragan miqdorda dorimiz mavjud emas. {self.dorilar[i][dori_name]["miqdor"]} ta mavjud.")
        elif sotildi == 2:
            print("Xaridingiz uchun tashakkur.")
        
        

    def delete(self, dori_name):
        for i in self.dorilar:
            if dori_name in self.dorilar[i]:
                self.dorilar[i][dori_name]["srok"] = "00.0000"
                self.dorilar[i][dori_name]["miqdor"] = 0

    def getSum(self):
        return self.__summa

    def setSum(self):
        sum = int(input("Summa: "))
        if self.__summa >= sum:
            self.__summa -= sum
            return sum
        else:
            return "Aptekada siz so'ragan pul mablag'i mavjud emas!"
        

    def infoApteka(self):
        return f"""
Apteka: {self.nomi}
Location: {self.location}
Tel: {self.tel}"""


    def infoDorilar(self):
        for i in self.dorilar:
            print(i)
            for dori in self.dorilar[i]:
                print(f"{dori} => {self.dorilar[i][dori]}")

d1 = Dori("og'riq", "Tremol", "10.2027", 5000)
d2 = Dori("ukol", "Glyukoza", "10.2026", 7000)
d3 = Dori("vitamen", "Askarbinka", "07.2029", 1000)
d4 = Dori("og'riq", "Setramon", "05.2024", 2000)
d5 = Dori("vitamen", "poliz", "10.2020", 4000)
apteka = Apteka()
apteka.infoApteka()
apteka.add(d1, 10)
apteka.add(d1, 15)
apteka.add(d2, 20)
apteka.add(d4, 20)
apteka.add(d3, 10)
apteka.add(d5, 100)
apteka.infoDorilar()
apteka.sotmoq("Tremol", 10)
apteka.delete("Askarbinka")
apteka.infoDorilar()
print(apteka.getSum())
print(apteka.setSum())
print(apteka.getSum())

