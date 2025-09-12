# List
data_list = []

# Read data from file and store in the list
def file():
    try:
        with open("DATA.txt", "r") as file:
            text = file.read()
            try:
                for number in text.split():
                    data_list.append(int(number))
            except ValueError:
                print("Error: Non-integer value found in the data file.")
    except FileNotFoundError:
        print("Error: File not found.")

# Mean
def datamean(data_list):
    return sum(data_list) / len(data_list)

# Median
def datamedian(data_list):
    sorted_list = sorted(data_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid - 1], sorted_list[mid])
    else:
        median = sorted_list[mid]
    return median

# Call the functions and print the results
file()
datamean(data_list)
datamedian(data_list)

print(f"The mean of the data set is: {datamean(data_list)}")
print(f"The median of the data set is: {datamedian(data_list)}")