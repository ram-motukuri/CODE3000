class Participant():
    def __init__(self,name,rollno,cgpa,branch=""):
        self.name=name
        self.rollno=rollno
        self.cgpa=cgpa
        self.branch=branch
    def isValidRollNo(self):
        global branches
        rollno=self.rollno
        if(len(rollno)!=10):
            return False
        try:
            year=int(rollno[:2])
        except:
            return "Invalid Year"
        if(rollno[2:4]!="A3"):
            return "Not a student of Pragati Engineering College"
        if(rollno[4:6]!="1A" and rollno[4:6]!="5A"):
            return "Not a valid Student"
        if(rollno[6:8] not in list(branches.keys())):
            return "Invalid Branch"
        else:
            self.branch=branches[rollno[6:8]]
        return True
    def isValidName(self):
        return self.name.isalpha()
    def isValidcgpa(self):
        cgpa=self.cgpa.split(".")
        if(len(cgpa)==2):
            try:
                num=int(cgpa[0])
                fraction=int(cgpa[1])
                if(num<10 and num>=0):
                    if(fraction<9 and fraction>=0):
                        return True
                    else:
                        return False
                elif(num==10):
                    if(fraction==0):
                        return True
                    else:
                        return False
                else:
                    return False
            except:
                return "Invalid CGPA"
        else:
            return False
    def toString(self):
        return self.name+"\t"+self.rollno+"\t"+str(self.cgpa)+"\t"+self.branch
    def add_participant(self):
        db=open("db.txt",'a')
        db.write(self.toString()+"\n")
        db.close()
    def delete_participant(self):
        with open("db.txt", "r") as f:
            lines = f.readlines()
        with open("db.txt", "w") as f:
            for line in lines:
                line=line.strip("\n")
                if(self.rollno not in line):
                    f.write(line+"\n")
            f.close()
    def validate_participant(self):
        flag1=self.isValidRollNo()
        flag2=self.isValidName()
        flag3=self.isValidcgpa()
        if(type(flag1)==bool):
            if(flag1):
                if(flag2==False):
                    print("Invalid Name")
                    return
                if(type(flag3)==bool):
                    if(flag3==False):
                        print("Invalid CGPA")
                        return
                else:
                    print(flag3)
                    return
            else:
                print("Invalid RollNo")
                return
        else:
            print(flag1)
            return
        if(flag1 and flag2 and flag3):
            return True
branches={"01":"CIVIL","02":"EEE","03":"MECH","04":"ECE","05":"CSE","12":"IT"}
def map(inp,branch=""):
    details=inp.split(":")
    return Participant(details[0],details[1],details[2],branch)
def getParticipantByName(name):
    with open("db.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if(name in line):
            return ':'.join(line.split("\t"))
print("*************Welcome to CODE 3000****************")
db=open("db.txt",'w')
db.close()
while(1):
    print("1.Add Participant Details")
    print("2.Delete Participant Details")
    print("3.Show Participants")
    print("4.Update exisiting Participant Details")
    print("5:Exit")
    choice=int(input("Make your choice: "))
    if(choice==1):
        print("Enter the participant details in the below format")
        print("Name:RollNo:CGPA")
        participant=map(input())
        if(participant.validate_participant()):
            participant.add_participant()
    elif(choice==2):
        del_participant=input("Enter the name of the participant you want to delete")
        participant=getParticipantByName(del_participant)
        participant=map(participant,branch=participant.split(":")[3])
        participant.delete_participant()
    elif(choice==3):
        with open("db.txt",'r') as db:
            lines=db.readlines()
        for i in lines:
            print(i.strip("\n"))
    elif(choice==4):
        name=input("Enter the participant name to update his/her details: ")
        participant=getParticipantByName(name)
        participant=map(participant)
        participant.delete_participant()
        print("Enter the updated details in below format")
        print("Name:RollNo:CGPA")
        participant=map(input())
        participant.validate_participant()
        participant.add_participant()
    elif(choice==5):
        break
    else:
        print("Invalid Input")