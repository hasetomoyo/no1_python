year_str = input('あなたの生まれ年を西暦4桁で入力してください： ')
year = int(year_str)
numbrt_of_eto = (year + 8) % 12
eto_tuple = ('子',
             '牛',
)
eto_name = eto_tuple[number_of_eto]
print('あなたの絵とは{}です。 '.format(eto_name))
 
