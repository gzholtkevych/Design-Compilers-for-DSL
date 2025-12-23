# Метамодель проєкту Arithmetics

## Контекст нотатки

- [[Проєкт Arithmetics]]
%%
- maybe other reference
%%
## Зміст нотатки

```python
// Головне правило: модель складається з одного виразу

// Вираз є послідовністю не менше ніж одного термів, між кожними двома сусдніми
// з яких стоїть або знак операції '+', або знак операції '-'.

Expression:
    expr_head=Term
    expr_tail*=ExpressionTail
;

ExpressionTail:
    op=MatcherPlusOrMinus
    term=Term
;

MatcherPlusOrMinus: /[+-]/;

// Терм є послідовністю не менше ніж одного термів, між кожними двома сусдніми
// з яких стоїть або знак операції '*', або знак операції '/',
// або знак операції '%'.

Term:
    term_head=Factor
    term_tail*=TermTail
;

TermTail:
    op=MatcherMultOrDivOrMod
    factor=Factor
;

MatcherMultOrDivOrMod: /[*\/%]/;

// Фактор є або цілою константою, або виразом в дужках.

Factor: Const | BracketedExpression;

Const: val=INT;

BracketedExpression: '(' expr=Expression ')';
```

```mermaid
---
  title: Arithmetic Expression Metamodel
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
	config showMethods false
	
	class Expression
	class Term
	class ExpressionTail { op: /[\\+\\-]/ }
	class Factor { <<abstract>> }
	
	class TermTail { op: /[\\*/%]/ }
	class Const { val: INT }
	class BracketedExpression
	Expression "1" --> "1" Term: expr_head
	Expression "1" o-- "*" ExpressionTail: expr_tail
	ExpressionTail "1" --> "1" Term: term
	Term "1" --> "1" Factor: term_head
	Term "1" o-- "*" TermTail: term_tail
	TermTail "1" --> "1" Factor: factor
	Factor <|-- Const
	Factor <|-- BracketedExpression
	BracketedExpression "1" --> "1" Expression: expr
```

