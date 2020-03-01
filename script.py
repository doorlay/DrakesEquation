# Main file for the Drake's equation calculator
# import numpy as np
	
def askuser():
  rstar = input("What is the rate of formation of stars in the galaxy?")
  fsubp = input("What fraction of those stars have planetary systems?")
  nsube = input("What is the number of planets per solar system that have an enviornment suitable for life?")
  fsubl = input("What fraction of suitable planets does life occur on?")
  fsubi = input("What fraction of life-bearing planets does intelligent life occur on?")
  fsubc = input("What fraction of civilizations develop a technology that releases detectable signs of their existence into space?")
  l = input("What length of time (in years) do these civilizations release detectable signs?")
  myList = [rstar, fsubp, nsube, fsubl, fsubi, fsubc, l]
  return myList


  
lst = askuser()

product = 1
for number in lst:
    product = float(number) * float(product)
print(product)
