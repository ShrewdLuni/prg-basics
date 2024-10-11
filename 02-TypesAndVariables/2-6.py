import math

def calculate_distance(height):
    return 3.57 * math.sqrt(height)

print("Horizon from beach is", calculate_distance(1.75))
print("Horizon from hotel is", calculate_distance(20))  