# https://www.acmicpc.net/problem/1259
def palindrome_check(list):
    for i, n in enumerate(list):
        if list[i] != list[-(i + 1)]:
            return False
    return True


while True:
    num = input()
    if num == str(0):
        break
    num_list = list(map(int, num))
    if palindrome_check(num_list):
        print("yes")
    else:
        print("no")