import random
import time


seed = 0

def set_seed(value):
    global seed
    seed = value

def random_seed():
    global seed
    seed = int(time.time())
    linear_congruential_generator(2147483648, 1103515245, 12345)
    
    
    
def linear_congruential_generator(modulus, multiplier, increment):
    global seed
    seed = (multiplier * seed + increment) % modulus
    return seed
    
  
def middle_square_generator(length):
    global seed
    seed_str = str(seed)
    seed = int(seed_str[len(seed_str) - length:])
    square = str(seed * seed)
    square = square.zfill(length*2)
    y = (len(square)-length)/2
    seed = int(square[y : y + length])
    return seed

