class SellectiveSearch:

    def sellectiveSearch(self, array):
        for i in range(len(array)):
            secondIndex = self.findSmallest(array, i)
            array = self.swap(array, i, secondIndex)
        return array

    @classmethod
    def findSmallest(cls, array, startIndex):
        minIndex = startIndex
        minValue = array[startIndex]
        for i in range(startIndex, len(array)):
            if(minValue > array[i]):
                minIndex = i
                minValue = array[i]
        print(minIndex)
        return minIndex

    @classmethod
    def swap(cls, array, firstIndex, secondIndex):
        temp = array[firstIndex]
        array[firstIndex] = array[secondIndex]
        array[secondIndex] = temp
        return array


class InsertSearh:

    def inserSearch(self, array):
        for i in range(1, len(array)):
            array = self.move(array, i, array[i])
        return array

    @classmethod
    def move(cls, array, startIndex, value):
        i = startIndex
        while(array[i - 1] > array[i] and i > 0):
            temp = array[i - 1]
            array[i-1] = array[i]
            array[i] = temp
            i -= 1
        return array
