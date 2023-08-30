import copy
import math
import random
    
class arwing():
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        
        self.rot = [0, 0, 0]#Rotation on local axis.
        self.glo = [0, 0, 0]#Rotation on Global axis.

        self.shd = 0

        self.eng_min = 0
        self.eng_max = 255
        self.eng_acc = 255 * 8
        self.eng_clr = self.eng_min

        #Initialize vertices.
        self.ini_verts = [[0, 0, 3],
                         [-.5, 0, 0],
                         [0, .5, 0],
                         [.5, 0, 0],
                         [0, .2, -.5],
                         [0, .2, -.25],
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
        self.upd_verts = copy.deepcopy(self.ini_verts)#Create copy of initial vertices to apply rotation and transformation to.
        
        for i in range(0, len(self.upd_verts)):
            #Local rotation on the x-axis.
            self.new_y = math.cos(self.rot[0]) * self.upd_verts[i][1] - math.sin(self.rot[0]) * self.upd_verts[i][2]
            self.new_z = math.sin(self.rot[0]) * self.upd_verts[i][1] + math.cos(self.rot[0]) * self.upd_verts[i][2]
            self.upd_verts[i][1] = self.new_y
            self.upd_verts[i][2] = self.new_z

            #Local rotation on the y-axis.
            self.new_x = math.cos(self.rot[1]) * self.upd_verts[i][0] + math.sin(self.rot[1]) * self.upd_verts[i][2]
            self.new_z = - math.sin(self.rot[1]) * self.upd_verts[i][0] + math.cos(self.rot[1]) * self.upd_verts[i][2]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][2] = self.new_z 

            #Local rotation on the z-axis.
            self.new_x = math.cos(self.rot[2]) * self.upd_verts[i][0] - math.sin(self.rot[2]) * self.upd_verts[i][1]
            self.new_y = math.sin(self.rot[2]) * self.upd_verts[i][0] + math.cos(self.rot[2]) * self.upd_verts[i][1]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][1] = self.new_y

            #Transformation on all axes.
            self.upd_verts[i][0] += self.pos[0]
            self.upd_verts[i][1] += self.pos[1]
            self.upd_verts[i][2] += self.pos[2]

            #Global rotation on the x-axis.
            self.new_y = math.cos(self.glo[0]) * self.upd_verts[i][1] - math.sin(self.glo[0]) * self.upd_verts[i][2]
            self.new_z = math.sin(self.glo[0]) * self.upd_verts[i][1] + math.cos(self.glo[0]) * self.upd_verts[i][2]
            self.upd_verts[i][1] = self.new_y
            self.upd_verts[i][2] = self.new_z

            #Global rotation on the y-axis.
            self.new_x = math.cos(self.glo[1]) * self.upd_verts[i][0] + math.sin(self.glo[1]) * self.upd_verts[i][2]
            self.new_z = - math.sin(self.glo[1]) * self.upd_verts[i][0] + math.cos(self.glo[1]) * self.upd_verts[i][2]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][2] = self.new_z 

            #Global rotation on the z-axis.
            self.new_x = math.cos(self.glo[2]) * self.upd_verts[i][0] - math.sin(self.glo[2]) * self.upd_verts[i][1]
            self.new_y = math.sin(self.glo[2]) * self.upd_verts[i][0] + math.cos(self.glo[2]) * self.upd_verts[i][1]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][1] = self.new_y

        if self.eng_clr >= self.eng_max or self.eng_clr <= self.eng_min:
            if self.eng_acc < 0:
                self.eng_clr = self.eng_min
                
            if self.eng_acc > 0:
                self.eng_clr = self.eng_max

            self.eng_acc *= -1

    def render(self):
        self.ren_verts = copy.deepcopy(self.upd_verts)#Grab the updated vertices to edit for rendering.
        self.aperature = 1

        #Method to clip vertices against the camera when past a certain point.
        for i in range(0, len(self.ren_verts)):
            if self.ren_verts[i][2] <= self.aperature:
                self.ren_verts[i][2] = self.aperature
        
        #Define Triangles for render.
        self.tris =    [[self.ren_verts[0], self.ren_verts[1], self.ren_verts[2], (160, 160, 160)],
                        [self.ren_verts[0], self.ren_verts[2], self.ren_verts[3], (135, 135, 135)],
                        [self.ren_verts[0], self.ren_verts[1], self.ren_verts[3], (100, 100, 100)],
                        [self.ren_verts[1], self.ren_verts[2], self.ren_verts[4], (145, 145, 145)],
                        [self.ren_verts[2], self.ren_verts[3], self.ren_verts[4], (120, 120, 120)],
                        [self.ren_verts[1], self.ren_verts[5], self.ren_verts[4], (50, 50, 50)],
                        [self.ren_verts[4], self.ren_verts[5], self.ren_verts[3], (50, 50, 50)],
                        [self.ren_verts[1], self.ren_verts[5], self.ren_verts[3], (255, self.eng_clr, 0)],
                        [self.ren_verts[1], self.ren_verts[6], self.ren_verts[7], (50, 50, 150)],
                        [self.ren_verts[1], self.ren_verts[9], self.ren_verts[8], (145, 145, 145)],
                        [self.ren_verts[1], self.ren_verts[8], self.ren_verts[10], (125, 125, 125)],
                        [self.ren_verts[8], self.ren_verts[10], self.ren_verts[11], (145, 145, 145)],
                        [self.ren_verts[8], self.ren_verts[9], self.ren_verts[11], (135, 135, 135)],
                        [self.ren_verts[9], self.ren_verts[10], self.ren_verts[11], (100, 100, 100)],
                        [self.ren_verts[9], self.ren_verts[10], self.ren_verts[1], (100, 100, 100)],
                        [self.ren_verts[3], self.ren_verts[12], self.ren_verts[13], (50, 50, 150)],
                        [self.ren_verts[3], self.ren_verts[15], self.ren_verts[14], (145, 145, 145)],
                        [self.ren_verts[3], self.ren_verts[14], self.ren_verts[16], (125, 125, 125)],
                        [self.ren_verts[14], self.ren_verts[16], self.ren_verts[17], (145, 145, 145)],
                        [self.ren_verts[14], self.ren_verts[15], self.ren_verts[17], (135, 135, 135)],
                        [self.ren_verts[15], self.ren_verts[16], self.ren_verts[17], (100, 100, 100)],
                        [self.ren_verts[15], self.ren_verts[16], self.ren_verts[3], (100, 100, 100)]]
        
        #Create a copy of the triangles to render the shadow at ground level.
        self.shd_tris = copy.deepcopy(self.tris)

        #Render shadow.
        for i in range(0, len(self.shd_tris)):
            self.shd_tris[i][3] = (75, 75, 75)
            self.shd_tris[i][0][1] = self.shd
            self.shd_tris[i][1][1] = self.shd
            self.shd_tris[i][2][1] = self.shd
            
        self.flt_tris = []
        #self.flt_tris += self.shd_tris
        
        #Don't add tris to render that are behind the camera.
        for i in range(0, len(self.tris)):
            if self.tris[i][0][2] > self.aperature or self.tris[i][1][2] > self.aperature or self.tris[i][2][2] > self.aperature:
                self.flt_tris.append(self.tris[i])
            
        return self.flt_tris
    
class bullet():
    def __init__(self, pos, rot, glo):
        self.pos = pos
        
        self.rot = rot#Rotation on local axis.
        self.glo = glo#Rotation on Global axis.

        self.shd = 0

        #Initialize vertices.
        self.ini_verts = [[0, 0, 1],
                          [-.5, 0, 0], 
                          [.5, 0, 0],
                          [0, 0, -1.5]]

    def update(self):
        self.upd_verts = copy.deepcopy(self.ini_verts)#Create copy of initial vertices to apply rotation and transformation to.
        
        for i in range(0, len(self.upd_verts)):
            #Local rotation on the x-axis.
            self.new_y = math.cos(self.rot[0]) * self.upd_verts[i][1] - math.sin(self.rot[0]) * self.upd_verts[i][2]
            self.new_z = math.sin(self.rot[0]) * self.upd_verts[i][1] + math.cos(self.rot[0]) * self.upd_verts[i][2]
            self.upd_verts[i][1] = self.new_y
            self.upd_verts[i][2] = self.new_z

            #Local rotation on the y-axis.
            self.new_x = math.cos(self.rot[1]) * self.upd_verts[i][0] + math.sin(self.rot[1]) * self.upd_verts[i][2]
            self.new_z = - math.sin(self.rot[1]) * self.upd_verts[i][0] + math.cos(self.rot[1]) * self.upd_verts[i][2]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][2] = self.new_z 

            #Local rotation on the z-axis.
            self.new_x = math.cos(self.rot[2]) * self.upd_verts[i][0] - math.sin(self.rot[2]) * self.upd_verts[i][1]
            self.new_y = math.sin(self.rot[2]) * self.upd_verts[i][0] + math.cos(self.rot[2]) * self.upd_verts[i][1]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][1] = self.new_y

            #Transformation on all axes.
            self.upd_verts[i][0] += self.pos[0]
            self.upd_verts[i][1] += self.pos[1]
            self.upd_verts[i][2] += self.pos[2]

            #Global rotation on the x-axis.
            self.new_y = math.cos(self.glo[0]) * self.upd_verts[i][1] - math.sin(self.glo[0]) * self.upd_verts[i][2]
            self.new_z = math.sin(self.glo[0]) * self.upd_verts[i][1] + math.cos(self.glo[0]) * self.upd_verts[i][2]
            self.upd_verts[i][1] = self.new_y
            self.upd_verts[i][2] = self.new_z

            #Gloabl rotation on the y-axis.
            self.new_x = math.cos(self.glo[1]) * self.upd_verts[i][0] + math.sin(self.glo[1]) * self.upd_verts[i][2]
            self.new_z = - math.sin(self.glo[1]) * self.upd_verts[i][0] + math.cos(self.glo[1]) * self.upd_verts[i][2]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][2] = self.new_z 

            #Global rotation on the z-axis.
            self.new_x = math.cos(self.glo[2]) * self.upd_verts[i][0] - math.sin(self.glo[2]) * self.upd_verts[i][1]
            self.new_y = math.sin(self.glo[2]) * self.upd_verts[i][0] + math.cos(self.glo[2]) * self.upd_verts[i][1]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][1] = self.new_y

    def render(self):
        self.ren_verts = copy.deepcopy(self.upd_verts)#Grab the updated vertices to edit for rendering.
        self.aperature = 1

        #Method to clip vertices against the camera when past a certain point.
        for i in range(0, len(self.ren_verts)):
            if self.ren_verts[i][2] <= self.aperature:
                self.ren_verts[i][2] = self.aperature
        
        #Define Triangles for render.
        self.tris =    [[self.ren_verts[0], self.ren_verts[1], self.ren_verts[2], (100, 255, 255)],
                        [self.ren_verts[1], self.ren_verts[2], self.ren_verts[3], (100, 255, 255)]]
        
        #Create a copy of the triangles to render the shadow at ground level.
        #self.shd_tris = copy.deepcopy(self.tris)

        #Render shadow.
        #for i in range(0, len(self.shd_tris)):
            #self.shd_tris[i][3] = (75, 75, 75)
            #self.shd_tris[i][0][1] = self.shd
            #self.shd_tris[i][1][1] = self.shd
            #self.shd_tris[i][2][1] = self.shd
            
        self.flt_tris = []
        #self.flt_tris += self.shd_tris
        
        #Don't add tris to render that are behind the camera.
        for i in range(0, len(self.tris)):
            if self.tris[i][0][2] > self.aperature or self.tris[i][1][2] > self.aperature or self.tris[i][2][2] > self.aperature:
                self.flt_tris.append(self.tris[i])
            
        return self.flt_tris
    
class cube():
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        
        self.rot = [0, 0, 0]#Rotation on local axis.
        self.glo = [0, 0, 0]#Rotation on Global axis.

        self.shd = 0

        #Initialize vertices.
        self.ini_verts = [[-4, 6, -4],
                          [4, 6, -4], 
                          [4, -4, -4],
                          [-4, -4, -4],
                          [-4, 6, 4],
                          [4, 6, 4], 
                          [4, -4, 4],
                          [-4, -4, 4]]
                         
    def update(self):
        self.upd_verts = copy.deepcopy(self.ini_verts)#Create copy of initial vertices to apply rotation and transformation to.
        
        for i in range(0, len(self.upd_verts)):
            #Local rotation on the x-axis.
            self.new_y = math.cos(self.rot[0]) * self.upd_verts[i][1] - math.sin(self.rot[0]) * self.upd_verts[i][2]
            self.new_z = math.sin(self.rot[0]) * self.upd_verts[i][1] + math.cos(self.rot[0]) * self.upd_verts[i][2]
            self.upd_verts[i][1] = self.new_y
            self.upd_verts[i][2] = self.new_z

            #Local rotation on the y-axis.
            self.new_x = math.cos(self.rot[1]) * self.upd_verts[i][0] + math.sin(self.rot[1]) * self.upd_verts[i][2]
            self.new_z = - math.sin(self.rot[1]) * self.upd_verts[i][0] + math.cos(self.rot[1]) * self.upd_verts[i][2]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][2] = self.new_z 

            #Local rotation on the z-axis.
            self.new_x = math.cos(self.rot[2]) * self.upd_verts[i][0] - math.sin(self.rot[2]) * self.upd_verts[i][1]
            self.new_y = math.sin(self.rot[2]) * self.upd_verts[i][0] + math.cos(self.rot[2]) * self.upd_verts[i][1]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][1] = self.new_y

            #Transformation on all axes.
            self.upd_verts[i][0] += self.pos[0]
            self.upd_verts[i][1] += self.pos[1]
            self.upd_verts[i][2] += self.pos[2]

            #Global rotation on the x-axis.
            self.new_y = math.cos(self.glo[0]) * self.upd_verts[i][1] - math.sin(self.glo[0]) * self.upd_verts[i][2]
            self.new_z = math.sin(self.glo[0]) * self.upd_verts[i][1] + math.cos(self.glo[0]) * self.upd_verts[i][2]
            self.upd_verts[i][1] = self.new_y
            self.upd_verts[i][2] = self.new_z

            #Global rotation on the y-axis.
            self.new_x = math.cos(self.glo[1]) * self.upd_verts[i][0] + math.sin(self.glo[1]) * self.upd_verts[i][2]
            self.new_z = - math.sin(self.glo[1]) * self.upd_verts[i][0] + math.cos(self.glo[1]) * self.upd_verts[i][2]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][2] = self.new_z 

            #Global rotation on the z-axis.
            self.new_x = math.cos(self.glo[2]) * self.upd_verts[i][0] - math.sin(self.glo[2]) * self.upd_verts[i][1]
            self.new_y = math.sin(self.glo[2]) * self.upd_verts[i][0] + math.cos(self.glo[2]) * self.upd_verts[i][1]
            self.upd_verts[i][0] = self.new_x 
            self.upd_verts[i][1] = self.new_y

    def render(self):
        self.ren_verts = copy.deepcopy(self.upd_verts)#Grab the updated vertices to edit for rendering.
        self.aperature = 1

        #Method to clip vertices against the camera when past a certain point.
        for i in range(0, len(self.ren_verts)):
            if self.ren_verts[i][2] <= self.aperature:
                self.ren_verts[i][2] = self.aperature
        
        #Define Triangles for render.
        self.tris =    [[self.ren_verts[0], self.ren_verts[1], self.ren_verts[2], (190, 190, 190)],
                        [self.ren_verts[0], self.ren_verts[3], self.ren_verts[2], (190, 190, 190)],
                        [self.ren_verts[4], self.ren_verts[0], self.ren_verts[3], (170, 170, 170)],
                        [self.ren_verts[4], self.ren_verts[7], self.ren_verts[3], (170, 170, 170)],
                        [self.ren_verts[1], self.ren_verts[5], self.ren_verts[6], (150, 150, 150)],
                        [self.ren_verts[1], self.ren_verts[2], self.ren_verts[6], (150, 150, 150)],
                        [self.ren_verts[5], self.ren_verts[4], self.ren_verts[7], (130, 130, 130)],
                        [self.ren_verts[5], self.ren_verts[6], self.ren_verts[7], (130, 130, 130)],
                        [self.ren_verts[0], self.ren_verts[4], self.ren_verts[5], (150, 150, 150)],
                        [self.ren_verts[0], self.ren_verts[1], self.ren_verts[5], (150, 150, 150)],
                        [self.ren_verts[3], self.ren_verts[2], self.ren_verts[6], (170, 170, 170)],
                        [self.ren_verts[3], self.ren_verts[7], self.ren_verts[6], (170, 170, 170)]
                        ]
        
        #Create a copy of the triangles to render the shadow at ground level.
        self.shd_tris = copy.deepcopy(self.tris)

        #Render shadow.
        for i in range(0, len(self.shd_tris)):
            self.shd_tris[i][3] = (75, 75, 75)
            self.shd_tris[i][0][1] = self.shd
            self.shd_tris[i][1][1] = self.shd
            self.shd_tris[i][2][1] = self.shd
            
        self.flt_tris = []
        self.flt_tris += self.shd_tris
        
        #Don't add tris to render that are behind the camera.
        for i in range(0, len(self.tris)):
            if self.tris[i][0][2] > self.aperature or self.tris[i][1][2] > self.aperature or self.tris[i][2][2] > self.aperature:
                self.flt_tris.append(self.tris[i])
            
        return self.flt_tris
