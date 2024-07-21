----
<font size="+1">Перейти до [[INDEX|ЗМІСТУ]]</font>

----
<H1>Алфавіт. Класифікація символів</H1>

Зазвичай, всі мовні конструкції будуються як послідовності ***символів алфавіту***.

**С теоретичної точки зору**, символи, можуть бути елементами будь-якої скінченної множини, яка і зветься ***алфавітом***. Важливою властивістю цієї множини є те, що існує метод надійно розрізняти її елементи, які до того ж вважаються позбавленими будь-якої структури.

**З практичної точки зору**, символи представляються полями бітів у відповідності до кодових таблиць таких як [***ASCII*** (*American Standard Code for Information Interchange*)](https://uk.wikipedia.org/wiki/ASCII) або [***Unicode***](https://uk.wikipedia.org/wiki/%D0%AE%D0%BD%D1%96%D0%BA%D0%BE%D0%B4).

Нам знадобиться розрізняти такі підмножини символів:
- літери (***letters***);
- цифри (***digits***);
- пробільні символи (***whitespaces***);
- знаки (***signs***);
- інші символи (***others***).

Ця класифікація є умовною і змінюється від мови до мови.
Ми будемо вважати, що символи (***symbols***) і відповідні перелічені вище їх підмножини визначаються модулем ``alphabet``.

```python title:"Module alphabet" linenos:true
from typing import Set


__MINCODE = 32  # minimal and
__MAXCODE = 126 # maximal values of an admissible code


__LETTERS = ( # small and capital latin letters
	{chr(ic) for ic in range(ord('a'), ord('z') + 1)} |
	{chr(ic) for ic in range(ord('A'), ord('Z') + 1)})

__DIGITS = { # decimal digits
	chr(ic) for ic in range(ord('0'), ord('9') + 1)}

__SIGNS = set() # is defined by a user

__WHITESPACES = { # is extended by a user
	' ', '\n', '\t'}

__OTHERS = { # is extended by a user
	'(', ')', '.'}


def issymbol(x: str) -> bool:
	"""checks whether a string is a symbol of the alphabet
	Args:
		x (str): the string for checking
	Returns:
		True:  if 'x' is a symbol of the alphabet
		False: otherwise
	"""
	if not isinstance(x, str):
		return False
	return (x in __LETTERS or x in __DIGITS or
			x in __SIGNS or x in __WHITESPACES or
			x in __OTHERS) 


def letters() -> Set[str]:
	"""returns a copy of the set __LETTERS"""
	return {c for c in __LETTERS}

  
def digits() -> Set[str]:
	"""returns a copy of the set __DIGITS"""
	return {c for c in __DIGITS}

  
def signs() -> Set[str]:
	"""returns a copy of the set __SIGNS"""
	return {c for c in __SIGNS}


def whitespaces() -> Set[str]:
	"""returns a copy of the set __WHITESPACES"""
	return {c for c in __WHITESPACES}


def others() -> Set[str]:
	"""returns a copy of the set __OTHERS"""
	return {c for c in __OTHERS}


def addsign(x: str) -> None:
"""adds a new element to the set __SIGNS
	Args:
		x (str): string for adding
	Raises:
		ValueError: if 'x' is not permissible
		ValueError: if 'x' is already used
	"""
	if not (isinstance(x, str) and
			len(x) == 1 and
			__MINCODE <= ord(x) <= __MAXCODE):
		raise ValueError("bad symbol")
	if (x in __LETTERS or x in __DIGITS or
		x in __WHITESPACES or x in __OTHERS):
		raise ValueError(f"the symbol '{x}' is already used")
	__SIGNS.add(x)


def addother(x: str) -> None:
	"""adds a new element to the set __OTHERS
	Args:
		x (str): string for adding
	Raises:
		ValueError: if 'x' is not permissible
		ValueError: if 'x' is already used
	"""
	if not (isinstance(x, str) and
			len(x) == 1 and
			__MINCODE <= ord(x) <= __MAXCODE):
		raise ValueError("bad symbol")
	if (x in __LETTERS or x in __DIGITS or
		x in __SIGNS or x in __WHITESPACES):
		raise ValueError(f"the symbol '{x}' is already used")
	__OTHERS.add(x)
```

Роль класів літер і цифр є зрозумілою.
Пробільні символи змістовного навантаження не несуть і використовуються лише для позначення кінця фрагменту тексту.
Знаки використовуються для побудови інфіксних представлень бінарних операцій, які мають вигляд "`операнд1 оператор операнд2`". Саме оператори представляються послідовностями знаків, як, наприклад, `<=` чи `**`. 