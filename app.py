import csv
import re
from datetime import datetime


def log_progress(message, value):
    """
    Отображает прогресс в консоли.

    Args:
        message: Текст сообщения.
        value: Текущее значение.
    """
    print(f'\r{message}: {value}', end='')


def main():
    # Настройка
    data_file = 'data.csv'
    log_file = 'log.txt'
    regex_pattern = r'\b{}\b'.format('|'.join(['value1', 'value2']))

    # Обработка ошибок
    try:
        with open(data_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

        with open(log_file, 'r') as logfile:
            log_text = logfile.read()
    except FileNotFoundError as e:
        print(f'Ошибка: {e}')
        return

    # Перебор записей
    start_time = datetime.now()
    log_progress('Обработано записей:', 0)
    results = []
    i = 0
    while True:
        try:
            row = next(reader, None)
            if row is None:
                break

            value = row[7]
            match = re.search(regex_pattern, log_text)
            result = 'Да' if match else 'Нет'
            results.append('{} - {}'.format(value, result))
            i += 1
            log_progress('Обработано записей:', i)
        except StopIteration:
            break

    # Вывод информации
    end_time = datetime.now()
    processing_time = end_time - start_time
    print('\n\nОбработка завершена.')
    print(f'Время обработки: {processing_time}')
    print(f'Найдено записей: {len(results)}')

    # Запись результатов
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(results)


if __name__ == '__main__':
    main()
