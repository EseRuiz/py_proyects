class Garden:
    
    def __init__(self, diagram, students=""):
        self.diagram = diagram.split("\n")
        self.students = students

    def plants(self,student):
        res = []
        dict_plants = {"G":"Grass", "C":"Clover","R":"Radishes","V":"Violets"}
        dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if len(self.students) < 1:
            ind = dictionary.index(student[0].lower())
            res.append(dict_plants.get(self.diagram[0][(ind*2)]))
            res.append(dict_plants.get(self.diagram[0][(ind*2)+1]))
            res.append(dict_plants.get(self.diagram[1][(ind*2)]))
            res.append(dict_plants.get(self.diagram[1][(ind*2)+1]))
        elif len(self.students) > 1:
            self.students.sort()
            ind2 = self.students.index(student)
            res.append(dict_plants.get(self.diagram[0][(ind2*2)]))
            res.append(dict_plants.get(self.diagram[0][(ind2*2)+1]))
            res.append(dict_plants.get(self.diagram[1][(ind2*2)]))
            res.append(dict_plants.get(self.diagram[1][(ind2*2)+1]))
        return res

# garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
# print(garden.plants("Alice"), ["Violets", "Radishes", "Violets", "Radishes"])