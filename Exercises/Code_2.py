import wikipedia  # Импортируем модуль wikipedia, который позволяет взаимодействовать с API Wikipedia.


def main():  # Определяем основную функцию программы.
    wikipedia.set_lang("ru")  # Устанавливаем язык Wikipedia на русский, чтобы получать статьи на русском языке.

    query = input(
        "Введите запрос для поиска на Википедии: ")  # Запрашиваем у пользователя ввод запроса для поиска статьи.

    while True:  # Запускаем бесконечный цикл для постоянного взаимодействия с пользователем.
        try:
            page = wikipedia.page(query)  # Пытаемся получить страницу Wikipedia по запросу пользователя.
            # Если страница найдена, выводим заголовок статьи и первые 1000 символов её содержимого.
            print(f"\nСтатья: {page.title}\n\n{page.content[:1000]}...\n")
        except wikipedia.exceptions.DisambiguationError as e:  # Обрабатываем исключение, если найдено несколько вариантов.
            print("Найдено несколько вариантов, выберите один из них:")
            # Выводим первые три варианта на выбор пользователю.
            for option in e.options[:3]:
                print(option)
            query = input("Введите новый запрос: ")  # Запрашиваем новый запрос у пользователя для уточнения.
            continue  # Возвращаемся к началу цикла.
        except Exception as e:  # Обрабатываем любые другие исключения.
            print("Ошибка:", e)  # Выводим сообщение об ошибке.
            break  # Выходим из цикла и завершаем программу.

        # Запрашиваем у пользователя действие, которое он хочет выполнить.
        action = input("Выберите действие:\n1. Листать параграфы\n2. Перейти на связанную страницу\n3. Выйти\n")

        if action == "1":  # Если пользователь выбрал "Листать параграфы".
            # Разбиваем содержание страницы на параграфы по пустым строкам и сохраняем в списке.
            paragraphs = page.content.split("\n\n")
            for i, paragraph in enumerate(paragraphs):  # Итерируем по каждому параграфу.
                # Печатаем номер параграфа и первые 200 символов из него.
                print(f"{i + 1}. {paragraph[:200]}...")
            input("Нажмите Enter для продолжения...")  # Ждем, пока пользователь нажмет Enter, чтобы продолжить.

        elif action == "2":  # Если пользователь выбрал "Перейти на связанную страницу".
            related_query = input("Введите название связанной страницы: ")  # Запрашиваем новое название страницы.
            query = related_query  # Обновляем запрос для использования в следующей итерации.

        elif action == "3":  # Если пользователь выбрал "Выйти".
            print("Выход из программы.")  # Сообщаем, что программа завершает работу.
            break  # Выходим из цикла и завершаем программу.

        else:  # Если пользователь ввел неверный вариант.
            print("Неверный выбор, попробуйте еще раз.")  # Сообщаем о неправильном выборе и продолжаем цикл.

if __name__ == "__main__":  # Проверяем, запускается ли текущий файл как основной модуль программы.
    main()  # Если да, вызываем функцию main(), которая содержит основную логику программы.