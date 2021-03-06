
# Сутність класів

Аналогії класів з [toaster](https://toster.ru/answer?answer_id=20946):

- Клас — креслення
    - Об'єкт — машина зроблена по кресленю
- Статичний метод — якась функція (напр. GPS), яка йде разом з кресленням і знаходиться в кожній машині, що зроблена по кресленю.
    - Статичні методи не зв'язуються екземплярами класів та можуть бути викликані незалежно від того, створений екземпляр класу, чи ні.
    - Набір статичних методів може бути розглянутий, як набір глобальних ф-цій / змінних, які не потребують створення екземпляру класу.

---
- Клас описує — що це таке.
- Реалізація класу (instance) — реалізує конкретний екземпляр класу.

---
Клас — спосіб організації полів, методів і т.д. = інкапсульований „шматок“ функціональності, опис структури майбутніх об'єктів + свій простір імен всередині.

Статична складова класа — static-методи та static-поля. Це логічний спосіб організації ф-ціоналності, загальної для будь-якого об'єкта виділеної сутності.
Тут значення має логічна складова.

---
Можна думати про клас, як про набір ф-цій, а про об'єкт — як набір даних.

Деякі ф-ції в класі можуть бути використані тільки з набіром даних (тобто об'єктом), який передається неявно.

Інші ф-ції не потребують об'єкта, тому можуть викликані напряму із класу.

Дуже логічно виглядає Python, де у будь-якого методу є явний аргумент `self`, що вказує на об'єкт, із якого був викликаний метод.
А запис: `object.method(5)` є скороченням від `ObjectClass.method(object, 5)`.

---

- Клас — це визначення загальної поведінки для об'єктів, які цей клас породжує.
    - Об'єкт — буде мати поведінку, яку задає клас і відрізнятися від інших об'єктів — своїм станом. Якщо ж стан однаковий, то буде як два однакових автомобіля — дві різні сутності, але виглядають — однаково.
    - Класу можна додати статичні методи і поля. Тепер вже сам клас буде мати можливість зберігати свій стан та виконувати дії.
    В більшості випадків, це потрібно для контролю над виробництвом об'єктів цього класу (петерни Синглетон, Фабрика…)
    
В ООП — все є об'єктом. Це потрібно, щоб контролювати вже самі класи (які є теж об'єктами), під-завантажувати їх підчас роботи програми, чи старту і т.д.

#### Одною з переваг ООП є краща модульність програмного забезпечення (тисячу функцій процедурної мови, в ООП можна замінити кількома десятками класів із своїми методами).

На відміну від традиційних поглядів, коли програму розглядали як набір підпрограм, або як перелік інструкцій комп'ютеру, ООП програми можна вважати сукупністю об'єктів. Відповідно до парадигми об'єктно-орієнтованого програмування, кожен об'єкт здатний отримувати повідомлення, обробляти дані, та надсилати повідомлення іншим об'єктам. Кожен об'єкт — своєрідний незалежний автомат з окремим призначенням та відповідальністю.

Програмісти спочатку пишуть клас, а на його основі при виконанні програми створюються конкретні об'єкти (екземпляри класів). На основі класів можна створювати нові, які розширюють базовий клас і таким чином створюється ієрархія класів.

Алан Кей, основні принципи ООП:

- Все є об'єктами.
- Всі дії та розрахунки виконуються шляхом взаємодії (обміну даними) між об'єктами, при якій один об'єкт потребує, щоб інший об'єкт виконав деяку дію. Об'єкти взаємодіють, надсилаючи і отримуючи повідомлення. **Повідомлення** — це запит на виконання дії, доповнений набором аргументів, які можуть знадобитися при виконанні дії.
- **Кожен об'єкт має незалежну пам'ять**, яка складається з інших об'єктів.
- Кожен об'єкт є представником (екземпляром, примірником) класу, який виражає загальні властивості об'єктів.
- У класі задається поведінка (функціональність) об'єкта. Таким чином усі об'єкти, які є екземплярами одного класу, можуть виконувати одні й ті ж самі дії.
- Класи організовані у єдину деревоподібну структуру з загальним корінням, яка називається ієрархією успадкування. **Пам'ять та поведінка**, зв'язані з екземплярами деякого класу, **автоматично доступні будь-якому класу**, розташованому нижче в ієрархічному дереві.


Будується ієрархія об'єктів: 

- програма в цілому — це об'єкт, для виконання своїх функцій вона звертається до об'єктів що містяться у ньому, 
    - які у свою чергу виконують запит шляхом звернення до інших об'єктів програми. 
- Звісно, щоб уникнути безкінечної рекурсії у зверненнях, на якомусь етапі об'єкт трансформує запит у повідомлення до стандартних системних об'єктів, що даються мовою та середовищем програмування.

Для подальшого розвитку об'єктно-орієнтованого програмування велике значення мають поняття події (так зване подієво-орієнтоване програмування) і компоненти (компонентне програмування, КОП).

Формування КОП від ООП відбулося, так само як формування модульного від процедурного програмування: процедури сформувалися в модулі - незалежні частини коду до рівня збірки програми, так об'єкти сформувалися в компоненти - незалежні частини коду до рівня виконання програми. Взаємодія об'єктів відбувається за допомогою повідомлень. Результатом подальшого розвитку ООП, мабуть, буде агентно-орієнтоване програмування, де агенти - незалежні частини коду на рівні виконання. Взаємодія агентів відбувається за допомогою зміни середовища, в якій вони знаходяться.

В об'єктно-орієнтованому програмуванні, **клас** — це спеціальна конструкція, яка **використовується для групування** _пов'язаних змінних та функцій_. 

- При цьому, згідно з термінологією ООП, `глобальні змінні` класу (члени-змінні) називаються `полями даних` (також _властивостями_ або _атрибутами_), а _члени_-`функції` називають `методами класу`. 
- _Створений та ініціалізований_ `екземпляр класу` називають `об'єктом класу`. 

На основі одного класу можна створити безліч об'єктів, що відрізнятимуться один від одного своїм `станом` (_значеннями_ `полів`).

- **Метод**, який проводить створення та початкову _ініціалізацію_ екземпляра класу називають `конструктором` класу. 
- **Метод**, який проводить _знищення_ об'єкта, називають `деструктором` класу.

### Клас 

- Клас визначає абстрактні характеристики деякої сутності, включаючи характеристики самої сутності (її атрибути або властивості) та дії, які вона здатна виконувати (її поведінки, методи або можливості).
- Класи вносять модульність та структурованість в об'єктно-орієнтовану програму. Як правило, клас має бути зрозумілим для не-програмістів, що знаються на предметній області, що, у свою чергу, значить, що клас повинен мати значення в контексті.
- Також, код реалізації класу має бути досить самодостатнім. Властивості та методи класу, разом називаються його членами

### Об'єкт 

- Окремий екземпляр класу (створюється після запуску програми і ініціалізації полів класу).
    - Клас `Собака` відповідає всім собакам шляхом опису їхніх спільних рис; об'єкт `Сірко` є одним окремим собакою, окремим варіантом значень характеристик. Об'єкт `Сірко` **є екземпляром** (примірником) класу `Собака`
- Сукупність значень атрибутів окремого об'єкта називається **станом**.
    - На основі класу `Собака` можна, також, створити інший об'єкт `Дружок`, який відрізнятиметься від об'єкта `Сірко` своїм станом (наприклад кольором хутра). Обидва об'єкта (`Сірко` і `Дружок`) є екземплярами класу `Собака`.

### Метод 

- Можливості об'єкта. Функції.
В межах програми, використання методу має впливати лише на один об'єкт; всі 
    - Собаки можуть гавкати, але треба щоб гавкав лише один окремий собака.

### Обмін повідомленнями 

- «Передача даних від одного процесу іншому, або надсилання викликів методів.»



### Успадкування (наслідування) 

- Клас може мати «підкласи», спеціалізовані, розширені версії надкласу. Можуть навіть утворюватись цілі дерева успадкування. Підкласи _успадковують_ атрибути та поведінку своїх батьківських класів, і можуть вводити свої власні.

### Приховування інформації (інкапсуляція) 

- Приховування деталей про роботу класів від об'єктів, що їх використовують або надсилають їм повідомлення.
-  Інкапсуляція досягається шляхом вказування, які класи можуть звертатися до членів об'єкта. Як наслідок, кожен об'єкт представляє кожному іншому класу певний інтерфейс — члени, доступні іншим класам.
- Часто, члени класу позначаються як публічні (англ. public), захищені (англ. protected) та приватні (англ. private), визначаючи, чи доступні вони всім класам, підкласам, або лише до класу в якому їх визначено.

### Абстрагування 

- Спрощення складної дійсності шляхом моделювання класів, що відповідають проблемі, та використання найприйнятнішого рівня деталізації окремих аспектів проблеми. 

### Поліморфізм 

- Поліморфізм означає залежність поведінки від класу, в якому ця поведінка викликається, тобто, два або більше класів можуть реагувати по-різному на однакові повідомлення.
    - Наприклад, якщо Собака отримує команду голос(), то у відповідь можна отримати Гав; якщо Свиня отримує команду голос (), то у відповідь можна отримати Рох-рох. На практиці - це реалізовується шляхом реалізації ряду підпрограм (функцій, процедур, методи тощо) з однаковими іменами, але з різними параметрами. В залежності від того, що передається і вибирається відповідна підпрограма.



**Ме́тод** в об'єктно-орієнтованому програмуванні — підпрограма (процедура, функція), що використовується виключно разом із класом (методи класу) або з об'єктом (методи екземпляра).

Розрізняють прості методи і статичні методи (методи класу):

- прості методи мають доступ до даних об'єкта (конкретного екземпляра даного класу)
- статичні методи не мають доступу до даних об'єкта і для їх використання не потрібно створювати екземпляри (даного класу).

Залежно від способу використання, методи поділяються на:

- **змістовні** — надаються клієнтам класу і визначають його інтерфейс, звичайно є публічними;
- **спеціальні** — викликаються автоматично при створенні (конструктори), знищенні (деструктори), копіюванні (конструктори копіювання), перетворенні типу тощо;
- **допоміжні** — викликаються з змістовних та спеціальних методів, звичайно не надаються клієнтам класу і є захищеними або приватними.

Залежно від впливу на стан об'єкта, методи поділяються на:

- **конструктори** — встановлюють початковий стан об'єкта;
- **деструктори** — скидають стан об'єкта;
- **селектори** (геттери) — надають значення атрибута;
- **модифікатори** (сеттери) — встановлюють значення атрибута;
- **ітератори** — надають послідовний доступ до множини атрибутів.

Всі значення в JavaScript, за винятком `null` і `undefined`, містять набір допоміжних функцій і значень, доступних «через точку». Такі функції називають «методами», а значення - «властивостями». 

**Обмін повідомленнями** — в програмуванні, є способом координації в конкурентних, паралельних, та об'єктно-орієнтованих системах, та організації взаємодії між процесами. Координація робиться шляхом відсилання повідомлень отримувачу. Повідомлення можуть мати форму викликів функцій, сигналів, та пакетів даних.

Функції відправлення та отримання повідомлень зазвичай мають назву відправити (англ. send) та отримати (англ. receive) відповідно. Вони є примітивами в системах обміну повідомленнями. Функція «відправити» має два параметри — адресу, на яку слід надіслати повідомлення, та буфер даних повідомлення. Функція «отримати» також має два параметри — адреса звідки очікується повідомлення (може бути шаблоном) та буфер для збереження даних повідомлення.

### Інтерфе́йс (англ. interface):
У програмуванні існує поняття програмного інтерфейсу, що означає перелік можливих обчислень, які може виконати та чи інша частина програми, включаючи опис того, які аргументи і в якому порядку потрібно передавати на вхід алгоритмам з цього переліку, а також що і в якому вигляді вони будуть повертати. Абстрактний тип даних інтерфейс придуманий для формалізованого опису такого переліку. Самі алгоритми, тобто дійсний програмний код, який буде виконувати всі ці обчислення, інтерфейсом не задається, програмується окремо та називається реалізацією інтерфейсу.

- Сукупність засобів і правил, що забезпечують взаємодію пристроїв обчислювальної системи та (або) програм.
- Сукупність описів і узгоджень щодо процедури передачі керування в підпрограму та повернення до вихідної програми.

У контексті окремого елемента інтерфейс елемента протилежний до реалізації елементу (внутрішнього устрою та функціювання). Користувачеві елемента немає потреби знати, як реалізовано уживаний елемент, щоб керувати ним, але використовуваний елемент має надати інтерфейс керування.

Інтерфейси є основою взаємодії в сучасних інформаційних системах. Якщо інтерфейс якого-небудь об'єкту (персонального комп'ютера, програми, функції) не змінюється (стабільний, стандартизований), це дає можливість модифікувати сам об'єкт, не перероблюючи його принципи взаємодії з іншими об'єктами. Це дозволяє масштабувати інтерфейс, створювати інші пристрої чи функції, які будуть використовувати такий спосіб взаємодії.

> Клас дозволяє задати не лише програмний інтерфейс до самого себе і до своїх екземплярів, але і в явному вигляді написати код, відповідальний за обчислення. 

### 		Стан об'єкта, поняття областей доступу, конструктори
Правила, що визначають можливість або неможливість безпосередньо змінювати будь-які змінні, називаються правилами завдання областей доступу. Слова «приватний» та «публічний» в цьому випадку є так званими «модифікаторами доступу». Вони називаються «модифікаторами» тому, що в деяких мовах вони використовуються для зміни раніше встановлених прав при спадкуванні класу. Спільно класи та модифікатори доступу задають область доступу, тобто у кожної ділянки коду, залежно від того, до якого класу вона належить, буде своя область доступу щодо тих чи інших елементів (членів) свого класу та інших класів, включаючи змінні, методи, функції, константи, тощо. 

> Існує основне правило: ніщо в одному класі не може бачити приватних елементів іншого класу. *Щодо інших, більш складних правил, у різних мовах існують інші модифікатори доступу та правила їх взаємодії з класами.*

Майже кожному члену класа можна встановити модифікатор доступу (за винятком статичних конструкторів та деяких інших речей).

Проблема підтримки правильного стану змінних актуальна і для вихідного моменту виставлення початкових значень. Для цього в класах передбачені спеціальні методи/функції, звані конструкторами. Жоден об'єкт (екземпляр класу) не може бути створений інакше, як шляхом виклику на виконання коду конструктора, який поверне викликає стороні створений та правильно заповнений примірник класу. У багатьох мовах програмування тип даних «структура», як і клас, може містити змінні та методи, але екземпляри структур, залишаючись просто розміченими ділянками оперативної пам'яті, можуть створюватися в обхід конструкторам, що заборонено для примірників класів (за винятком спеціальних виняткових методів обходу всіх подібних правил ООП, передбачених в деяких мовах та платформах). У цьому виявляється відмінність класів від інших типів даних — виклик конструктора обов'язковий.

## Об'єкт
Властивості об'єкта визначаються його атрибутами (полями даних). Поточне значення атрибутів визначає поточний стан об'єкта у множині можливих станів.

Поведінка об'єкта визначається функціями (методами) об'єкта. Передача повідомлень між об'єктами (взаємодія об'єктів) призводить до виконання об'єктом, що отримав повідомлення, визначеної функції. Об'єкт також може надіслати повідомлення собі. В результаті отримання об'єктом повідомлення він змінює свій стан: на новий, якщо виконання операцій функції призвело до зміни значень атрибутів; або той самий, якщо атрибути не зазнали змін. В контексті отримання повідомлень та зміни станів об'єкт може розглядатись як [автомат](https://uk.m.wikipedia.org/wiki/Теорія_автоматів).

Властивості об'єкта звичайно доступні лише через його функції при цьому вважається, що об'єкт є екземпляром класу як абстрактного типу даних.

Відповідно до властивостей об'єкта та його стану функції поділяються на конструктори, селектори, модифікатори та деструктори:

- конструктори здійснюють первинну ініціалізацію об'єкта при його створенні;
- селектори повертають значення окремих властивостей;
- модифікатори змінюють значення окремих властивостей;
- деструктори скидають значення властивостей при знищенні об'єкта.

Об'єкти звичайно зберігаються в оперативній пам'яті під час виконання програми. При цьому вони представлені в пам'яті послідовністю значень атрибутів — структурою даних. Всі функції об'єктів зберігаються по-за межами об'єктів і для функцій лише забезпечується контекст — можливість звернення до атрибутів вказаного об'єкта.

