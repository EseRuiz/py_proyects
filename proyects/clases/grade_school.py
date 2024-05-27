class School:
    
    def __init__(self):
        self.school = {}
        self.aded = []

    def add_student(self, name, grade):
        self.name = name
        self.gradee = grade
        if self.name not in School.roster(self):
            self.school[self.name] = self.gradee
            self.aded.append(True)
        else: self.aded.append(False)


    def roster(self):
        ros= []
        sort_names = sorted(self.school.items(),  key=lambda t: t[::-1])
        convert_school = dict(sort_names)
        if self.school :
            for k ,v in convert_school.items():
                ros.append(k)
        return ros
    
    def grade(self, grade_number):
        grede = [name for name,grade in self.school.items() if grade == grade_number]
        grede.sort()
        return grede
        

    def added(self):
        return self.aded
