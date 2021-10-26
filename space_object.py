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

        self.x += config.speed[self.obj_type] * math.cos(math.radians(self.angle))
        self.y += config.speed[self.obj_type] * math.sin(math.radians(-self.angle))

        # if self.x <= 0 or self.x >= self.width:
        #     if self.x <= 0:
        #         self.x += self.width
        #     elif self.x >= self.width:
        #         self.x -= self.width
        # if self.y <= 0 or self.y >= self.height:
        #     if self.y <= 0:
        #         self.y += self.height
        #     elif self.y > self.height:
        #         self.y -= self.height
       
        if self.x <= 0:
            self.x += self.width
        elif self.x >= self.width:
            self.x -= self.width
       
        if self.y <= 0:
            self.y += self.height
        elif self.y > self.height:
            self.y -= self.height
            
            
            # pass # TODO 


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
        
        if config.radius[self.obj_type] + config.radius[other.obj_type] >= dist:
            return True
        return False

        

    def __repr__(self):
        
        # Enter your code here

        return '{} {:.1f},{:.1f},{},{}'.format(self.obj_type, self.x, self.y, self.angle, self.id)

    # You can add additional methods if required

    




