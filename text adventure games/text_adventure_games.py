print ("Hi! im an E-safety AI and im going to be quizzing you on e safety, whats your name?")
name = input()
lives = 3 
print (f"Hi {name} this quiz includes a 3 life system")
print ("if you answer a questions incorectly you lose a life, if not you move on")
print ("if you run out of lives you lose if you complete all 5 questions you win!")
print ( "first question")
print("what software can you download to prevent getting a virus is it?")
print ( "C: Anti-viirus software")
print ("B: firewall software")
print ("A:disk clean up software")
C = ("C: Anti-viirus software.")
B =("B: firewall software.")
A =("A:disk clean up software")
answer = input()
if answer == "C":
    print("well done")
else:
    print("you lost a life, an anti virus software will protect you from viruses")
    lives -=1
    print (f"lives {lives}")


print ("next question")
print("Should you share your adress online?")
print ("is it")
print("A: yes")
print(" B: no")
A = ("A: yes")
B = ("B: no")
answer = input()
if answer == "B":
    print ("well done")
else:
    print ("you lost a life, you should never share your adress online.")
    lives -=1
    print (f"lives {lives}")
    
print ("next question")
print("should you have the same password for every account you have?")
print ("A: yes")
print("B: no")
A = ("A: yes")
B = ("B: no")
answer = input()
if answer == "B":
    print ("well done")
else:
    print("you lost a life")
    lives -=1
    print (f"lives {lives}")

if lives > 0 :
    print("next question")
    print("is it safe to share your ip adress with other people?")
    print ("A: yes")
    print("B: no")
    A = ("A: yes")
    B = ("B: no")
    answer = input()
    if answer == "B":
        print ("well done")
    else:
        print("you lost a life")
        print(f"lives {lives}")

if lives > 0 :
    print("should your password be something predictable such as your name/date of birth?")
    print("A: yes")
    print("B: no")
    A = ("A: yes")
    B = ("B: no")
    if answer == "B":
        print ("well done")
    else:
        print("you lost a life")
        print(f"lives {lives}")
        
if lives > 0:
    print("next question")
    print("should you trust sites that are not secure?")
    print("A: yes")
    print("B: no")
    A = ("A: yes")
    B = ("B: no")
    if answer == "B":
        print("well done")
    else:
        print("you lost a life")

if lives > 0:
    print("next question")
    print("should you share personal information online?")
    print("A: yes")
    print("B: no")
    A = ("A: yes")
    B = ("B: no")
    if answer == "B":
        print("well done")
    else:
        print("you lost a life")

if lives > 0:
    print("Well done you won!!")