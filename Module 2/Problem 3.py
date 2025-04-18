# Create a program that prompts for the side length of a triangle and computes the area using Heron's formula. 

import math

SideA = float(input("How long is side A? "))
SideB = float(input("How long is side B? "))
SideC = float(input("How long is side C? "))

Side = (SideA + SideB  + SideC) / 2

area = math.sqrt(Side * (Side - SideA) * (Side - SideB) * (Side - SideC))

print(area)

