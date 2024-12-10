import sys

def extend(l):
    res = []
    id = 0
    for i, d in enumerate(l.strip()):
        if i % 2 == 0:
            for _ in range(int(d)):
                res.append(id)
            id += 1
        else:
            for _ in range(int(d)):
                res.append(".")
    return res

def getCheck(file):
    res = 0
    for i, n in enumerate(file):
        if n == ".":
            continue
        res += i * n
    return res

def compact(file):
    f, b = 0, len(file) - 1
    while f < b:
        while f < len(file) and file[f] != ".":
            f += 1
        while b >= 0 and file[b] == ".":
            b -= 1
        temp = file[f]
        file[f] = file[b]
        file[b] = temp

    temp = file[f]
    file[f] = file[b]
    file[b] = temp

    return file

def attempt2(file):
    # for every file
        # for every freespace
            # if file fits
                # move file, advance empty space pointer
                # else, look at next file
    
    b_end = len(file) - 1
    while b_end >= 0:
        while file[b_end] == ".":
            b_end -= 1
        b_start = b_end - 1
        while file[b_start] == file[b_end]:
            b_start -= 1
        b_start += 1

        f_start = 0
        while f_start < len(file):
            while file[f_start] != ".":
                f_start += 1
            f_end = f_start + 1
            while f_end < len(file) and file[f_end] == ".":
                f_end += 1
            if f_end > b_start:
                break
            f_end -= 1

            f_range = f_end - f_start
            b_range = b_end - b_start
            if f_range < b_range:
                f_start = f_end + 1
                # could not move case
                continue

            # otherwise swap
            for i in range(b_end - b_start + 1):
                temp = file[f_start + i]
                file[f_start + i] = file[i + b_start]
                file[i + b_start] = temp
            f_start = f_end + 1
        b_end = b_start - 1

def compact2(file):
    f_start, b_end = 0, len(file) - 1
    while f_start < b_end:
        print(file)
        while f_start < len(file) and file[f_start] != ".":
            f_start += 1
        while b_end >= 0 and file[b_end] == ".":
            b_end -= 1

        b_start = b_end
        while file[b_start] == file[b_end]:
            b_start -= 1
        b_start += 1

        f_end = f_start
        while file[f_start] == file[f_end]:
            f_end += 1
        f_end -= 1

        front_range = f_end - f_start
        back_range = b_end - b_start
        if front_range < back_range:
            b_end = b_start - 1
            # could not move case
            continue

        for i in range(b_end - b_start + 1):
            print(i, f_start, b_start)
            temp = file[f_start + i]
            file[f_start + i] = file[i + b_start]
            file[i + b_start] = temp
        b_end -= 1
        f_start = f_end + 1

    return file

if __name__ == "__main__":
    file = sys.argv[1]
    e = ""
    with open(file) as f:
        for l in f:
            e = extend(l)
    print(e)
    c = attempt2(e)
    print(''.join([str(x) for x in e]))

    print(getCheck(e))