# import the module and refer to the function with the . syntax
import function_exercises

function_exercises.is_two(2)
function_exercises.is_vowel("f")
function_exercises.is_consonant("g")

# use from to import the function directly
from function_exercises import is_two, is_vowel, is_consonant

is_two(4)

is_vowel("a")

is_consonant("z")

# use from and give the function a different name

from function_exercises import is_two as num, is_vowel as vowel, is_consonant as cons

num(2)
vowel("a")
cons("a")

# itertools module

import itertools as it

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

len(list(it.product("abc","123", repeat=1)))

# How many different ways can you combine two of the letters from "abcd"?

len(list(it.product("abcd", repeat=2)))

import json as j
with open("profiles.json", "r") as prof:
    profiles = j.load(prof)
print(profiles)

print(profiles[0].keys())

#Total number of users

users = len(profiles)
print(users)

#Number of active users

active_users = [u['isActive'] for u in profiles if u['isActive'] == True]
len(active_users)

#Number of inactive users

active_users = [u['isActive'] for u in profiles if u['isActive'] == False]
len(active_users)

#Grand total of balances for all users

['balances']



Average balance per user
User with the lowest balance
User with the highest balance
Most common favorite fruit
Least most common favorite fruit
Total number of unread messages for all users


count = 0
for profile in profiles: 
        count += len(profile) 
print(count) 

isin