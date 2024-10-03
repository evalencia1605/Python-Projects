import random

# Function to create a text file with random numbers
def create_number_file(filename, num_count, num_range):
    with open(filename, 'w') as f:
        # Generate num_count random numbers within the range of 1 to num_range
        numbers = [str(random.randint(1, num_range)) for _ in range(num_count)]
        # Write the numbers to the file, separated by spaces
        f.write(" ".join(numbers))

# Example: Create a file with 100 random numbers ranging from 1 to 1000
create_number_file('numbers.txt', 100, 1000)
print("File 'numbers.txt' created with 100 random numbers.")