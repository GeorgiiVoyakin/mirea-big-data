# mirea-big-data
Python Big Data programming tasks for institute

## Task 1
* Написать программу, которая вычисляет площадь фигуры, параметры которой подаются на вход. Фигуры, которые подаются на вход: треугольник, прямоугольник, круг. Результатом работы является словарь, где ключ – это название фигуры, а значение – это площадь.
* Написать программу, которая на вход получает: 1) два числа; 2) операцию, которую к ним нужно применить. Должны быть реализованы следующие операции: +, -, /, //, **. Результатом работы программы является одно число.
* Написать программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона. На вход программе подаются целые числа, выводом программы должно являться вещественное число, соответствующее площади треугольника.

## Task 2
* Написать программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и после этого выводит сумму квадратов всех считанных чисел.
* Написать программу, которая выводит последовательность чисел, длинною N, где каждое число повторяется столько раз, чему оно равно. На вход программе передаётся неотрицательное целое число N. Например, если N = 7, то программа должна вывести 1 2 2 3 3 3 4.
* Матрицу произвольного размера вытянуть в один вектор, не применяя встроенные методы Python.
* Даны два списка:
```python3
А = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
В = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
```
Создать словарь, в котором ключи – это содержимое списка В, а значения для ключей словаря – это сумма всех элементов списка А в соответствии с буквой, содержащийся на той же позиции в списке В. Пример результата программы: 
```python3
{'a' : 10, 'b' : 15, 'c' : 6}
```
* Скачать и загрузить данные о стоимости домов в калифорнии, используя библиотеку sklearn.
* Используя метод pd.concat([датафрейм1, датафрейм2], axis = 1), добавить к данным столбец, содержащий информацию о медианной стоимости дома.
* Использовать метод info().
* Узнать, есть ли пропущенные значения, используя isna().sum().
* Вывести записи, где средний возраст домов в районе более 50 лет и население более 2500 человек, используя метод loc().
* Узнать максимальное и минимальное значения медианной стоимости дома (max(), min()).
* Используя метод apply(), вывести на экран название признака и его среднее значение.

## Task 3
* Найти и выгрузить многомерные данные с использованием библиотеки pandas. (Данные взяты отсюда: https://www.kaggle.com/datasets/kevinmorgado/us-energy-generation-2001-2022)
* Вывести информацию о данных при помощи методов ```.info()```, ```.head()```. Проверить данные на наличие пустых значений. В случае их наличия удалить данные строки или интерполировать пропущенные значения. При необходимости дополнительно предобработать данные для дальнейшей работы с ними.
* Построить столбчатую диаграмму (.bar) с использованием библиотеки Plotly со следующими параметрами:
  * По оси Х указать дату или название, по оси У указать количественный показатель.
  * Сделать так, чтобы столбец принимал цвет в зависимости от количественного показателя.
  * Отобразить заголовок диаграммы, разместив его по центру, с 20 размером текста.
  * Добавить подписи для осей X и Y с размером текста, равным 16. Для оси абсцисс развернуть метки так, чтобы они читались снизу вверх. Для оси ординат шаг меток участить в 1.5 раза.
  * Размер текста меток осей сделать равным 14.
  * Обрезать график снизу по минимальному значению количественного показателя, вычтя из него 10%.
* Построить круговую диаграмму, использовав данные и оформление из предыдущего графика.
* Построить линейный график с накопленными значениями количественного показателя от даты (названия).
  * Сделать график с линиями и маркерами, цвет линии 'crimson', цвет точек 'darkblue', цвет границ точек 'black'.
  * Добавить легенду на график в нижнем левом углу.
  * Добавить сетку на график, сделать цвет 'azure'.
  * Остальное оформление сохранить с предыдущих графиков.
* Построить ящик с усами, сохранив оформление с предыдущих графиков.
* Постараться создать аналогичные графики с использованием библиотеки matplotlib.

## Task 6
* Загрузить данные из файла ECDCCases.csv.
* Проверить в данных наличие пропущенных значений. Вывести количество пропущенных значений в процентах. Удалить два признака, в которых больше всех пропущенных значений. Для оставшихся признаков обработать пропуски: для категориального признака использовать заполнение значением по умолчанию (например, 'other'), для числового признака использовать заполнение медианным значением. Показать, что пропусков больше в данных нет.
* Посмотреть статистику по данным, используя describe(). Сделать выводы о том, какие признаки содержат выбросы. Посмотреть, для каких стран количество смертей в день превысило 3000 и сколько таких дней было.
* Найти дублирование данных. Удалить дубликаты.
* Загрузить данные из файла "bmi.csv". Взять оттуда две выборки. Одна выборка – это индекс массы тела людей c региона northwest, вторая выборка – это индекс массы тела людей с региона southwest. Сравнить средние значения этих выборок, используя t-критерий Стьюдента. Предварительно проверить выборки на нормальность (критерий Шопиро-Уилка) и на гомогенность дисперсии (критерий Бартлетта).
* Кубик бросили 600 раз, получили следующие результаты:

| N | Количество выпадений  |
|---|---|
| 1 | 97  |
| 2 | 98  |
| 3 | 109 |
| 4 | 95  |
| 5 | 97  |
| 6 | 104 |

С помощью критерия Хи-квадрат проверить, является ли полученное распределение равномерным.
* С помощью критерия Хи-квадрат проверить, являются ли переменные зависимыми. Создать датафрейм, используя следующий код:
```python3
data = pd.DataFrame({'Женат': [89,17,11,43,22,1],
                     'Гражданский брак': [80,22,20,35,6,4],
                     'Не состоит в отношениях': [35,44,35,6,8,22]})
data.index = ['Полный рабочий день',
              'Частичная занятость',
              'Временно не работает',
              'На домохозяйстве',
              'На пенсии',
              'Учёба']
```
