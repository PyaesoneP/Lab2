print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu ():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    user_inputlist = user_input.split(",")
    user_input_float_list = [float(x) for x in user_inputlist]
    return user_input_float_list

def calc_average(temp_list):
    total_temp = 0
    for x in temp_list:
        total_temp += x
    avg = total_temp / len(temp_list)
    return avg

def find_min_max(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    min_max_list = [min_temp, max_temp]
    return min_max_list

def sort_temperature(temp_list):
    sorted_list = temp_list.sort()
    return sorted_list

def calc_median_temperature(temp_list):
    sorted_list = sort_temperature(temp_list=temp_list)