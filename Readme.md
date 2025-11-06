# CSV Reporter

Скрипт для генерации отчётов по CSV-файлам.

## Пример запуска

python main.py --files data/sample.csv --report average-rating
Добавление нового отчёта
Создайте файл в reports/, например average_price.py

Реализуйте функцию generate(data)

Зарегистрируйте отчёт в main.py в словаре REPORTS


## 📄 Пример CSV (data/sample.csv)


name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
ipad air,apple,799,4.7

✅ Как запустить
bash
pip install -r requirements.txt
python main.py --files data/sample.csv --report average-rating
pytest --cov=reports