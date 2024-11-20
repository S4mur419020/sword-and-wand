from Jatekos import Jatekos
class Jatekter:
    def __init__(self):
        self.warrior=Jatekos("Nobunaga",0,"Sword Saint","🥋")
        self.mage=Jatekos("Gandalf",2,"Great Mage","🧙‍♀️")
        self.lista=["_","_","_"]
        self.lista[self.warrior.poz]=self.warrior.emo
        self.lista[self.mage.poz]=self.mage.emo
        self.kor=1
        self.kiir()


    def kiir(self):
        print(f"{self.kor}. kör")
        print(f"*"*15, "   ","-"*27,"","-"*27, "  ")
        print(f"* {self.lista[0]:<3}  {self.lista[1]:^3}  {self.lista[2]:>3} *  | A {self.warrior.nev} életereje: {self.warrior.hp} |  | A {self.mage.nev} életereje: {self.mage.hp} |")
        print(f"*"*15, "   ","-"*27,"","-"*27, "  ")
        print("")
    


    def jatekmenet(self):
        while(self.warrior.hp>0 and self.mage.hp>0):
            self.warrior.set_pozicio()
            self.mage.set_pozicio()
            self.lista=["_","_","_"]
            self.lista[self.warrior.poz]=self.warrior.emo
            self.lista[self.mage.poz]=self.mage.emo
            if(self.warrior.poz==self.mage.poz):
                self.lista[self.mage.poz]="X"
                self.warrior.set_hp()
                self.mage.set_hp()  
            self.kor+=1
            self.kiir()
            input()
