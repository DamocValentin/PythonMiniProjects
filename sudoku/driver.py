
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, forward_checking, lcv, mac
from backtrack import backtracking_search


first = True

for puzzle in [easy1, harder1]:
    if first:
        s = Sudoku(puzzle)  # construct a Sudoku problem easy1
        print("Initial State easy")
        print()
        s.display(s.infer_assignment())
        print()
        print('Solving the problem...')
        print()
        AC3(s)
        s.display(s.infer_assignment())
        print()
        first = False
    else:
        h = Sudoku(puzzle) # construct a Sudoku problem hard1
        print("Initial State hard")
        print()
        h.display(h.infer_assignment())
        print()
        print('Solving the problem. Apply AC3...')
        print()
        AC3(h)
        print()
        for var in h.curr_domains:
            h.curr_domains[var] = list(h.domains[var])
        if not h.goal_test(h.curr_domains):
            print("After AC3")
            h.display(h.infer_assignment())
            print()
            print("Try backtraking")
            print()
            solved = backtracking_search(h, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
            print("Final status")
            print()
            if solved is None:
                print("The problem was not solved")
            else:
                if h.goal_test(solved):
                    h.display(solved)
                else:
                    print("Invalid solution")
