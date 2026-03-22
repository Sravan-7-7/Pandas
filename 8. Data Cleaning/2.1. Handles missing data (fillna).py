
'''IN PLACE OF DROPPING ANY ROWS WHERE THE VALUES ARE NOT AVALIABLE, LET'S REPLACE THEM INSTEAD WITH A DIFFERENT FUNCTION'''

df = df.fillna({'Type2' :'None' })

# fillna = FILL ANY NOT AVALIABLE VALUES

print(df.to_string())
print('----------------------------------------')
