# Consider using the modules imported above.
import random


class Hat:
    def __init__(self, red=0, orange=0, yellow=0, blue=0, green=0):
        self.contents = [];
        for i in range(red):
            self.contents.append('red')
        for i in range(orange):
            self.contents.append('orange')
        for i in range(yellow):
            self.contents.append('yellow')
        for i in range(blue):
            self.contents.append('blue')
        for i in range(green):
            self.contents.append('green')
        print(self.contents)

    def draw(self, num_of_balls):
        if num_of_balls > len(self.contents):
            self.contents = []

        remove_list = []
        for i in range(num_of_balls):
            remove_index = random.randint(0, len(self.contents) - 1)
            remove_item = self.contents[remove_index]
            remove_list.append(remove_item)
            del self.contents[remove_index]
        print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    for key, value in expected_balls.items():
        print(key, value)
    hat.draw(num_balls_drawn)
