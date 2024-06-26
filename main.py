import pygame
import math
import mesh
import player
pygame.init()

canvas = pygame.display.set_mode((256, 224), pygame.SCALED, vsync=1)
refresh = pygame.time.Clock()
refresh_rate = 60

viewport_pos = [0, 0, 0]
viewport_rot = [0, 0, 0]
viewport_width = 1
viewport_height = canvas.get_height()/canvas.get_width()
viewport_distance = 1

bg_img = pygame.image.load('Asteriod Belt.png')
bg_pos = [-512/4, -512/3]
bg_rot = 0

#Functions:
def scale_to_canvas(x, y):
    #Scale points from 3D coordintates to fit on canvas.
    return [x * canvas.get_width()/viewport_width, y * canvas.get_height()/viewport_height]

def project_vertex(p): #vertex coordinate format: [x, y, z].
    #Use the viewport variables described in initialization.
    x, y, z = p[0], p[1], p[2]
    x1, y1 = (x * viewport_distance)/z, (y * viewport_distance)/z#Projection formula.
    return scale_to_canvas(x1, y1)

def draw_triangle(p0, p1, p2, color):
    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1] 

    pygame.draw.polygon(canvas, color, ((canvas.get_width()/2 + x0, canvas.get_height()/2 - y0),
                                        (canvas.get_width()/2 + x1, canvas.get_height()/2 - y1),
                                        (canvas.get_width()/2 + x2, canvas.get_height()/2 - y2)))

def sort_triangles(tri_list):
    pass_limit = 100
    passes = 0
    while passes <= pass_limit:
        for i in range(0, len(tri_list) - 1):
            j = i + 1
              
            origin1 = [(tri_list[i][0][0] + tri_list[i][1][0] + tri_list[i][2][0])/3,
                        (tri_list[i][0][1] + tri_list[i][1][1] + tri_list[i][2][1])/3,
                        (tri_list[i][0][2] + tri_list[i][1][2] + tri_list[i][2][2])/3]
            
            origin2 = [(tri_list[j][0][0] + tri_list[j][1][0] + tri_list[j][2][0])/3,
                        (tri_list[j][0][1] + tri_list[j][1][1] + tri_list[j][2][1])/3,
                        (tri_list[j][0][2] + tri_list[j][1][2] + tri_list[j][2][2])/3]
            
            distance1 = math.sqrt(origin1[2] **2 + origin1[1] ** 2 + origin1[0] ** 2)

            distance2 = math.sqrt(origin2[2] **2 + origin2[1] ** 2 + origin2[0] ** 2)
            

            if distance1 < distance2:
                cache = tri_list[i]
                tri_list[i] = tri_list[j]
                tri_list[j] = cache

        passes += 1

def distance_shade(tri_list):
    for i in range(0, len(tri_list)):
        dis_mod = 1

        origin1 =   [(tri_list[i][0][0] + tri_list[i][1][0] + tri_list[i][2][0])/3,
                    (tri_list[i][0][1] + tri_list[i][1][1] + tri_list[i][2][1])/3,
                    (tri_list[i][0][2] + tri_list[i][1][2] + tri_list[i][2][2])/3] 
        
        distance =  math.sqrt(origin1[2] **2 + origin1[1] ** 2 + origin1[0] ** 2)

        ini_color = tri_list[i][3]
        ren_color = [ini_color[0] - distance * dis_mod, ini_color[1] - distance * dis_mod, ini_color[2] - distance * dis_mod]

        for i in range(0, len(ren_color)):
            if ren_color[i] >= 0:
                ren_color[i] = 0

            elif ren_color[i] <= 0:
                ren_color[i] = 0

        tri_list[i][3] = (ren_color[0], ren_color[1], ren_color[2])

#Initialize game objects:
player = player.player()

#Start the main loop:
main_loop = True
while main_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

    key_state = pygame.key.get_pressed()
    delta_time = refresh.tick(refresh_rate)/1000

    player.update(pygame, key_state, delta_time)

    #Clear render layers:
    render_layer1 = []
    render_layer1 += player.render()
    
    bg_pos[0] -= player.vel[0] * 20 * delta_time
    bg_pos[1] += player.vel[1] * 20 * delta_time
    bg_rot = -player.vel[0] * 20 * delta_time
    
    rot_img =pygame.transform.rotate(bg_img, bg_rot)

    #Perform layer functions:
    sort_triangles(render_layer1)

    #Shade by distance:
    #distance_shade(render_layer1)

    #Start render loop:
    canvas.fill((0, 0, 0))
    canvas.blit(rot_img, (bg_pos[0], bg_pos[1]))

    for i in range(0,len(render_layer1)):
        draw_triangle(project_vertex(render_layer1[i][0]), project_vertex(render_layer1[i][1]), project_vertex(render_layer1[i][2]), render_layer1[i][3])

    pygame.display.flip()