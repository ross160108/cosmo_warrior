import config
from space_object import SpaceObject


#!! 지워야됨
from player import Player
from gui import GUI
#!!

GAME_STATE_KEYS = [
    'width',
    'height',
    'score',
    'spaceship',
    'fuel',
    'asteroids_count',
    'bullets_count',
    'upcoming_asteroids_count'
]
ASTEROID_TYPES = [
    'upcoming_asteroid_small',
    'upcoming_asteroid_large',
    'asteroid_large',
    'asteroid_small'
]
GAME_STATE_KEYS += ASTEROID_TYPES

class Engine:
    #Engine('examples/game_state_good.txt', Player, GUI)
    def __init__(self, game_state_filename, player_class, gui_class):
        self.debug = False

        # vars
        self.game_dict = {}
        self.bullets = []

        self.object_dict = {
            'asteroid_large': [],
            'asteroid_small': [],
            'upcoming_asteroid_large': [],
            'upcoming_asteroid_small': [],
            'bullet' : [] #! TBD
        }

        # TODO
        '''
        self.object_dict = {
            'asteroid': [],
            'upcoming_asteroid': [],
            'bullet' : [] #! TBD
        }
        '''
        
        self.import_state(game_state_filename)
        
        #self.export_state('./export_test.txt')
        
        self.player = player_class()
        self.GUI = gui_class(self.width, self.height)


    def parse_args(self, file_path):
        # Enter your code here
        try:
            f = open(file_path, 'r')
            while True:
                data = f.readline()
                if not data:
                    break
                for_key = data.split()[0]
                
                if len(data.split()) != 2:
                    try:
                        raise ValueError
                        #raise ValueError('Error: game state incomplete')
                    except ValueError:
                        print('Error: expecting a key and value in line <line number>')
                        exit()

                for_value = data.split()[1].split(',')

                if len(for_value) == 1:
                    for_value = for_value[0]

                if for_key in ASTEROID_TYPES:
                    if for_key in self.game_dict.keys():
                        self.game_dict[for_key].append( for_value )
                    else:
                        self.game_dict[for_key] = []
                        self.game_dict[for_key].append( for_value )
                else:
                    self.game_dict[for_key] = for_value
            
                
            f.close()
        except FileNotFoundError:
            #raise FileNotFoundError('Error: unable to open {}'.format(file_path))
            print('Error: unable to open {}'.format(file_path))
            exit()
        
        #! debug code
        if False:
        #if True:
            for key, val in self.game_dict.items():
                print(key, val)
        
            
    def is_numeric(self, key):
        if self.game_dict[key].isnumeric():
            self.game_dict[key] = int(self.game_dict[key])
            return True
        else:
            #! code line 명시 필요  
            raise ValueError('Error: invalid data type in line <line number')

    def is_valid_list(self, key):
        if not isinstance(self.game_dict[key], list):
            #! code line 명시 필요  
            raise ValueError('Error: expecting a key and value in line <line number')
                    
            if len(self.game_dict[key]) != 4:
                raise ValueError('Error: expecting a key and value in line <line number')
                    
            try:
                self.game_dict[key][0] = float(self.game_dict[key][0])
                self.game_dict[key][1] = float(self.game_dict[key][1])
                self.game_dict[key][2] = int(self.game_dict[key][2])
                self.game_dict[key][3] = int(self.game_dict[key][3])
                return True
            except:
                #! code line 명시 필요  
                raise ValueError('Error: invalid data type in line <line number')

    
    def import_state(self, game_state_filename):
        self.parse_args(game_state_filename)

        # incomplete check and key-val pair check
        for key in GAME_STATE_KEYS:
            if not key in self.game_dict.keys():
                try:
                    raise ValueError
                    #raise ValueError('Error: game state incomplete')
                except ValueError:
                    print('Error: game state incomplete')
                    exit()
      
        # 1. game width, height 
        for key in GAME_STATE_KEYS:
            if key == 'width': 
                if self.is_numeric(key):
                    self.width = self.game_dict[key]
            elif key == 'height':
                if self.is_numeric(key):
                    self.height = self.game_dict[key]
            elif key in ['score', 'fuel', 'asteroids_count', 'bullets_count', 'upcoming_asteroids_count']:
                self.is_numeric(key)

            elif key == 'spaceship':
                self.is_valid_list(key)
            
            elif key in ASTEROID_TYPES:
                self.is_valid_list(key)
                self.object_dict[key].append( self.game_dict[key] )

        #! debug
        #print(self.object_dict)
        
        #* 2. 

    def export_state(self, game_state_filename):

        #print(self.game_dict)
        pass


        
        
        
        

    def run_game(self):
        # self, x, y, width, height, angle, obj_type, id):
        obj1 = SpaceObject(150, 100, self.width, self.height, 30, 'asteroid_large', 1)
        obj2 = SpaceObject(200, 300, self.width, self.height, 90, 'asteroid_large', 1)
        spaceship = SpaceObject(500, 300, self.width, self.height, 0, 'spaceship', 0)


        #! debug code 
        if self.debug:
            from inputimeout import inputimeout, TimeoutOccurred

        asteroid_list = [obj1, obj2]
        bullet_list = []
        score = 0
        fuel = 100

        while True:
            # 1. Receive player input
            if self.debug:
                try:
                    key = inputimeout('', timeout=10)
                except:
                    pass

                # spaceship control
                if key == 'w':           
                    spaceship.move_forward()
                elif key == 'a':
                    spaceship.turn_left()
                elif key == 'd':
                    spaceship.turn_right()
                # elif key == 's':
                #     pass # TODO : bullet
                elif key == 'q':
                    break
                key = None
            else:
                thrust, left, right, bullet = self.player.action(spaceship, [], [], 200, 100)

                if thrust:
                    spaceship.move_forward()
                elif left:
                    spaceship.turn_left()

            # # 2. Process game logic
            # #obj1.move_forward()
            # #obj2.move_forward()

            # for asteroid in asteroid_list:
            #     if spaceship.collide_with(asteroid):
            #         score -= 50

            # 3. Draw the game state on screen using the GUI class
                                 
            self.GUI.update_frame(spaceship, asteroid_list, bullet_list, score, fuel)

            # Game loop should stop when:
            # - the spaceship runs out of fuel, or
            # - no more asteroids are available

            #break

        # Display final score
        # self.GUI.finish(???)

    # You can add additional methods if required





#***************************************#
# game = Engine('examples/game_state_good.txt', Player, GUI)




# game = Engine('examples/game_state_good.txt', Player, GUI)
# # game.import_state()

# if __name__ == '__main__':



#     file_path = 'examples/game_state_test.txt'
#     game = Engine(file_path, Player, GUI)




