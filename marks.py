class Students:
    def __init__(self):
        self.s1=self.getMarks()
        self.s2=self.getMarks()
        self.s3=self.getMarks()
        self.s4=self.getMarks()
        self.s5=self.getMarks()

    def getMarks(self):
        try:
            return int(input("please enter marks:"))
        except:
            print("exception: invalid input")

    def totalMarks(self):
        return self.s1+self.s2+self.s3+self.s4+self.s5
    
    def getGrade(self):
        percent = self.totalMarks()/5
        if percent >=90:
            return "Merit"
        elif(percent>=60 and percent<90):
            return "1st"
        elif(percent>=50 and percent<60):
            return "2nd"
        elif(percent>=33 and percent<50):
            return "3rd"
        else:
            return "Fail"

m1 = Students()
print(m1.getGrade())