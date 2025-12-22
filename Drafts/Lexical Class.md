# Лексичний клас

%% Insert text %%
## Визначення

**Лексичний клас** є класифікатором для атомарних (елементарних) мовних конструкцій.

## Залежності

- Клас `Pattern` з бібліотеки `re`

## Визначення класу `LexClass`

```python
@dataclass(frozen=True)
class LexClass:
	name: str
	pattern: re.Pattern
```

## Приклад створення специфікації лексичних класів

```python
import re
from frozenlist import FrozenList

# Створюємо список лексичних класів з урахуваням їх пріорітетів
temp = [
	# Пробіли, найвищий пріоритет
    LexClass("SKIP", re.compile(r"[ \t\n]+")),
    # Ключові слова перед ідентифікаторами
	LexClass("KEYWORD_IF", re.compile(r"if\b")),
    LexClass("OP_EQ", re.compile(r"==")),
    LexClass("OP_ASSIGN", re.compile(r"=")),
    LexClass("INT_LITERAL", re.compile(r"\d+")),
    LexClass("ID", re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")),
    # ... інші правила
]
# Перевіряємо, що всі поля 'name' створюваних лексичних класів є різними
for ic, name1 in enumerate(temp):
	for name2 in temp[ic + 1:]:
		if name1 == name2:
			raise ValueError(f"lexical class name '{name1}' is duplicated")
# Оформлюємо специфікацію як незмінний список лексичних класів
LEXICAL_CLASS_SPECIFICATION = FrozenList(temp)
LEXICAL_CLASS_SPECIFICATION.freeze() 
```