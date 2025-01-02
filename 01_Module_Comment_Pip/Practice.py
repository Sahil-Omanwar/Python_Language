#Question 1:Print twinkle twinkle little star

print('''
Twinkle, twinkle, little star,
How I wonder what you are,
Up above the world so high,
Like a diamond in the sky.

When the traveler in the dark
Thanks you for thy tiny spark,
He could not see which way to go,
If you did not twinkle so.

When the blazing sun is gone,
And he nothing shines upon,
Then appears thy tiny spark,
Twinkle, twinkle, in the dark
''')

# Question 2:Install external module and use it according to your choice

import pyttsx3
engine=pyttsx3.init()
engine.say("I am Sahil Omanwar")
engine.runAndWait()

#Question 3:Write a program to print content of directory using os module
import os
path='/Users/Public/Desktop'
content=os.listdir(path)
for items in content:
    print(items)
