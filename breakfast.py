meals = {

    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
     }
sum = 0.0

while True:
    try:
        meal = input("Блюдо: ").lower()
        if meal in meals:
            sum += meals[meal]
    except EOFError:
        break


print(f"\nСумма: {sum:.2f}")