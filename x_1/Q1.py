import abc
from math import factorial

class Phone(abc.ABC):
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size
    
    @abc.abstractmethod
    def special_feature(self):
        return NotImplemented


class GooglePhone(Phone):
    def __init__(self):
        super().__init__(price=10, camera_count=3, screen_size=5)
    
    def __check_int_list(self, int_list):
        if type(int_list) is not list:
            print("Input data is not a list.")
            return False
        for element in int_list:
            if type(element) is not int:
                print("A element which type is not int in list.")
                return False
        return True
    
    def special_feature(self, int_list):
        if self.__check_int_list(int_list):
            target_nums = []
            for num in int_list:
                if num > 10 and num % 2 == 0:
                    target_nums.append(num)
            return sorted(target_nums, reverse=True)


class TaiwanPhone(Phone):
    def __init__(self):
        super().__init__(price=20, camera_count=1, screen_size=3)

    def __fibonacci(self, n):
        if n == 0 or n ==1:
            return n
        else:
            return self.__fibonacci(n - 1) + self.__fibonacci(n - 2)

    def special_feature(self, num):
        if num < 0:
            print("Input number is not a positive number.")
            return 0
        fib_number = self.__fibonacci(num)
        if fib_number < 10:
            print("x is zero.")
            return 0
        x = fib_number % 100 // 10
        y = fib_number % 10
        if x < y:
            print("x < y")
            return 0
        return factorial(x) // factorial(x - y)