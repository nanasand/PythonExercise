def format_address(address_string):
    # Declare variables
    house_number = " "
    street_name = " "

    # Separate the address string into parts
    address_string = address_string.split()
    # Traverse through the address parts
    for number in address_string:
        # Determine if the address part is the
        # house number or part of the street name
        if number.isdigit():
            house_number = number
    # Does anything else need to be done
    # before returning the result?
        else:
            street_name += number
            street_name += " "
    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# replace method https://www.w3schools.com/python/ref_string_replace.asp

def highlight_word(sentence, word):
    return(sentence.replace(word, word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# range exercise

def squares(start, end):
    return [number**2 for number in range(start, end+1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# reverse, range exercise

def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order

    new_list = list2
    for i in reversed(range(len(list1))):
        new_list.append(list1[i])
    return new_list

# dictionary exercise


def car_listing(car_prices):
    result = ""
    for cars in car_prices:
        result += "{} costs {} dollars".format(cars, car_prices[cars]) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
      "Ford Fiesta": 13000, "Toyota Prius": 24000}))
