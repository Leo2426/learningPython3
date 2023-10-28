arr = []


def loop():
    stop = ""
    while stop != "done":
        stop = input("Enter number or done ")
        if validate(stop):
            arr.append(int(stop))


def validate(parametro):
    try:
        parametro = int(parametro)
        return True
    except:
        if parametro != "done":
            print("Invalid input")
        return False


def major(array):
    _major = 0
    for number in array:
        if number > _major:
            _major = number
    return _major


def minor(array):
    _minor = 0
    for number in array:
        if _minor == 0:
            _minor = number

        if _minor > number:
            _minor = number

    return _minor


def execute():
    loop()
    print("Maximum", major(arr))
    print("Minimum", minor(arr))



execute()
