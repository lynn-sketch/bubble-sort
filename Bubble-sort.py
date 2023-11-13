class Bubble(object):
    def __init__(self, numbers):
        self.numbers = numbers
        
    def implementation(self):
        for i in range(len(self.numbers)-1, 0, -1):
            for j in range(i):
                if self.numbers[j] > self.numbers[j+1]:
                    temp = self.numbers[j]
                    self.numbers[j] = self.numbers[j+1]
                    self.numbers[j+1] = temp
        return self.numbers     
      
if __name__ == '__main__':
    numbers = []
    size = int(input('Enter the size of the list: '))
    print(f'Enter your {size} numbers: ')
    for number in range(size):
        number_inputs = int(input(''))
        numbers.append(number_inputs)

    bubble = Bubble(numbers)
    sorted = bubble.implementation()
    print(sorted)
              

                    
                    