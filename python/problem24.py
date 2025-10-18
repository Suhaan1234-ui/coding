english=float(input("enter your marks":))
maths=float(input("enter your marks":))
science=float(input("enter your marks":))
percentage=((english+maths+science)/300)*100
if(percentage>=40 and english >33 and maths>=33 and science>=33):
    print("you have passed the exam")
else:
    print("you have not passes the exam")
    print("better luck next time")
    