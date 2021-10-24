# import config
# from space_object import SpaceObject

# #!! 지워야됨
# from player import Player
# from gui import GUI
# #!!

# class Engine:
#     def __init__(self, game_state_filename, player_class, gui_class):
#         self.import_state(game_state_filename)
#         self.player = player_class()
#         self.GUI = gui_class(self.width, self.height)

#     def import_state(self, game_state_filename):
#         self.width = 900 # CHANGE THIS!!!
#         self.height = 600 # CHANGE THIS!!!


#         # Enter your code here
#         try:
#             with open(game_state_filename, 'r') as f:
#                 while True:
#                     data = f.readline()
#                     if not data:
#                         break
#                     for_key = data.split()[0]
#                     for_value = data.split()[1].split(',')
                
#         except FileNotFoundError:
#             print('Error: unable to open {}'.format(game_state_filename))

        


                
                

                





#     def export_state(self, game_state_filename):
        
#         # Enter your code here
        
#         pass

#     def run_game(self):

#         spaceship1 = SpaceObject(300,300,10,10,30,'spaceship', 2)
#         i = 0

#         # while True:
#         while i < 200:
#             # 1. Receive player input
            
#             # 2. Process game logic

#             # 3. Draw the game state on screen using the GUI class
#             # self.GUI.update_frame(???)

#             #!
#             self.GUI.update_frame(spaceship1, [], [], 10, 10)
            

#             # Game loop should stop when:
#             # - the spaceship runs out of fuel, or
#             # - no more asteroids are available

#             # break
#             i += 1

#         # Display final score
#         # self.GUI.finish(???)

#     # You can add additional methods if required







# #***************************************#
# # game = Engine('examples/game_state_good.txt', Player, GUI)
# # game.import_state()







# import config
# from space_object import SpaceObject

# class Engine:
#     #Engine('examples/game_state_good.txt', Player, GUI)
#     def __init__(self, game_state_filename, player_class, gui_class):
#         self.import_state(game_state_filename)
#         self.player = player_class()
#         self.GUI = gui_class(self.width, self.height)

#     def import_state(self, game_state_filename):
#         self.width = 900 # CHANGE THIS!!!
#         self.height = 600 # CHANGE THIS!!!

#         # Enter your code here


#     def export_state(self, game_state_filename):
        
#         # Enter your code here
        
#         pass

#     def run_game(self):
#         # self, x, y, width, height, angle, obj_type, id):
#         obj1 = SpaceObject(150, 100, self.width, self.height, 30, 'asteroid_large', 1)
#         obj2 = SpaceObject(200, 300, self.width, self.height, 90, 'asteroid_large', 1)
#         spaceship = SpaceObject(500, 300, self.width, self.height, 0, 'spaceship', 0)
        
#         from inputimeout import inputimeout, TimeoutOccurred
#         while True:
#             # 1. Receive player input
#             try:
#                 key= inputimeout('', timeout=10)
#             except:
#                 pass

#             if key == 'w':           
#                 spaceship.move_forward()
#             elif key == 'a':
#                 spaceship.turn_left()
#             elif key == 'd':
#                 spaceship.turn_right()
#             elif key == 'q':
#                 break


#             # self.GUI.update_frame(spaceship, [obj1, obj2], [], 50, 200)
            

#             # # 1. Receive player input
            
#             # # 2. Process game logic
#             # obj1.turn_left()
#             # obj1.move_forward()
#             # obj2.turn_right()
#             # obj2.move_forward()


#             # # spaceship.move_forward()

#             # # 3. Draw the game state on screen using the GUI class
#             self.GUI.update_frame(spaceship, [obj1, obj2], [], 50, 200)

#             # # Game loop should stop when:
#             # # - the spaceship runs out of fuel, or
#             # # - no more asteroids are available

#             #break

#         # Display final score
#         # self.GUI.finish(???)

#     # You can add additional methods if required












#!

import config
from space_object import SpaceObject


#!! 지워야됨
from player import Player
from gui import GUI
#!!



class Engine:
    #Engine('examples/game_state_good.txt', Player, GUI)
    def __init__(self, game_state_filename, player_class, gui_class):
        self.import_state(game_state_filename)
        self.player = player_class()
        self.GUI = gui_class(self.width, self.height)

    def import_state(self, game_state_filename):
        self.width = 900 # CHANGE THIS!!!
        self.height = 600 # CHANGE THIS!!!

        # Enter your code here

        try:
            with open(game_state_filename, 'r') as f:
                while True:
                    data = f.readline()
                    if not data:
                        break
                    for_key = data.split()[0]
                    for_value = data.split()[1].split(',')
                    print(for_key)
                    print(for_value)                
        except FileNotFoundError:
            print('Error: unable to open {}'.format(game_state_filename))


# width, height, score, spaceship, fuel, asteroids_count, bullets_count, upcoming_asteroids_count






    def export_state(self, game_state_filename):
        
        # Enter your code here
        
        pass

    def run_game(self):
        # self, x, y, width, height, angle, obj_type, id):
        obj1 = SpaceObject(150, 100, self.width, self.height, 30, 'asteroid_large', 1)
        obj2 = SpaceObject(200, 300, self.width, self.height, 90, 'asteroid_large', 1)
        spaceship = SpaceObject(500, 300, self.width, self.height, 0, 'spaceship', 0)


        #! debug code 
        from inputimeout import inputimeout, TimeoutOccurred

        asteroid_list = [obj1, obj2]
        bullet_list = []
        score = 0
        fuel = 100

        while True:
            # 1. Receive player input
            
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
            elif key == 'q':
                break
            key = None
            
            # 2. Process game logic
            #obj1.move_forward()
            #obj2.move_forward()

            for asteroid in asteroid_list:
                if spaceship.collide_with(asteroid):
                    score -= 50

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