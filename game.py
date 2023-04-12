import pygame
import button

class Game_Block:
    def __init__(self):
        self.x9 = None
        self.y9 = None

    __white = (255, 255, 255)
    __light_grey = (200, 200, 200)
    __black = (0, 0, 0)
    __blue = (0, 122, 255)
    __red = (255, 0, 0)
    __grey = (128, 128, 128)
    __yellow = (255, 255, 0)


    __user_level = 0
    __user_level_temp = []
    __player = {'row': 0, 'col': 0}
    player_rect = pygame.Rect(0, 0, 0, 0)

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

    def __ender(self, n):
        end = [[j for j in i] for i in n]
        # given a certain matrix, returns the ending one
        for i in range(len(end)):
            for j in range(len(end[0])):
                if end[i][j] == 2:
                    end[i][j] = 1
                if end[i][j] == 9:
                    end[i][j] = 2  # end will be the objective matrix, since the beggining point will be a 1, and the ending 9 will be the last pos of the block
        return end  # end matrix

    def __check_9(self,m):
        pos1, pos2 = 0, 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 9:
                    pos1 = i
                    pos2 = j
        return pos1, pos2

    def __get_pos(self, m):
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

    def __get_status(self, m):
        c1 = self.__get_pos(m)[0]
        c2 = self.__get_pos(m)[1]
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

    # Creation of the first instance of the block

    def __string_appender(self, m, operator):  # operator is the concatenation of direction_state
        if len(m) == 6:
            if len(m[0]) == 10:
                temp = 1
            else:
                temp = 2
        else:
            temp = 3
        # way to know which list
        c1 = self.__get_pos(m)[0]
        c2 = self.__get_pos(m)[1]
        stat = self.__get_status(m)
        out = 'self.b.' + operator + '(' + str(c1) + ',' + str(c2) + ",'" + stat + "'," + 'level' + str(temp) + ')'
        return out  # to execute out later, exec(out)

    def __operator_maker(self, a, b):
        c = str(a) + '_' + str(b)  # a=direction, b=state
        return c

    def __aux_9(self, m, a, b):
        if m[a][b] == 1:
            m[a][b] = 9
        return m

    def __save(self):
        self.x9 = self.__check_9(self.__user_level)[0]
        self.y9 = self.__check_9(self.__user_level)[1]


    def set_level(self, level, __screen):
        match level:
            case 1:
                self.__user_level = self.level1
            case 2:
                self.__user_level = self.level2
            case 3:
                self.__user_level = self.level3
        self.__save()
        self.__user_level_temp = [[j for j in i] for i in self.__user_level]
        self.__draw_level(__screen)



    def update_player_position(self, event, __screen):
        self.__end = [[j for j in i] for i in self.__ender(self.__user_level_temp)]
        stat = self.__get_status(self.__user_level)
        x, y = self.__get_pos(self.__user_level)

        if self.__end==True:
            __font = pygame.font.Font(None, 32)
            __text_rect = __font.render('Congratulations', True, self.__blue)
            return

        game_over = False

        # Move up with W or Up arrow
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            if stat == 'stand':
                if x >= 2:
                    if stat == 'stand' and self.__user_level[x - 1][y] != 0 and self.__user_level[x - 2][y] != 0:
                        self.__user_level[x-1][y] = 2
                        self.__user_level[x-2][y] = 2
                        self.__user_level[x][y] = 1
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'vert':
                if x >= 1:
                    if stat == 'vert' and self.__user_level[x - 1][y] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x+1][y] = 1
                        self.__user_level[x-1][y] = 2
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'horiz':
                if x-1 >= 0:
                    if stat == 'horiz' and self.__user_level[x-1][y] != 0 and self.__user_level[x-1][y+1] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x][y+1] = 1
                        self.__user_level[x-1][y] = 2
                        self.__user_level[x-1][y+1] = 2
                    else:
                        game_over = True
                else:
                    game_over = True

        # Move down with S or Down arrow key
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if stat == 'stand':
                if x < len(self.__user_level) - 2:
                    if stat == 'stand' and self.__user_level[x+1][y] != 0 and self.__user_level[x+2][y] != 0:
                        self.__user_level[x+1][y] = 2
                        self.__user_level[x+2][y] = 2
                        self.__user_level[x][y] = 1
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'vert':
                if x < len(self.__user_level[0]) - 2:
                    if stat == 'vert' and self.__user_level[x+1][y] != 0 and self.__user_level[x+2][y] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x+1][y] = 1
                        self.__user_level[x+2][y] = 2
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'horiz':
                if x+1 < len(self.__user_level):
                    if stat == 'horiz' and self.__user_level[x+1][y] != 0 and self.__user_level[x+1][y+1] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x][y+1] = 1
                        self.__user_level[x+1][y+1] = 2
                        self.__user_level[x+1][y] = 2
                    else:
                        game_over = True
                else:
                    game_over = True

        # Move left with A or Left arrow key
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if stat == 'stand':
                if y>=2:
                    if stat == 'stand' and self.__user_level[x][y-1] != 0 and self.__user_level[x][y-2] != 0:
                        self.__user_level[x][y-1] = 2
                        self.__user_level[x][y-2] = 2
                        self.__user_level[x][y] = 1
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'vert':
                if y>=1:
                    if stat == 'vert' and self.__user_level[x][y - 1] != 0 and self.__user_level[x + 1][y - 1] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x + 1][y] = 1
                        self.__user_level[x][y - 1] = 2
                        self.__user_level[x + 1][y - 1] = 2
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'horiz':
                if y >= 1:
                    if stat == 'horiz' and self.__user_level[x][y - 1] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x][y + 1] = 1
                        self.__user_level[x][y - 1] = 2
                        status = 'stand'
                    else:
                        game_over = True
                else:
                    game_over = True

        # Move right with D or Right arrow key
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if stat == 'stand':
                if y < len(self.__user_level[0])-2:
                    if stat == 'stand' and self.__user_level[x][y+1] != 0 and self.__user_level[x][y+2] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x][y+2] = 2
                        self.__user_level[x][y+1] = 2
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'vert':
                if y + 1 < len(self.__user_level[0]):
                    if stat == 'vert' and self.__user_level[x][y + 1] != 0 and self.__user_level[x + 1][y + 1] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x + 1][y] = 1
                        self.__user_level[x][y + 1] = 2
                        self.__user_level[x + 1][y + 1] = 2
                    else:
                        game_over = True
                else:
                    game_over = True
            elif stat == 'horiz':
                if y + 2 < len(self.__user_level[0]):
                    if stat == 'horiz' and self.__user_level[x][y + 2] != 0:
                        self.__user_level[x][y] = 1
                        self.__user_level[x][y + 1] = 1
                        self.__user_level[x][y + 2] = 2
                        status = 'stand'
                    else:
                        game_over = True
                else:
                    game_over = True
        # print(str(game_over))
        if game_over == True:
            self.__user_level = [[j for j in i] for i in self.__user_level_temp]
        if self.__user_level == self.__end:
            '''__font = pygame.font.Font(None, 32)
            __text_rect = __font.render('Congratulations', True, self.__blue)'''
            pygame.quit()
        self.__draw_level(__screen)
    def __draw_level(self, __screen):
            square_size = 40
            num_rows = len(self.__user_level)
            num_cols = len(self.__user_level[0])
            c = 0
            # start_row = self.__get_pos(self.__user_level)[0]
            # start_col = self.__get_pos(self.__user_level)[1]

            for row in range(num_rows):
                for col in range(num_cols):
                    square_color = self.__grey
                    if self.__user_level[row][col] == 0:
                        square_color = self.__white
                    elif self.__user_level[row][col] == 1:
                        square_color = self.__blue
                    elif self.__user_level[row][col] == 2:
                        square_color = self.__yellow
                    elif self.__user_level[row][col] == 9:
                        c += 1
                        square_color = self.__red
                    if c == 0:
                        self.__aux_9(self.__user_level, self.x9, self.y9)

                    rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
                    pygame.draw.rect(__screen, square_color, rect)



