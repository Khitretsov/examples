import xml.etree.ElementTree as ET

path = input('Укажите относительный путь к файлу с расширением "xml" или нажмите "Enter", чтобы использовать файл, имеющийся по умолчанию: ')
path = path if path else 'xml_data.xml'

root = ET.parse(path).getroot()

answer = [0]

def counter(arr, count=0):
    arr = list(arr)
    for item in arr:
        if len(list(item)) == 0:
            answer.append(count + 1)
        else:
            counter(item, count + 1)
            

counter(root)
print(max(answer))

input('Для завершения работы нажмите "Enter"')
