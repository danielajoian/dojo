#dictionary or maps; 
#they have key:value pairs; for every value there is a key
# we can't join 2 dictionary with + like in lists 

animal_names ={'cat' : 'Luna',
               'dog' : 'Azorel',
               'lion' : 'Simba',
               'fish' : 'Nemo',
               'bird' : 'Polly'}

print(animal_names)

print(animal_names['cat'])

del animal_names['bird']
print(animal_names)

animal_names['bird'] = 'Polly2'
print(animal_names)

print(len(animal_names))

print(animal_names.get('fish'))
print(animal_names.keys())
print(animal_names.values())