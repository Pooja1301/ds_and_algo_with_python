def getMaximumOccuringChar(input_string):
    freq = [0] * 100
    max = -1

    ch = ' '

    length = len(input_string)

    for i in range(length):
        freq[ord(input_string[i]) - ord('a')] += 1

    for i in range(26):
        if max < freq[i]:
            max = freq[i]
            ch = chr(ord('a') + i)

    return ch


def main():
    print("Enter no of testcases you want to test : ")
    no_of_testcases = int(input())

    for i in range(no_of_testcases):
        print("Enter String : ")
        input_string = input()
        print("Character is : "+getMaximumOccuringChar(input_string))


main()
