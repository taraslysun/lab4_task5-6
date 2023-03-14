'''Module for game logic'''

class Room:
    '''Class to represent a room for player'''
    def __init__(self, room):
        '''
        Init method for Room class
        '''
        self.name = room
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None


    def set_description(self, description):
        '''
        Set description for room
        >>> kitchen = Room('Kitchen')
        >>> kitchen.set_description('A dank and dirty room buzzing with flies.')
        '''
        self.description = description

    def link_room(self, room, direction):
        '''
        Link room to another room
        '''
        self.linked_rooms[direction] = room

    def get_details(self):
        '''
        Get details of room
        '''
        print(self.description)

    def get_character(self):
        '''
        Get character in room
        '''
        return self.character

    def set_character(self, character):
        '''
        Set character in room
        '''
        self.character = character

    def set_item(self, item):
        '''
        Set item in room
        '''
        self.item = item

    def get_item(self):
        '''
        Get item in room
        '''
        return self.item

    def move(self, direction):
        '''
        Move to another room
        '''
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
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
