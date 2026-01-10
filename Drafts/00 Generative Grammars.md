# 00 Породжуючі граматики

%% Insert text %%
***Породжуюча граматика*** є стандартним інструментом специфікації синтаксису формальної мови.
### [[Generative Grammar Definition|Визначення породжуючої граматики]]
 
### [[Generating Language by Grammar|Як граматики породжують мови?]]


## Чернетки

```dataviewjs
let pages = dv.pages().where(p => p.file.outlinks.some(l => l.path.includes("00 Породжуюча граматика.md")));

if (pages.length > 0) {
//    dv.header(3, "Нотатки, що посилаються на '00 Наскрізний приклад'");
    dv.list(pages.map(p => p.file.link));
} else {
    dv.paragraph("Не знайдено нотаток, які посилаються на '00 Породжуюча граматика'.");
}
```

## Зміст

1. [[Generating Language by Grammar]].
2. [[Обчислювальні властивості мови породженої граматикою]].
3. [[Контекстно-вільні граматики]].