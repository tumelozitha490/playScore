#Teams vs Teams getting my score based on the teams and how they played
print("Lions ")
ScoreA = input(" ") 
print("Snakes")
ScoreB = input(" ")

print("Tarantulas")
ScoreC = input(" ") 
print("FC Awesome ")
ScoreD = input(" ")

print("Lions ")
ScoreE = input(" ") 
print("FC Awesome  ")
ScoreF = input(" ")

print("Tarantulas ")
ScoreG = input(" ")
print("Snakes ")
ScoreH = input(" ")


print("Lions ")
ScoreI = input(" ")
print("Grouches ")
ScoreJ = input(" ")

# List of Integers
numbers = [ScoreA,ScoreB,ScoreC,ScoreD,ScoreE,ScoreF,ScoreG,ScoreH,ScoreI,ScoreJ]
  
# Sorting list of Integers
numbers.sort(reverse=True)
  
print(numbers)
# put my teams in a array to be used later at the end of code 
words = ["Tarantulas", "Lions", "FC Awesome","Snakes","Grouches"]

#to avoid overwrite this i am diclaring my points in order to be easy in used when wanna calculate 
draw = int("1")
win= int("3")
loss= int("0")
pos= int("0")

#team By initializ this I will be able to easy calculate score/point per team played in all the games
po1= int("0")
po1a= int("0")
po1b= int("0")
point1= int("0")
#team
po2= int("0")
po2a= int("0")
po2b= int("0")
point2= int("0")
#team
po3= int("0")
po3a= int("0")
po3b= int("0")
point3= int("0")
#team
po4= int("0")
po4a= int("0")
po4b= int("0")
point4= int("0")
#team
po5= int("0")
po5a= int("0")
po5b= int("0")
point5= int("0")
#team
po6= int("0")
po6a= int("0")
po6b= int("0")
point6= int("0")
#team
po7= int("0")
po7a= int("0")
po7b= int("0")
point7= int("0")
#team
po8= int("0")
po8a= int("0")
po8b= int("0")
point8= int("0")
#team
po9= int("0")
po9a= int("0")
po9b= int("0")
point9= int("0")
#team
po10= int("0")
po10a= int("0")
po10b= int("0")
point10= int("0")
#intitaliz my sum up team in order to get total per team played
pointLion= int("0")
pointSnakes= int("0")
pointTarantulas= int("0")
pointFC= int("0")
pointGr= int("0")
#
# compare game played on number 1 try get which won loss and draw then calculate at end
if ScoreA == ScoreB:
    po1=draw
elif ScoreA > ScoreB:
    po1a=win
elif ScoreA < ScoreB:
   po1b=loss

point1=po1+po1a+po1b
#
# compare game played on try get which won loss and draw then calculate at end
if ScoreA == ScoreB:
    po2=draw
elif ScoreA < ScoreB:
    po2a=win
elif ScoreA > ScoreB:
   po2b=loss

point2=po2+po2a+po2b
#
#compare game played on number 2 try get which won loss and draw then calculate at end
if ScoreC == ScoreD:
    po3=draw
elif ScoreC > ScoreD:
    po3a=win
elif ScoreC < ScoreD:
   po3b=loss

point3=po3+po3a+po3b
#
# compare game played on try get which won loss and draw then calculate at end
if ScoreC == ScoreD:
    po4=draw
elif ScoreC < ScoreD:
    po4a=win
elif ScoreC > ScoreD:
   po4b=loss

point4=po4+po4a+po4b
#
#compare game played on number 3 try get which won loss and draw then calculate at end
if ScoreE == ScoreF:
    po5=draw
elif ScoreE > ScoreF:
    po5a=win
elif ScoreE < ScoreF:
   po5b=loss

point5=po5+po5a+po5b
#
#compare game played on try get which won loss and draw then calculate at end
if ScoreE == ScoreF:
    po6=draw
elif ScoreE < ScoreF:
    po6a=win
elif ScoreE > ScoreF:
   po6b=loss

point6=po6+po6a+po6b
#
#compare game played on number 4 try get which won loss and draw then calculate at end
if ScoreG == ScoreH:
    po7=draw
elif ScoreG > ScoreH:
    po7a=win
elif ScoreG < ScoreH:
   po7b=loss

point7=po7+po7a+po7b
#
#compare game played on  try get which won loss and draw then calculate at end
if ScoreG == ScoreH:
    po8=draw
elif ScoreG < ScoreH:
    po8a=win
elif ScoreG > ScoreH:
   po8b=loss

point8=po8+po8a+po8b
#
#compare game played on number 5 try get which won loss and draw then calculate at end
if ScoreI == ScoreJ:
    po9=draw
elif ScoreI > ScoreJ:
    po9a=win
elif ScoreI < ScoreJ:
   po9b=loss

point9=po9+po9a+po9b
#
#compare game played on  try get which won loss and draw then calculate at end
if ScoreI == ScoreJ:
    po10=draw
elif ScoreI < ScoreJ:
    po10a=win
elif ScoreI > ScoreJ:
   po10b=loss

point10=po10+po10a+po10b
#
# total small everthing based on the games been played try get the total which will be displayed at the end as points
#lions
pointLion=point1+point5+point9
#snakes
pointSnakes=point2+point8
#Tarantulas
pointTarantulas=point3+point7
#FC Awesome
pointFC=point4+point6
#Grouches
pointGr=point10


# creating my array to be sort
pos = [pointLion,pointSnakes,pointTarantulas,pointFC,pointGr]
  
# Sorting list of Integers the point/score is sort correct from big to small
pos.sort(reverse=True)
#

#output my display when runing the code this will show up  
print(pos)
print("1. Tarantulas, "+ str(pointTarantulas) + "pt ")
print("2. Lions, "+ str(pointLion) + " pt ")
print("3. FC Awesome, "+ str(pointFC) + " pt ")
print("3. Snakes, "+ str(pointSnakes) + " pt ")
print("5. Grouches, "+ str(pointGr) + " pt ")

# Here was trying to make use of array sort it using pos and also score
# for i in numbers:
#  print(str(pos) +","+ words + str(numbers) + "pt ") 
# print(i)