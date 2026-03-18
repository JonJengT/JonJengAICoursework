class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.backtracks = 0
        self.solution = None

    def solve(self):
        assignment = {}
        self.solution = self.backtrack(assignment)
        return self.solution

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        
        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                else:
                    del assignment[var]
                    self.backtracks += 1
        return None

    def select_unassigned_variable(self, assignment):
        unassigned = [value for value in self.variables if value not in assignment]

        smallest = 10
        smallest_coor = None
        for var in unassigned:
            if len(self.domains[var]) < smallest:
                smallest = len(self.domains[var])
                smallest_coor = var

        return smallest_coor
    
    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_consistent(self, var, value, assignment):
        for constraint_var in self.constraints[var]:
            if constraint_var in assignment and assignment[constraint_var] == value:
                return False
        return True