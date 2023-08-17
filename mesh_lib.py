import copy
import math
    
class arwing():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.rot_x = 0
        self.rot_y = 0
        self.rot_z = 0

        self.vertices = [[0, 0, 3],
                         [-.5, 0, 0],
                         [0, .5, 0],
                         [.5, 0, 0],
                         [0, .15, -.5],
                         [0, .15, -.25],
                         [- .75, - .35, 1.5],
                         [- 1.25, .65, - .50], 
                         [- 1, 0, 0], 
                         [- .8, - .15, .25], 
                         [- .8, - .15, - .25],
                         [- 2, - .5, 0],
                         [.75, - .35, 1.5],
                         [1.25, .65, - .50], 
                         [1, 0, 0], 
                         [.8, - .15, .25], 
                         [.8, - .15, - .25],
                         [2, - .5, 0]]
                         

    def update(self):
        self.new_vertices = copy.deepcopy(self.vertices)

        #Local rotation:
        for i in range(0, len(self.new_vertices)):
            self.new_y = math.cos(self.rot_x) * self.new_vertices[i][1] - math.sin(self.rot_x) * self.new_vertices[i][2]
            self.new_z = math.sin(self.rot_x) * self.new_vertices[i][1] + math.cos(self.rot_x) * self.new_vertices[i][2]
            self.new_vertices[i][1] = self.new_y
            self.new_vertices[i][2] = self.new_z

        for i in range(0, len(self.new_vertices)):
            self.new_x = math.cos(self.rot_y) * self.new_vertices[i][0] + math.sin(self.rot_y) * self.new_vertices[i][2]
            self.new_z = - math.sin(self.rot_y) * self.new_vertices[i][0] + math.cos(self.rot_y) * self.new_vertices[i][2]
            self.new_vertices[i][0] = self.new_x
            self.new_vertices[i][2] = self.new_z 

        for i in range(0, len(self.new_vertices)):
            self.new_x = math.cos(self.rot_z) * self.new_vertices[i][0] - math.sin(self.rot_z) * self.new_vertices[i][1]
            self.new_y = math.sin(self.rot_z) * self.new_vertices[i][0] + math.cos(self.rot_z) * self.new_vertices[i][1]
            self.new_vertices[i][0] = self.new_x 
            self.new_vertices[i][1] = self.new_y

        #Transformation:
        for i in range(0, len(self.new_vertices)):
            self.new_vertices[i][0] += self.x
            self.new_vertices[i][1] += self.y
            self.new_vertices[i][2] += self.z

    def render(self):
        try:
            self.aperature = 1
            self.temp_vertices = copy.deepcopy(self.new_vertices)

            for i in range(0, len(self.temp_vertices)):
                if self.temp_vertices[i][2] <= self.aperature:
                    self.temp_vertices[i][2] = self.aperature

            self.tris =    [[self.temp_vertices[0], self.temp_vertices[1], self.temp_vertices[2], (180, 180, 210)],
                            [self.temp_vertices[0], self.temp_vertices[2], self.temp_vertices[3], (150, 150, 170)],
                            [self.temp_vertices[0], self.temp_vertices[1], self.temp_vertices[3], (110, 110, 130)],
                            [self.temp_vertices[1], self.temp_vertices[2], self.temp_vertices[4], (170, 170, 210)],
                            [self.temp_vertices[2], self.temp_vertices[3], self.temp_vertices[4], (140, 140, 160)],
                            [self.temp_vertices[1], self.temp_vertices[5], self.temp_vertices[4], (50, 50, 50)],
                            [self.temp_vertices[4], self.temp_vertices[5], self.temp_vertices[3], (50, 50, 50)],
                            [self.temp_vertices[1], self.temp_vertices[5], self.temp_vertices[3], (200, 0, 0)],
                            [self.temp_vertices[1], self.temp_vertices[6], self.temp_vertices[7], (50, 50, 150)],
                            [self.temp_vertices[1], self.temp_vertices[9], self.temp_vertices[8], (180, 180, 210)],
                            [self.temp_vertices[1], self.temp_vertices[8], self.temp_vertices[10], (140, 140, 160)],
                            [self.temp_vertices[8], self.temp_vertices[10], self.temp_vertices[11], (150, 150, 170)],
                            [self.temp_vertices[8], self.temp_vertices[9], self.temp_vertices[11], (180, 180, 210)],
                            [self.temp_vertices[9], self.temp_vertices[10], self.temp_vertices[11], (110, 110, 130)],
                            [self.temp_vertices[9], self.temp_vertices[10], self.temp_vertices[1], (110, 110, 130)],
                            [self.temp_vertices[3], self.temp_vertices[12], self.temp_vertices[13], (50, 50, 150)],
                            [self.temp_vertices[3], self.temp_vertices[15], self.temp_vertices[14], (180, 180, 210)],
                            [self.temp_vertices[3], self.temp_vertices[14], self.temp_vertices[16], (140, 140, 160)],
                            [self.temp_vertices[14], self.temp_vertices[16], self.temp_vertices[17], (150, 150, 170)],
                            [self.temp_vertices[14], self.temp_vertices[15], self.temp_vertices[17], (180, 180, 210)],
                            [self.temp_vertices[15], self.temp_vertices[16], self.temp_vertices[17], (110, 110, 130)],
                            [self.temp_vertices[15], self.temp_vertices[16], self.temp_vertices[3], (110, 110, 130)]]
            
            self.shadow_tris = copy.deepcopy(self.tris)

            for i in range(0, len(self.shadow_tris)):
                self.shadow_tris[i][0][1] = -4
                self.shadow_tris[i][1][1] = -4
                self.shadow_tris[i][2][1] = -4
                self.shadow_tris[i][3] = (25, 50, 25)

            self.filter_tris = []
            self.filter_tris += self.shadow_tris
            
            for i in range(0, len(self.tris)):
                if self.tris[i][0][2] > self.aperature or self.tris[i][1][2] > self.aperature or self.tris[i][2][2] > self.aperature:
                    self.filter_tris.append(self.tris[i])
        except:
            pass
            
            

        return self.filter_tris