import re
# re is a built-in module in Python for working with regular expressions

html_content = '<p>Price : 19.99$</p>'
pattern = r'Price\s*:\s*(\d+\.\d{2})\$'

match = re.search(pattern, html_content)
if match:
    print(match.group(1))



html_content2 = '<p>Price : 123.45$</p>  <p>Price : 2.45$</p>'
match = re.findall(pattern, html_content2)
if match:
    print(match)
else:
    print("No matches found")