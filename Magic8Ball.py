#Magic8Ball.py
#Name:Mauricio Martinez
#Date:02/11/25
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["thing 1", "thing 2", "thing 3"]
  #Answer question randomly with one of the options from your earlier list.
r=random.random() * 3

r=int(r) #cut off any decimal values

print(r)
response=answers[r]
print(response)

if __name__ == '__main__':
  main()
