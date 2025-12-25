# Arithmetics. Метамодель мови простого програмованого стекового обчислювача

## Контекст нотатки

- [[Arithmetics]]
%%
- maybe other reference
%%
## Зміст нотатки

```textx
Program:
    instructions+=Instruction
; 

Instruction: Save | Eval;

Save:
    'save' operand=INT
;

Eval:
    'eval' operand=OpSign
;

OpSign: /[-+*\/%]/;
```

```mermaid
---
title: Метамодель програми простого програмованого стекового обчислювача
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
	class Program
	class Instruction {<<abstract>>}
	class Save {operand: INT}
	class Eval {operand: OpSign}
	
	Program "1" o-- "1..*" Instruction: instructions
	Instruction <|-- Save
	Instruction <|-- Eval
	note for Eval "OpSign обмежує значення operand тими рядками,<br/>що відповідають шаблону r'^[+-*\\/%]$'"
```
