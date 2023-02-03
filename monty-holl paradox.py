'''Скрипт автоматической прогонки парадокса Монти-Холла'''
import random


def monty(will_change):
    boxes = [1, 2, 3]
    gift_box = random.choice(boxes)
    selected_box = random.choice(boxes)
    if will_change:
        if selected_box != gift_box:
            boxes.remove(selected_box)
            while True:
                box_to_open = random.choice(boxes)
                if box_to_open != gift_box:
                    break
            boxes.remove(box_to_open)
        selected_box = random.choice(boxes)
    return [selected_box, gift_box]


total_tries = 10000000

# will_change = True
will_change = False

match_counter = 0
unmatch_counter = 0
rate = None

for i in range(total_tries):
    data = monty(will_change)
    if data[0] == data[1]:
        match_counter += 1
    else:
        unmatch_counter += 1

rate = match_counter/total_tries

print("Всего попыток: ", total_tries)
print("Угадано ", match_counter, " раз, не угадано ", unmatch_counter, " раз. Доля угадываний: ", rate)
