while True:
    data = input()
    if data == "# 0 0":
        break

    name, age, weight = data.split()
    if int(age) <= 17 and int(weight) < 80:
        print(name, "Junior")
    else:
        print(name, "Senior")