import math
import copy
import random

from basicsearch_lib.board import Board


class TileBoard(Board):
    def __init__(self, n, multiple_solutions=False, force_state=None,
                 verbose=False):
        """"TileBoard(n, multiple_solutions
        Create a tile board for an n puzzle.

        If multipleSolutions are true, the solution need not
        have the space in the center.  This defaults to False but
        is automatically set to True when there is no middle square

        force_state can be used to initialize an n puzzle to a desired
        configuration.  No error checking is done.  It is specified as
        a list with n+1 elements in it, 1:n and None in the desired order.

        verbose is a boolean for turning on debugging
        """

        self.verbose = verbose  # not debug state, up to you to use it

        self.boardsize = int(math.sqrt(n + 1))
        if math.sqrt(n + 1) != self.boardsize:
            multiple_solutions = True

        # initialize parent
        super().__init__(self.boardsize, self.boardsize)

        # Compute solution states
        # If multiple_solutions is true, None can be anywhere:
        # [(None,1,2,3,...), (1,None,2,3,...), (1,2,None,3,...)]
        # Otherwise, must be the last square:  [(1,2,3,...,None)]
        self.goals = []
        if multiple_solutions:
            for i in range(0, n + 1):
                sol = []
                for j in range(1, n + 1):
                    if i + j == n:
                        sol.append(self.empty_symbol)
                    sol.append(j)
                self.goals.append(tuple(sol))
        else:
            sol = []
            for j in range(1, n + 1):
                if j == int(n / 2):
                    sol.append(self.empty_symbol)
                sol.append(n)
            self.goals.append(tuple(sol))

        initial_state = [i for i in self.state_tuple()]
        self.is_solvable = self.solvable(initial_state)

        if force_state is None:
            values_to_seed = list()
            for i in range(0, self.rows * self.cols - 1):
                values_to_seed.append(i + 1)
            values_to_seed.append(self.empty_symbol)
            random.shuffle(values_to_seed)

            index = 0
            for line in range(0, self.rows):
                for col in range(0, self.cols):
                    self.place(line, col, values_to_seed[index])
                    index += 1
        else:
            self.board = force_state

    def solvable(self, tiles, verbose=False):
        """solvable - Determines if a puzzle is solvable

            Given a list of tiles, determine if the N-puzzle is solvable.
            You do not need to know how to do this, but the calculation
            is based on the inversion order.

            for each number in the list of tiles,
               How many following numbers are less than that one
               e.g. [13, 10, 11, 6, 5, 7, 4, 8, 1, 12, 14, 9, 3, 15, 2, None]
               Example:  Files following 9:  [3, 15, 2, None]
               Two of these are smaller than 9, so the inversion order
                   for 9 is 2

            A puzzle's inversion order is the sum of the tile inversion
            orders.  For puzzles with even numbers of rows and columns,
            the row number on which the blank resides must be added.
            Note that we need not worry about 1 as there are
            no tiles smaller than one.

            See Wolfram Mathworld for further explanation:
                http://mathworld.wolfram.com/15Puzzle.html
            and http://www.cut-the-knot.org/pythagoras/fifteen.shtml

            This lets us know if a problem can be solved.  The inversion
            order modulo 2 is invariant across moves.  This means that
            when we make a legal move, the inversion order will always
            be even or odd.  The solution state always has an even
            inversion order, so any puzzle with an odd inversion
            number cannot be solved.
        """

        inversionorder = 0
        # Make life easy, remove None
        reduced = [t for t in tiles if t is not None]
        # Loop over all but last (no tile after it)
        for idx in range(len(reduced) - 1):
            value = reduced[idx]
            after = reduced[idx + 1:]  # Remaining tiles
            smaller = [x for x in after if x < value]
            numtiles = len(smaller)
            inversionorder = inversionorder + numtiles
            if verbose:
                print("idx {} value {} tail {} #smaller {} sum: {}".format(
                    idx, value, after, numtiles, inversionorder))

        # Even number of rows must take the blank position into account
        if self.get_rows() % 2 == 0:
            if verbose:
                print("Even # rows, adding for position of blank")
            inversionorder = inversionorder + math.floor(tiles.index(None) / self.boardsize) + 1

        solvable = inversionorder % 2 == 0  # Solvable if even
        return solvable

    def __hash__(self):
        "__hash__ - Hash the board state"

        # Convert state to a tuple and hash
        return hash(self.state_tuple())

    def __eq__(self, other):
        "__eq__ - Check if objects equal:  a == b"

        if self.cols != other.cols:
            return False
        if self.rows != other.cols:
            return False
        for line in range(0, self.rows):
            for col in range(0, self.cols):
                if self.board[line][col] != other.board[line][col]:
                    return False
        return True

    def state_tuple(self):
        "state_tuple - Return board state as a single tuple"
        state_list = list()
        for line in range(0, self.rows):
            for col in range(0, self.cols):
                state_list.append(self.board[line][col])
        return tuple(state_list)

    def get_actions(self):
        "Return row column offsets of where the empty tile can be moved"
        empty_line = 0
        empty_col = 0
        for line in range(0, self.rows):
            for col in range(0, self.cols):
                if str(self.board[line][col]) == '.':
                    empty_line = line
                    empty_col = col

        "So we have found the position of the empty tile"
        valid_actions = list()
        if empty_line > 0:
            valid_actions.append((-1, 0))
        if empty_line < self.rows - 1:
            valid_actions.append((1, 0))
        if empty_col > 0:
            valid_actions.append((0, -1))
        if empty_col < self.cols - 1:
            valid_actions.append((0, 1))

        return valid_actions

    def move(self, offset):
        "move - Move the empty space by [delta_row, delta_col] and return new board"
        new_board = copy.deepcopy(self.board)

        empty_line = 0
        empty_col = 0
        for line in range(0, self.rows):
            for col in range(0, self.cols):
                if str(new_board[line][col]) == self.empty_symbol:
                    empty_line = line
                    empty_col = col

        new_board[empty_line][empty_col] = new_board[empty_line + offset[0]][empty_col + offset[1]]
        new_board[empty_line + offset[0]][empty_col + offset[1]] = '.'

        self.board = copy.deepcopy(new_board)
        return self

    def solved(self):
        "solved - Is the puzzle solved?  Returns boolean"
        actual_state = self.state_tuple()
        for solution in self.goals:
            identical = True
            for i in range(0, len(solution)):
                if actual_state[i] != solution[i]:
                    identical = False
                    break
            if identical:
                return True
        return False