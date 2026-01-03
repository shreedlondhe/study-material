
aList = [ 
            [11, 'Karan', 'Pune'], 
            [21, 'Devendra','Hyd'], 
            [101, 'Prachi','Pune']
        ]



aDictionary = { 
                'key': 'value',
                'marks' : 100,
                11 : ['Karan', 'Pune'], 
                21 : [21, 'Devendra','Hyd'], 
                101 : [101, 'Prachi','Pune'],
                True : "Some true value",
                True : "another true value",
                None : "value null"

            }

## ---------------------------------------

print(aDictionary)

##print(aDictionary[0])       #KeyError: 0  # we can not get element with index
print(aDictionary[11])       #['Karan', 'Pune']

print(aDictionary['key'])       # value
print(aDictionary['marks'])       # 100
print(aDictionary[True])       # 100
print(aDictionary[None])       # value null


#---------------------------------------------------

















