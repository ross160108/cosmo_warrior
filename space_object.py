import math
import config

class SpaceObject:
    def __init__(self, x, y, width, height, angle, obj_type, id):
        
        # Enter your code here

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle

        #!obj_type : spaceship / bullet / asteriods small / big 
        self.obj_type = obj_type 
        self.id = id


        #!! radius?
        self.radius = config.radius[self.obj_type]

        # self.radius = config.radius['spaceship']

        # self.radius = config.radius['bullet']
        # self.radius = config.radius['asteroid_small']
        
        

    def turn_left(self):
        
        # Enter your code here

        #! only for spaceship
        self.angle += config.angle_increment

        if self.angle >= 360:
            self.angle -= 360
        

    def turn_right(self):
        
        # Enter your code here

        #! only for spaceship

        self.angle -= config.angle_increment

        if self.angle < 0:
            self.angle += 360
        
        


    def move_forward(self):
        
        # Enter your code here

        
        # if self.obj_type == 'spaceship':
        #     self.x += config.speed['spaceship'] * math.cos(math.radians(self.angle))
        #     self.y += config.speed['spaceship'] * math.sin(math.radians(self.angle))

        # elif self.obj_type == 'bullet':
        #     self.x += config.speed['bullet'] * math.cos(math.radians(self.angle))
        #     self.y += config.speed['bullet'] * math.sin(math.radians(self.angle))

        # elif self.obj_type == 'asteroid_small':
        #     self.x += config.speed['asteroid_small'] * math.cos(math.radians(self.angle))
        #     self.y += config.speed['asteroid_small'] * math.sin(math.radians(self.angle))

        # elif self.obj_type == 'asteroid_large':
        #     self.x += config.speed['asteroid_large'] * math.cos(math.radians(self.angle))
        #     self.y += config.speed['asteroid_large'] * math.sin(math.radians(self.angle))

        #!
        # distance_update = config.speed[self.obj_type] * config.frame_delay
        # i = 0
        # while i < 1000:
        #     distance_update += config.speed[self.obj_type] * config.frame_delay
        #     self.x += distance_update * math.cos(math.radians(self.angle))
        #     self.y += distance_update * math.sin(math.radians(self.angle))
        #     i+=1
        #!

        self.x += config.speed[self.obj_type]  * math.cos(math.radians(self.angle))
        self.y += config.speed[self.obj_type]  * math.sin(math.radians(-self.angle))

        

    def get_xy(self):
        
        # Enter your code here

        return (self.x, self.y) 
        
        

    def collide_with(self, other):
        
        # Enter your code here
        self.other = other

        #! distance between 2 obj
        dist = math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )
        #! colliding/not
        # print(config.radius[self.obj_type])
        # print(config.radius[other.obj_type])
        print(dist)
        if config.radius[self.obj_type] + config.radius[other.obj_type] <= dist:
            return True
        return False

        

    def __repr__(self):
        
        # Enter your code here

        return '{} {:.1f},{:.1f},{},{}'.format(self.obj_type, self.x, self.y, self.angle, self.id)

    # You can add additional methods if required

    


#**********************************#
# (self, x, y, width, height, angle, obj_type, id)

# asteriod1 = SpaceObject(30,30,10,10,30, 'asteroid_small', 1)
# spaceship1 = SpaceObject(0,0,10,10,30,'spaceship', 2)

# spaceship1.move_forward()

# print(spaceship1.collide_with(asteriod1))

# print(spaceship1.get_xy())
# print(spaceship1.turn_right())
# print(spaceship1.__repr__())
# print(asteriod1.__repr__())

