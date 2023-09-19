from collections import deque
from datetime import datetime, timedelta


def add_robot(robots_str):
    robots = {}
    for robot in robots_str.split(";"):
        name, process_time = robot.split("-")
        robots[name] = [int(process_time), 0]
    return robots


def formatting_time(starting_time_str):
    starting_time = datetime.strptime(starting_time_str, "%H:%M:%S")
    return starting_time


def add_product(product_):
    products_queue = deque()
    while product_ != "End":
        products_queue.append(product_)
        product_ = input()
    return products_queue


def processing_products(robots, starting_time, products_queue):
    while products_queue:
        starting_time += timedelta(0, 1)

        free_robots = []

        for name, time in robots.items():
            if time[1] != 0:
                robots[name][1] -= 1

            if time[1] == 0:
                free_robots.append([name, time])

        if not free_robots:
            products_queue.rotate(-1)
            continue

        robot_name, data = free_robots[0]
        robots[robot_name][1] = data[0]

        print(f"{robot_name} - {products_queue.popleft()} [{starting_time.strftime('%H:%M:%S')}]")


def base_function(robots_str, starting_time_str, product_):
    robots_queue = add_robot(robots_str)
    starting_time = formatting_time(starting_time_str)
    products_queue = add_product(product_)
    processing_products(robots_queue, starting_time, products_queue)


robots_string = input()
starting_time_string = input()
product = input()

base_function(robots_string, starting_time_string, product)