def split_and_join(line):
    x = line.split()
    return "-".join(x)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
