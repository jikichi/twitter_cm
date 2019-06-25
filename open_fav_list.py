def open_fav_list():
    with open('fav_list.txt') as f2:
        a = f2.read()
        even_list = a.split(",")
        even_list = filter(lambda a: a != "", even_list)
        new_list = [int(float(x)) for x in even_list]
    return new_list