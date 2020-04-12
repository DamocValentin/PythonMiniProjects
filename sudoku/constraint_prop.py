'''
Constraint propagation
'''
from queue import Queue


def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    
    """
    
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x

    def revise(csp, x_i, x_j):
        revised = False
        for x in csp.domains[x_i]:
            found = False
            for y in csp.domains[x_j]:
                if csp.constraints(x_i, x, x_j, y):
                    found = True
            if not found:
                if len(csp.domains[x_i]) == 1:
                    csp.domains[x_i] = []
                else:
                    domain = list(csp.domains[x_i])
                    domain.remove(x)
                    csp.domains[x_i] = ''.join(domain)
                revised = True
        return revised

    q = Queue()
    for element in csp.variables:
        for neighbour in csp.neighbors[element]:
            q.put((element, neighbour))

    while not q.empty():
        (x_i, x_j) = q.get()
        if revise(csp, x_i, x_j):
            if len(csp.domains[x_i]) == 0:
                return False
            else:
                x_i_neighbours = list(csp.neighbors[x_i])
                x_i_neighbours.remove(x_j)
                for x_k in x_i_neighbours:
                    q.put((x_k, x_i))

    csp.curr_domains = csp.domains
    return True




