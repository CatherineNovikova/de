#  Dataset Steam 2012-2021 from kaggle
## Найдем топ-5 игр по среднему количеству игроков в месяц, за все доступные годы

import pandas as pd
import os

input_file = 'Valve_Player_Data.csv'
output_file = 'top_games_2012_2021.csv'

folder = (r'C:\Users\Public')
input_file_path = os.path.join(folder, input_file)
output_file_path = os.path.join(folder, output_file)

#  Прочитаем файл
df = pd.read_csv(input_file_path)

#  Посмотрим на данные
print (df.columns)
print(f'\nКоличество строк: {len(df)}')

#  Проверим типы данных
print (df.dtypes)

#  Проверим, нет ли дубликатов
has_dupl = df.duplicated(keep='first')
print(f'\nНайдено дубликатов: {sum(has_dupl)}')

#  Возьмем нужные колонки
df=df[['Month_Year', 'Date', 'Game_Name', 'Avg_players', 'Peak_Players']]

#  Проверим null
cnt_null = df.isnull().sum()
print(f'\nПропущенных значений: {cnt_null}\n')

#  Преобразуем в дату, создадим столбец с годом
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

#  Сгруппируем по году и названию игр
group = df.groupby(['Year', 'Game_Name'])['Avg_players'].mean().reset_index()

#  Округлим значение Avg_players до двух знаков после запятой
group['Avg_players'] = group['Avg_players'].round(2)  

#  Отсортируем по году и среднему онлайну
sort = group.sort_values(['Year','Avg_players'], ascending=[True, False])

top_per_year = sort

print(top_per_year)
print(f'Результат сохранен в {output_file}')
top_per_year.to_csv(output_file_path, index=False)