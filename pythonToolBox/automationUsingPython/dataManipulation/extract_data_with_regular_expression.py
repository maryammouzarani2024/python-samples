# an example of working with RE to extract phone numbers from the text

import re

phone_number_re=re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example_text="Hi. My phone number is 123-456-7890."

result=phone_number_re.search(example_text)

if result:
    print("phone number: ", result.group())
    print("Local code: ", result.group()[0:3])