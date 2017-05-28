def escaperplan(value):
    number = str(value)
    if int(number) < 10:
        return number
    else:
        Bunny_Count = 0
        for counter in number:
            Bunny_Count += int(counter)
    return escaperplan(Bunny_Count)


print(escaperplan(13))