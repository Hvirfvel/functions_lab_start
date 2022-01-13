def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)



list_of_months = [
    {
    "full_name": "January",
    "short_name": "Jan"
    },
    {
    "full_name": "February",
    "short_name": "Feb"
    },
    {
    "full_name": "March",
    "short_name": "Mar"
    },
    {
    "full_name": "April",
    "short_name": "Apr"
    },
    {
    "full_name": "May",
    "short_name": "May"
    },
    {
    "full_name": "June",
    "short_name": "Jun"
    },
    {
    "full_name": "July",
    "short_name": "Jul"
    },
    {
    "full_name": "August",
    "short_name": "Aug"
    },
    {
    "full_name": "September",
    "short_name": "Sep"
    },
    {
    "full_name": "October",
    "short_name": "Oct"
    },
    {
    "full_name": "November",
    "short_name": "Nov"
    },
    {
    "full_name": "December",
    "short_name": "Dec"
    }
]

def number_to_full_month_name(input_num):
    return list_of_months[input_num - 1]["full_name"]

def number_to_short_month_name(input_num):
    return list_of_months[input_num - 1]["short_name"]

def volume_of_cube(length_of_side):
    return length_of_side ** 3

def reverse_string(input_string):
    return input_string[::-1]

def fahrenheit_to_celsius(input_degrees):
    degrees_celsius = (input_degrees - 32) / 1.8
    return int(degrees_celsius)
    