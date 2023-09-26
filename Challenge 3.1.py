
def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices
products = ["apple", "banana", "apple", "orange", "apple"]
target_product = "apple"

result = linear_search_product(products, target_product)

if result:
    print(f"The target product '{target_product}' was found at indices: {result}")
else:
    print(f"The target product '{target_product}' was not found.")
