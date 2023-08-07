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
    
    def rotate_local(self, rotation, delta_time):
        #X rotation
        for i in range(0, len(self.vertices)):
            self.new_x = self.vertices[i][0]
            self.new_y = math.cos(rotation[0] * delta_time) * self.vertices[i][1] - math.sin(rotation[0] * delta_time) * self.vertices[i][2] + rotation[0] * 10 * delta_time
            self.new_z = math.sin(rotation[0] * delta_time) * self.vertices[i][1] + math.cos(rotation[0] * delta_time) * self.vertices[i][2]
            self.vertices[i][0] = self.new_x
            self.vertices[i][1] = self.new_y
            self.vertices[i][2] = self.new_z
        #Y rotation
        for i in range(0, len(self.vertices)):
            self.new_x = math.cos(rotation[1] * delta_time) * self.vertices[i][0] + math.sin(rotation[1] * delta_time) * self.vertices[i][2] - rotation[1] * 10 * delta_time
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