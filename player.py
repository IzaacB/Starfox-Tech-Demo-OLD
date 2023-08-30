import mesh
import copy
import math

class player:
    def __init__(self):
        self.pos = [0, 0, 10]#Initalize player position in 3D space.
        self.rot = [0, 0, 0]#Initialize player local rotation.
        self.glo = [0, 0, 0]#Iniitailize player global rotation in 3D space.

        #Physics controls/settings for the player.
        self.vel = [0, 0, 0]
        self.acc = .15
        self.frc = .05
        self.spd = 3
        self.spd0 = 3
        self.lev = 0

        #Player bounds, make it so the player cannot travel past a certain point.
        self.bnd_t = 4
        self.bnd_b = -4
        self.bnd_l = -5
        self.bnd_r = 5
        
        #Setup the bullet system for the player.
        self.blt_cache = []
        self.blt_timer = 0
        self.blt_timer_max = .2
        self.blt_spd = 500

        #Render settings for the player, and a render pipline to add to main.
        self.mesh = mesh.arwing(self.pos[0], self.pos[1], self.pos[2])
        self.rnd = []

    def update(self, pygame, key_state, delta_time):
        self.rnd = []

        #Physics based movement.
        if self.pos[1] + self.vel[1] <= self.bnd_t:
            if key_state[pygame.K_s] and self.vel[1] <= self.spd:
                self.vel[1] += self.acc 

            if self.vel[1] > 0:
                if self.vel[1] <= self.frc:
                    self.vel[1] = 0

                else:
                    self.vel[1] -= self.frc
        else:
            self.vel[1] -= self.frc

        if self.pos[1] + self.vel[1] >= self.bnd_b:
            if key_state[pygame.K_w] and self.vel[1] >= -self.spd:
                self.vel[1] -= self.acc

            if self.vel[1] < 0:
                if self.vel[1] >= -self.frc:
                    self.vel[1] = 0
                    
                else:
                    self.vel[1] += self.frc
        
        else:
            self.vel[1] += self.frc

        if self.pos[0] + self.vel[0] <= self.bnd_r:
            if key_state[pygame.K_d] and self.vel[0] <= self.spd:
                self.vel[0] += self.acc

            if self.vel[0] > 0:
                if self.vel[0] <= self.frc:
                    self.vel[0] = 0

                else:
                    self.vel[0] -= self.frc
                
        else:
            self.vel[0] -= self.frc

        if self.pos[0] + self.vel[0] >= self.bnd_l:
            if key_state[pygame.K_a] and self.vel[0] >= -self.spd:
                self.vel[0] -= self.acc

            if self.vel[0] < 0:
                if self.vel[0] >= -self.frc:
                    self.vel[0] = 0
                    
                else:
                    self.vel[0] += self.frc

        else:
            self.vel[0] += self.frc

        #End of movement section.

        if key_state[pygame.K_DOWN] and self.blt_timer <= 0:
            #Add the bullet settings based on the current player position, local, and global rotation.
            self.blt_rot = copy.deepcopy(self.rot)
            self.blt_pos = copy.deepcopy(self.mesh.upd_verts[0])
            self.blt_glo = copy.deepcopy(self.glo)

            #Add the data to the bullet entity list, and reset the bullet timer.
            self.blt_cache.append([self.blt_pos, self.blt_rot, self.blt_glo])
            self.blt_timer = self.blt_timer_max

        #Make the bullet timer go down.
        if self.blt_timer >= 0:
            self.blt_timer -= 1 * delta_time

        self.deleted = []

        for i in range(0, len(self.blt_cache)):
            if self.blt_cache[i][0][2] <= 500: 
                self.blt = mesh.bullet(self.blt_cache[i][0], self.blt_cache[i][1], self.blt_cache[i][2])
                self.blt.rot = self.blt_cache[i][1]
                self.blt.update()

                self.blt_cache[i][0][0] += math.sin(self.blt_cache[i][1][1]) * self.blt_spd * delta_time
                self.blt_cache[i][0][0] -= self.vel[0] * 20 * delta_time

                self.blt_cache[i][0][1] -= math.sin(self.blt_cache[i][1][0]) * self.blt_spd * delta_time
                self.blt_cache[i][0][1] -= self.vel[1] * 20 * delta_time

                self.blt_cache[i][0][2] += math.cos(self.blt_cache[i][1][1]) * self.blt_spd * delta_time

                self.blt.shd = self.bnd_b
                self.rnd += self.blt.render()

            else:
                self.deleted.append(i)

        for i in range(0, len(self.deleted)):
            self.blt_cache.pop(self.deleted[i])

        #Apply movement to player properties.
        self.pos[0] += self.vel[0] * delta_time
        self.pos[1] += self.vel[1] * delta_time

        self.rot[0] = -self.vel[1] * delta_time * 6
        self.rot[1] = self.vel[0] * delta_time * 6
        self.rot[2] = -self.vel[0] * delta_time * 6

        #Link to model.
        self.mesh.pos[0] = self.pos[0]
        self.mesh.pos[1] = self.pos[1]
        self.mesh.pos[2] = self.pos[2]

        self.mesh.rot[0] = self.rot[0]
        self.mesh.rot[1] = self.rot[1]
        self.mesh.rot[2] = self.rot[2]

        self.mesh.glo[0] = self.glo[0]
        self.mesh.glo[1] = self.glo[1]
        self.mesh.glo[2] = self.glo[2]

        self.mesh.shd = self.bnd_b - 1
        self.mesh.eng_clr += self.mesh.eng_acc * delta_time

        #Update mesh.
        self.mesh.update()

    def render(self):
        #Add bullet and ship render pipline to the main pipeline.
        self.rnd += self.mesh.render()
        return self.rnd
