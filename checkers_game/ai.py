import abstractstrategy


class AlfaBetaPrunning():
    def __init__(self, strategy):
        self.strategy = strategy

    def alfa_beta_prunning(self, board, plies_left):
        actions = board.get_actions(self.strategy.maxplayer)
        v = self.max_value(board, -500, 500, plies_left)
        for action in actions:
            new_board = board.move(action)
            if self.max_value(new_board, -500, 500, plies_left) == v:
                return new_board, action

    def min_value(self, board, alfa, beta, plies_left):
        v = 0
        if board.is_terminal()[0] or plies_left == 0:
            v = self.strategy.utility(board)
        else:
            v = 500
            actions = board.get_actions(self.strategy.maxplayer)
            for action in actions:
                new_board = board.move(action)
                max_val = self.max_value(new_board, alfa, beta, plies_left - 1)
                v = self.min(v, max_val)
                if v <= alfa:
                    break
                else:
                    beta = self.min(beta, v)
        return v

    def max_value(self, board, alfa, beta, plies_left):
        v = 0
        if board.is_terminal()[0] or plies_left == 0:
            v = self.strategy.utility(board)
        else:
            v = -500
            actions = board.get_actions(self.strategy.maxplayer)
            for action in actions:
                new_board = board.move(action)
                min_val = self.min_value(new_board, alfa, beta, plies_left - 1)
                v = self.max(v, min_val)
                if v >= beta:
                    break
                else:
                    alfa = self.max(alfa, v)
        return v

    def max(self, num_one, num_two):
        if num_one > num_two:
            return num_one
        return num_two

    def min(self, num_one, num_two):
        if num_one < num_two:
            return num_one
        return num_two


class Strategy(abstractstrategy.Strategy):
    "Human player"

    def play(self, board):
        """"play - make a move
        You are to implement class Strategy in the file ai.py (respect case as we may test on a
        case-sensitive system). You will need to design an alpha-beta pruning minimax search
        and utility function. The utility function is a subclass of Strategy, and the alpha-beta
        search is a separate function or class. Both must be contained within AI.py
        """
        alfa_beta_prunning_strategy = AlfaBetaPrunning(self)
        return alfa_beta_prunning_strategy.alfa_beta_prunning(board, self.maxplies)

    def utility(self, board):
        red_score = board.pawnsN[0] + board.kingsN[0] * 2
        black_score = board.pawnsN[1] + board.kingsN[1] * 2
        if self.maxplayer == 'r':
            return red_score - black_score
        else:
            return black_score - red_score
