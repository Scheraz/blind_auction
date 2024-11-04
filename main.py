import art
print(art.logo)
print("Welcome to the secret auction program")

dictionary = {}
bidders = True
while bidders:
    name = input("What is your name?: ")

    while True:
        try:
            bid = int(input("What's your bid?: $"))
            break
        except ValueError:
            print("Invalid number. Type a positive number")

    dictionary[name] = bid

    max_key = max(dictionary, key=dictionary.get)
    max_value = dictionary[max_key]
    max_value_dict = {max_key:max_value}



    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")

    while other_bidders not in ['yes', 'no']:
        print("Invalid input. Type 'yes' or 'no'")
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")


    if other_bidders == "yes":
        print("\n" * 20)

    elif other_bidders == "no":
        bidders =  False
        print(f"This winner is {max_key} with bid of {max_value_dict[max_key]}")







