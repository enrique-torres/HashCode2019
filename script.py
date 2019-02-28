import importlib

clases = input('objetos.py')
importlib.import_module(clases)

def search(photo_list):
    output = []
    num_photos = len(photo_list)
    found_best = False
    index = 0
    while (index < num_photos):
        current = photo_list[index]
        j = index + 1
        current_num_tags = current.get_num_tags()
        while (not found_best and j < num_photos):
            candidate = photo_list[j]
            if candidate.get_num_tags() == current_num_tags / 2:
                found_best = True
                output = output + []



    return output