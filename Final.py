import math
import numpy as np
import array as arr
class Q:
    def get_bit(self,num_qubits):
        global c
        global phia
        c=num_qubits
        phia =arr.array('i',[])   
        for i in range(0,2**int(num_qubits)):
            if(i==0):
                phia.append(1)
            else:
                phia.append(0)  
        return(phia)

    def operator(self,O):
        print('Operator::',)
        print(O)
        total=2**int(c)
        I = np.identity(2)
        if int(c)==1:
            gate_unitary = np.array([1, 0])
            return gate_unitary  
        elif int(c)==2:
            gate_unitary=np.kron(I,O)
            return gate_unitary
        elif int(c)==3:
            gate_unitary=np.kron(np.kron(I, I), O)
            return gate_unitary
    def Hadamard(self):
        self.h= np.array([
            [1/np.sqrt(2), 1/np.sqrt(2)],
            [1/np.sqrt(2), -1/np.sqrt(2)]
            ])
        s=self.operator(self.h)
        print ("Initial State::",)
        print (phia)
        result=np.dot(phia,s)
        return result
    
    def XGate(self):
        self.x = np.array([
                    [0, 1],
                    [1, 0]
                    ])
        s=self.operator(self.x)
        print ("Initial State::",)
        print (phia)
        result=np.dot(phia,s)
        return result

    def measure_all(self):
        print("Index(dec)\tAmplitude \t Probability \n========================================")
        index=0
        for i in phia:
            probability=np.abs(i)**2
            print (str(index)+'                     '+ str(i)+'                      ' +str(probability))
            index=index+1
        return "END !!"

#Main Program
q=Q()
e="RUNNING"
while True:
    print(e.center(100,'='))
    b=input("Enter:")
    print(q.get_bit(b))
    print("OPERATIONS:")
    print("1.Hadamard Gate")
    print("2.X Gate")  
    a=int(input("Enter your choice(1 or 2):"))
    r='Final result:: '

    if (a==1):
        print (r,q.Hadamard())
        print ("Measures")
        print(q.measure_all())
    elif (a==2):
        print (r,q.XGate())
        print ("Measures")
        print(q.measure_all())
    
