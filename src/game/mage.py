import character
import fireball
# import level
import level_data
import sprite_data


class Mage(character.Character):

    def __init__(self,
                 # Level
                 lvl,

                 # Draw Engine
                 de,

                 s_index,
                 x=1,
                 y=1,
                 lives=3,
                 spell_key=" ",
                 up_key="w",
                 down_key="s",
                 left_key="a",
                 right_key="d"):

        # Call the constructor of the parent class
        super(Mage, self).__init__(lvl,
                                   de,
                                   s_index,
                                   x,
                                   y,
                                   lives,
                                   up_key,
                                   down_key,
                                   left_key,
                                   right_key)

        # What key on the keyboard we have to press to shoot the spell
        self.spellKey = spell_key

        self.classID = sprite_data.Enum.MAGE_CLASSID

    def keyPress(self,
                 c):

        # Call parent class method
        val = super().keyPress(c)

        # if val == False:
        if val is False:
            if c == self.spellKey:
                self.castSpell()

                return True

        return val

    def castSpell(self):

        # Check to see if it is a valid space for the fireball
        # If not, quit method. Do not make a fireball
        result = self.isValidLevelMove(self.pos.x + self.facingDirection.x,
                                       self.pos.y + self.facingDirection.y)
        # if result == False:
        if result is False:
            return

        temp = fireball.Fireball(self.level,
                                 self.drawArea,
                                 level_data.Enum_Entity.SPRITE_FIREBALL,

                                 # Initial position for where the fireball
                                 # will be. It will START in front of the
                                 # character's facing direction
                                 self.pos.x + self.facingDirection.x,
                                 self.pos.y + self.facingDirection.y,

                                 # This sets the direction of our fireball
                                 self.facingDirection.x,
                                 self.facingDirection.y)

        # Draw it the first time
        temp.draw(temp.pos.x, temp.pos.y)

        self.level.addNPC(temp)
