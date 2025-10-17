letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "24 September 2050"))#THIS IA A NEW STRING NOT THE
                                                                                   # ORIGINAL ONE
# this is called method chaining
print(letter)  # original letter remains unchanged ie strings are immutable