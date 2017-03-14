import pandas as pd

s = pd.Series(list('abcdef'))
a = pd.DataFrame(list('abcdef'))

#reindex and fill nan with nulll
print(s.reindex(range(10),fill_value="nulll"))

print('**********************************************************')

d = {'US': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'IDN': pd.Series([1., 2.], index=['a', 'b'])}

df = pd.DataFrame(d)
print(df)

print('**********************************************************')

# add new coloum in df
df['three'] = df['US'] * 2

print(df)
