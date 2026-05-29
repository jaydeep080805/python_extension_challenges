import os
import math

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    return os.path.isfile(filename)


def clean_empty_vals(data):
    indexes_to_remove = []

    for index, entry in enumerate(data):

        if entry.split(";")[0] == "":
            indexes_to_remove.append(index)
            # print(entry)

    # clear the empty values
    count = 0
    for i in indexes_to_remove:
        try:
            data.pop(i - count)
            count += 1
        except IndexError as e:
            print("not in range")

    return data

# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
def get_file_contents(filename):
    if does_file_exist(filename) == False:
        return "This file cannot be found!"
    
    with open(filename, "r") as file:
        return file.readlines()

# print(get_file_contents("AirQuality.csv"))

# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def christmas_day_air_quality(filename, include_header_row):
    data = get_file_contents(filename)
    # print(data[0])

    christmas_data = []

    if (include_header_row == True):
        christmas_data.append(data[0])

    # print(data[0])

    for i in data:
        if i[0:5] == "25/12":
            christmas_data.append(i)

    return christmas_data

# print(christmas_day_air_quality("AirQuality.csv", True))

# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    data = christmas_day_air_quality(filename, True)
    # print(data[0].split(";"))
    # print(data[1].split(";"))

    amount_of_entries = len(data[1:])
    # print(amount_of_entries)

    total_pto = 0

    data_without_header = data[1:]
    
    for air_quality in data_without_header:
        # print(air_quality.split(";")[3])
        total_pto += int(air_quality.split(";")[3])
        # print((air_quality.split(";")[3]))

    mean_average = (total_pto / amount_of_entries)
    return round(mean_average, ndigits=2)

christmas_day_average_air_quality("AirQuality.csv")

# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    data = get_file_contents(filename)

    monthly_averages = {}
    indexes_to_remove = []

    for index, entry in enumerate(data):

        if entry.split(";")[0] == "":
            # print(entry)
            indexes_to_remove.append(index)

    # clear the empty values
    count = 0
    for i in indexes_to_remove:
        try:
            data.pop(i - count)
            count += 1
        except IndexError as e:
            print("not in range")


    # for index, entry in enumerate(data):
    #     print(entry.split(";"))

        # if entry.split(";")[0] == "":
        #     data.pop(index)
        #     print(index)
        #     print(entry)

    # print(data)
    # for entry in data:
    #     print(entry)

    amount_of_entries_per_month = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    total_polution_per_month = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    
    data_without_header = data[1:]

    for entry in data_without_header:
        date = (entry.split(";")[0].split("/"))

        # turn into an into to remove the first 0
        month = int(date[1])
        air_quality = int(entry.split(";")[3])

        amount_of_entries_per_month[month] = amount_of_entries_per_month[month] + 1
        total_polution_per_month[month] = total_polution_per_month[month] + air_quality

    for key, val in total_polution_per_month.items():
        monthly_averages[key] = round(val / amount_of_entries_per_month[key], ndigits=2)

    return (monthly_averages)

# get_averages_for_month("AirQuality.csv")

# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    data = get_file_contents(filename)

    march_data = [data[0]]

    indexes_to_remove = []

    for index, entry in enumerate(data):

        if entry.split(";")[0] == "":
            indexes_to_remove.append(index)
            # print(entry)

    # clear the empty values
    count = 0
    for i in indexes_to_remove:
        try:
            data.pop(i - count)
            count += 1
        except IndexError as e:
            print("not in range")

    for i in data:
        try:
            month = int((i.split(";")[0].split("/")[1]))

            if month == 3:
                march_data.append(i)


        except Exception as e:
            print(e)

    with open("AirQualityMarch.csv", "w") as file:
        for date_entry in march_data:
            # print(date_entry)
            file.write(date_entry)
            

    return


# create_march_data("AirQuality.csv")

# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    if os.path.exists("monthly_responses") == False:
        os.makedirs("monthly_responses")

    data = clean_empty_vals(get_file_contents(filename))
    data_without_headers = data[1:]

    monthly_keys = {}

    for i in data_without_headers:
        try:
            month = i.split(";")[0].split("/")[1]
            year = i.split(";")[0].split("/")[2]
            temp_key = f"{month}-{year}"

            monthly_keys[temp_key] = []
        except Exception as e:
            print(e)

    for i in data_without_headers:
        try:
            month = i.split(";")[0].split("/")[1]
            year = i.split(";")[0].split("/")[2]
            temp_key = f"{month}-{year}"

            monthly_keys[temp_key].append(i)

        except Exception as e:
            print(e)

    # print(monthly_keys)


    for key in monthly_keys.keys():
        with open(f"monthly_responses/{key}.csv", "w") as file:
            file.write(data[0])
            file.writelines(monthly_keys[key])

    return

create_monthly_responses("AirQuality.csv")