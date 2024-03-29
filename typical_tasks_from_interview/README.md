## Typical tasks from interview
<details>
<summary>A. Значения функции</summary>

[Решение](A.py)

### Ограничение времени
0.2 секунды
### Ограничение памяти
64Mb

Младший брат Аллы Вася делает тест по математике: вычисляет значение функций в различных 
точках. Стоит отличная погода, и друзья зовут Васю гулять. Но мама разрешила мальчику 
пойти на улицу только после того, как он закончит тест. К сожалению, Вася пока не умеет 
программировать. Зато Алла умеет. Она решила помочь брату и написала код функции 
y = ax2 + bx + c. Повторите успех Аллы. Напишите программу, которая будет по коэффициентам 
a, b, c и числу x выводить значение функции в точке x.

### Формат ввода

На вход через пробел подаются числа a, x, b, c.

### Формат вывода

Выведите одно число - значение функции в точке x.
</details>

<details>
<summary>B. Любители конференций</summary>

[Решение](B.py)

### Ограничение времени
0.08 секунд
### Ограничение памяти
39Mb

На IT-конференции присутствовали студенты из разных вузов со всей страны. Для каждого 
студента известен ID университета, в котором он учится.
Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше всего учащихся.


### Формат ввода

В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).
Во второй строке через пробел записаны n целых чисел —– ID вуза каждого студента. 
Каждое из чисел находится в диапазоне от 0 до 10 000.
В третьей строке записано одно число k.

### Формат вывода

Выведите через пробел k ID вузов с максимальным числом участников. Они должны быть 
отсортированы по убыванию популярности (по количеству гостей от конкретного вуза). 
Если более одного вуза имеет одно и то же количество учащихся, то выводить их ID нужно 
в порядке возрастания. 

</details>

<details>
<summary>C. Списочная форма</summary>

[Решение](C.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма –— это массив его цифр слева направо. 
К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход подается количество цифр числа Х, 
списочная форма неотрицательного числа Х и неотрицательное число K. Числа К и Х не превосходят 10000.

Нужно вернуть списочную форму числа X + K.

### Формат ввода

В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма 
с цифрами записанными через пробел.
В последней строке записано число K.

### Формат вывода

Выведите списочную форму числа X+K. 

</details>


<details>
<summary>D. Убрать очки</summary>

[Решение](D.py)

### Ограничение времени
0.08 секунд
### Ограничение памяти
64Mb

Гоша решил убрать из статистики дни, когда ничего в «Черепашеньке» не заработал и 
не проиграл. Дан список заработанных очков. Нужно удалить из него нули. Дополнительную 
память больше O(1) использовать нельзя. 

### Формат ввода

В первой строке - одно число n. Во второй - n целых чисел через пробел.

### Формат вывода

Напечатайте очки за все дни, где выигрыш был отличен от нуля.

</details>

<details>
<summary>E. Работа из дома</summary>

[Решение](E.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Алла осталась работать из дома. Во время её рабочего видеозвонка с Тимофеем и Гошей 
подошёл Вася. Он решил показать им написанный им недавно код функции, переводящей целое 
число из десятичной системы в двоичную. Ему было интересно, смогут ли ребята написать 
более короткую, или более эффективную программу. Тимофей, Алла и Гоша с радостью отвлеклись 
от работы, чтобы попробовать. А у вас получится обойти Васю?

**Не используйте встроенные средства языка по переводу чисел в бинарное представление.**


### Формат ввода

На вход подается целое число в диапазоне от 0 до 10000.

### Формат вывода

Выведите двоичное представление этого числа.

</details>

<details>
<summary>F. База данных</summary>

[Решение](F.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Алла писала код, добавляющий запись в новую таблицу базы данных. И вдруг получила 
ошибку duplicate foreign key constraint. В тот же момент её отвлекла Рита. Алла 
случайно закрыла окно терминала с информацией о том, какое именно значение стало 
причиной ошибки. Зато у неё сохранился список id, использованных при запросе. Помогите 
ей выяснить, какой id стал причиной ошибки.

Дан массив чисел, состоящий  из n целых чисел. Одно число встречается более одного раза. 
Нужно определить это число.

### Формат ввода

В первой строке записано число n, которое не превосходит 1000. В следующей строке 
через пробел записаны n целых чисел, каждое из которых также не превосходит 10000. 

### Формат вывода

Выведите одно число.

</details>

<details>
<summary>G. Анаграммы</summary>

[Решение](G.py)

### Ограничение времени
0.055 секунд
### Ограничение памяти
64Mb

Вася вернулся домой под вечер и вспомнил, что ещё не сделал домашнее задание по 
русскому языку. Чтобы понять разницу между анаграммой и палиндромом, Вася снова 
обратился к Алле. Она объяснила брату, что два слова — анаграммы, если одно можно 
получить из другого перестановкой букв. А палиндром — это слово или фраза, которая 
читается одинаково, если читать слева направо и справа налево. Теперь Васе интересно: 
как закодить функцию, определяющую, анаграммы слова или нет. Помогите ему. 

### Формат ввода

Два слова - каждое на отдельной строке.
Слова состоят из строчных букв латинского и русского алфавитов. 

### Формат вывода

Слово True, если слова являются анаграммами друг друга, слово False - если не являются.

</details>

<details>
<summary>H. Палиндром</summary>

[Решение](H.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

А теперь помогите Васе понять, будет ли фраза палиндромом. Учитываются только 
буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N - длина строки на входе.

### Формат ввода

В единственной строке записана фраза или слово. Буквы могут быть только латинские.

### Формат вывода

Выведите True, если фраза является палиндромом и False, если не является. 

</details>

<details>
<summary>I. Двоичная система</summary>

[Решение](I.py)

### Ограничение времени
0.07 секунд
### Ограничение памяти
39Mb

Тимофей спросил у студента Саши, умеет ли тот работать с числами в двоичной системе 
счисления. Он ответил, что проходил это на одной из первых лекций по информатике. 
Тимофей предложил Саше решить задачку. Два числа записаны в двоичной системе счисления. 
Нужно вывести их сумму, также в двоичной системе. Встроенную в язык программирования 
возможность сложения двоичных чисел применять нельзя.

Решение должно работать за O(N), где N - количество разрядов максимального числа на входе.

### Формат ввода

Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого 
числа не превосходит 10000 цифр.

### Формат вывода

Одно число в двоичной системе счисления.

</details>

<details>
<summary>J. Обеды</summary>

[Решение](J.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Руководство компании, где работают Гоша с друзьями, подарило каждому сотруднику 
два талона на обед в близлежащем ресторане. Сотрудники могли взять талоны и записать 
номер своего бейджика на каждом из них. Талон с записанным на нём номером обменивается 
на обед в ресторане. Все сотрудники, кроме одного, сходили в ресторан по талонам дважды. 
Отличившийся сотрудник сходил в ресторан только один раз. Нужно вычислить, кто же это такой. 
По списку номеров на сданных в ресторан талонах найдите номер отличившегося сотрудника.

**Примечание: Эту задачу можно решить за O(n) времени и O(1) дополнительной памяти — 
подумайте, как это сделать!**


### Формат ввода

На вход подаётся число номеров в списке — n (3 ≤ n ≤ 104), и n натуральных чисел, 
не превышающих M=104, — сам список номеров сотрудников. Все числа, кроме одного, 
встречаются в списке дважды. 

### Формат вывода

Выведите номер сотрудника, который сходил на обед всего один раз.

</details>

<details>
<summary>K. Единицы</summary>

[Решение](K.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Пока Вася писал программу про степени четверки, погода на улице ухудшилась. Он долго 
не расстраивался и придумал новую задачку! Ему нравится работать с системами счисления. 
И вот что на этот раз получилось: Дано целое положительное число. Нужно посчитать, сколько 
1 встречается в двоичной записи этого числа. 

### Формат ввода

На вход подается число в диапазоне от 1 до 10000

### Формат вывода

Выведите одно число - количество единиц.

</details>

<details>
<summary>L. Лишняя буква</summary>

[Решение](L.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки s и t, 
состоящие только из строчных букв. Строка t получена перемешиванием букв строки s и 
добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву. 

### Формат ввода

На вход подаются строки s и t, разделенные переносом строки. Длины строк не превосходят 
1000 символов. Строки не бывают пустыми.

### Формат вывода

Выведите лишнюю букву.

</details>

<details>
<summary>M. Частоты</summary>

[Решение](M.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

А теперь помогите Васе решить задачу по информатике. Он снова томится дома в хорошую погоду.
На вход подается строка длиной от 1 до 10000 символов. Нужно отсортировать её в порядке 
частот букв по встречаемости. Заглавные и строчные буквы считаются разными. Если частота 
одинаковая, нужно применить вторичную сортировку лексикографически.

### Формат ввода

Одна строка длиной не более 10000 символов.

### Формат вывода

Строка, в которой символы отсортированы в порядке убывания частотности.

</details>

<details>
<summary>N. Степень четырех</summary>

[Решение](N.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Вася на уроке математики проходил степени. Он хочет написать программу, которая 
определяет, будет ли положительное целое число степенью четверки. 

### Формат ввода

На вход подается целое число в диапазоне от 1 до 10000.

### Формат вывода

True, если число является степенью четырех, False - в обратном случае.

</details>

<details>
<summary>O. И снова Вася</summary>

[Решение](O.py)

### Ограничение времени
1 секунда
### Ограничение памяти
64Mb

Вы думали, что эта задача про Васю, но она про Тимофея.
Тимофей собирает метрики посещаемости сайта за последний месяц с двух серверов. 
На каждой машине имеется список id пользователей, отсортированный в порядке от 
минимального количества посещений к максимальному, вам известно число посещений 
каждого пользователя. Пользователи, не посещавшие сайт в последний месяц, не учитываются. 
Вам нужно сделать общий список числа посещений для двух серверов так, чтобы в нем тоже числа 
шли по возрастанию. Так как сайт Тимофея очень популярен, то данных о пользователях много, 
поэтому Тимофей может позволить себе только линейное время работы алгоритма. 

### Формат ввода

В первой строке записаны количества посещений пользователей с первого сервера через 
пробел, в конце - k нулей. Во второй строке записано число m - количество пользователей, 
пришедших с первого сервера (без учета нулей в конце списка). В третьей - число k - которое, 
помимо количества нулей, также является длиной списка пользователей со второго сервера. 
В последней строке - список посещений со второго сервера (k штук).

Количество посещений каждого пользователя не превосходит 10000, числа m и k также не 
превосходят 10000

### Формат вывода

В одной строке через пробел выведите элементы получившегося списка в отсортированном порядке.

</details>