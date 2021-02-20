class ProblemOne():    
    
    def __init__(self, size, multiple_one, multiple_two):
        self.size = size
        self.multiple_one = multiple_one
        self.multiple_two = multiple_two
        list_one = self.get_multiples(self.size, self.multiple_one)
        list_two = self.get_multiples(self.size, self.multiple_two)
        print(sum(list_one) + sum(list_two))

    def get_multiples(self, size, multiple):
        list_of_multiples = []
        for i in range(size):
            list_of_multiples.append(i*multiple)
        return list_of_multiples            

class ProblemTwo():

    def __init__(self):
        self.starting_value_one = 1
        self.starting_value_two = 2
        self.fib_limit = 4000000
        print(sum(self.generate_fib_sequence()))

    def generate_fib_sequence(self):
        current_value_one = self.starting_value_one
        current_value_two = self.starting_value_two
        values = [current_value_one, current_value_two]
        while True:            
            temp = current_value_one + current_value_two
            current_value_one = current_value_two
            current_value_two = temp
            if temp >= self.fib_limit:
                break
            else:
                if temp % 2 == 0:
                    values.append(temp)
        return values        

class ProblemThree():
    def __init__(self, number):
        self.number = number
    
    def generate_prime_factors():
        print("primes")