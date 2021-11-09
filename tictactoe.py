# simple game of tictactoe :-)
import sys
usin = "         "
print ('---------')
i=0
r=0
c=0
z=[0]
while i<len(usin) :
  print('|',usin[i],usin[i+1],usin[i+2],'|')
  i = i+3
print ('---------')
listy = [[usin[i+j] for j in range(3)]for i in range(0,9,3)]
def centerchk():
    x = input("Enter the coordinates:").split()
    for y in x:
        if y.isnumeric==False:
            print("You should enter numbers!")
            centerchk()
            continue
        elif int(y)>3 or int(y)<1:
            print("Coordinates should be from 1 to 3!")
            centerchk()
            continue
    r= int(x[0])-1
    c= int(x[1])-1
    if listy[r][c]=="X" or listy[r][c]=="O":
        print("This cell is occupied! Choose another one!")
        centerchk()
    elif listy[r][c]==" ":
       if z[0]==0 :
           listy[r][c] ="X"
           z[0]=1
       else :
           listy[r][c]="O"
           z[0]=0
       print ('---------')
       a=0
       while a<3:
        print ('|',listy[a][0],listy[a][1],listy[a][2],'|')
        a=a+1
       print ('---------')
       wincheck()
       sys.exit()
listn = [[j-j for j in range(3)] for i in range(3)]
def wincheck() :
    res=False
    rest=False
    for j in range(3):
        res=all(ele==listy[j][0] for ele in listy[j])
        if (res):
            if listy[j][0]!=" ":
             print(listy[j][0],"wins")
             sys.exit()
        else :
            continue

    for j in range(3):
         if listy[0][j]==listy[1][j]==listy[2][j]:
             if listy[0][j]!=" ":
                 print(listy[0][j],"wins")
                 sys.exit()
             else:
                 continue
    if listy[0][0]==listy[1][1]==listy[2][2]:
        if listy[0][0]!=" ":
            print(listy[0][0],"wins")
            sys.exit()
    elif listy[0][2]==listy[1][1]==listy[2][0]:
        if listy[0][2]!=" ":
            print(listy[0][2],"wins")
            sys.exit()
    for w in range(3):
        if " " in listy[w]:
            centerchk()
            sys.exit()

    print ("Draw")
    return
centerchk()

