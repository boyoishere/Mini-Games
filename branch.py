import random

def generate_crack(depth=0, max_depth=3):
    if depth > max_depth:
        return ""
    
    # Main vertical branch at the current depth
    result = " " * depth * 2 + "|" + "\n"
    
    # Left and right side branches at the current level
    if depth < max_depth:
        left_branch = " " * depth * 2 + "\\" + "-" * random.randint(1, 2) + "\n"
        right_branch = " " * depth * 2 + "/" + "-" * random.randint(1, 2) + "\n"
        result += left_branch + right_branch
        
        # Recurse further for each side to add more branches
        result += generate_crack(depth + 1, max_depth)
    
    return result

# Generate and print the ASCII "crack" pattern with aligned branches
print(generate_crack())