# Ланцюжок

## Пов'язано з

- %% reference %%
- %% maybe other reference %%%% Insert text %%

## Визначення




```python
class Chain(FrozenList):

	def __init__(self, prototype: Iterable = []):
		if not 'all member of prototypy is Token or Variable':
			raise TypeError("'prototype' is bad for constructing a chain")
		super().__init__([member for member in prototype])
		self.freeze()
		
	def append(self, member: Token | Variable) -> 'Chain':
		temp = [member for member in self]
		temp.append(member)
		return Chain(temp)
		
	def extend(self, addition: Chain) -> 'Chain':
		temp = [member for member in self]
		temp.extend(addition)
		return Chain(temp)
```