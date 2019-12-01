from NorgesGruppen.norgesgruppen import Store
from NorgesGruppen.norgesgruppen import Product

spar = Store(1210)
cola = Product(spar, 'Cola')

print('\ncontent_type:')
print(cola.get_content_type())

print('\nget_title:')
print(cola.get_title())

print('\nget_description:')
print(cola.get_description())

print('\nget_content_id:')
print(cola.get_content_id())

print('\nget_content_image:')
print(cola.get_content_image())

print('\nget_content_index:')
print(cola.get_content_index())

print('\nget_content_underscore_type:')
print(cola.get_content_underscore_type())

print('\nget_content_underscore_id:')
print(cola.get_content_underscore_id())

print('\nget_unit_weight:')
print(cola.get_unit_weight())

print('\nget_shopping_list_group_name:')
print(cola.get_shopping_list_group_name())

print('\nget_source_title:')
print(cola.get_source_title())

print('\nget_category_name:')
print(cola.get_category_name())

print('\nget_calc_unit:')
print(cola.get_calc_unit())

print('\nget_price:')
print(cola.get_price())

print('\nget_unit_type:')
print(cola.get_unit_type())

print('\nget_age_limit:')
print(cola.get_age_limit())

print('\nget_recycle_value:')
print(cola.get_recycle_value())

print('\nget_ean:')
print(cola.get_ean())

print('\nget_total_hits:')
print(cola.get_total_hits())
