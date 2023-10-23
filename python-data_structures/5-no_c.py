#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i != 'c' and i != "C":
            new_str += i
    return new_str


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))