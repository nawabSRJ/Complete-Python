# * As shown in the image for list comprehension, we can think of the syntax like 
# step 1 -> [] : simply create en empty list
# step 2 -> [par1 par2 part3] : consider the entire list comprehension syntax of 3 parts
# step 3 -> [part3] : start with part that that will be the original_list on which loop was to be applied in traditional code, so [original_list] 

# step 4 -> [for variable in original_list] : assign a variable in the loop of original_list
# step 5 -> [variable ** 2 for variable in original_list] : perform operation on the variable in the part1 area
# * So the ultimate syntax as shown in the image becomes : [operation for var in original_list]

# ? Now this list comprehension can also be applied on different types of data and not just numeric data :

tv_shows = ['silicon valley','BIG BANG THEORY','the office', 'modern FAMILY']
# todo : our task is to capitalize the first letter of each entry in tv_shows list or in other words ~ put the content in title case
# * Obv we can do it using loop, but here is the list comprehension implementation : 

tv_shows_cap = [var.title() for var in tv_shows]
print(tv_shows_cap)
print()
# =======================================================

# ? Conditionals in list comprehension

# * What if we also need to apply a certain condition also while looping, that if block comes after the loop (part4)
# [part1 part2 part3 condition]
# todo : Square the list of numbers in list nums but only those who are even
nums = [1,2,3,4,5]
even_squared = [n**2 for n in nums if n % 2 == 0]
print(even_squared) # [4,16]

# ! but what if we want to keep others as it is and only square the even ones 
# ? Simple, use else, but here there is a catch, if you have an else block as well then you need to put the condition after operation
# ? If there is no else condition then you need to make sure that it is part4

result = [n**2 if n % 2 == 0 else n for n in nums]
print(result)

print()
# =============================================================
# ? Generating Entire New List from Scratch

# ex : square of numbers from 1 to 10 without creating the original list
print('Square of 1 to 10 : ',[n**2 for n in range(1,11)])
# we use range() function for these sequential list operations ~ No need to create a separate list

# todo : Create a list where the numbers from 1 to 10 are squared but only added if they are even and there square is greater than 10
nums = [1,2,3,4,5,6,7,8,9,10]
result = []

# using loop
for n in nums:
    if n % 2 ==0:
        sq = n**2
        if sq > 10:
            result.append(sq)
    
print('Result using loop : ', result)

# using list comprehension
print([n**2 for n in nums if n%2==0 and n**2 > 10])

# ==============================================
# ! Trade offs
# * List comprehension provides performance benefits (see file list_comp_speed.png) but it decreases readability
# * We have to decide where to optimize what
# ? Tip : When dealing with large datasets or ranges then try using the list comprehension as it will be better to optimize for performance there instead of readability and maybe we can prefer more readability where the dataset is not too big.



