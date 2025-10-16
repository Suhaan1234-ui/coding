letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "24 September 2050"))
# this is called method chaining