def upper_work(line):
    """преобразует все символы строки в заглавные буквы"""
    return line.upper()

def upper_first_letter(text):
    """преобразует первые буквы каждого слова в заглавные буквы"""
    list = text.split()
    list_new = []
    for work in list:
        new_work = work.title()
        list_new.append(new_work)
    return (' '.join(list_new))





