def egypt_formula(num, ko, oya):
    if oya % ko == 0:
        return str(oya / ko)

    if oya == num:
        return str(num)

    result = ""
    if oya / ko < num and oya % num == 0:
        result = str(num) + " "
        ko -= oya / num
    return result + egypt_formula(num + 1, ko, oya)

if __name__ == '__main__':
    with open('testdata.in.txt', 'r') as input_file:
        for ko, oya in [l[:-1].split(" ") for l in input_file.readlines()[1:]]:
            print egypt_formula(1, int(ko), int(oya))
