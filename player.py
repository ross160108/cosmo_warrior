class Player:
    def __init__(self):
        
        # Enter your code here
        
        pass

    # TODO
    def is_caution(self):
        # return False, None

        


        for _ in range(t):
            snx, sny = self.expect( )

        '''
        

        return True, 'forward'
        return True, 'turn_left'
        '''

    def action(self, spaceship, asteroid_ls, bullet_ls, fuel, score):

        nx, ny = obj.get_xy()
        for obj in asteroid_ls: #self.asteroid_list = [obj1, obj2]
            nx, ny = obj.expect(nx, ny)

        self.spaceship = spaceship
        self.asteroid_ls = asteroid_ls
        self.bullet_ls = bullet_ls
        self.fuel = fuel
        self.score = score
        

        thrust = True
        left = False
        right = False
        bullet = False




        # flag1, act = self.is_caution()
        # if flag1:
        #     if act == 'forward':
        #         thrust = True
        # else:
        #     # 공격 or 이동 (사냥하러)
        #     flag2 = self.is_bullet_range()
        #     if flag2:
        #         bullet = True

        #     else:
        #         flag3, act = self.hunt()
        #         if act == 'forward':
        #             thursh = True


        return (thrust, left, right, bullet)

    # You can add additional methods if required
