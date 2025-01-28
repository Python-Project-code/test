products = {"Laptop": 800, "Mouse": 25, "Keyboard": 45, "Monitor": 150}


filtered_products = sorted(
    [(product,price)for product,price in products.items() if price > 25]
)

print(filtered_products)



nums = [1, 2, 3, 4, 5, 6, 7]

res_nums = [
    num*num for num in nums if num %2 !=0
]
print(res_nums)

