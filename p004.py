def largest_palindrome():
    largest_num = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            num = i * j
            if str(num) == str(num)[::-1]:  # it is a palindrome
                largest_num = num if num > largest_num else largest_num

    return largest_num


print(largest_palindrome())
