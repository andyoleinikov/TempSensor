# Скрипт, который получает данные с датчика
# Датчик DS18B20 пишет данные в /sys/bus/w1/devices/28-051673688aff/w1_slave
def get_temp_from_file():
    with open('/sys/bus/w1/devices/28-051673688aff/w1_slave', 'r', encoding='utf-8') as f:
        content = f.read()
        # данные будут иметь такой вид, температура в конце:
        # 30 00 4b 46 ff ff 0f 10 b8 : crc=b8 YES
        # 30 00 4b 46 ff ff 0f 10 b8 t=24567
        # получаю температуру через поиск и преобразую ее в число
        temp = float(content[content.find('t=')+2:])/1000
        return(temp)
if __name__== "__main__":
    temp = get_temp_from_file()
    print(temp)



