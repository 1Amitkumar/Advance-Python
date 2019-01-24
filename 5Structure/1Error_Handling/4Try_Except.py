value = ["22", "33", "40", "51", "16", "17", "18", "19", "10", "A", "M", "I", "T"]


for val in value:               # print all values divisible by 2:
    try:
        num = int(val)
        if num % 2 == 0:
            print(val, "is an even val.")
    except ValueError:
        print(val, "can not be divided")
    else:
        print(val, "could be divided")
    finally:
        print("next number.")

