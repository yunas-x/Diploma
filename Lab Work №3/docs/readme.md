# Разработка BI-системы для исследования учебных планов образовательных программ университетов
## Диаграмма компонентов
По сути это немного измененная модель из второй лабораторной (красным/пунктиром выделены те части, которые опускаются). Более детально потоки (чтобы не заграмождать диаграмму компонентов) отражены на диаграмме последовательностей. Так как как-то нужно продемонстрировать принцип YAGNI и KISS в качестве иллюстрации покажем его на данном уровне. На этапе первого прототипа можно пожертвовать базой с логами и ограничиться средствами фреймворка или библиотекой (например, loguru, так как целевым языком взят Python). На первом этапе пренебрежем межсерверным взаимодейтсвием между компонентами и будем записывать напрямую в базу данных. Система не теряет функциональности, однако необходимо продумать заменяемость инструментов логирования и разработать модуль-загрузчик в Базу Данных с учетом будущего перехода на взаимодействие по сети.<br/>
Таким образом, реализуем принципы YAGNI и KISS на этапе проектирования.
![plot](https://github.com/yunas-x/Diploma/blob/Lab-Work-3/Lab%20Work%20%E2%84%963/docs/SSAD%203-2.png)

## Диаграмма последовательностей
На диаграмме нарочно опущены сценарии отказа (ошибки), чтобы избежать загромождения. При возникновении ошибки при любом из промежуточных вызовов процесс прекращается, ошибка "всплывает" по стэку вызовов, пока не дойдет обратно до уровня API, где она "запаковывается" в 400-code ответ и возвращается пользователю. 
![plot](https://github.com/yunas-x/Diploma/blob/Lab-Work-3/Lab%20Work%20%E2%84%963/docs/SSAD%203.png)

## Модель БД
В данной работе используется OLAP-подход к построению Хранилищ Данных. Хранилище спроектировано по схеме "Звезда". В папке src приложена соответствующая приложенной ниже json-схема (может быть полезна для изучения ограничений модели).<br/>
Справка по модели данных:
|Таблица|Моделируемый объект|Описание|
| --- | --- | --- |
| Curricula | Учебный план | В данной таблице аггрегируются измерения (качественные характеристики) и показатели (количественные характеристики) учебных планов |
| Competence | Компетенция | В данной таблице описана вся информация, относящаяся к наборам компетенций, получаемых во время обучения |
| Program | Образовательная программа | В данной таблице приведена основная информация о образовательных программах |
| Degree | Уровень квалификации | В данной таблице приведена информация об уровне получаемого образования |
| University | Университет | В данной таблице приведена информация об образовательной организации, в которой реализуется программа |
| Faculty | Факультет | В данной таблице приведена информация о факультете, которые реализует программу |
| Field of Study | Направление подготовки | В данной таблице указаны направления подготовки, соответствующие программе |
| Course | Учебная дисциплина | В данной таблице содержится информация о курсах, которые реализуются на программе |

![plot](https://github.com/yunas-x/Diploma/blob/Lab-Work-3/Lab%20Work%20%E2%84%963/docs/DW.png)

## Применение основных принципов разработки
[Описаны здесь](../src/readme.md)

## Дополнительные принципы разработки
### BDUF
<b>Big Design Up Front</b> — подход (зачастую водопадный), при которым дизайн системы тщательно прорабатывается перед его реализацией. Как правило в данном случае проектирование предполагает рассмотрение возможных расширений системы. Так как времени на данную работу мало и не требуется ее полная реализация для защиты, данный подход решено не использовать и работать по гибким методологиям.
### SoC
<b>Separation of Concerns</b> — разделение ответственности. При данном подходе система (или подсистемы) проектируется так, что функциональная ответственность модулей была четко разделена. В данной работе имеется разделение на фронт, модель машинного обучения, чат-бот для технической поддержки и загрузчик данных.
### MVP
<b>Minimal Viable Product</b> — разработка минимально жизнеспособного продукта для демонстрации заказчику. При данном подходе бэклог задач приоритизируется с точки зрения полезности для достижения минимальной рабочей версии системы. Отчасти схож с подходом Proof of Concept, однако от MVP требуется продуктовый демонстрационный результат, тогда как PoC относится скорее к техническим и исследовательским аспектам. По сути разрабатывая система является MVP в силу ограничений по ресурсам и времени.
### PoC
<b>Proof of Concept</b> — построение пилотной версии системы для тестирования какой-либо технической (иногда продуктовой) гипотезы. Предполагается первоочередная реализация той части системы, работоспособность которой нужно доказать. Данный подход используется при разработке данной системе, так как требуется проверить жизнеспособность предполагаемых моделей машинного обучения.
