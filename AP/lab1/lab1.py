def task_2():
    msg = "Hello, world!"
    print("=" * len(msg) + "\n" + msg + "\n" + "=" * len(msg))

def task_3(a, b):
    try:
        if a < 0 or b < 0 or b == 0:
            raise ValueError
        if a % b == 0:
            return True
        else:
            return False
    except ValueError:
        return "Numbers must be greater than zero!"

def task_4(a, b):
    try:
        if a < b:
            lst = list(range(a, b))
            return lst
        else:
            raise ValueError
    except ValueError:
        return "No simple digits!"

def task_5(a, result = []):
    for i in a:
        if type(i) != list:
            result.append(i)
        else:
            task_5(i, result)
    return result

def task_6():
    msg = "Goodbye, world!"
    print("=" * len(msg) + "\n" + msg + "\n" + "=" * len(msg))

def main():
    task_2()
    print(task_3(25, -5))
    print(task_3(25, 5))
    print(task_3(25, 3))
    print(task_4(7, 5))
    print(task_4(3, 7))
    print(task_4(-7, -5))
    print(task_5([1, [1, 2, 3], [1], [5, [5, ["f"]]]]))
    print(task_5(['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]))
    task_6()
    
main()