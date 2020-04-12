
from copy import deepcopy
from csp_lib.backtrack_util import (first_unassigned_variable, unordered_domain_values, no_inference)


def backtracking_search(csp, select_unassigned_variable=first_unassigned_variable, order_domain_values=unordered_domain_values, inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    
    # See Figure [6.5] of your book for details
    def assignment_complete(assignment):
        for i in range(0, 81):
            if i not in assignment:
                return False
        return True

    def value_consistent_assignment(var, value, assignment, inter_csp):
        for neighbour in inter_csp.neighbors[var]:
            if neighbour in assignment:
                if assignment[neighbour] == value:
                    return False
            if len(inter_csp.domains[neighbour]) == 1:
                if value in inter_csp.domains[neighbour]:
                    return False
        return True

    def backtrack(assignment, inter_csp):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        temp_csp = deepcopy(inter_csp)
        if assignment_complete(assignment):
            return assignment
        var = select_unassigned_variable(assignment, inter_csp)
        for value in order_domain_values(var, assignment, inter_csp):
            if value_consistent_assignment(var, value, assignment, inter_csp):
                assignment[var] = value
                inferences = inference(inter_csp, var, value, assignment, removals)
                if inferences is not None:
                    resp = backtrack(assignment, inter_csp)
                    if resp is not None:
                        return resp
            if var in assignment:
                assignment.pop(var)
            inter_csp = temp_csp
        return None

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    removals = []
    result = backtrack({}, csp)
    assert result is None or csp.goal_test(result)
    return result
