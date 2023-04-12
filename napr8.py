import time
__import__

def printer(m):
    for i in m:
        print(i)
    print("\n")  # matrix printer aux function


class block:
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

    ''' - '''

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

def ender(n):
    end = [[j for j in i] for i in n]
    # given a certain matrix, returns the ending one
    for i in range(len(end)):
        for j in range(len(end[0])):
            if end[i][j] == 2:
                end[i][j] = 1
            if end[i][j] == 9:
                end[i][j] = 2  # end will be the objective matrix, since the beggining point will be a 1, and the ending 9 will be the last pos of the block
    return end  # end matrix

def check_9(m):
    pos1,pos2=0,0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==9:
                pos1=i
                pos2=j
    # returns the position of the 9
    return pos1,pos2


def compare_states(initial_state, final_state):
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            if initial_state[i][j] != final_state[i][j]:
                return False
    return True  # check for the right names when calling!!!


def legal_moves(m):
    stat = get_status(m)
    x, y = get_pos(m)
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


def get_status(m):
    c1 = get_pos(m)[0]
    c2 = get_pos(m)[1]
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
        if abs(c1-c3) == 1:
            return 'vert'
        return 'horiz'

def get_pos(m):
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


# This changes when in the graphic environment a level is chosen by the program user.
def sizer(m):
    rows = len(m)
    cols = len(m[0])
    return rows, cols


# Creation of the first instance of the block
def create_block(m):
    c1 = get_pos(m)[0]
    c2 = get_pos(m)[1]
    stat = get_status(m)
    b = block(c1, c2, stat)
    return b


def string_appender(m, operator):  # operator is the concatenation of direction_state
    if len(m) == 6:
        if len(m[0]) == 10:
            temp = 1
        else:
            temp = 2
    else:
        temp = 3
    #way to know which list
    c1 = get_pos(m)[0]
    c2 = get_pos(m)[1]
    stat = get_status(m)
    out = 'init.' + operator + '(' + str(c1) + ',' + str(c2) + ",'" + stat + "'," + 'level' + str(temp) + ')'
    return out  # to execute out later, exec(out)


def operator_maker(a, b):
    c = str(a) + '_' + str(b)  # a=direction, b=state
    return c


def aux_9(m,a,b):
    if m[a][b] == 1:
        m[a][b] = 9
    return m


def extract_directions(input_string):
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


def apply_action(z, op, state):
    m = get_matrix(z,state) # z is the lvl
    out = string_appender(m, op)
    exec(out)
    r = (get_pos(m)[0], get_pos(m)[1], get_status(m))
    return r


def get_matrix(lvl, state): #state is a tuple (x1,x2,status)
    for i in range(len(lvl)):
        for j in range(len(lvl[0])):
            if lvl[i][j] == 2:
                lvl[i][j] = 1
    x9 = check_9(lvl)[0]
    y9 = check_9(lvl)[1]
    lvl[x9][y9] = 9 #if block on the hole, not right,the hole would be deleted
    a = int(state[0])
    b = int(state[1])
    lvl[a][b] = 2
    status = state[2]
    if status == 'stand':
        return lvl
    else:
        if status == 'vert':
            lvl[a+1][b] = 2
            return lvl
        elif status == 'horiz':
            lvl[a][b+1] = 2
            return lvl
    return 404


def compare_states2(a, b):
    # compare_states2 check the tuple, not the matrix, temporary
    a1 = clean_string(a)
    b1 = clean_string(b)
    if str(a1) == str(b1):
        return True
    return False


def clean_string(s):
    cleaned = ''
    for c in s:
        if c != "'":
            cleaned += str(c)
    return cleaned


####################


def bfs(init, final, nivel):
    start = time.time()
    move_sequence = ''
    expand = [(init, move_sequence)]  # expand is the queue, each element is a tuple of (state, move_sequence)
    visited = [init]
    while len(expand) > 0:
        state, move_sequence = expand.pop(0)
        if compare_states2(state, final):
            end = time.time() # running time
            print(f'running time: {round((end - start)*1000, 1)} ms')
            return move_sequence
        else:
            for legal in legal_moves(get_matrix(nivel, state)):
                new_state = apply_action(nivel, legal, state)
                if new_state not in visited:
                    new_move_sequence = move_sequence + legal  # generate new move sequence
                    visited.append(new_state)
                    expand.append((new_state, new_move_sequence))
                    #to not forget that extract_directions

def dfs(init, final, nivel):
    start = time.time()  # record the start time of the search
    move_sequence = ''  # initialize the move sequence as an empty string
    stack = [(init, move_sequence)]  # initialize the stack with the initial state and the empty move sequence
    visited = [init]  # initialize the list of visited states with the initial state
    while len(stack) > 0:  # continue while the stack is not empty
        state, move_sequence = stack.pop()  # remove the last state from the stack and get its move sequence
        if compare_states2(state, final):  # check if the state is the final state
            end = time.time()  # record the end time of the search
            print(f'running time: {round((end - start)*1000, 1)} ms') # print the running time of the search
            return move_sequence  # return the move sequence that leads to the final state
        else:
            for legal in legal_moves(get_matrix(nivel, state)):  # generate all legal moves from the current state
                new_state = apply_action(nivel, legal, state)  # apply a legal move to the current state to get a new state
                if new_state not in visited:  # check if the new state has not been visited before
                    new_move_sequence = move_sequence + legal  # generate a new move sequence that includes the current move
                    visited.append(new_state)  # add the new state to the list of visited states
                    stack.append((new_state, new_move_sequence))  # add the new state and its move sequence to the stack
    return None  # return None if no solution is found


def get_heuristic(nivel, final):
    # calculate the sum of the Manhattan distances of each tile to its final position
    h = 0
    for i in range(len(nivel)):
        for j in range(len(nivel[0])):
            tile = nivel[i][j]
            if tile != 0:
                # find the position of the tile in the final state
                x, y = divmod(final.index(tile), nivel)
                # calculate the Manhattan distance between the current position and the final position of the tile
                h += abs(i - x) + abs(j - y)
    return h

'''
def astar(init, final, nivel):
    start = time.time()  # record the start time of the search
    move_sequence = ''  # initialize the move sequence as an empty string
    frontier = [(init, move_sequence, 0)]  # initialize the frontier with the initial state, empty move sequence and the cost so far
    visited = {init: 0}  # initialize the dictionary of visited states with the initial state and its cost so far
    while len(frontier) > 0:  # continue while the frontier is not empty
        # sort the frontier by f(n) = g(n) + h(n), where g(n) is the cost so far and h(n) is the estimated cost to the goal
        frontier.sort(key=lambda x: len(x[1]) + get_heuristic(nivel, final))
        state, move_sequence, cost_so_far = frontier.pop(0)  # remove the state with the lowest f(n) from the frontier
        if compare_states2(state, final):  # check if the state is the final state
            end = time.time()  # record the end time of the search
            print('running time: ', end - start)  # print the running time of the search
            return move_sequence  # return the move sequence that leads to the final state
        else:
            for legal in legal_moves(get_matrix(nivel, state)):  # generate all legal moves from the current state
                new_state = apply_action(nivel, legal, state)  # apply a legal move to the current state to get a new state
                new_move_sequence = move_sequence + legal  # generate a new move sequence that includes the current move
                new_cost_so_far = cost_so_far + 1  # add the cost of the current move to the cost so far
                if new_state not in visited or new_cost_so_far < visited[new_state]:  # check if the new state has not been visited before or if a shorter path to the new state has been found
                    visited[new_state] = new_cost_so_far  # update the cost so far of the new state
                    frontier.append((new_state, new_move_sequence, new_cost_so_far))  # add the new state, its move sequence and its cost so far to the frontier
    return None  # return None if no solution is found


'''

lvl = int(input('Nivel: '))
if lvl == 1:
    init = create_block(level1)
    final = create_block(ender(level1))
    print(init, final)
    alg = int(input('1-BFS, 2-DFS: '))
    if alg == 1:
        x = bfs(init, final, level1)
        if x is None:
            print('No solution found.')
        else:
            print(extract_directions(x))
    elif alg == 2:
        x = dfs(init, final, level1)
        if x is None:
            print('No solution found.')
        else:
            print(extract_directions(x))
            '''
    else:
        x = astar(init, final, level1)
        if x is None:
            print('No Solution found.')
        else:
            print(extract_directions(x))
'''


elif lvl == 2:
    level = create_block(level2)
    init = create_block(level2)
    final = create_block(ender(level2))
    print(init, final)
    alg = int(input('1-BFS, 2-DFS: '))
    if alg == 1:
        x = bfs(init, final, level2)
        if x is None:
            print('No solution found.')
        else:
            print(extract_directions(x))
    elif alg == 2:
        x = dfs(init, final, level2)
        if x is None:
            print('No solution found.')
        else:
            print(extract_directions(x))
            '''
    else:
        x = astar(init, final, level1)
        if x is None:
            print('No Solution found.')
        else:
            print(extract_directions(x))'''

elif lvl == 3:
    level = create_block(level3)
    init = create_block(level3)
    final = create_block(ender(level3))
    print(init, final)
    alg = int(input('1-BFS, 2-DFS: '))
    if alg == 1:
        x = bfs(init, final, level3)
        if x is None:
            print('No solution found.')
        else:
            print(extract_directions(x))
    elif alg == 2:
        x = dfs(init, final, level3)
        if x is None:
            print('No solution found.')
        else:
            print(extract_directions(x))
            '''
    else:
        x = astar(init, final, level1)
        if x is None:
            print('No Solution found.')
        else:
            print(extract_directions(x))'''
else:
    print('Invalid Level.')