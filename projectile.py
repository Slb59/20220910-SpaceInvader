import animation

class Projectile(animation.AnimateSprite):

    def __init__(self, player):
        super().__init__('laser-bolts')

        self.player = player

        self.rect = self.image.get_rect()
        self.rect.center = [self.player.rect.centerx, self.player.rect.top ]

        self.animation_images = [self.get_image(0, 16), self.get_image(16, 16)]


        self.velocity = 3
        self.scale = 2



    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        # check if projectile is not in the screen
        if self.rect.y < 0:
            self.remove()

        # check if projectile collide a monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage()


