# lang-auto-test

<p> Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.</p>
<p> Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
<p> Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
<p> В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
<p> Тест должен запускаться с параметром language следующей командой:
<p> pytest --language="es" test_items.py
<p> и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
