# Take a sample dictionary
sample_dict = {'key_1': 3.14, 'key_2': 1.618,
               'key_3': True, 'key_4': [3.14, 1.618],
               'key_5': (3.14, 1.618), 'key_6': 2022, (3.14, 1.618): 'pi and golden ratio'}
sample_dict


# Accessing to the value using the key
print(sample_dict['key_1'])
print(sample_dict['key_2'])
print(sample_dict['key_3'])
print(sample_dict['key_4'])
print(sample_dict['key_5'])
print(sample_dict['key_6'])
print(sample_dict[(3.14, 1.618)]) # Keys can be any immutable object like tuple



# Take a sample dictionary
product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
product


# Retrieving the value by keys
print(product['Aspergillus niger'])
print(product['Saccharomyces cerevisiae'])
print(product['Scheffersomyces stipitis'])


# What are the keys in the dictionary?
product.keys()


# What are the values in the dictionary?
product.values()


product['Yarrovia lipolytica'] = 'microbial oil'
product


del(product['Aspergillus niger'])
del(product['Aspergillus sojae_1'])
product


del product
print(product)
# The dictionary was deleted.


print('Saccharomyces cerevisiae' in product)
print('Saccharomyces cerevisiae' not in product)


dict_sample = dict(family = 'music', type='pop', year='2022' , name='happy new year')
dict_sample



# Numerical index is not used to take the dictionary values. It gives a KeyError
dict_sample[1]


dict_sample = dict(family = 'music', type='pop', year='2022' , name='happy new year')
dict_sample.clear()
dict_sample


sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
sample_copy = sample_original.copy()
print(sample_original)
print(sample_copy)


# This method can be made usign '=' sign
sample_copy = sample_original
print(sample_copy)
print(sample_original)


sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
print(sample_original.pop('type'))
print(sample_original)


sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
print(sample_original.popitem())
print(sample_original)


sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
print(sample_original.get('family'))
print(sample_original.get(3))


keys = {'A', 'T', 'C', 'G'}
sequence = dict.fromkeys(keys)
print(sequence)



product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
product.update(sample_original)
print(product)



product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
product.items()


# 'for' loop print all the keys in the dictionary
product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
for k in product:
    print(k)



# 'for' loop to print the values of the dictionary by using values() and other method
product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
for x in product.values():
    print(x)
print()
# 'for' loop to print the values of the dictionary by using values() and other method
for x in product:
    print(product[x])



# 'for' loop to print the items of the dictionary by using items() method
product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
for x in product.items():
    print(x)



product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
           'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
           'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
           'Aspergillus sojae_2': 'polygalacturonase'}
for x, y in product.items():
    print(x, y)



