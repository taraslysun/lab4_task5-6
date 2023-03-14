'''Module for game logic'''

class Street:
    '''Class to represent a room for player'''
    def __init__(self, street):
        '''
        Init method for Room class
        '''
        self.name = street
        self.description = None
        self.linked_streets = {}
        self.character = None
        self.item = None


    def set_description(self, description):
        '''
        Set description for street
        >>> street = Street('Krakivska')
        >>> street.set_description('You are in the street Krakivska')
        >>> street.description
        'You are in the street Krakivska'
        '''
        self.description = description

    def link_street(self, street, direction):
        '''
        Link street to another street
        '''
        self.linked_streets[direction] = street

    def get_details(self):
        '''
        Get details of street
        '''
        print(self.description)

    def get_character(self):
        '''
        Get character in street
        '''
        return self.character

    def set_character(self, character):
        '''
        Set character in street
        '''
        self.character = character

    def set_item(self, item):
        '''
        Set item in street
        '''
        self.item = item

    def get_item(self):
        '''
        Get item in street
        '''
        return self.item

    def move(self, direction):
        '''
        Move to another street
        '''
        if direction in self.linked_streets:
            return self.linked_streets[direction]
        return self

class Enemy:
    '''Class to represent an enemy'''
    defeated_enemies = 0
    def __init__(self, enemy, description):
        '''
        Init method for Enemy class
        '''
        self.name = enemy
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        '''
        Set conversation for enemy
        '''
        self.conversation = conversation

    def set_weakness(self, weakness):
        '''
        Set weakness for enemy
        '''
        self.weakness = weakness

    def describe(self):
        '''
        Describe enemy
        '''
        print(self.description)
        return self.description

    def talk(self):
        '''
        Talk to enemy
        '''
        if self.conversation is not None:
            print(self.conversation)
            return self.conversation
        return 'I will not talk to you'

    def fight(self, item):
        '''
        Fight with enemy
        '''
        if item == self.weakness:
            Enemy.defeated_enemies += 1
            return True
        return False

    def get_defeated(self):
        '''
        Get how many enemies player defeated
        '''
        return Enemy.defeated_enemies

class Item:
    '''Class to represent an item'''
    def __init__(self, item):
        '''
        Init method for Item class
        '''
        self.name = item
        self.description = None

    def set_description(self, description):
        '''
        Set description for item
        '''
        self.description = description

    def describe(self):
        '''
        Describe item
        '''
        print(self.description)
        return self.description

    def get_name(self):
        '''
        Get name of item
        '''
        return self.name

class Friend:
    '''Class to represent a friend of player'''
    def __init__(self, friend, description):
        '''
        Init method for Friend class
        '''
        self.name = friend
        self.description = description
        self.conversation = None

    def set_description(self, description):
        '''
        Set description for friend
        '''
        self.description = description

    def set_conversation(self, conversation):
        '''
        Set conversation for friend
        '''
        self.conversation = conversation

    def describe(self):
        '''
        Describe friend
        '''
        print(self.description)

    def fight(self, item):
        '''
        Fight with friend
        '''
        print('You cannot fight with your friend')

class Boss(Enemy):
    '''Class to represent a boss'''
    def __init__(self, boss, description):
        '''
        Init method for Boss class
        '''
        super().__init__(boss, description)
        self.defeated = False
        self.weakness = None

    def get_defeated(self):
        '''
        Set defeated for boss
        '''
        return self.defeated

    def set_weakness(self, weakness):
        '''
        Set weakness for boss
        '''
        self.weakness = weakness
