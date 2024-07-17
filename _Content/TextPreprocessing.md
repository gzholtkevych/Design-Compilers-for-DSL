----
<font size="+1">Перейти до [[INDEX|ЗМІСТУ]]</font>

----
<H1>Первинна обробка тексту</H1>

Первинна обробка тексту забезпечує перетворення тексту `text: str`, на об'єкт типу `preprocessed_text: list[str]`, який задовольняє наступним умовам:
1. кожний елемент вихідного списку не містить жодного пробільного символу;
2. якщо об'єднати елементи вихідного списку в текстовий рядок у такий спосіб `"".join(preprocessed_text)`, то буде отриманий рядок, що співпадає з первинним текстом, з якого видалили пробільні символи;
3. якщо елемент вихідного списку містить знак, то всі символи цього елементу є знаками.

```plantuml

@startuml
(*) -right-> "preprocessed_text = []" as init

init -right-> "text_piece = []" as outer_loop

outer_loop --> "try c = get_char(text)" as inner_loop

inner_loop --> if "" then
	-right->[succes] if "" then
		-->[iswhitespace(c)] inner_loop
	else
		->[not iswhitespace(c)] continue
	endif
else
	-->[fail] if "text_piece != []" then
		-->[true] "preprocessed_text.add(text_piece)"
		--> (*)
	else
		-->[false] (*)
	endif
endif



@enduml
```
 