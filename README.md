Останавливает все инстансы на ec2

# Как запустить?
1. Клоним 
`git clone git@github.com:Birdi7/terminate-ec2.git`
2. Создаем венв для питона `cd terminate-ec2 && python3 -m venv .venv`
3. Устаналиваем зависимости в венв `.venv/bin/pip3 install -r requirements.txt`
4. Копируем вывод из `$pwd` в первую строку файла [auto_remove_ec2](auto_remove_ec2)
5. Добавляем в запуск по расписанию. Дефолтная конфигурация - запуйскайся в 21:01 каждый день
