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


# print(aDictionary)
# print(aDictionary.items())          # to get all element in form of tuple enclosing list

###print(aDictionary[221])

# print(aDictionary.keys())

# # --------------------------------
# # - Update value of key 

# aDictionary["marks"] = 200
# aDictionary.update({'marks': 201})
# print(aDictionary["marks"])


# aDictionary["marks2"] = 200
# aDictionary.update({'marks2': 201, 'marks3': 300})
# print(aDictionary["marks2"])
# print(aDictionary["marks3"])


# ------------------------------------------------
print(aDictionary["marks"])     # 100
print(aDictionary.get("marks"))     #100

#print(aDictionary["marks2"])     # 100
print(aDictionary.get("marks2"))     #None   - if key not available 





