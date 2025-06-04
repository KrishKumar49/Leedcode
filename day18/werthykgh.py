def solve_group_arrays_by_mean():
    
    while True:
        try:
            n_str = input("Enter the number of arrays (n, an integer between 1 and 100): ")
            n = int(n_str)
            if 1 <= n <= 100:
                break
            else:
                print("Invalid input: n must be between 1 and 100.")
        except ValueError:
            print("Invalid input: Please enter an integer for n.")

    # 2. Read the sizes of each array
    while True:
        try:
            array_sizes_str = input(f"Enter {n} space-separated integers for array sizes (each between 1 and 15): ")
            array_sizes = [int(s) for s in array_sizes_str.split()]
            
            if len(array_sizes) != n:
                print(f"Invalid input: Please enter exactly {n} sizes.")
                continue
            
            # Check if each size is within constraints
            if all(1 <= size <= 15 for size in array_sizes):
                break
            else:
                print("Invalid input: Each array size must be between 1 and 15.")
        except ValueError:
            print("Invalid input: Please enter space-separated integers for array sizes.")

    # Use a set to store unique mean values
    # Using a set automatically handles the "distinct groups" requirement
    unique_means = set()

    # 3. Process each of the n arrays
    print("\nNow, enter the elements for each array:")
    for i in range(n):
        while True:
            try:
                current_size = array_sizes[i]
                current_array_elements_str = input(f"Enter {current_size} space-separated integers for array {i+1}: ")
                current_array_elements = [int(e) for e in current_array_elements_str.split()]

                if len(current_array_elements) != current_size:
                    print(f"Invalid input: Please enter exactly {current_size} elements for array {i+1}.")
                    continue
                
                # Check for non-empty array (though constraints say size >= 1)
                if current_size == 0:
                    print(f"Warning: Array {i+1} has a size of 0. It will be skipped for mean calculation.")
                    break # Break inner loop, effectively skipping this array's mean calculation
                    
                current_sum = sum(current_array_elements)
                
                # Calculate the mean. Use float division.
                current_mean = current_sum / current_size

                # Add the mean to the set of unique means
                unique_means.add(current_mean)
                break # Break out of the inner while loop after successful input
            except ValueError:
                print("Invalid input: Please enter space-separated integers for array elements.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    # The number of unique means is the total number of groups
    print("\n--- Result ---")
    print(f"The total number of groups formed is: {len(unique_means)}")

# Call the user-defined function to start the program
if __name__ == "__main__":
    solve_group_arrays_by_mean()