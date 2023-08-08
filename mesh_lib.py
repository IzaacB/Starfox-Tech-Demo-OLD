import copy
import math

class cube():
    def __init__(self, x, y, z):
        self.vertices = [[-1 + x, 1 + y, 1 + z],
                        [1 + x, 1 + y, 1 + z],
                        [1 + x, -1 + y, 1 + z],
                        [-1 + x, -1 + y, 1 + z],
                        [-1 + x, 1 + y, -1 + z],
                        [1 + x, 1 + y, -1 + z],
                        [1 + x, -1 + y, -1 + z],
                        [-1 + x, -1 + y, -1 + z]]
        
    def transform(self, transformation, delta_time):
        for i in range(0, len(self.vertices)):
            self.vertices[i][0] += transformation[0] * delta_time
            self.vertices[i][1] += transformation[1] * delta_time
            self.vertices[i][2] += transformation[2] * delta_time

    def rotate_global(self, rotation, delta_time):
        #X rotation
        for i in range(0, len(self.vertices)):
            self.new_x = self.vertices[i][0]
            self.new_y = math.cos(rotation[0] * delta_time) * self.vertices[i][1] - math.sin(rotation[0] * delta_time) * self.vertices[i][2]
            self.new_z = math.sin(rotation[0] * delta_time) * self.vertices[i][1] + math.cos(rotation[0] * delta_time) * self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z
        #Y rotation
        for i in range(0, len(self.vertices)):
            self.new_x = math.cos(rotation[1] * delta_time) * self.vertices[i][0] + math.sin(rotation[1] * delta_time) * self.vertices[i][2]
            self.new_y = self.vertices[i][1]
            self.new_z = -math.sin(rotation[1] * delta_time) * self.vertices[i][0] + math.cos(rotation[1] * delta_time) * self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z
        #Z rotation
        for i in range(0, len(self.vertices)):
            self.new_x = math.cos(rotation[2] * delta_time) * self.vertices[i][0] - math.sin(rotation[2] * delta_time) * self.vertices[i][1]
            self.new_y = math.sin(rotation[2] * delta_time) * self.vertices[i][0] + math.cos(rotation[2] * delta_time) * self.vertices[i][1]
            self.new_z = self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z

    def render(self):
        self.aperature = 1
        self.temp_vertices = copy.deepcopy(self.vertices)

        for i in range(0, len(self.temp_vertices)):
            if self.temp_vertices[i][2] <= self.aperature:
                self.temp_vertices[i][2] = self.aperature

        self.tris =    [[self.temp_vertices[0], self.temp_vertices[1], self.temp_vertices[2], (255, 0, 0)],
                        [self.temp_vertices[0], self.temp_vertices[3], self.temp_vertices[2], (255, 0, 0)],
                        [self.temp_vertices[4], self.temp_vertices[0], self.temp_vertices[3], (225, 0, 0)],
                        [self.temp_vertices[4], self.temp_vertices[7], self.temp_vertices[3], (225, 0, 0)],
                        [self.temp_vertices[1], self.temp_vertices[5], self.temp_vertices[6], (200, 0, 0)],
                        [self.temp_vertices[1], self.temp_vertices[2], self.temp_vertices[6], (200, 0, 0)],
                        [self.temp_vertices[5], self.temp_vertices[4], self.temp_vertices[7], (150, 0, 0)],
                        [self.temp_vertices[5], self.temp_vertices[6], self.temp_vertices[7], (150, 0, 0)],
                        [self.temp_vertices[0], self.temp_vertices[4], self.temp_vertices[5], (125, 0, 0)],
                        [self.temp_vertices[0], self.temp_vertices[1], self.temp_vertices[5], (125, 0, 0)],
                        [self.temp_vertices[3], self.temp_vertices[2], self.temp_vertices[6], (100, 0, 0)],
                        [self.temp_vertices[3], self.temp_vertices[7], self.temp_vertices[6], (100, 0, 0)],]
        
        self.filter_tris = []
        
        for i in range(0, len(self.tris)):
            if self.tris[i][0][2] > self.aperature or self.tris[i][1][2] > self.aperature or self.tris[i][2][2] > self.aperature:
                self.filter_tris.append(self.tris[i])

        return self.filter_tris
    
class arwing():
    def __init__(self, x, y, z):
        self.vertices = [[0 + x, 0 + y, 3 + z],
                         [x -.5, 0 + y, 0 + z],
                         [0 + x, .5 + y, 0 + z],
                         [.5 + x, 0 + y, 0 + z],
                         [0 + x, .25 + y, -.5 + z],
                         [0 + x, .15 + y, -.25 + z],
                         [x - 1, y - .25, z + 1.5],
                         [x - 1.25, y + .75, z - .75], 
                         [x - 1, y, z], 
                         [x - .8, y - .15, z + .25], 
                         [x - .8, y - .15, z - .25],
                         [x - 2, y - .5, z],
                         [x + 1, y - .25, z + 1.5],
                         [x + 1.25, y + .75, z - .75], 
                         [x + 1, y, z], 
                         [x + .8, y - .15, z + .25], 
                         [x + .8, y - .15, z - .25],
                         [x + 2, y - .5, z]]
        
    def transform(self, transformation, delta_time):
        for i in range(0, len(self.vertices)):
            self.vertices[i][0] += transformation[0] * delta_time
            self.vertices[i][1] += transformation[1] * delta_time
            self.vertices[i][2] += transformation[2] * delta_time

    def rotate_global(self, rotation, delta_time):
        #X rotation
        for i in range(0, len(self.vertices)):
            self.new_x = self.vertices[i][0]
            self.new_y = math.cos(rotation[0] * delta_time) * self.vertices[i][1] - math.sin(rotation[0] * delta_time) * self.vertices[i][2]
            self.new_z = math.sin(rotation[0] * delta_time) * self.vertices[i][1] + math.cos(rotation[0] * delta_time) * self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z
        #Y rotation
        for i in range(0, len(self.vertices)):
            self.new_x = math.cos(rotation[1] * delta_time) * self.vertices[i][0] + math.sin(rotation[1] * delta_time) * self.vertices[i][2]
            self.new_y = self.vertices[i][1]
            self.new_z = -math.sin(rotation[1] * delta_time) * self.vertices[i][0] + math.cos(rotation[1] * delta_time) * self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z
        #Z rotation
        for i in range(0, len(self.vertices)):
            self.new_x = math.cos(rotation[2] * delta_time) * self.vertices[i][0] - math.sin(rotation[2] * delta_time) * self.vertices[i][1]
            self.new_y = math.sin(rotation[2] * delta_time) * self.vertices[i][0] + math.cos(rotation[2] * delta_time) * self.vertices[i][1]
            self.new_z = self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z

    def render(self):
        self.aperature = 1
        self.temp_vertices = copy.deepcopy(self.vertices)

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
                        [self.temp_vertices[1], self.temp_vertices[6], self.temp_vertices[7], (50, 50, 200)],
                        [self.temp_vertices[1], self.temp_vertices[9], self.temp_vertices[8], (180, 180, 210)],
                        [self.temp_vertices[1], self.temp_vertices[8], self.temp_vertices[10], (140, 140, 160)],
                        [self.temp_vertices[8], self.temp_vertices[10], self.temp_vertices[11], (150, 150, 170)],
                        [self.temp_vertices[8], self.temp_vertices[9], self.temp_vertices[11], (180, 180, 210)],
                        [self.temp_vertices[9], self.temp_vertices[10], self.temp_vertices[11], (110, 110, 130)],
                        [self.temp_vertices[9], self.temp_vertices[10], self.temp_vertices[1], (110, 110, 130)],
                        [self.temp_vertices[3], self.temp_vertices[12], self.temp_vertices[13], (50, 50, 200)],
                        [self.temp_vertices[3], self.temp_vertices[15], self.temp_vertices[14], (180, 180, 210)],
                        [self.temp_vertices[3], self.temp_vertices[14], self.temp_vertices[16], (140, 140, 160)],
                        [self.temp_vertices[14], self.temp_vertices[16], self.temp_vertices[17], (150, 150, 170)],
                        [self.temp_vertices[14], self.temp_vertices[15], self.temp_vertices[17], (180, 180, 210)],
                        [self.temp_vertices[15], self.temp_vertices[16], self.temp_vertices[17], (110, 110, 130)],
                        [self.temp_vertices[15], self.temp_vertices[16], self.temp_vertices[3], (110, 110, 130)]]
        
        self.filter_tris = []
        
        for i in range(0, len(self.tris)):
            if self.tris[i][0][2] > self.aperature or self.tris[i][1][2] > self.aperature or self.tris[i][2][2] > self.aperature:
                self.filter_tris.append(self.tris[i])

        return self.filter_tris