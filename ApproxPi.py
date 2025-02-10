#ApproxPi.py
#Name:Nomaan Ahmed 
#Date:2/9/25
#Assignment:Lab 3 
import math
import time

def calculate_pi(precision):
    pi = 0
    for i in range(precision):
        pi += ((-1) ** i) / (2 * i + 1)
    return pi * 4

#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  target_pi = 3.14159
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  precision = int(input("Enter the number of terms for the approximation (e.g., 10000): "))

  start = time.time()
  #calculate pi using the approximation technique
  pi_approximation = calculate_pi(precision)
  #Loop until the level of percision is reached
  
  end = time.time()

  elapsedTime = end - start
  print(f"Approximated value of pi: {pi_approximation}")
  print(f"Actual value of pi: {realPi}")
  print(f"Elapsed time: {elapsedTime} seconds")
  
if __name__ == '__main__':
  main()
