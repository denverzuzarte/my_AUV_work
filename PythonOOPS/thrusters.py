class thrusters:
    def __init__(self,co):
        self.coeff=co;
    acc=7;
    def force(self,acc): 
        force=self.coeff;
        return force;
leftT=thrusters(1.01);
print(leftT.force(leftT.acc));