#knights and knaves

print ("Knights an Knaves");

import random

#number of players

n=int(input("number of players"));

#playerlist
i=0;
player=[];
#giving identity
while (i<n):
    player.append([i]);
    i=i+1;
#giving roles
i=0;
while (i<n):
    if(random.random()<0.5):
        player[i].append('knave');
        i=i+1;
    else:
        player[i].append('knight');
        i=i+1;

imp=random.randint(0,n-1);
player[imp]=[imp,"imp"];

#asking questions
def quest(i,j):
    ians="";
        if (player[i][1]=='knight'):
            if (player[j][1]=="knight"):
                ians='yes';
            elif (player[j][1]=="knave"):
                ians='yes';
            elif (player[j][1]=="imp"):
                ians='yes';

         elif (player[i][1]=="knave"):
            if (player[j][1]=="knight"):
                       ians='yes';

            elif (player[j][1]=="knave"):
                   ians='yes';

            elif (player[j][1]=="imp"):
                ians='yes';


          elif (player[i][1]=="imp"):
            if (player[j][1]=="knight"):
                ians='yes';

            elif (player[j][1]=="knave"):
                       ians='yes';
    return ians;
i=0;
while (i<n/2):
    if (quest(i,i+1)==quest(i+1,i)):
        i=i+2;
        incap=True;
    else:
        incap=False;
        if(quest(i-1,i)==quest(i,i-1)):
            imp=i;
        else:
            imp=i-1;
        break;
if(incap):
    imp=n-1;

print("IMP = "+imp);




print(player);

