def pascal_triangle(n):
    result = [[1]]
    
    for r in range(2, n + 1):
        sol = [1]
        for c in range(1, r - 1):
            sol.append(result[-1][c] + result[-1][c-1])
        sol.append(1)
        
        result.append(sol)
        
    return result



if __name__ == "__main__":
    print(pascal_triangle(5))