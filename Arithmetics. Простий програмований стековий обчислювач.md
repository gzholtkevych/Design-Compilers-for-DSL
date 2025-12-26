# Arithmetics. Простий програмований стековий обчислювач

## Контекст нотатки

- [[Arithmetics]]
%%
- maybe other reference
%%
## Зміст нотатки

### Змістовний опис

Простий програмований стековий обчислювач (**SPSC**) має пам'ять, що організована як стек та вміє виконувати *інструкції* двох типів. Непророжня послідовність інструкцій утворює *програму* обчислювача.

#### Інструкції обчислювача

Інструкції першого типу відповідають зразку "$\mathtt{save}\ n$" де $n$ є цілим числом. Інструкція цього типу проштовшує операнд $n$ у стек.

Інструкції другого типу відповідають зразку "$\mathtt{eval\ op}$" де $\mathtt{op}$ є або '$+$', або '$-$', або '$*$', або '$/$', або '$\%$'. Інструкція цього типу
1. виштовхує спочатку $y$, а потім $x$ зі стеку;
2. обчислює $z$ у такий спосіб:
   - $z=x+y$, якщо $\mathtt{op}=$ '$+$',
   - $z=x-y$, якщо $\mathtt{op}=$ '$-$',
   - $z=x\cdot y$, якщо $\mathtt{op}=$ '$*$',
   - $z=\left\lceil\dfrac{x}{y}\right\rceil$, якщо $\mathtt{op}=$ '$/$',
   - $z=x\mod y$, якщо $\mathtt{op}=$ '$\%$';
3. проштовхує $z$ у стек.

#### Виконання програми

Перед виконанням програми пам'ять очищується - стек встановлюється у стан "порожній".
Програма виконується шляхом послідовного аиконання її інструкцій.
Програма завершує виконання штатно, якщо всі інструкції виконалися без помилок. У цьому випадку результат обчислення знаходиться на вершині стеку.

В процесі виконання програми можуть виникнути помилки виконання:
1. помилка "Недостатньо даних" - виникає, якщо необхідно виконати інструкцію типу "$\mathtt{eval\ op}$" проте стек містить менше ніж два числа;
2. помилка "Ділення на нуль" - виникає при діленні з нульовим дільником;
3. помилка "Обчислення залишку за модулем нуль" - виникає при обчислені залишку з нульовим модулем.

### Програмна модель обчислювача

Клас `SPSC` є програмною моделлю простого програмованого стекового обчислювача.
```python
class SPSC:

	def __init__(self):
		self._memory: list[int] = [] # створюємо та ініціалізуємо пам'ять
```

Методи `_save()` та `_eval()` цього класу моделюють виконання ігструкцій $\mathtt{save}$ та $\mathtt{eval}$ відповідно. 

```python	
	def _save(self, op: int) -> None:
		"""
		Моделювання інструкції 'save'.
		"""
		self._memory.append(op)
	
	def _eval(self, op: str) -> None:
		"""
		Моделювання інструкції 'eval'.
		"""
		try: # намагаємося отримати два числа з вершини стеку
			second = self._memory.pop(-1)
			first = self._memory.pop(-1)
		except IndexError: # спроба неуспішна
			raise ValueError("Для виконання не вистачає даних")
		# Безпечні операції
		if op == '+':
			self._memory.append(first + second)
		elif op == '-':
			self._memory.append(first - second)
		elif op == '*':
			self._memory.append(first * second)
		# Небезпечні операції
		elif op == '/':
			if second == 0:
				raise ValueError("Помилка: ділення на нуль")
			self._memory.append(first // second)
		elif op == '%':
			if second == 0:
				raise ValueError("Помилка: обчислення залишку за модулем нуль")
			self._memory.append(first % second)
		else: # операція нерозпізнано
			raise ValueError(f"Помилка: невідома операція: {op}")
```

Метод `run()` забезпечує виконання програми в цілому.

```python	
		def run(self, program: list[str]) -> int:
			self._memory = [:] # чистимо пам'ять
			if not isinstance(program, list):
			raise ValueError(
				"Програма має бути списком, а отримано {type(instr)}")
		if not list:
			raise ValueError("Програма має містити хоча б одну інструкцію")
		# Патерн для інструкції 'save'
		pattern_save = r"^\s*save\s+(0|[\+\-]?[1-9]\d*)\s*$"
		save = re.compile(pattern_save)
		# Патерн для інструкції 'eval'
		pattern_eval = r"^\s*eval\s+([\+\-\*/%])\s*$"
		eval = re.compile(pattern_eval)
		for instr in program: # цикл виконання програми
			if not isinstance(instr, str):
				raise ValueError(
					f"Інструкція має бути рядком, а отримано {type(instr)}")
			result = save.match(instr)
			if result is None: # інструкція 'save' не розпізнана
				result = eval.match(instr)
				if result is None: # інструкція 'eval' також не розпізнана
					raise ValueError(
						f"Неприпустимий формат інструкції: {instr}")
				else: # інструкція 'eval' розпізнана
					op = result.group(1)
					self._eval(op)
			else: # інструкція 'save' розпізнана
				op = int(result.group(1))
				self._save(op)
		return self._memory[-1] # результат беремо з вершини стеку
```