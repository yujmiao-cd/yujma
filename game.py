#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Hero(object):
    
    def __init__(self,name,attract,defender,weapon):
        self.name=name
        self.life=100
        self.is_live=True
        self.attract=3
        self.defender=2
        self.weapon=weapon
  
    def kill(self,mon):
        if not self.is_live:
            print "Sorry. you are dead."
            return
        if not mon.is_live:
            return 
        print(self.name+"sunzi,shousiba"+self.weapon+"chong"+mon.name)
        # 怪物受伤
        mon.hurt(self)
        # 反击
        mon.fight(self)
 
    def hurt(self,mon):
        base_lose = 5
        lose_life = mon.attract - self.defender
        if lose_life >= 0:
            self.life = lose_life + base_lose 
        else:
            self.life -= base_lose
        if self.life <= 0:
            print("tian du ying cai...")
            self.dead()
        self.show()
        
    def dead(self):
        self.is_live=False

    def show(self):
        print(self.name+'----'+str(self.is_live)+"---shengyu life--"+str(self.life))

class Monster():
    def __init__(self,name,weapon,type):
        if type == 1:
            self.life=20
            self.attract=1
            self.defender=1
        elif type == 2:
            self.life=50
            self.attract=2
            self.defender=2
        elif type == 3:
            self.life=80
            self.attract=3
            self.defender=2
        elif type == 4:
            self.life=100
            self.attract=10
            self.defender=1

        self.name=name
        self.is_live=True
        self.weapon = weapon
       
    def hurt(self,hero):
        base_lose = 5
        lose_life = hero.attract - self.defender
        if lose_life >= 0:
            self.life = lose_life + base_lose 
        else:
            self.life -= base_lose

        if self.life <= 0:
            print ("silasilasila......wo hai hui zai hui lai de ....")
            self.dead()

        self.show()
        
    def dead(self):
        self.is_live=False
 
    def fight(self,hero):
        print(self.name+"sunzi,shousiba"+self.weapon+"chong"+hero.name)
        if not hero.is_live:
            print "Sorry. you are dead."
            return
        if not hero.is_live:
            return 
        hero.hurt(self)
    
    def show(self):
        print(self.name+'----'+str(self.is_live)+"---shengyu life--"+str(self.life))

if __name__ == '__main__':
    m1 = Monster("路人甲","futou",type=1)
    m2 = Monster("路人甲","futou",type=1)
    m3 = Monster("路人甲","futou",type=1)
    h = Hero("huluwa",5,3,"huo")
    h.kill(m1)
    h.kill(m1)
    h.kill(m1)
    h.kill(m1)
    h.kill(m1)
    h.kill(m1)
