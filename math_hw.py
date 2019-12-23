import math
print("Hi, welcome to the math homework calculator! I can calculate any math problem for you, just input one!")
problem = input("Please enter a math problem, or press 'q' to quit\n")
while (problem != "q"):
	print ("The answer to",problem, "is", eval(problem))
	problem = input("Please enter another math problem, or press 'q' to quit\n")
