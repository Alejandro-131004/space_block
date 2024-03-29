import time
import button


class Block:
    # adapted from notebook, not entirely used
    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y, self.status))

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.status) + ")"

    # this is to be able to call the parts of the class as if it were a tuple
    # x = object[0] wouldn't work otherwise
    def __getitem__(self, idx):
        if idx == 0:
            return self.x
        elif idx == 1:
            return self.y
        elif idx == 2:
            return self.status
        else:
            raise IndexError('Block index out of range')
    # ----------------------------------------------------------------------------#

    # ----------------------------------------------------------------------------#

# solution class
class Solution:
    def __init__(self, level, alg):
        self.start_game(level, alg)

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
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 9, 1],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]]

    # operators
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

    #---------#

    # some of these functions were explained previously on game.py
    def ender(self, n):
        end = [[j for j in i] for i in n]
        # given a certain matrix, returns the ending one
        for i in range(len(end)):
            for j in range(len(end[0])):
                if end[i][j] == 2:
                    end[i][j] = 1
                if end[i][j] == 9:
                    end[i][
                        j] = 2  # end will be the objective matrix, since the beggining point will be a 1, and the ending 9 will be the last pos of the block
        return end  # end matrix

    # explained
    def check_9(self, m):
        pos1, pos2 = 0, 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 9:
                    pos1 = i
                    pos2 = j
        # returns the position of the 9
        return pos1, pos2

    # compares states, given 2 matrices
    def compare_states(self, initial_state, final_state):
        for i in range(len(initial_state)):
            for j in range(len(initial_state[0])):
                if initial_state[i][j] != final_state[i][j]:
                    return False
        return True  # check for the right names when calling!!!

    # returns a list of the legal moves, given the matrix
    def legal_moves(self, m):
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

    # explained
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

    # explained
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

    # Creation of the first instance of the block
    def create_block(self, m):
        c1 = self.get_pos(m)[0]
        c2 = self.get_pos(m)[1]
        stat = self.get_status(m)
        self.b = Block(c1, c2, stat)
        return self.b

    # explained
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
        out = 'self.' + operator + '(' + str(c1) + ',' + str(c2) + ",'" + stat + "'," + 'self.level' + str(temp) + ')'
        return out  # to execute out later, exec(out)

    # explained
    def operator_maker(self, a, b):
        c = str(a) + '_' + str(b)  # a=direction, b=state
        return c

    # explained
    def aux_9(self, m, a, b):
        if m[a][b] == 1:
            m[a][b] = 9
        return m

    # extract the directions from the very confusing string from the search algorithm
    def extract_directions(self, input_string):
        directions = []
        input_list = input_string.split("_")
        for item in input_list:
            if item.endswith("right"):
                directions.append("right")
            elif item.endswith("left"):
                directions.append("left")
            elif item.endswith("up"):
                directions.append("up")
            elif item.endswith("down"):
                directions.append("down")
        print(f"Amount of directions: {len(directions)}")
        return " -> ".join(directions)

    # given the tuple of the state (x, y, status), the operator
    def apply_action(self, z, op, state):
        m = self.get_matrix(z, state)  # z is the lvl
        out = self.string_appender(m, op)
        exec(out)
        r = (self.get_pos(m)[0], self.get_pos(m)[1], self.get_status(m))
        return r

    # gets matrix from the tuple
    def get_matrix(self, lvl, state):  # state is a tuple (x1,x2,status)
        for i in range(len(lvl)):
            for j in range(len(lvl[0])):
                if lvl[i][j] == 2:
                    lvl[i][j] = 1
        x9 = self.check_9(lvl)[0]
        y9 = self.check_9(lvl)[1]
        lvl[x9][y9] = 9  # if block on the hole, not right,the hole would be deleted
        a = int(state[0])
        b = int(state[1])
        lvl[a][b] = 2
        status = state[2]
        if status == 'stand':
            return lvl
        else:
            if status == 'vert':
                lvl[a + 1][b] = 2
                return lvl
            elif status == 'horiz':
                lvl[a][b + 1] = 2
                return lvl
        return 404

    # instead of comparing matrices, compare the tuples
    def compare_states2(self, a, b):
        # compare_states2 check the tuple, not the matrix, temporary
        a1 = self.clean_string(a)
        b1 = self.clean_string(b)
        if str(a1) == str(b1):
            return True
        return False

    # compliment to compare_states2
    def clean_string(self, s):
        cleaned = ''
        for c in s:
            if c != "'":
                cleaned += str(c)
        return cleaned

    ####################

    # breadth-first search algorithm implementation
    def bfs(self, init, final, level):
        start = time.time()
        move_sequence = ''
        expand = [(init, move_sequence)]  # expand is the queue, each element is a tuple of (state, move_sequence)
        visited = [init]
        while len(expand) > 0:
            state, move_sequence = expand.pop(0)
            if self.compare_states2(state, final):
                end = time.time()  # running time
                print(f'running time: {round((end - start) * 1000, 1)} ms')
                return move_sequence
            else:
                for legal in self.legal_moves(self.get_matrix(level, state)):
                    new_state = self.apply_action(level, legal, state)
                    if new_state not in visited:
                        new_move_sequence = move_sequence + legal  # generate new move sequence
                        visited.append(new_state)
                        expand.append((new_state, new_move_sequence))
                        # to not forget that extract_directions

    # depth-first search algorithm implementation
    def dfs(self, init, final, nivel):
        start = time.time()  # record the start time of the search
        move_sequence = ''  # initialize the move sequence as an empty string
        stack = [(init, move_sequence)]  # initialize the stack with the initial state and the empty move sequence
        visited = [init]  # initialize the list of visited states with the initial state
        while len(stack) > 0:  # continue while the stack is not empty
            state, move_sequence = stack.pop()  # remove the last state from the stack and get its move sequence
            if self.compare_states2(state, final):  # check if the state is the final state
                end = time.time()  # record the end time of the search
                print(f'running time: {round((end - start) * 1000, 1)} ms')  # print the running time of the search
                return move_sequence  # return the move sequence that leads to the final state
            else:
                for legal in self.legal_moves(
                        self.get_matrix(nivel, state)):  # generate all legal moves from the current state
                    new_state = self.apply_action(nivel, legal,
                                                  state)  # apply a legal move to the current state to get a new state
                    if new_state not in visited:  # check if the new state has not been visited before
                        new_move_sequence = move_sequence + legal  # generate a new move sequence that includes the current move
                        visited.append(new_state)  # add the new state to the list of visited states
                        stack.append(
                            (new_state, new_move_sequence))  # add the new state and its move sequence to the stack
        return None  # return None if no solution is found

    # heuristic
    def manhattan_distance(self, state, final):
        """
        Calculates the Manhattan distance between two states.
        """
        distance1 = abs(int(state[0]) - int(final[0])) + abs(int(state[1]) - int(final[1]))
        if state[2] == 'stand':
            distance = distance1-1
        elif state[2] == 'vert':
            distance2 = abs(int(state[0] + 1) - int(final[0]) + 1) + abs(int(state[1]) - int(final[1]))
            distance = min(distance1, distance2)
        elif state[2] == 'horiz':
            distance2 = abs(int(state[0]) - int(final[0])) + abs(int(state[1] + 1) - int(final[1]) + 1)
            distance = min(distance1, distance2)

        return distance

    # a* search algorithm implementation
    def astar(self, init, final, nivel):
        start = time.time()
        move_sequence = ''
        expand = [(init, move_sequence, self.manhattan_distance(init,final))]  # expand is the queue, each element is a tuple of (state, move_sequence, f_score)
        visited = {init: self.manhattan_distance(init, final)}
        while len(expand) > 0:
            expand.sort(key=lambda x: x[2])  # sort the queue by f_score
            state, move_sequence, f_score = expand.pop(0)
            if self.compare_states2(state, final):
                end = time.time()  # running time
                print(f'running time: {round((end - start) * 1000, 1)} ms')
                return move_sequence
            else:
                for legal in self.legal_moves(self.get_matrix(nivel, state)):
                    new_state = self.apply_action(nivel, legal, state)
                    new_move_sequence = move_sequence + legal
                    new_f_score = self.manhattan_distance(new_state, final) + len(new_move_sequence)  # calculate f_score for the new state
                    if new_state not in visited or new_f_score < visited[new_state]:
                        visited[new_state] = new_f_score
                        expand.append((new_state, new_move_sequence, new_f_score))
        return None

    # starts the search, compliment to other class
    def start_game(self, lvl, alg):
        match lvl:
            case 1:
                level_chosen = [[j for j in i] for i in self.level1]
            case 2:
                level_chosen = [[j for j in i] for i in self.level2]
            case 3:
                level_chosen = [[j for j in i] for i in self.level3]

        for x in level_chosen:
            print(x)
        init = self.create_block(level_chosen)
        final = self.create_block(self.ender(level_chosen))
        print(init, final)

        match alg:
            case button.ButtonIdentifiers.BFS:
                if level_chosen == [[j for j in i] for i in self.level1]:
                    x = self.bfs(init, final, Solution.level1)
                if level_chosen == [[j for j in i] for i in self.level2]:
                    x = self.bfs(init, final, Solution.level2)
                if level_chosen == [[j for j in i] for i in self.level3]:
                    x = self.bfs(init, final, Solution.level3)
            case button.ButtonIdentifiers.DFS:
                if level_chosen == [[j for j in i] for i in self.level1]:
                    x = self.dfs(init, final, Solution.level1)
                if level_chosen == [[j for j in i] for i in self.level2]:
                    x = self.dfs(init, final, Solution.level2)
                if level_chosen == [[j for j in i] for i in self.level3]:
                    x = self.dfs(init, final, Solution.level3)
            case button.ButtonIdentifiers.ASTAR:
                if level_chosen == [[j for j in i] for i in self.level1]:
                    x = self.astar(init, final, Solution.level1)
                if level_chosen == [[j for j in i] for i in self.level2]:
                    x = self.astar(init, final, Solution.level2)
                if level_chosen == [[j for j in i] for i in self.level3]:
                    x = self.astar(init, final, Solution.level3)


        if x is None:
            print('No solution found.')
        else:
            print(self.extract_directions(x))

