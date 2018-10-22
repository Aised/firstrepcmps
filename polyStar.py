#Student's name:Assaad El Halabi
#ID:201907829
#Section:9 till 10 am
#Instructor's name:Dr.Ahmad Dhaini

import turtle

n=int(input('use an even number bigger than or equal to 8 for a star:',)) #Number of polygon sides
p=int(input('number of pixels(length) of each side',)) #Number of pixels in each side(length)

for i in range(n):
    turtle.forward(p)
    turtle.right(((n-2)*180)/n)  #angle of each turn using polygon angle sum's formula divided by the number of sides,
    #by accident I discovered that this one will give a star if you use value 10,and will do cool other drawings for n>10.

turtle.done()
