def isfirstnum():
    integers = input("Podaj liczby oddzielone przecinkami: ")
    integers = integers.replace("\n", " ").replace("\t", " ").strip()
    integers = integers.split(",")
    result = []
    for integer in integers:
        integer = int(integer)
        if integer < 2:
            result.append(f"{integer} is not a prime number")
        elif integer == 2:
            result.append(f"{integer} is a prime number")
        else:
            for i in range(2, integer):
                if integer % i == 0:
                    result.append(f"{integer} is not a prime number")
                    break
            else:
                result.append(f"{integer} is a prime number")
    print("\n".join(result))

isfirstnum()