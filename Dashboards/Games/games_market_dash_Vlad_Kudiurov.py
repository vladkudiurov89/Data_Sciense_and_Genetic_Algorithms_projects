"""
Задача 3. Постройте дашборд в dash
Дана таблица истории состояния игровой индустрии games.csv. Описание полей:
●  	Name - название проекта;
●  	Platform - платформа;
●  	Year_of_Release - год выпуска;
●  	Genre - жанр игры;
●  	Critic_Score - оценка критиков;
●  	User_Score - оценка игроков;
●  	Rating - возрастной рейтинг.
"""
# Библиотека для создания дашборда
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
# Библиотека визуализации данных
import plotly.express as px
import plotly.graph_objects as go
# Библиотека загрузки и очистки данных
import pandas as pd

# Настройка для вывода значений
pd.options.display.float_format = '{:.0f}'.format
pd.set_option('max_columns', 20)

# Загрузка и очистска данных
df = pd.read_csv('games.csv')
df = df.dropna()
# df = df.loc[df.User_Score != 'tbd']
df = df.loc[df['Year_of_Release'] > 2000]
Years = pd.unique(df['Year_of_Release']).tolist()
# print(df)
# Установка стиля дашборда

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Table(style={"width": "80%"}, className="responsive-table", children=[
    # Заголовок
    html.Tr(children=[
        html.H3(
            children='Индустрия игр с 2000 года', style={'align': "center"}
        )]),

    # Инструкция
    html.Tr(children=[
        html.H4(children='Дашборд предназначен для демонстрации тенденции игровой индустрии. '
                         'Представлено два графика: '
                         'Первый описывает динамику релизов игр. '
                         'Второй - качество игровых продуктов', style={'textalign': "center"})]),

    # Установка фильтров
    html.Tr(children=[
        # Фильтр 1: Фильтр жанров (множественный выбор)
        html.Th(children=[
            html.Label('Фильтр 1: Фильтр жанров (множественный выбор)'),
            dcc.Dropdown(id='genre_filter', clearable=False, options=[
                {'label': 'Спортивные', 'value': 'Sports'},
                {'label': 'Гонки', 'value': 'Racing'},
                {'label': 'Платформа', 'value': 'Platform'},
                {'label': 'Развлечения', 'value': 'Misc'},
                {'label': 'Экшн-Игры', 'value': 'Action'},
                {'label': 'Пазл', 'value': 'Puzzle'},
                {'label': 'Стрелялки', 'value': 'Shooter'},
                {'label': 'Борьба', 'value': 'Fightling'},
                {'label': 'Симуляция', 'value': 'Simulation'},
                {'label': 'Ролевые Игры', 'value': 'Role-Playing'},
                {'label': 'Приключения', 'value': 'Adventure'}],
                         value=['Sports', 'Racing', 'Platform', 'Action', 'Puzzle', 'Simulation', ], multi=True)]),

        # Фильтр 2: Фильтр рейтингов (множественный выбор)
        html.Th(children=[html.Label('Фильтр 2: Фильтр рейтингов'),
                          dcc.Dropdown(id='rating_filter', clearable=False, options=[
                              {'label': 'E', 'value': 'E'},
                              {'label': 'M', 'value': 'M'},
                              {'label': 'T', 'value': 'T'},
                              {'label': 'E10+', 'value': 'E10+'},
                              {'label': 'AO', 'value': 'AO'},
                              {'label': 'RP', 'value': 'RP'}], value=['RP', 'E10+', 'T'], multi=True)])],),

    html.Tr(children=[html.Th(dcc.Markdown(id='quantity')), html.Th()]),
    html.Tr(children=[
        html.Th(dcc.Graph(id='graph_0', style={'display': 'inline-block', 'width': '60vh', 'height': '45vh',
                                               'align': "center"})),
        html.Th(dcc.Graph(id='graph_1', style={'width': '60vh', 'height': '45vh', 'align': 'center'}))]),

    html.Tr(children=[
        # 'Фильтр 3: Интервал выпуска года
        html.Th(children=[html.Label('Фильтр 3: Интервал выпуска года'),
                          dcc.RangeSlider(id='years_filter', marks={i: '{}'.format(i) for i in range(int(min(Years)),
                                                                                                     int(max(Years) + 1)
                                                                                                     )},

                                          max=int(max(Years)), min=int(min(Years)),
                                          value=[int(min(Years)) + 1, int(min(Years)) + 14])]),
        html.Th(id='output-container-range-slider')])])


# Декоратор - обработчик фильтров
@app.callback(Output('graph_0', 'figure'),
              Output('graph_1', 'figure'),
              Output('quantity', 'children'),
              Input('genre_filter', 'value'),
              Input('rating_filter', 'value'),
              Input('years_filter', 'value'))
def update_output(genre_filter, rating_filter, years_filter):
    print(genre_filter, rating_filter, years_filter)
    # Цикл для обработки годового фильтра
    num = years_filter[0]
    result_1 = df[df.Year_of_Release == num]
    num += 1
    while num <= years_filter[1]:
        result_1 = pd.concat([df[df.Year_of_Release == num], result_1])
        num += 1

    # Работаем с фильтром рейтингов
    if rating_filter:
        result_2 = result_1[result_1.Rating == rating_filter[0]]
        for elem in range(1, len(rating_filter)):
            result_2 = pd.concat([result_1[result_1.Rating == rating_filter[elem]], result_2])
    else:
        result_2 = result_1
        rating_filter = pd.unique(df['Rating']).tolist()

    # Работаем с фильтром жанров
    if genre_filter:
        result_3 = result_2[result_2.Genre == genre_filter[0]]
        for elem in range(1, len(genre_filter)):
            result_3 = pd.concat([result_2[result_2.Genre == genre_filter[elem]], result_3])
    else:
        result_3 = result_2
        genre_filter = pd.unique(df['Genre']).tolist()

    """
    Функция Stacked area plot, 
    показывающего выпуск игр по годам и платформам
    """
    platforms = pd.unique(result_3['Platform']).tolist()
    stacked_area_plot = go.Figure(layout=go.Layout(
        title=go.layout.Title(text="Stacked area plot - выпуск игр по годам и платформам")))
    for platform in platforms:
        res_years = []
        amount_games = []
        for year in Years:
            if years_filter[0] <= year <= years_filter[1]:
                res_years.append(year)
                amount_games.append(df[(df.Platform == platform) & (df.Year_of_Release == year) &
                                       (df.Genre.isin(genre_filter)) & (df.Rating.isin(rating_filter))].index.shape[0])
        stacked_area_plot.add_trace(go.Scatter(name=platform, x=res_years, y=amount_games, stackgroup='one'))
    quantity_games = result_3.shape[0]
    return stacked_area_plot, px.scatter(result_3, x="User_Score", y="Critic_Score", color="Genre", hover_name="Name",
                                         log_x=True, title='Scatter plot с разбивкой по жанрам'), \
                                        ("Количество игр: " + str(quantity_games))


if __name__ == "__main__":
    app.run_server(debug=True, host='127.0.0.1')
