import random


def random_string():
    random_list = [
        "Zip folder create successfully."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
