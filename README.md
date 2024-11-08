Этот код реализует эмулятор командной строки (ShellEmulator) на Python, который работает с виртуальной файловой системой (VFS), загружаемой из zip-архива, и логирует действия пользователя в CSV-файл. Эмулятор поддерживает команды, аналогичные Unix-подобной оболочке: ls, cd, mkdir, touch, cal, и exit.

Основные компоненты программы:
1. Класс ShellEmulator
Конструктор __init__: Загружает конфигурационный файл config.toml, который содержит путь к VFS и к файлу для логирования. Устанавливает текущую директорию (current_dir) как корневую (/) и вызывает метод load_virtual_fs для загрузки виртуальной файловой системы.

Метод load_virtual_fs: Проверяет, существует ли указанный zip-архив с VFS. Если архив существует, он извлекает его содержимое во временную директорию (/tmp/vfs), которая становится корневой виртуальной файловой системой.

Метод log_action: Записывает действия пользователя в лог-файл. Каждое действие записывается вместе с временной меткой в формате CSV.

Метод ls: Выводит список файлов и директорий в текущей директории. Если директория существует, выполняется логирование и возвращается список содержимого. Если директория не найдена, выводится сообщение об ошибке.

Метод cd: Меняет текущую директорию. Если указана корневая директория (/), она становится текущей. В случае, если указанная директория существует, текущая директория обновляется, иначе выбрасывается исключение.

Метод mkdir: Создает новую директорию в текущей директории виртуальной файловой системы. Если директория успешно создана, она добавляется в виртуальную файловую систему, а действие логируется.

Метод touch: Создает новый пустой файл в текущей директории. Файл создается, и действие записывается в лог.

Метод cal: Выводит текущий месяц и год. Действие логируется.

Метод exit: Логирует команду выхода и завершает работу эмулятора.

Метод run: Запускает цикл, который ожидает команды пользователя и выполняет соответствующие действия. Поддерживаются команды: ls, cd, touch, cal, и exit. Если команда не распознана, выводится сообщение о неизвестной команде.
Тестирование с использованием unittest:
Тесты проверяют корректность работы отдельных методов эмулятора:

Тест test_cd: Проверяет, правильно ли эмулятор меняет текущую директорию на новую.

Тест test_invalid_cd: Проверяет, выбрасывает ли эмулятор ошибку при попытке перейти в несуществующую директорию.

Тест test_ls: Проверяет, что команда ls корректно выводит список директорий после создания новой папки.

Тест test_mkdir: Проверяет, что команда mkdir создает новую директорию и что она отображается в результате выполнения ls.

Тест test_cal: Проверяет, выводит ли команда cal текущий месяц и год корректно.

Конфигурационный файл config.toml:

Файл содержит настройки эмулятора:

```python
[emulator]
vfs_path = "C:/Users/Станислав/Desktop/DZ1_konfig-main/Конфигурационка1/filesystem.zip"
log_file = "C:/Users/Станислав/Desktop/DZ1_konfig-main/Конфигурационка1/log.csv"
```

Пример использования:
Эмулятор загружает виртуальную файловую систему из архива filesystem.zip.
Пользователь может вводить команды, такие как:
ls: для просмотра содержимого текущей директории.
cd <directory>: для перехода в другую директорию.
mkdir <directory>: для создания новой директории.
touch <filename>: для создания нового файла.
cal: для вывода текущего месяца и года.
exit: для завершения работы эмулятора.
Все действия пользователя записываются в лог-файл log.csv.

Этот эмулятор представляет собой простую оболочку с ограниченным набором команд, но может быть расширен для поддержки других функций и улучшений
