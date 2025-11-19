import pygame
from fighter import Fighter

class Enemy(Fighter):

    def __init__(self, x, y,flip, character_name, actions, steps):
        super().__init__(x, y,flip, character_name, actions, steps)

        self.vision_range = 300       # kitni door tak player ko dekhega
        self.attack_range = 80        # kitni door tak attack karega
        self.speed = 2                # AI movement speed
        self.idle_timer = 0           # random movement ke liye

    # -----------------------------
    #     ENEMY AI MAIN FUNCTION
    # -----------------------------
    def update_ai(self, target):

        distance_x = target.rect.centerx - self.rect.centerx
        distance_y = target.rect.centery - self.rect.centery

        abs_dist = abs(distance_x)

        # -----------------------
        #  ENEMY PLAYER KO DEKHEGA
        # -----------------------
        if abs_dist < self.vision_range:  # player detect ho gaya

            # Face the player
            self.flip = distance_x < 0

            # -------------------
            #  ATTACK CONDITION
            # -------------------
            if abs_dist < self.attack_range:
                self.running = False
                self.attack_ai(target)
                return

            # -------------------
            #  MOVE TOWARD PLAYER
            # -------------------
            self.running = True

            if distance_x > 0:
                self.rect.x += self.speed     # right move
            else:
                self.rect.x -= self.speed     # left move

        else:
            # -----------------------
            #  IDLE / RANDOM MOVEMENT
            # -----------------------
            self.running = False
            self.random_idle_movement()

    # ------------------------------------
    #     ENEMY ATTACK (Auto Attack)
    # ------------------------------------
    def attack_ai(self, target):
        if not self.attacking:           # cool-down ke baad attack
            self.attacking = True
            self.frame = 0               # attack animation start se
            target.health -= 5

    # --------------------------
    #  RANDOM IDLE WALKING
    # --------------------------
    def random_idle_movement(self):

        self.idle_timer += 1

        if self.idle_timer > 120:  # 2 sec baad random direction change
            self.idle_timer = 0

            import random
            move = random.choice([-1, 0, 1])  # left, idle, right

            if move == -1:
                self.rect.x -= 1
                self.flip = True
                self.running = True
            elif move == 1:
                self.rect.x += 1
                self.flip = False
                self.running = True
            else:
                self.running = False
