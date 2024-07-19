----
<font size="+1">Перейти до [[INDEX|ЗМІСТУ]]</font>

----
<H1>Алфавіт. Класифікація символів</H1>

Зазвичай, всі мовні конструкції будуються як послідовності ***символів алфавіту***.

**С теоретичної точки зору**, символи, можуть бути елементами будь-якої скінченної множини, що зветься ***алфавітом***. Важливою властивістю цієї множини є те, що існує метод надійно розрізняти її елементи, які до того ж вважаються атомарними.

**З практичної точки зору**, символи представляються полями бітів у відповідності до кодових таблиць таких як [***ASCII*** (*American Standard Code for Information Interchange*)](https://uk.wikipedia.org/wiki/ASCII) або [***Unicode***](https://uk.wikipedia.org/wiki/%D0%AE%D0%BD%D1%96%D0%BA%D0%BE%D0%B4).

Нам знадобиться розрізняти такі підмножини символів:
- літери (***chars***);
- цифри (***digits***);
- пробільні символи (***whitespaces***);
- знаки (***signs***);
- інші символи (***other_symbols***).

Ця класифікація є умовною і змінюється від мови до мови.
Ми будемо вважати, що символи (***symbols***) і відповідні перелічені вище їх підмножини визначаються наступними предикатами
```python
def issymbol(x) -> bool:
	return isinstance(x, str) and len(x) == 1

def ischar(x) -> bool:
	return issymbol(x) and (ord('a') <= ord(x) <= ord('z') or
	                        ord('A') <= ord(x) <= ord('Z'))

def isdigit(x) -> bool:
	return issymbol(x) and (ord('0') <= ord(x) <= ord('9'))

def iswhitespace(x) -> bool:
	whitespaces = " \n\t"  # this item can be changed
	return issymbol(x) and x in whitespaces

def issign(x) -> bool:
	signs = "+-*/><="  # this item can be changed
	return issymbol(x) and x in signs

def isother(x) -> bool:
	return issymbol(x) and not (ischar(x) or
								isdigit(x) or
								iswhitespace(x) or
								issign(x))
```

Роль класів літер і цифр є зрозумілою.
Пробільні символи змістовного навантаження не несуть і використовуються лише для позначення кінця фрагменту тексту.
Знаки використовуються для побудови інфіксних представлень бінарних операцій, які мають вигляд "`операнд1 оператор операнд2`". Саме оператори представляються послідовностями знаків, як, наприклад, `<=` чи `**`. 