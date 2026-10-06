## Jay Vie R. Sodsod
## 9 - Silicom

## This line asks the user's birth year
year = int(input("Enter your birth year: "))

## Checks if the it is less than 1900 and prints an error message if it is
if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    ## Continues with the calculation if the year is valid
    zodiac_animals = [
        ("Rat", "鼠 / Shǔ"),
        ("Ox", "牛 / Niú"),
        ("Tiger", "虎 / Hǔ"),
        ("Rabbit", "兔 / Tù"),
        ("Dragon", "龙 / Lóng"),
        ("Snake", "蛇 / Shé"),
        ("Horse", "马 / Mǎ"),
        ("Goat", "羊 / Yáng"),
        ("Monkey", "猴 / Hóu"),
        ("Rooster", "鸡 / Jī"),
        ("Dog", "狗 / Gǒu"),
        ("Pig", "猪 / Zhū")
    ]

    ## Subtracts the year with 1900 to get a simpler number
    ## Calculates the index of the zodiac animal by taking the remainder of the division by 12
    index = (year - 1900) % 12
    name, chinese = zodiac_animals[index]
    print(f"Your Chinese Zodiac Sign is: {name} ({chinese})")
