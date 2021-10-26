import config
from space_object import SpaceObject





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
ITER_OBJECTS = [
    'upcoming_asteroid_small',
    'upcoming_asteroid_large',
    'asteroid_large',
    'asteroid_small',
    'bullet'
]
ALL_GAME_KEYS = GAME_STATE_KEYS + ITER_OBJECTS
COUNT_PARAM = [
    'asteroids_count',
    'upcoming_asteroids_count',
    'bullets_count'
]
CURRENT_ASTEROIDS = [
    'asteroid_large',
    'asteroid_small'
]
UPCOMING_ASTEROIDS = [
    'upcoming_asteroid_small',
    'upcoming_asteroid_large'
]

class Engine:
    #Engine('examples/game_state_good.txt', Player, GUI)
    def __init__(self, game_state_filename, player_class, gui_class):
        # vars
        self.game_dict = {}
        #self.bullets = []
        #self.asteroid_list = []

        self.import_state(game_state_filename)
        
        self.player = player_class()
        self.width = self.game_dict['width']
        self.height = self.game_dict['height']
        self.GUI = gui_class(self.width, self.height)

    def import_state(self, game_state_filename):
        lines = []
        try:
            f = open(game_state_filename, 'r')
            while True:
                data = f.readline()
                if not data:
                    break

                # key_name: str
                lines.append(data.replace('\n', ''))
                
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError('Error: unable to open {}'.format(game_state_filename))
            
        if len(lines) == 0:
            raise ValueError('Error: game state incomplete')

        offset = 0
        for i, ref_key in enumerate(GAME_STATE_KEYS):
            # 1-1. check the number of inputs

            if len(lines[i+offset].split()) != 2:
                raise ValueError('Error: expecting a key and value in line <line number>')
            key, value = lines[i+offset].split()

            # 1-2. check unexpected keys or game state incomplete
            if ref_key != key:
                if key in GAME_STATE_KEYS or key in ITER_OBJECTS:
                    raise ValueError(f'Error: unexpected key: {key} in line <line number>')
                else:
                    raise ValueError('Error: game state incomplete')
            
            # 2. check value 
            if ref_key in ITER_OBJECTS + ['spaceship']:
                length_should_be = 4
            else:
                length_should_be = 1

            # 2-1 value length
            if len(value.split(',')) != length_should_be:
                raise ValueError('Error: expecting a key and value in line <line number>')
            # 2-2 value type
            if length_should_be == 1:
                try:
                    value = int(value)
                    if value < 0:
                        raise ValueError('Error: invalid data type in line <line number>')    
                except:
                    raise ValueError('Error: invalid data type in line <line number>')
            elif length_should_be == 4:
                try:
                    value = [val for val in value.split(',')]
                    value[0] = float(value[0])
                    value[1] = float(value[1])
                    value[2] = float(value[2])
                    value[3] = float(value[3])
                except:
                    raise ValueError('Error: invalid data type in line <line number>')                            
            
            # internal iter. -> check asteroids, upcoming_asteroids, bullets 
            self.game_dict[key] = value
            if ref_key in COUNT_PARAM:
                

                if ref_key == 'asteroids_count':
                    possible_names = CURRENT_ASTEROIDS
                elif ref_key == 'bullets_count':
                    possible_names = ['bullet']
                elif ref_key == 'upcoming_asteroids_count':
                    possible_names = UPCOMING_ASTEROIDS
                else:
                    assert False

                # iter. object
                self.game_dict[ref_key] = []
                for t in range(1, value+1):
                    obj_key, obj_value = lines[i+offset+t].split()
                    
                    # check key
                    if not obj_key in possible_names:
                        if obj_key in ALL_GAME_KEYS:
                            raise ValueError(f'Error: unexpected key: {obj_key} in line <line number>')
                        else:
                            raise ValueError('Error: game state incomplete')
                    
                    # check value
                    if 4 != len(obj_value.split(',')):
                        raise ValueError('Error: expecting a key and value in line <line number>')

                    try:
                        obj_value = [val for val in obj_value.split(',')]
                        obj_value[0] = float(obj_value[0])
                        obj_value[1] = float(obj_value[1])
                        obj_value[2] = float(obj_value[2])
                        obj_value[3] = float(obj_value[3])
                    except:
                        raise ValueError('Error: invalid data type in line <line number>')                            

                    
                    self.game_dict[ref_key].append([obj_key] + obj_value)
                offset += value

        '''
        print('ok')
        for key in self.game_dict:
            print(key, self.game_dict[key])
        exit(1)  
        '''
        
  

    

    def export_state(self, game_state_filename):
        pass
        '''
        f1 = open(game_state_filename, 'w')
        for key in self.game_dict:
            if isinstance(self.game_dict[key], list):
                value_str = ''
                for val_idx in range(len(self.game_dict[key])):
                    value_str += str(self.game_dict[key][val_idx])
                    if val_idx == len(self.game_dict[key])-1:
                        continue
                    value_str += ','
                a = '{} {}\n'.format(key, value_str)
                f1.write(a)

            else:
                a = '{} {}\n'.format(key, str(self.game_dict[key]))
                f1.write(a)
        '''
        

    def run_game(self):
        # self, x, y, width, height, angle, obj_type, id):
        obj1 = SpaceObject(150, 100, self.width, self.height, 30, 'asteroid_large', 1)
        obj2 = SpaceObject(200, 300, self.width, self.height, 90, 'asteroid_large', 1)
        spaceship = SpaceObject(500, 300, self.width, self.height, 0, 'spaceship', 0)


        #! debug code 
        

        asteroid_list = [obj1, obj2]
        bullet_list = []
        score = 0
        fuel = 100

        while True:
            # 1. Receive player input
            

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
# game.import_state()