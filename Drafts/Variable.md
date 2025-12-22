# Металінгвістична змінна

%% Insert text %%

## Визначення

Змінна використовується для посилання на певну мовну конструкцію.

## Визначення класу `Variable`

```python
@dataclass(frozen=True)
class Variable:
	name: str
```

## Приклад створення специфікації змінних

```python
from Frozenlist import FrozenList

# Створюємо список змінних
temp = [
	# першою йде стартова змінна
	Variable(name='E'),
	Variable(name='C'),
	Variable(name='T')
]
# Перевіряємо що змінні у списку не повторюються
for ic, name1 in enumerate(temp):
	for name2 in temp[ic + 1:]:
		if name1 == name2:
			raise ValueError(f"variable name '{name1}' is duplicated")
# Оформлюємо специфікацію як незмінний список змінних
VARIABLE_SPECIFICATION = FrozenList(temp)
VARIABLE_SPECIFICATION.freeze()
```