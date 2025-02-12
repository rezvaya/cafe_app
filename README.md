# 📌 Разработка приложения управления заказами кафе (Python + SQLite)

👋 Сегодня мы создадим консольное приложение для управления заказами в кафе, используя **Python и SQLite**.

## 📖 Чему вы научитесь?
✅ **Работа с SQL-запросами** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`)
✅ **Создание базы данных и подключение SQLite в Python**
✅ **CRUD-операции: добавление, просмотр, изменение и удаление данных**

---

## 📅 План работы

### 1️⃣ Подготовка среды
🔹 Установите Python (если не установлен)
🔹 Убедитесь, что у вас есть VS Code или другой редактор
🔹 Клонируйте этот репозиторий:
```bash
git clone [https://github.com/your-repo/cafe-orders.git](https://github.com/rezvaya/cafe_app.git)
cd cafe_app
```

---

### 2️⃣ Разбираемся с базой данных
📌 В файле `template.py` уже создана **структура базы данных** с таблицами:
- `clients` (клиенты)
- `menu` (меню)
- `orders` (заказы)
- `order_items` (детали заказов)

🎯 **Задача:** Исследовать структуру БД и связи между таблицами.

---

### 3️⃣ Реализация CRUD-операций
В **шаблоне кода** с заготовками для функций вам нужно дописать код в местах `TODO`, реализовав **CRUD**:

✅ **Добавить клиента** 
✅ **Добавить блюдо в меню** 
✅ **Создать заказ** 
✅ **Вывести список клиентов** 
✅ **Вывести меню** 
✅ **Вывести заказы** 

💡 Используйте SQL-запросы в `cursor.execute(...)`. Не забудьте про `conn.commit()`!

---

### 4️⃣ Тестируем и отлаживаем
🔹 Запустите программу:
```bash
python template.py
```
🔹 Проверьте, корректно ли добавляются клиенты, блюда и заказы
🔹 Исправьте возможные ошибки

---

## 🎯 Ожидаемый результат
🔹 Вы разработаете **рабочее приложение** с консольным меню
🔹 Научитесь **подключать SQLite к Python**
🔹 Разберетесь с **работой SQL-запросов**
🔹 Сможете использовать **CRUD-операции** в проектах

---

## 📌 Как улучшить проект?
🚀 После завершения основной части, попробуйте:
🔹 **Добавить удаление данных** (клиентов, заказов, блюд)
🔹 **Реализовать проверку данных** (например, проверять, существует ли клиент)
🔹 **Добавить интерфейс** например через телеграм-бота