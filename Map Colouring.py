class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.assignment = {}
    def is_consistent(self, variable, color):
        for neighbor in self.neighbors[variable]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True
    def backtracking_search(self):
        return self.backtrack({})
    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None
    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var
    def order_domain_values(self, var):
        return self.domains[var]
# Example usage
if __name__ == "__main__":
    # Example variables representing regions on a map
    variables = ['WA', 'NT', 'SA', 'QL', 'NSW', 'VIC', 'TAS']
    # Example domains (colors)
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue'],
        'QL': ['red', 'green', 'blue'],
        'NSW': ['red', 'green', 'blue'],
        'VIC': ['red', 'green', 'blue'],
        'TAS': ['red', 'green', 'blue']
    }
    # Example neighbors (adjacent regions)
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'QL'],
        'SA': ['WA', 'NT', 'QL', 'NSW', 'VIC'],
        'QL': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'QL', 'VIC'],
        'VIC': ['SA', 'NSW', 'TAS'],
        'TAS': ['VIC']
    }
    csp = MapColoringCSP(variables, domains, neighbors)
    assignment = csp.backtracking_search()
    if assignment:
        print("Map coloring solution found:")
        for region, color in assignment.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")
