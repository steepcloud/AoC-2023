def number_to_words(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= number <= 9:
        return ones[number]
    elif 11 <= number <= 19:
        return teens[number - 10]
    elif 20 <= number <= 99 or number == 10:
        return tens[number // 10] + (ones[number % 10] if number % 10 != 0 else "")
    else:
        return "zero"

with open("spelled_numbers.txt", "w") as file:
    for i in range(100):
        file.write(f"{number_to_words(i)}\n")
