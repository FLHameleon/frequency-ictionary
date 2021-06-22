''''''
import re
def shit_faila(filename):
    daniy_text_string = open(filename, mode = 'r').read()
    daniy_text_string = daniy_text_string.lower()# перевод в нижний регистр
    daniy_text_string = re.sub(r'[^\w\s]','',daniy_text_string)#удаление всей пунктуации
    spisok_slov = daniy_text_string.split(' ')# разбиения на список по пробелу
    
    return spisok_slov

def sort_mnog(spisok_slov):
    mnogestvo = set(spisok_slov)# Избавление от повтор слов
    return sorted(mnogestvo)# Сортировка и возращение

def sozd_slovary(mnogestvo, vse_slova):
    slov = list(mnogestvo)#Преобразование из множества в список

    #Заполнение количества встречаний в тексте
    ############################
    kolih_slov = 0
    for _ in range(len(slov)):
        for _2 in range(len(vse_slova)):
            if slov[_] == vse_slova[_2]:
                kolih_slov += 1
        slov[_] = slov[_] + ' ' + str(kolih_slov)
        kolih_slov = 0
    
    return slov

def zapis_v_fail(name_fail, dannie):
    
    with open(name_fail, 'w') as of:
        of.write('{}\n'.format(dannie))
 
    
def hastotniy_slovar():

    name_faila_texta = input("name faila iz english store ")
    name_faila_rezyltata = input("name faila chastotnogo slovary ")
    
    
    rez_shit_spisok_slov = shit_faila(name_faila_texta)# берем английский расказ и преабразуем его в список слов
    
    poly_slovar = sort_mnog(rez_shit_spisok_slov)# в спске избавляемся от повторений и сортируем
    
    polniy_slovar = sozd_slovary(poly_slovar, rez_shit_spisok_slov)# добавляем через пробел количество слов в тексте
    
    zapis_v_fail(name_faila_rezyltata, polniy_slovar)# записыввем результат в текстовый фаил
    
    


if __name__ == "__main__":
    hastotniy_slovar()