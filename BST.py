class Histogram():
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.parent = None

class Node():
    def __init__(self, element1, element2, value, freq):
        self.left = element1
        self.right = element2
        self.value = value
        self.freq = freq

def GetHistogram(charList):
    dictionary = dict()
    list = []

    for char in charList:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    for i in dictionary:
        temp = Histogram(i, dictionary[i])
        list.append(temp)

    return list

def RemoveElement(element, list):
    list.remove(element)

def AddElement(element, list):
    list.append(element)

def GetMinimumFrequencyElement(list):
    temp = list[0]

    for element in list:
        if element.freq < temp.freq:
            temp = element

    return temp

def CreateNewElement(element1, element2):
    val = element1.value + element2.value
    freq = element1.freq + element2.freq

    newNode = Node(element1, element2, val, freq)

    element1.parent = newNode
    element2.parent = newNode

    return newNode

def GetEncodedValue(element, list):
    encodedValue = ""

    while element not in list:
        if element.parent.left.freq >= element.parent.right.freq:
            if element.parent.left == element:
                encodedValue += "1"
            else:
                encodedValue += "0"
        else:
            if element.parent.right == element:
                encodedValue += "0"
            else:
                encodedValue += "1"

        element = element.parent

    return encodedValue[::-1]

if __name__ == "__main__":
    input1 = ['a', 'b']
    print(input1)

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    print(input2)

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    print(input3)

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    print(input4)

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    print(input5)

    allInputs = [input1, input2, input3, input4, input5]

    for i in allInputs:
        histogram = GetHistogram(i)

        temp = histogram[:]

        print("Input:", i)

        for j in histogram:
            print("Value:", j.value, ", Frequency:", j.freq)

        while len(histogram) > 1:
            element1 = GetMinimumFrequencyElement(histogram)
            RemoveElement(element1, histogram)
            element2 = GetMinimumFrequencyElement(histogram)
            RemoveElement(element2, histogram)
            histogram.append(CreateNewElement(element1, element2))

        dictionary = dict()

        print("Output:")

        out = ""

        for encode in temp:
            a = GetEncodedValue(encode, histogram)
            dictionary[encode.value] = a

        for k in i:
            out += dictionary[k] + " | "

        print(out)
