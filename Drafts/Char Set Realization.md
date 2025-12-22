# Реалізація таблиці символів

%% Insert text %%

## Пов'язано з

- [[00 Technology|Технологія]]
%% - maybe other reference %%

## Реалізує

- [[Alphabet|Алфавіт]]

---

Ми будемо вважати, що символи (***chars***) і відповідні їх підмножин —

- літер (***letters***),
- цифр (***digits***),
- пробільних символів (***whitespaces***),
- знаків (***signs***),
- інших символів (***others***)

— визначаються класом ``Char``, приклад реалізації якого наведено нижче.

```python title:"Class Alphabet" linenos:true
from typing import Set
from functools import reduce


class Char:

	__MINCODE = 32  # minimal and
	__MAXCODE = 126 # maximal values of an admissible code

	__LETTERS = ("".join( # small latin letters
		[chr(ic) for ic in range(ord('a'), ord('z') + 1)]) +
		"".join( # capital latin letters
		[chr(ic) for ic in range(ord('A'), ord('Z') + 1)]) +
		# underscore symbol
		"_"
	)

	__DIGITS = "".join( # decimal digits
		[chr(ic) for ic in range(ord('0'), ord('9') + 1)])

	__SIGNS = "" # is defined by a user

	__WHITESPACES = "".join( # is extended by a user
		[' ', '\n'])

	__OTHERS = "" # is defined by a user

	def issymbol(x: str) -> bool:
		"""checks whether a char is a symbol
		Args:
			x (str of length 1): the string for checking
	Returns:
		True:  if x is a symbol of the alphabet
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


def wsstr() -> str:
	"""returns the string containing all whitespaces
	Returns:
		str: string of whitespaces
	"""
	return reduce(lambda x, y: f"{x}{y}", __WHITESPACES)
```

Роль класів літер і цифр є зрозумілою.
Пробільні символи змістовного навантаження не несуть і використовуються лише для позначення кінця фрагменту тексту.
Знаки використовуються для побудови інфіксних представлень бінарних операцій, які мають вигляд "`операнд1 оператор операнд2`". Саме оператори представляються послідовностями знаків, як, наприклад, `<=` чи `**`. 
Іншими символами можуть бути такі, як, наприклад, десяткова крапка.