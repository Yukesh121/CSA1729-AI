from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Extracting unique characters from the puzzle
    unique_chars = set(char for word in puzzle for char in word)
    if len(unique_chars) > 10:
        print("Invalid puzzle. More than 10 unique characters.")
        return

    # Generating all possible permutations of digits from 0 to 9
    for perm in permutations(range(10)):
        mapping = dict(zip(unique_chars, perm))
        if all(sum(mapping[char] * (10 ** (len(word) - idx - 1)) for idx, char in enumerate(word[::-1])) == 0 
               for word in puzzle[:-1]) and \
               sum(mapping[char] * (10 ** (len(puzzle[-1]) - idx - 1)) for idx, char in enumerate(puzzle[-1][::-1])) == 0:
            print("Solution found:")
            for word in puzzle:
                print(word, '=', ''.join(str(mapping[char]) for char in word))
            return

    print("No solution found.")

# Example usage:
puzzle = ["SEND", "MORE", "MONEY"]
solve_cryptarithmetic(puzzle)
