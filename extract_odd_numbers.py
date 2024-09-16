def extract_odd_inlist(potato: list) -> list:
    oddnumberlist : list = []
    print("ODD NUMBERS")

    for value in potato:
        if value is not None and value % 2 == 0:
            # push value inside oddNumberList
            oddnumberlist.append(value)
            print(f"{potato.index(value)}. {value}")
        # print(value)
    return oddnumberlist


def extract_odd_in_tuple(potato: list) -> tuple:
    oddnumberlist : tuple = ()
    print("ODD NUMBERS")

    for value in potato:
        if value is not None and value % 2 == 0:
            # push value inside oddNumberList
            oddnumberlist += (value,)
            print(f"{potato.index(value)}. {value}")
        # print(value)
    return oddnumberlist





def main():
    potatolist: list = [-1, 0, 14, 80, None, 22]
    potatolist2: list = [11.5, 0, None, -20, None, 22]
    print(f"returning a list of odd numbers")
    extract_odd_inlist(potatolist)
    print(f"returning a tuple of odd numbers")
    extract_odd_in_tuple(potatolist2)

if __name__ == "__main__":
    main()