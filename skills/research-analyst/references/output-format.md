# Output format

## Citation format

Inline, in the sentence carrying the claim. In chat use Markdown links; in `.docx` these must survive as real hyperlinks, not as bare text.

```
Выручка «Компании А» за 2024 г. — 3,7 млрд ₽ [источник]([ссылка на ГИР БО]),
при валовой марже 22% [расчёт: 0,81 млрд ÷ 3,7 млрд]([ссылка]).
Доля рынка — примерно 12–15% [оценка: от размера рынка снизу вверх, см. раздел 3].
```

Three markers, one on every number:

| Маркер | Когда | Что обязательно рядом |
|---|---|---|
| `[источник]` | Цифра взята из документа | Прямая ссылка + период/единицы, как в источнике |
| `[расчёт]` | Цифра выведена | Формула прямо в строке + ссылки на входы |
| `[оценка]` | Суждение модели без источника | На чём основано + диапазон, а не точка |

Rules that make the markers mean something:

- **No unmarked numbers.** Including ones that feel like common knowledge.
- **`[оценка]` gets a range**, not a fake-precise point value. "примерно 40–55%" is honest; "47,3%" pretending to be an estimate is not.
- **Where a claim rests only on press reporting**, say so at the claim: «по сообщению [издания](ссылка), первичный документ недоступен».
- **As-of dates** on everything that moves: prices, shares, headcounts, market sizes, regulatory status.
- **Currency and period** stated every time; if a conversion was applied, state the rate and its date.

## Report skeleton

Adapt the weighting to the question, but keep the block order — it runs from "what is true" to "what to do", which is how a decision-maker reads.

```markdown
# [Тема]: аналитический разбор

**Вопрос, на который отвечает отчёт:** [одно предложение]
**Решение, которое он обслуживает:** [инвестировать / запускать / выходить / …]
**Данные актуальны на:** [дата]

**Допущения** (если бриф не был уточнён): …

---

## 1. Итог за 60 секунд
- [Самый значимый вывод — одним предложением]
- [Второй]
- [Третий]

## 2. Как устроен рынок
Цепочка создания стоимости, распределение маржи по звеньям, кто владеет
клиентом, структурные ограничения.

## 3. Размер и динамика
Расчёт снизу вверх с формулой. Сверка со стороны предложения.
Расхождение с публичными оценками и объяснение расхождения.

## 4. Аудитория и психология спроса
Работа (JTBD), триггерное событие, что «нанимают» сейчас, барьеры переключения,
формулировки самих клиентов (цитаты).

## 5. Конкуренты и реальные преимущества
Позиции, юнит-экономика где выводима, вердикт по каждому «преимуществу»:
ров или просто фича.

## 6. Скрытые паттерны
Что показывают опережающие индикаторы и где они расходятся с публичной картиной.

## 7. Возможности
Каждая — с «почему именно сейчас».

## 8. Риски
### Убивающие тезис
### Управляемые
Для каждого: наблюдаемый триггер, вероятность, что делать.

## 9. Бизнес-идеи
Для каждой: первый клиент, самый дешёвый тест, его стоимость и критерий
прохождения, почему это до сих пор не сделали.

## 10. Прогнозы
| Утверждение | Вероятность | Горизонт | Наблюдаемый триггер |
|---|---|---|---|

**Что изменит мой вывод:** [2–3 наблюдения]

---

## Источники
[Сводный список — вторичен по отношению к инлайн-ссылкам]

## Что проверить не удалось
[Прямо: какие данные недоступны, что они бы решили]
```

The «Что проверить не удалось» section is not an apology. It tells the reader where their residual risk sits, and its absence reads as "everything was checked", which is the worst possible false impression.

## Length

Match it to the decision, not to the topic. A go/no-go on a niche can be two pages of dense, sourced argument; a market entry study is longer because sizing and regulation need space. Padding is not thoroughness — a report where the reader can skip paragraphs without loss has failed the generic-filler check in the main skill.

## Chat delivery

The default. Markdown, links live, tables where the data is comparative. Lead the message itself with the single most consequential finding in one sentence before the structure starts — the user should get the answer before they get the report.

## .docx delivery

Only on explicit request ("сделай документом", "оформи в Word", "нужен файл для клиента").

- Use the `docx` skill. If this repository's `legal-digest-alert` skill and its firm template are available, follow its convention: copy the template and use the unzip-edit-rezip workflow so `styles.xml`, numbering, header and footer come across intact, rather than generating a document from scratch. Never invent placeholder contact details or a placeholder logo.
- **Hyperlinks must be real hyperlinks** in the document. A report whose inline citations flatten into plain text loses the property that makes it defensible.
- The `[источник]` / `[расчёт]` / `[оценка]` markers carry over into the document unchanged.
- Tables for the prediction block and any comparative competitor data.
- If the content has not been approved yet, draft in chat first, then produce the file once it is settled — and say which mode you are in, so the user knows whether they are reviewing content or a final artifact.

## HTML artifact

Reasonable for a long report the user will forward to a team, and it handles charts and wide tables better than chat. Offer it; do not default to it. If charts are involved, read the `dataviz` skill before writing any chart code.
