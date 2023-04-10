
class Game_Block:


    # ----------------------------------------------------------------------------#

    level1 = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 2, 1, 1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 1, 1, 1, 9, 1],
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]

    level2 = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
              [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
              [1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 9, 1],
              [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]

    level3 = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
              [2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 9, 1],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]]

    # missing theoretical level 3 with buttons to bridges represented by 4, and will 2 live
    def printer(self, m):
        for i in m:
            print(i)
        print("\n")  # matrix printer aux function

    def ender(self, n):
        end = [[j for j in i] for i in n]
        # given a certain matrix, returns the ending one
        for i in range(len(end)):
            for j in range(len(end[0])):
                if end[i][j] == 2:
                    end[i][j] = 1
                if end[i][j] == 9:
                    end[i][j] = 2  # end will be the objective matrix, since the beggining point will be a 1, and the ending 9 will be the last pos of the block
        return end  # end matrix

    def check_9(self,m):
        pos1, pos2 = 0, 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 9:
                    pos1 = i
                    pos2 = j
        return pos1, pos2

    def compare_states(self,initial_state, final_state):
        for i in range(len(initial_state)):
            for j in range(len(initial_state[0])):
                if initial_state[i][j] != final_state[i][j]:
                    return False
        return True  # check for the right names when calling!!!

    def legal_moves(self,m):
        stat = self.get_status(m)
        x, y = self.get_pos(m)
        l = []

        if x >= 2:
            if stat == 'stand' and m[x - 1][y] != 0 and m[x - 2][y] != 0:
                l.append('up_stand')
        if x < len(m) - 2:
            if stat == 'stand' and m[x + 1][y] != 0 and m[x + 2][y] != 0:
                l.append('down_stand')
        if y >= 2:
            if stat == 'stand' and m[x][y - 1] != 0 and m[x][y - 2] != 0:
                l.append('left_stand')
        if y < len(m[0]) - 2:
            if stat == 'stand' and m[x][y + 1] != 0 and m[x][y + 2] != 0:
                l.append('right_stand')
        #####
        if x >= 1:
            if stat == 'vert' and m[x - 1][y] != 0:
                l.append('up_vert')
        if x < len(m) - 2:
            if stat == 'vert' and m[x + 1][y] != 0 and m[x + 2][y] != 0:
                l.append('down_vert')
        if y >= 1:
            if stat == 'vert' and m[x][y - 1] != 0 and m[x + 1][y - 1] != 0:
                l.append('left_vert')
        if y + 1 < len(m[0]):
            if stat == 'vert' and m[x][y + 1] != 0 and m[x + 1][y + 1] != 0:
                l.append('right_vert')
        #####
        if x - 1 >= 0:
            if stat == 'horiz' and m[x - 1][y] != 0 and m[x - 1][y + 1] != 0:
                l.append('up_horiz')
        if x + 1 < len(m):
            if stat == 'horiz' and m[x + 1][y] != 0 and m[x + 1][y + 1] != 0:
                l.append('down_horiz')
        if y >= 1:
            if stat == 'horiz' and m[x][y - 1] != 0:
                l.append('left_horiz')
        if y + 2 < len(m[0]):
            if stat == 'horiz' and m[x][y + 2] != 0:
                l.append('right_horiz')
        return l

    def get_pos(self, m):
        global c1, c2
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 2:
                    c1 = i
                    c2 = j
                    break
            else:
                continue
            break  # explanation on mar18/19
        return c1, c2

    def get_status(self, m):
        c1 = self.get_pos(m)[0]
        c2 = self.get_pos(m)[1]
        c3, c4 = -1, -1
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 2:
                    if i != c1 or j != c2:
                        c3 = i
                        c4 = j
        if c3 == -1 and c4 == -1:
            return 'stand'
        else:
            if abs(c1 - c3) == 1:
                return 'vert'
            return 'horiz'

    # This changes when in the graphic environment a level is chosen by the program user.
    def sizer(self, m):
        rows = len(m)
        cols = len(m[0])
        return rows, cols

    # Creation of the first instance of the block
    def create_block(self, m):
        c1 = self.get_pos(m)[0]
        c2 = self.get_pos(m)[1]
        stat = self.get_status(m)
        b = Game_Block(c1, c2, stat)
        return b

    def string_appender(self, m, operator):  # operator is the concatenation of direction_state
        if len(m) == 6:
            if len(m[0]) == 10:
                temp = 1
            else:
                temp = 2
        else:
            temp = 3
        # way to know which list
        c1 = self.get_pos(m)[0]
        c2 = self.get_pos(m)[1]
        stat = self.get_status(m)
        out = 'init.' + operator + '(' + str(c1) + ',' + str(c2) + ",'" + stat + "'," + 'level' + str(temp) + ')'
        return out  # to execute out later, exec(out)

    def operator_maker(self, a, b):
        c = str(a) + '_' + str(b)  # a=direction, b=state
        return c

    def aux_9(self, m, a, b):
        if m[a][b] == 1:
            m[a][b] = 9
        return m

    '''def main(self,lvl):
        printer(lvl)
        final_state = ender(lvl)
        x9 = check_9(lvl)[0]
        y9 = check_9(lvl)[1]
        while not compare_states(lvl, final_state):
            y = str(input('Direção: '))
            state = get_status(lvl)
            if y == 'a':
                direction = 'left'
                op = operator_maker(direction, state)
                if op in legal_moves(lvl):
                    out = string_appender(lvl, op)
                    exec(out)
                else:
                    continue
            elif y == 'w':
                direction = 'up'
                op = operator_maker(direction, state)
                if op in legal_moves(lvl):
                    out = string_appender(lvl, op)
                    exec(out)
                else:
                    continue
            elif y == 's':
                direction = 'down'
                op = operator_maker(direction, state)
                if op in legal_moves(lvl):
                    out = string_appender(lvl, op)
                    exec(out)
                else:
                    continue
            elif y == 'd':
                direction = 'right'
                op = operator_maker(direction, state)
                if op in legal_moves(lvl):
                    out = string_appender(lvl, op)
                    exec(out)
                else:
                    continue
            else:
                continue
            print(legal_moves(lvl))
            lvl = aux_9(lvl, x9, y9)
            printer(lvl)
            print(get_pos(lvl), get_status(lvl))'''
    def set_level(self, level):
        match level:
            case 1:
                user_level = self.level1
            case 2:
                user_level = self.level2
            case 3:
                user_level = self.level3
        final_state=self.ender(user_level)
        self.printer(user_level)


    def up_stand(self, x, y, status, m):
        if x >= 2:
            if status == 'stand' and m[x - 1][y] != 0 and m[x - 2][y] != 0:
                m[x - 1][y] = 2
                m[x - 2][y] = 2
                m[x][y] = 1
                status = 'vert'
                return m, status  # returning now the status as well, an updating it. ask how to implement it
        return None

    def down_stand(self, x, y, status, m):
        if x < len(m) - 2:
            if status == 'stand' and m[x + 1][y] != 0 and m[x + 2][y] != 0:
                m[x + 1][y] = 2
                m[x + 2][y] = 2
                m[x][y] = 1
                status = 'vert'
                return m, status
        return None

    def left_stand(self, x, y, status, m):
        if y >= 2:
            if status == 'stand' and m[x][y - 1] != 0 and m[x][y - 2] != 0:
                m[x][y - 1] = 2
                m[x][y - 2] = 2
                m[x][y] = 1
                status = 'horiz'
                return m, status
        return None

    def right_stand(self, x, y, status, m):
        if y < len(m[0]) - 2:
            if status == 'stand' and m[x][y + 1] != 0 and m[x][y + 2] != 0:
                m[x][y + 1] = 2
                m[x][y + 2] = 2
                m[x][y] = 1
                status = 'horiz'
                return m, status
        return None

    # ----------------------------------------------------------------------------#

    def up_vert(self, x, y, status, m):
        if x >= 1:
            if status == 'vert' and m[x - 1][y] != 0:
                m[x][y] = 1
                m[x + 1][y] = 1
                m[x - 1][y] = 2
                status = 'stand'
                return m, status
        return None

    def down_vert(self, x, y, status, m):
        if x < len(m[0]) - 2:
            if status == 'vert' and m[x + 2][y] != 0 and m[x + 1][y] != 0:
                m[x][y] = 1
                m[x + 1][y] = 1
                m[x + 2][y] = 2
                status = 'stand'
                return m, status
        return None

    def left_vert(self, x, y, status, m):
        if y >= 1:
            if status == 'vert' and m[x][y - 1] != 0 and m[x + 1][y - 1] != 0:
                m[x][y] = 1
                m[x + 1][y] = 1
                m[x][y - 1] = 2
                m[x + 1][y - 1] = 2
                status = status  # still vertical
                return m, status
        return None

    def right_vert(self, x, y, status, m):
        if y + 1 < len(m[0]):
            if status == 'vert' and m[x][y + 1] != 0 and m[x + 1][y + 1] != 0:
                m[x][y] = 1
                m[x + 1][y] = 1
                m[x][y + 1] = 2
                m[x + 1][y + 1] = 2
                status = status  # still vertical
                return m, status
        return None

    # ----------------------------------------------------------------------------#

    def up_horiz(self, x, y, status, m):
        if x - 1 >= 0:
            if status == 'horiz' and m[x - 1][y] != 0 and m[x - 1][y + 1] != 0:
                m[x][y] = 1
                m[x][y + 1] = 1
                m[x - 1][y] = 2
                m[x - 1][y + 1] = 2
                status = status  # still horizontal
                return m, status
        return None

    def down_horiz(self, x, y, status, m):
        if x + 1 < len(m):
            if status == 'horiz' and m[x + 1][y] != 0 and m[x + 1][y + 1] != 0:
                m[x][y] = 1
                m[x][y + 1] = 1
                m[x + 1][y] = 2
                m[x + 1][y + 1] = 2
                status = status  # still horizontal
                return m, status
        return None

    def left_horiz(self, x, y, status, m):
        if y >= 1:
            if status == 'horiz' and m[x][y - 1] != 0:
                m[x][y] = 1
                m[x][y + 1] = 1
                m[x][y - 1] = 2
                status = 'stand'
                return m, status
        return None

    def right_horiz(self, x, y, status, m):
        if y + 2 < len(m[0]):
            if status == 'horiz' and m[x][y + 2] != 0:
                m[x][y] = 1
                m[x][y + 1] = 1
                m[x][y + 2] = 2
                status = 'stand'
                return m, status
        return None

    # ----------------------------------------------------------------------------#




####################


'''init = create_block(level3)
print(init)

init.main(level3)'''

