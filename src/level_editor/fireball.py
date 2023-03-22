import level_data
import sprite
import sprite_data


class Fireball(sprite.Sprite):

    def __init__(self,
                 lvl,
                 de,
                 s_index,
                 x,
                 y,

                 # Set initial direction of our fireball
                 xDir=0,
                 yDir=0,

                 i_lives=1):

        # Call the constructor of the parent class
        super(Fireball, self).__init__(lvl,
                                       de,
                                       s_index,
                                       x,
                                       y,
                                       i_lives)

        self.facingDirection = sprite_data.Vector()
        self.facingDirection.x = xDir
        self.facingDirection.y = yDir

        self.classID = sprite_data.Enum.FIREBALL_CLASSID

    def idleUpdate(self):
        """
        Fireball will move in the CORRECT direction.
        """

        # Check if we can move in that direction, meaning we did NOT hit a wall
        if (self.move(self.facingDirection.x, self.facingDirection.y)):

            # If we hit an enemy, they die
            for npc in level_data.NPC:

                # Make sure this classID of the NPC is NOT our classID.
                # i.e. if we are a fireball, we cannot shoot another fireball.
                if npc.classID != self.classID:
                    if npc.getX() == self.pos.x:
                        if npc.getY() == self.pos.y:

                            # Reduce the enemy life
                            npc.addLives(-1)

                            # Reduce our own (Fireball) life
                            self.addLives(-1)

        # If we are here, that means that the move method returned false which
        # means that the fireball hit a wall. Reduce the fireball's life.
        else:
            self.addLives(-1)
