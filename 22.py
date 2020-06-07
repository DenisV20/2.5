import time

class Timer:
    def __init__(self):
        self.time = time.time()

    def __enter__(self):
        print(f' Стартовое время {time.ctime(self.time)}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f' Время потраченное {time.time() - self.time}')

with Timer():
    def new_book(file_out):

        with open('recipes.txt', 'r', encoding='UTF-8') as fi:
            cook_book = {}
            for line in fi:
                dishes = line.strip()
                cook_book[dishes] = []
                counter = int(fi.readline().strip())

                for i in range(counter):
                    list_of_ingredients = fi.readline().strip().split('|')
                    temp_dict = {'ingredient_name': list_of_ingredients[0], 'quantity': list_of_ingredients[1],
                                 'measure': list_of_ingredients[2]}
                    cook_book[dishes].append(temp_dict)
                fi.readline()
            return cook_book


    print(new_book('fi'))