import animation

class MonsterBullet(animation.AnimateSprite):

    def __init__(self, monster):
        super().__init__('laser-bolts')

        self.monster = monster

        self.rect = self.image.get_rect()
        self.rect.center = [self.monster.rect.centerx, self.monster.rect.bottom]

        self.animation_images = [self.get_image(0, 0, 16), self.get_image(16, 0, 16)]


        self.velocity = 3
        self.scale = 1.5


    def remove(self):
        self.monster.all_bullets.remove(self)

    def move(self, screen):
        self.rect.y += self.velocity

        # check if projectile collide with the player
        for player in self.monster.game.check_collision(self, self.monster.game.all_players):
            self.remove()
            player.damage()

        # check if projectile is not in the screen
        if self.rect.y > screen.get_height():
            self.remove()
