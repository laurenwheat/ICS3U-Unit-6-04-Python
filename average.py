#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: June 2021
# This program determines the smallest of 10 numbers


import random


def avg_2D(list_2D):

    total = 0
    rows = len(list_2D)
    columns = len(list_2D[0])

    for row_value in list_2D:
        for value in row_value:
            total += value

    avg = total / (rows*columns)

    return avg


def main():

    list_2D = []

    while True:
        try:
            rows_input = input("Enter the number of rows: ")
            rows = int(rows_input)
            columns_input = input("Enter the number of columns: ")
            columns = int(columns_input)

            if rows > 0 and columns > 0:

                for loop_counter_rows in range(0, rows):
                    temp_column = []
                    for loop_counter_columns in range(0, columns):
                        random_num = random.randint(0, 50)
                        temp_column.append(random_num)
                        print("{0} ".format(random_num), end="")
                    list_2D.append(temp_column)
                    print(" ")

            avg_array = avg_2D(list_2D)
            avg_rounded = '{0:.5g}'.format(avg_array)

            print("The average is: {0}".format(avg_rounded))
            break

        except Exception:
            print("That is not a valid input!!")


if __name__ == "__main__":
    main()
