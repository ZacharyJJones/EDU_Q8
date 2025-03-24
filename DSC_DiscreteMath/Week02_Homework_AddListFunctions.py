import ctypes


class CreateList:

    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def append(self, item):

        if self.n == self.size:
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n = self.n + 1

    def find(self, item):

        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'

    def remove(self, item):

        pos = self.find(item)
        if type(pos) == int:

            self.__delitem__(pos)
        else:
            return pos

    def __resize(self, new_capacity):

        B = self.__make_array(new_capacity)
        self.size = new_capacity

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    def __getitem__(self, index):

        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

    def __delitem__(self, pos):

        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]

            self.n = self.n - 1

    def __make_array(self, capacity):

        return (capacity * ctypes.py_object)()

    # using same logic as when creating a new list
    def clear(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def insert_at(self, index, value):
        if index < 0:
            return 'IndexError'

        # we will let the append method handle
        # ... increasing size where necessary
        self.append(value)

        for i in range(self.n, index + 1, -1):
            self.A[i] = self.A[i - 1]
            pass

        self.A[index] = value


listC = CreateList()

listC.append("Hello")
listC.append(230)
listC.append(34.20)

print(listC)