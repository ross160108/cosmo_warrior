class Player:
    def __init__(self):
        
        # Enter your code here
        
        pass

    # TODO
    def is_caution(self):
        return False, None
        
        '''
        

        return True, 'forward'
        return True, 'turn_left'
        '''

    def action(self, spaceship, asteroid_ls, bullet_ls, fuel, score):
        thrust = False
        left = False
        right = False
        bullet = False

        flag1, act = self.is_caution()
        if flag1:
            if act == 'forward':
                thrust = True
        else:
            # 공격 or 이동 (사냥하러)
            flag2 = self.is_bullet_range()
            if flag2:
                bullet = True

            else:
                flag3, act = self.hunt()
                if act == 'forward':
                    thursh = True


        return (thrust, left, right, bullet)

    # You can add additional methods if required
