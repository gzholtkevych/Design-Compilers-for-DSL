# 000 Розбір за допомогою лівого рекурсивного спуску

%% Insert text %%
## Структури даних

1. [[Token|Токен]]
2. [[Variable|Металінгвістична змінна]]
3. [[Chain|Ланцюжок]]
4. [[Rule|Продукційне правило]]

> вершина, що помічена $X$ та буфер $u$
> > якщо $X\in\Sigma$ та $X=u[0]$
> > > повернути $(\mathtt{succ},Leaf(u[0]),u[1:])$
> > якщо $X\in\Sigma$ та $X\neq u[0]$
> > > повернути $(\mathtt{fail},u)$
> > якщо $X\in\Mu$
> > > *обрати підстановку* $X\to\alpha$
> > > створити $\mathtt{children}\gets[Y\mathtt{\ for\ }Y\mathtt{\ in\ }\alpha]$
> > > для кожного $Y\ \mathtt{in\ children}$
> > > > виконати для вершини, що помічена $Y$ та буферу $u$
> > > > якщо повернуто $(\mathtt{fail},u)$
> > > > > спробувати перейти до наступного $Y$
> > > > > якщо спроба невдала
> > > > > > повернути $(\mathtt{fail},u)$


```python
Chain = List[Token | Variable]
Rules = Dict[Variable, List[Chain]]
Grammar = Dict[Variable, List[Token  Variable]]
Tree = Dict[Variable, List[Tree]]
```

```python
class Tree(ABC)
```

```python
def parse(u: Chain, g: Grammar) -> 'SyntacticTree':
	def handle(A: Variable):
		nonlocal g, buffer, scanner
		alter: None | Chain = select(A, g)
		if alter is None:
			return None
		for smb in alter:
			if smb is Token:
				if smb != buffer[scanner]:
					return None
	# end of handle()
	buffer: Chain, scanner = u, 0
	node = STNode(label=g.header, children=[])
	root = handle(node)
```


```python
@dataclass
class STNode:
	label: Token | Variable
	children: List[STNode]
```

```python
def handle(label: Token | Variable) -> 'Tree':
	nonlocal buffer: List[Token]
	node = STNode(label, children=[])
	if node.label is Token:
		if node.label == buffer[0]:
			return node
		raise ValueError(f"parsing error at {buffer}")
	# node.label is Variable
	node.children = select(label)
	for child in node.children:
		handle(child.label, buffer)
```