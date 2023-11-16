# Разработка BI-системы для исследования учебных планов образовательных программ университетов

## Описание проекта
Данная система призвана удовлетворить потребность студентов в инструменте для анализа и сравнения образовательных программ на основе учебных планов для выбора наиболее подходящего для них ВУЗа. <br>
Система так же будет полезна руководителям образовательных программ при разработке учебных планов, предоставляя им возможность выделить сильные и слабые стороны аналогичных образовательных программ.

## Целевые пользователи
Абитурьенты, преподаватели ВУЗов. <br>
При доведения до продуктового уровня возможны тысячи (или даже миллионы) пользователей в день.

## Пользовательские требования
<ul>
  <li> Реализация системы минимум для 5 ВУЗов на раннем этапе с возможностью расширения; </li>
  <li> Интуитивно понятная инфографика при сравнении пользователем образовательных программ; </li>
  <li> Разработать метрики и критерии для анализа и сравнения учебных планов; </li>
  <li> Хранить историю по учебным планам программ за последние 3-4 года; </li>
  <li> Скорость анализа и сравнения не должна превышать 5-10 секунд; </li>
  <li> Необходима возможность просмотра и фильтрации пользователем списка уже загруженных образовательных программ; </li>
  <li> Реализовать возможность выгрузки результатов анализа в формате Excel-таблицы. </li>
</ul>

## Дополнительный контекст
<ul>
  <li> Пиковая нагрузка в сезон приемной кампании (май-август); </li>
  <li> Ограниченные ресурсы на раннем этапе разработки (домашний ПК); </li>
  <li> Необходима расширяемость под разные форматы учебных планов разных ВУЗов. </li>
</ul>

## Заинтересованные лица:

<b> У-1: Пользователи (доступность, скорость) </b> <br>
Под пользователями системы подразумеваются <i> абитуриенты </i> и <i> работники университетов </i>, которые будут использовать данную систему для анализа образовательных программ. Приоритетными качествами в системе для них является доступность, отзывчивость и скорость работы. <br>

<b> У-1.1: Абитуриенты </b> <br>
Выпускники, подбирающие себе университет. <br>

<b> У-1.2: Работники университетов  </b> <br>
Лица из числа профессорско-преподавательского состава, ответственные за разработку курсов и учебных планов образовательных программ. <br>

<b> У-2: Команда разработки (расширяемость, масштабируемость) </b>
Команда разработки отвечает за создание и улучшение функциональности разрабатываемой системы. Для них важна простота внесения улучшений и интеграции новых модулей.

<b> У-3: Эксперты (документация, новизна) </b> <br>
Для заказчиков (<i>научного руководителя </i> и <i> комиссии </i>) является важным соблюдение всех университетских регламентов защиты выпускной работы. Также его необходимо впечатлить научной новизной разрабатываемого решения. <br>

<b> У-3.1: Научный руководитель </b> <br>
Вячеслав Владимирович Ланин. Ему как научному руководителю нужно презентовать разработку и предоставить хорошо оформленную документацию, состоящую из текста выпускной работы и технического задания. <br>

<b> У-3.2: Комиссия </b> <br>
Все то же самое, что руководителю. <br>

<b> У-4: Техническая поддержка (устойчивость) </b> <br>
Техническая поддержка системы заинтересована в стабильной работе системы и ведении журнала операций для отслеживания возможных аварийных ситуаций. <br>

<b> У-5: Data Engineer (доступность, расширяемость) </b> <br>
Data Engineer занимается обновлением данных об учебных планах. Ему необходима возможность к загрузке новых данных и по встраиванию новых инструментов извлечения данных. <br>


## Характеристики системы:
<b> Х-1: Доступность (У-1, У-5) </b> <br>
<ul>
  <li> Система должна быть доступна везде в пределах России. </li>
  <li> Система должна работать без перебоев в дневное время (по Москве); допустимо отключение системы для проведения технических работ в ночное время). </li>
</ul>
<b> Х-2: Скорость (У-1) </b> <br>
<ul>
  <li> Скорость отклика системы при требовательных по ресурсам запросам около 5-10 секунд. </li>
</ul>
<b> Х-3: Расширяемость (У-2, У-5) </b> <br>
<ul>
  <li> Система должна быть модульной и обеспечивать расширение с наименьшими изменениями в ранее разработанных компонентах. </li>
</ul>
<b> Х-4: Масштабируемость (У-2) </b> <br>
<ul>
  <li> Поскольку планируется большое число пользователей необходимо обеспечить масштабируемость системы за счет конвейерного параллелизма. </li>
</ul>
<b> Х-5: Документация (У-3) </b> <br>
<ul>
  <li> См. НФТ-1 </li>
</ul>
<b> Х-6: Новизна (У-3) </b> <br>
<ul>
  <li> Необходимо разработать и использовать алгоритмы интеллектуального анализа и визуализации данных для представления и сравнения содержаний учебных планов. </li>
</ul>
<b> Х-7: Устойчивость (У-4) </b> <br>
<ul>
  <li> Система должна быть устойчивой, чтобы минимизировать затраты на поддержку. </li>
</ul>

##  Функциональные требования (сценарии использования):
Шаблон описания взят из книги <b> А. Коберна </b> <i> «Современные методы описания функциональных требований» </i>. <br>

<b> ФТ-1: Анализ образовательной программы. </b> <br>
<b> Цель в контексте  </b>: Получить инсайты о содержании образовательной программы. <br>
<b> Область действия  </b>: Основная функциональность <br>
<b> Уровень  </b>: Цель пользователя. <br>
<b> Участники  </b>: Пользователь. <br>
<b> Предусловия  </b>: Нет. <br>
<b> Постусловие  </b>: Пользователь получил информацию об образовательной программе в структурированном виде. <br>
<b> Основной сценарий  </b>: <br>
1.	Выбор образовательной программы для анализа.
2.	Просмотр набора основных дисциплин программы.
3.	Просмотр набора всех дисциплин программы.
4.	Просмотр метрик (В-2) образовательной программы.
5.	Просмотр истории изменения образовательной программы.
6.	Просмотр графа связей (В-3) учебных курсов образовательной программы.
7.	Просмотр основных развиваемых компетенций. <br>

<b> Расширения  </b>: <br>
2.а. Просмотр подробной информации о дисциплинах. <br>

<b> ФТ-2: Сравнение образовательных программ. </b> <br>
<b> Цель в контексте </b>: Выявить сильные и слабые стороны программы. <br>
<b> Область действия </b>: Основная функциональность. <br>
<b> Уровень </b>: Цель пользователя. <br>
<b> Участники </b>: Пользователь. <br>
<b> Предусловия </b>: Нет. <br>
<b> Постусловие </b>: Пользователь получил сравнительный анализ нескольких образовательных программ. <br>
<b> Основной сценарий </b>: <br>
1.	Выбор образовательных программ для сравнения. 
2.	Просмотр набора общих дисциплин.
3.	Просмотр набора похожих дисциплин.
4.	Просмотр набора различающихся дисциплин.
5.	Просмотр всего набора дисциплин.
6.	Просмотр метрик (В-2) образовательных программ.
7.	Просмотр общих развиваемых образовательных компетенций.
8.	Просмотр различающихся развиваемых образовательных компетенций. <br>

<b> ФТ-3: Техническая поддержка. </b> <br>
<b> Цель в контексте </b>: Понять причину ошибки. <br>
<b> Область действия </b>: Техническая поддержка пользователей, разработка. <br>
<b> Уровень </b>: Цель пользователя. <br>
<b> Участники </b>: Пользователь, Техническая поддержка. <br>
<b> Предусловие </b>: Произошла ошибка у пользователя. Пользователь сообщает об ошибке. <br>
<b> Постусловие </b>: Ошибка устранена. <br>
<b> Основной сценарий </b>: <br>
1.	Техническая поддержка принимает сообщение об ошибке.
2.	Техническая поддержка ищет сведения об ошибке в журнале операций.
3.	Техническая поддержка воспроизводит ошибку.
4.	Техническая поддержка производит решение случившейся проблемы.
5.	Сообщает о решении пользователю. <br>

<b> Расширения </b>: <br>
2.а. Сообщение неинформативно, и потому отклонено поддержкой. <br>
2.б. В сообщении описана не ошибка, а особенность работы системы («не баг, а фича»). <br>
2.в. Ошибка слишком незначительная, и потому отклонена. <br>
4.а. Ошибка не воспроизводится, но при этом незначительная, поддержка отклоняет ошибку. <br>
4.б. Ошибка не воспроизводится и является критичной, поддержка сообщает об этом разработке. <br>
5.а. Решение требует критических исправлений, поддержка передает ошибку программистам. <br>

<b> Время реакции </b>: 1-2 дня. <br>

<b> ФТ-4: Извлечение данных. </b> <br>
<b> Цель в контексте </b>: Расширение аналитической базы данных. <br>
<b> Область действия </b>: Обновление данных. <br>
<b> Уровень </b>: Цель пользователя. <br>
<b> Участники </b>: Data Engineer. <br>
<b> Предусловие </b>: Собраны свежие данные для преобразования и загрузки. <br>
<b> Постусловие </b>: Загружены свежие данные, интегрированы новые инструменты. <br>
<b> Основной сценарий </b>: <br>
1.  Data Engineer пишет парсер нового формат учебных планов.
2.  Data Engineer открывает панель администратора.
3.  Data Engineer добавляет туда разработанные парсер.
4.  Data Engineer заполняет сведения о парсере (целевой ВУЗ, формат данных).
5.  Система помечает его в статусе <i>beta</i>. <br>


## Нефункциональные требования:
<b> НФТ-1 </b>: Нужно разработать пакет документов (текст выпускной работы и техническое задание), оформленный в соответствии с правилами оформления выпускных работ и ГОСТ (У-3). <br>

<b> НФТ-2 </b>: Необходимо обеспечить возможность расширения аппаратных мощностей при увеличении числа пользователей (порядка 100_000 человек) в пиковый период (У-1, У-2). <br>

<b> НФТ-3 </b>: Архитектура MVP должна быть разработана и реализована на домашнем компьютере (Intel Core i5, 8 ГБ ОЗУ DDR4, ОС Windows 10 / Linux Ubuntu 22). <br>

<b> НФТ-4 </b>: Нужно спроектировать расширяемость системы под разные форматы входных данных, так как учебные планы у разных вузов имеют разный формат: как содержание, так и представление информации (У-5). <br>

## Ограничения:
<b> О-1 </b>: Не хранятся персональные данные, чтобы не обеспечивать их безопасность. <br>
<b> О-2 </b>: Используются по возможности открытое и/или отечественное внешнее программное обеспечение. <br>

## Предположения и допущения:
<b> П-1 </b>: Оценка неучтенных в учебных планах и иных документах образовательных программ параметров находится вне рамок данного проекта. <br>
<b> П-2 </b>: Считаем, что в качества рабочего прототипа подойдет реализация системы в виде интерактивного дашборда. <br>
<b> П-3 </b>: На первом этапе разработки закладываем работу с учебными планами 5 разных вузов. <br>

## Вопросы:
<b> В-1 </b>: Определить какой ГОСТ использовать для технического задания и согласовать с руководством образовательной программы. <br>
<b> В-2 </b>: Определить по каким метрикам будем сравнивать образовательные программы. <br>
<b> В-3 </b>: Определить, что представить в качестве вершин и ребер графа. <br>


