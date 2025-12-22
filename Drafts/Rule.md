# Продукційне правило

%% Insert text %%

```python
class Rules(dict):

	def __init__(self, prototype: Dict[Variable, Chain]):
		pass
	
```


```haskell
data Term = Atom Var
          | Abstraction Var Term
          | Application Term Term
```