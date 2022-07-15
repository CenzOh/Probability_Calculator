import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs): #dict of all arg being passed
    #print(kwargs) #test and works
    self.contents = []
    for key, value in kwargs.items(): #ex, key is blue ball example. value is 4
      for i in range(value): #will print blue four times
        self.contents.append(key)
    #print(self.contents) #prints 

  
  def draw(self, number):
    if number > len(self.contents): #if draw more balls than how much we have, return
      return self.contents
    balls =[]
    for i in range(number):
      #balls.append(self.contents.pop(random.randrange(0,len(self.contents)))) #one liner version
      random_ball = random.randint(0,(len(self.contents)-1)) #pick random ball
      balls.append(self.contents[random_ball])
      self.contents.remove(self.contents[random_ball])
    return balls
   

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments): #draw the balls out but create copies
    expected_copy = copy.deepcopy(expected_balls) #reason for copy is to avoid getting random colors when running the for loop again
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)
    for color in colors_gotten: #this is the random colors that were drawn with draw fcn
      if (color in expected_copy): #ex, if red is in the expected copy
        expected_copy[color] -=1 #expected balls is the dict, ex blue and red in main
        #expected value for red lets say is 2. If we detect red, subtract it by 1
    if( all( x <= 0 for x in expected_copy.values())): #if all the values in the expected copy equal 0
      count += 1
  return count / num_experiments #amount of successful draws / total amount of experiments