item_a = {'name':'item_A', 'Qualitu':'Best', 'price':'37.9'}
item_b = {'name':'item_B', 'Qualitu':'Good', 'price':'33.5'}
#item_c = {'name':'item_C', 'Qualitu':'Average', 'price':'28.7'}

if item_a['price']<item_b['price']:
    if item_a['Qualitu'] == 'Best' and item_b['Qualitu'] == 'Good' and (item_a['price'] - item_b['price']) > 4:
        Best = item_a
    else:
        Best = item_b
else:
    if item_b['Qualitu'] == 'Best' and item_a['Qualitu'] == 'Good' and (item_b['price'] - item_a['price']) < 4:
        Best = item_b
    else:
        Best = item_a
print(f"Best Item Name is : {Best['name']}")
