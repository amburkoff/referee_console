rosrun referee_console referee.py - Запускает судья

rostopic pub /robot_start std_msgs/Empty "{}" - Команда роботу на старт

rostopic pub /robot_finish std_msgs/String "data: 'ITMO'"  - должен отправить робот после того как остановился помле того как переехал черту финиша! 
Указать газвание своей команды!