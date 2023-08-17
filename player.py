import mesh_lib

class player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 11

        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

        self.rot_x = 0
        self.rot_y = 0
        self.rot_z = 0

        self.acc = .5
        self.spd = 0
        self.spd0 = 5
        self.frc = .1

        self.bound = 5

        self.mesh = mesh_lib.arwing(self.x, self.y, self.z)

    def update(self, pygame, key_state, delta_time):

        if key_state[pygame.K_w] and self.vel_y <= self.spd and (self.y + self.vel_y) <= self.bound:
            self.vel_y += self.acc

        if self.vel_y > 0:
            if self.vel_y <= self.frc:
                self.vel_y = 0

            else:
                self.vel_y -= self.frc

        if key_state[pygame.K_s] and self.vel_y >= -self.spd and self.y + self.vel_y >= -self.bound + 2:
            self.vel_y -= self.acc

        if self.vel_y < 0:
            if self.vel_y >= -self.frc:
                self.vel_y = 0
                
            else:
                self.vel_y += self.frc

        if key_state[pygame.K_d] and self.vel_x <= self.spd and self.x + self.vel_x <= self.bound:
            self.vel_x += self.acc

        if self.vel_x > 0:
            if self.vel_x <= self.frc:
                self.vel_x = 0

            else:
                self.vel_x -= self.frc

        if key_state[pygame.K_a] and self.vel_x >= -self.spd and self.x + self.vel_x >= -self.bound:
            self.vel_x -= self.acc

        if self.vel_x < 0:
            if self.vel_x >= -self.frc:
                self.vel_x = 0
                
            else:
                self.vel_x += self.frc

        if self.vel_x != 0 and self.vel_y != 0:
            self.spd = self.spd0/.71
            
        else:
            self.spd = self.spd0

        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

        self.rot_x = -self.vel_y * 2 * delta_time
        self.rot_y = self.vel_x * delta_time
        self.rot_z = -self.vel_x/2 * delta_time

        self.mesh.rot_x = self.rot_x * 2
        self.mesh.rot_y = self.rot_y * 2
        self.mesh.rot_z = self.rot_z * 2
        self.mesh.x = self.x
        self.mesh.y = self.y
        self.mesh.z = self.z
        self.mesh.update()

    def render(self):
        return self.mesh.render()