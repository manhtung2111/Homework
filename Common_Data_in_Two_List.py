class CommonData:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_common(self):
        result = False
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    result = True
        return result


lst1 = [1, 2, 3, 4, 10]
lst2 = [5, 6, 7, 8, 9, 10]
func = CommonData(lst1, lst2)
print(func.find_common())
