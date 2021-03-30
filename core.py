import random

class Player:
    def __init__(self):
        self.HP = 20
        self.STR = 10
        self.AGI = 10
        self.DEF = 0
        self.ATK = 5
        self.aim = int(self.AGI / 4)
        self.dodge = int(self.AGI / 4)
        self.damage = self.ATK + int(self.STR / 4)
        self.Weapon = None
        self.Offhand = None
        self.Armour = None
    
    def is_dead(self):
        if self.HP <= 0:
            return True
        return False

    def trap_avoidance_stat(self):
        return self.AGI + self.DEF

    def take_damage(self, damage):
        applyed_damage = damage - self.Defence_type()
        self.HP -= applyed_damage
        print(f"you get hit for {applyed_damage}.")

    def hit_check(self, luck = random.randint(0, 20)):
        return luck + self.aim

    def Dodge_chance(self, luck = random.randint(0, 10)):
        return luck + self.dodge

    def Braced_hit(self, damage):
        damage_taken = (damage / 2) - self.Defence_type()
        if damage_taken >= 1:
            self.HP -= damage_taken
            print(f'You braced yourself and only took {damage_taken}.')
        else:
            print('The hit was ineffective')

    def Parry_check(self, luck = random.randint(0, 15)):
        chance = luck + int(Char.AGI / 2) + int(Char.STR / 2)
        return chance
    
    def Repose(self):
        return Char.damage + int(Char.STR / 2)

    def Attack_type(self):
        if self.Weapon == None:
            return self.Unarmed_attack()
        else: 
            return self.Armed_attack(self.Weapon)

    def Armed_attack(self, weapon):
        return self.ATK + int(self.STR / 4) + weapon.ATK
    
    def Unarmed_attack(self):
        return self.ATK + int(self.STR / 4)

    def Defence_type(self):
        if self.Armour == None and self.Offhand == None:
            return self.Unarmoured_defence()
        elif self.Armour and self.Offhand != None:
            return self.Unarmoured_defence_with_shield(self.Offhand)
        elif self.Offhand == None:
            return self.Armoured_defence_without_shield(self.Armour)
        else: 
            return self.Armoured_defence_with_shield(self.Armour, self.Offhand)
        
    def Armoured_defence_without_shield(self, Armour):
        return self.DEF + Armour.DEF

    def Armoured_defence_with_shield(self, Armour, shield):
        return self.DEF + Armour.DEF + shield.DEF

    def Unarmoured_defence(self):
        return self.DEF
    
    def Unarmoured_defence_with_shield(self, shield):
        return self.DEF + shield.DEF

Char = Player()

class Event:
    #print("not working correctly")
    def __init__(self, room = random.randint(0,4)):
        self.room = room
    def Create_room(self):
        if self.room == 0:
            Trap()
            return False
        if self.room == 1:
            Loot()
            return False
        if self.room == 2:
            Fight()
            return False
        if self.room == 3:
            Empty()
            return False
        if self.room == 4:
            return Exit()

def Item_factory(item = random.randint(0,5)):
    if item == 0:
        return Dagger()
    if item == 1:
        return Shield()
    if item == 2:
        return Leathor_armour()
    if item == 3:
        return Axe()
    if item == 4:
        return Sword()
    if item == 5:
        return Iron_armour()

class Object:
    def pick_up(self):
        if self.catigory == 'Weapon':
            Char.Weapon = self
            print(f'You pick up the {self.name}.')
        elif self.catigory == 'Offhand':
            Char.Offhand = self
            print(f'You pick up the {self.name}.')
        elif self.catigory == 'Armour':
            Char.Armour = self
            print(f'You put on the {self.name}.')


class Dagger(Object):
    def __init__(self):
        self.ATK = 2
        self.name = 'Dagger'
        self.catigory = 'Weapon'
    #super().pick_up(self)

class Shield(Object):
    def __init__(self):
        self.DEF = 5
        self.name = 'Shield'
        self.catigory = 'Offhand'
    #super().pick_up(self)

class Leathor_armour(Object):
    def __init__(self):
        self.DEF = 2
        self.name = 'Leathor Armour'
        self.catigory = 'Armour'
    #super().pick_up(self)

class Sword(Object):
    def __init__(self):
        self.ATK = 5
        self.name = 'Sword'
        self.catigory = 'Weapon'
    #super().pick_up(self)

class Iron_armour(Object):
    def __init__(self):
        self.DEF = 5
        self.name = 'Iron Armour'
        self.catigory = 'Armour'
    #super().pick_up(self)

class Axe(Object):
    def __init__(self):
        self.ATK = 10
        self.name = 'Axe'
        self.catigory = 'Weapon'
    #super().pick_up(self)

class Monster:
    def __init__(self):
        self.HP = 10
        self.STR = 2
        self.AGI = 3
        self.DEF = 0
        self.ATK = 3
        self.dodge = int(self.AGI / 4)
        self.aim = int(self.AGI / 4)
        self.damage = self.ATK + int(self.STR / 4)

    def Dodge_chance(self, luck = random.randint(0,10)):
        return luck + self.dodge
    
    def hit_check(self, luck = random.randint(0,20)):
        return luck + self.aim

    def take_damage(self, damage):
        applyed_damage = damage - self.DEF
        print(f"You hit the {self.name} for {applyed_damage} damage.")
        self.HP -= applyed_damage

    def is_dead(self):
        if self.HP <= 0:
            return True
        return False

def Trap():
    print('You set off a trap.')
    Char.take_damage(15 - Char.trap_avoidance_stat())

def Fight():
    win = False
    lose = False
    OPT = Monster_factory(random.randint(0,4))
    print("You come across a {name}.".format(name = OPT.name))
    while win == False and lose == False:
        print("You can, Attack, Brace, or Parry")
        x = input()
        if x == "Attack":
            Attack(OPT)
        elif x == "Brace":
            Brace(OPT)
        elif x == "Parry":
            Parry(OPT)
        else:
            print("Please enter a valid response.")
        if OPT.is_dead():
            win = True
        if Char.is_dead():
            lose = True
    if win == True:
        Win_fight(OPT)

def Loot():
    item = Item_factory(random.randint(0,5))
    print(f"you come across a {item.name} do you pick it up?")
    decition = input()
    if decition == "yes":
        item.pick_up()
    elif decition == "no":
        print("you continue in the dungen")
    else:
        print("Please enter a valid responce.")

def Empty():
    print("You come across on empty room and get some much needed rest. \n you recover 5 HP")
    Char.HP += 5

def Exit():
    return True

def Game():
    end = False
    l = False
    c = 0
    while not end:
        events = Event(random.randint(0,3))
        if events.Create_room():
            end = True
            break
        c += 1
        if Char.is_dead():
            Lose_game()
        if reached_end_of_dungeon(c):
            Win_game()
 
def reached_end_of_dungeon(c):
    if c > 100:
        return True
    return False

def Win_game():
    print("You have come across a starway leading up to the surface, now you only need to find the way back home.")
    exit()

def Lose_game():
    print("Your life ends. better luck next time")
    exit()

def Attack(OPT):
    if Char.hit_check() >= OPT.Dodge_chance():
        OPT.take_damage(Char.Attack_type())
    else:
        print(f"you missed the {OPT.name}.")
    if OPT.hit_check() >= Char.Dodge_chance():
        Char.take_damage(OPT.damage)
    else:
        print(f"The {OPT.name} missed.")

def Win_fight(OPT):
    print(f"you kill the {OPT.name} and contine in the dungen.")

def Brace(OPT):
    if OPT.hit_check() >= Char.Dodge_chance():
        Char.Braced_hit(OPT.damage)
    else:
        print(f"The {OPT.name} missed.")

def Parry(OPT):
    if Char.Parry_check() >= OPT.hit_check():
        OPT.take_damage(Char.Repose())
    else:
        Char.take_damage(OPT.damage)

def Monster_factory(type_of_monster = random.randint(0,4)):
    if type_of_monster == 0:
        return Goblin()
    if type_of_monster == 1:
        return Slime()
    if type_of_monster == 2:
        return Spider()
    if type_of_monster == 3:
        return Skeleton()
    if type_of_monster == 4:
        return Wolf()

class Goblin(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin'
        self.AGI = 5

class Slime(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'Slime'
        self.AGI = 0
        self.HP = 15

class Spider(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'Spider'
        self.AGI = 9

class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'Skeleton'
        self.ATK = 5
        self.DEF = 3

class Wolf(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'Wolf'
        self.AGI = 5
        self.ATK = 5

test_monster = Monster_factory()
#print(test_monster.DEF)
#
#test_item = Item_factory()
#print(test_item.name)
#test_item.pick_up()

if __name__ == '__main__':
    Game()
