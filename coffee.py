price_per_coffee = 50
total_inserted = 0
print ("Нужная сумма:",price_per_coffee - total_inserted)

while total_inserted < price_per_coffee:
    coin = input("Вставьте монету: ")

    if coin == "50" or coin == "20" or coin == "10" or coin == "5":
        total_inserted += int(coin)

change_owed = total_inserted - price_per_coffee

print(f"Ваша сдача: {change_owed}")
