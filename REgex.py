## .  matches any char except newline
## \d digits
## \D non digits
## \w word chars (numbers of alphabet)
## \W not a word char
## \s whitespaces
## \S non whitespaces

## \b word boundary (\bHa will match if Ha is in the begining of a word of the first in line)
## \B non word boundary
## ^  Beginning of a string
## $  End of a string

## [] matching set have the chars that we might choose from. [ab] means match a or b
## [1-5] matches only digits from 1 to 5
## [^1-5] matches everything that is not in the charchter set

## \d* match 0 or more numbers
## \d+ match 1 or more numbers
## \d? match 0 or one
## \d{3} match 3 digits
## \d{3,5} match digit range (3,4,5)

## () groups allow for matching several pattern
## M(r|s|rs) match Mr, Ms, Mrs

## r'(https?://)?(www.)?(\w+)\.(com|gov|net)'
## each group can be stripped out of the matches into a separate variable using match.group(<group_number>)

## r'(?:www.)?(\w+)' this is non capturing group that will not be counted in the group method

## Lookahead and Lookbehind
## apple(?=\spie) return the word 'apple' only if followed by pie
## apple(?!\spie) return the word 'apple' only if now followed by pie

## (?<=carrot\s)cake return the word 'cake' only if it is preceeded by carrot
## (?<!carrot\s)cake return the word 'cake' only if it is not preceeded by carrot
## the lookahead groups are not captured groups.

import re

text = '''
abcdefghijklmnopqrstuvwxyz
1234567890

Hello123! This is a test string.
Line2: A1b2C3@# Example line with numbers & symbols!
TestLine3: abcXYZ1234$% More text to check regex.
4thLine: Special characters like ^&*()_+{}|?[] and numbers 987654.
FinalLine: Mixed content with letters, numbers 2024, and symbols ~!@#$.

word boundary:
Ha HaHa

Telephone numbers:
01224048256
+20 122 404 8256
123-456-7891

03 1212272
02 1216676
04 6768943

IP Add
192.168.1.1
10.1.1.100
your ip add is : 179.1.1.67

URL:
www.greyskies.com
http://nasa.gov
https://www.youtube.com

Email:
tkamal@eventumsolutions.com
tarek.mohamed@gmail.com
t_kamal@greyskies-inc.net
Andrew198@eventum.edu

Mr. Tarek
Mrs Tarek
Ms Susan
Mr Ahmed
Mr T

apple pie
apple cake
carrot cake
browny cake
'''
sentence = 'Start End Start End'

#we use raw string r'' instead of strings so that python does not interpret 
#back slashes in any different way

#Compile method separates the regex into a variable to re-use it 

pattern = re.compile(r'abc')    #regex to search for 'abc'
special_pattern = re.compile(r'\.') #look for special chars by escaping

test_pattern = re.compile(r'End$')

match_phone = re.compile(r'\d{3}.\d{3}.\d{4}')
match_phone_landline = re.compile(r'0[^23]\s\d{7}') #landines in cairo or alex only

match_MR = re.compile(r'M(r|s|rs)?\.?\s[A-Z]\w*')

match_email = re.compile(r'^[a-zA-Z.0-9-]+@[a-zA-Z-]*\.(com|net|edu)')

match_url = re.compile(r'(https?:/+)?(www\.)?(\w+)(\.(gov|com|net))')

match_cake = re.compile(r'apple(?!\spie)') #lookahead
match_cake2 = re.compile(r'(?<!carrot\s)cake') #lookbehind

match_lines = re.compile(r'.*(?!com)')

matches = match_lines.finditer(text)    #finditer finds the index in the string of the matches


for i in matches:
    print(i)

matches_icase = re.compile(r'start', re.IGNORECASE)
match_first = match_email.search(sentence)  #only gets the first match
match_all = match_phone_landline.findall(text) #returns a list of strings