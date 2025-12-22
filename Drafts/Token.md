# Токен

%% Insert text %%

## Залежності

- [[Lexical Class|Клас `LexClass`]]

```python
@dataclass(frozen=True)
class Token:
	lexcls: LexClass
	value: str
```