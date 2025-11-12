import os

def create_path(path: str) -> str:
    """
    Функція для побудови абсолютного шляху
    """
    try:
        path_elements_list = path.split("/")
        """
        Зберігаємо параметр path у список, елементи списку відокремлено символом -> /
        """
        
        base_path = os.path.abspath(os.path.join(__file__, "..", ".."))
        """
        Зберігаємо шлях до базової директорії
        """
        
        for element in path_elements_list:
            base_path = os.path.join(base_path, element)
        """
        Зшиваємо шляхи, в один повний абсолютний шлях до нашого файлу
        """
        path_file = os.path.abspath(base_path)
        """
        Зберігаємо нормалізовану абсолютну версію шляху до файлу
        """
        return path_file
        """
        Повертаємо отриманий у результаті виконання функції шлях
        """
    except Exception as error:
        print(f"Помилка під час побудови абсолютного шляху до файлу: {error}")
        """
        Відпрацьовуємо помилки, якщо щось пішло не так
        """