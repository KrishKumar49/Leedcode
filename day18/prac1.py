def minimum_moves_to_restore(n, dancers, permutation):
    # Store the original configuration
    original = dancers[:]
    
    # Initialize move counter
    moves = 0
    
    # Start by copying current dancers array
    current = dancers[:]
    
    # Keep applying the permutation until we reach the original
    while True:
        # Apply permutation
        next_position = [0] * n
        for i in range(n):
            next_position[i] = current[permutation[i] - 1]  # permutation is 1-indexed

        current = next_position[:]
        moves += 1

        if current == original:
            break
    
    return moves

# Input reading
n = int(input())
dancers = list(map(int, input().split()))
permutation = list(map(int, input().split()))

# Output result
print(minimum_moves_to_restore(n, dancers, permutation))