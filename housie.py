import random
import numpy as np
from tabulate import tabulate
from datetime import date


def _sort_col(ticket_array, col):
    print(ticket_array[:, col], end=" ")
    s = sorted(ticket_array[:, col])
    while 0 in s:
        s.remove(0)
    for i in [0, 1, 2]:
        if ticket_array[i][col] != 0:
            ticket_array[i][col] = s.pop(0)
    print(ticket_array[:, col])


def get_ticket(username):
    date_str = date.today().strftime("%Y%m%d")
    seed = date_str + username
    random.seed(seed)
    ticket_array = np.zeros((3, 9), dtype=int)
    total_indices = [(i, j) for i in range(3) for j in range(9)]
    random_indices = []

    first_row = random.sample(total_indices[:9], 5)
    second_row = random.sample(total_indices[9:18], 5)
    third_row = random.sample(total_indices[-9:], 5)

    for i in first_row:
        random_indices.append(i)

    for i in second_row:
        random_indices.append(i)

    for i in third_row:
        random_indices.append(i)

    total_numbers = list(range(1, 91))

    for num in random_indices:
        start = num[1] * 10
        end = start + 10
        number = 0
        while number == 0:
            number = random.choice(total_numbers[start:end])
        ticket_array[num] = number
        total_numbers[number - 1] = 0

    for col in range(9):
        _sort_col(ticket_array, col)

    ticket_table = tabulate(ticket_array, tablefmt="html", numalign="center", stralign="center")
    ticket_table = ticket_table.replace("<table>", "<table border=1>")
    ticket_table = ticket_table.replace("style=\"", "style=\"padding: 10px;")
    ticket_table = ticket_table.replace("\">0 </", "\">&nbsp;&nbsp;&nbsp;</")
    ticket_table = ticket_table.replace("\">0</", "\">&nbsp;&nbsp;&nbsp;</")
    return ticket_table
