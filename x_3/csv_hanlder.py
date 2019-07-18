import os
from random import choice, choices
from string import ascii_letters, digits

import pandas as pd

FOLDER = "ilovecoffee"
NAME_LIST = ["tom", "ray", "andy", "john", "peter",
             "lisa", "tina", "vivian", "clara", "sharon"]
COUSTOMER_COUNT = 500

class Coustomer(object):
    def __init__(self):
        self.customer_id = self.__generate_customer_id()
        self.customer_name = self.__generate_cutomer_name()
        self.customer_mobile = self.__generate_customer_mobile()
        self.frequency = self.__generate_frequency()

    def __generate_customer_id(self):
        return ''.join([choice(ascii_letters)] + choices(ascii_letters + digits, k=7))

    def __generate_cutomer_name(self):
        return choice(NAME_LIST) + "." + self.customer_id

    def __generate_customer_mobile(self):
        return ''.join(["+8869"] + choices(digits, k=8))

    def __generate_frequency(self):
        return choice(range(21))


class CsvHanlder(object):
    def __init__(self):
	    if not os.path.isdir(FOLDER):
	        os.mkdir(FOLDER)

    def __generate_customers(self):
        coustomer_list = []
        used_customer_mobile = []
        for _ in range(COUSTOMER_COUNT):
            coustomer = Coustomer()
            while coustomer.customer_mobile in used_customer_mobile:
                coustomer = Coustomer()
            used_customer_mobile.append(coustomer.customer_mobile)
            coustomer_list.append(coustomer)
        return coustomer_list

    def create_csv(self):
        coustomers = self.__generate_customers()
        customers_df = pd.DataFrame([c.__dict__ for c in coustomers],
                                    columns=["customer_id", "customer_name", "customer_mobile", "frequency"])
        customers_df.to_csv("ilovecoffee/customers.csv", index = 0)

    def calculate_csv(self):
        if not os.path.isfile("ilovecoffee/customers.csv"):
            print("The file \"ilovecoffee/customers.csv\" does not exist.")
            return 0
        customers_df = pd.read_csv("ilovecoffee/customers.csv")
        frequency_series = pd.Series(customers_df["frequency"])
        print("Frequency: median: {}, mode: {}, mean: {:.5f}".format(frequency_series.median(), frequency_series.mode()[0], frequency_series.mean()))