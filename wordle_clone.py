from numpy import random


allwords = [
    "apple", "grape", "sheep", "stone", "train", "water", "light", "flame", "chair", "smile",
    "green", "bread", "house", "plant", "heart", "sweet", "dream", "cloud", "laugh", "spark",
    "beach", "river", "music", "earth", "shine", "happy", "table", "candy", "storm", "voice",
    "wheat", "books", "dance", "fruit", "peace", "sword", "piano", "track", "north", "south",
    "field", "drink", "lover", "night", "ocean", "sound", "tower", "flock", "round", "wings"
]
word=(random.choice(allwords))
l=0
while(True):
 l=l+1
 chwrd=[]
 for x in word:
     chwrd.append(x)
 guess=input(f"type your {len(word)} letter guess:-")
 wordtype=[]
 result=[]
 i=0
 k=0
 while(i<len(word)):
  if word[i]==guess[i]:
   wordtype.append("True")
  elif guess[i] in word:
   wordtype.append("is in wrong place")
  elif guess[i] not in word:
   wordtype.append("False")
  
  i=i+1
 for x in guess:
       result.append(x+" "+wordtype[k])
       k=k+1 
 print(result)
 if(word!=guess):
        print(f"you have {6-l} attempts left")
 if(word==guess):
     print("you won")
     break
 if(l==6):
        print("you lost")
        print(f"the word was {word}")
        break