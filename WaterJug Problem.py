def water_jug_dfs(capacity_x, capacity_y, target):
    visited_states = set()

    def dfs(x, y):
        if (x, y) in visited_states:
            return False
        visited_states.add((x, y))

        if x == target or y == target:
            print("Goal reached! ({}, {})".format(x, y))
            return True

        # Fill jug x
        if dfs(capacity_x, y):
            print("Fill jug x: ({}, {})".format(x, y))
            return True

        # Fill jug y
        if dfs(x, capacity_y):
            print("Fill jug y: ({}, {})".format(x, y))
            return True

        # Empty jug x
        if dfs(0, y):
            print("Empty jug x: ({}, {})".format(x, y))
            return True

        # Empty jug y
        if dfs(x, 0):
            print("Empty jug y: ({}, {})".format(x, y))
            return True

        # Pour water from x to y
        pour_amount = min(x, capacity_y - y)
        if dfs(x - pour_amount, y + pour_amount):
            print("Pour water from x to y: ({}, {})".format(x, y))
            return True

        # Pour water from y to x
        pour_amount = min(y, capacity_x - x)
        if dfs(x + pour_amount, y - pour_amount):
            print("Pour water from y to x: ({}, {})".format(x, y))
            return True
        return False
    print("Starting Water Jug Problem:")
    dfs(0, 0)
water_jug_dfs(4, 3, 2)
