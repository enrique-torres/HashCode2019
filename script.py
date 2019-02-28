from objetos import *

def find_worst_vertical(photo_list, candidate):
    length = len(photo_list)
    i = 1
    while length - i >= 0:
        if photo_list[length-i].position == 'V' and candidate != photo_list[length-i]:
            return photo_list[length-i]
        else:
            i = i + 1
    return None

def search(photo_list): 
    output = []
    found_best = False
    current = photo_list[0]
    if current.position == 'V':
        worst = find_worst_vertical(photo_list, current)
        if (worst != None):
            print("Encontrado vertical primero")
            output = output + [Slide([current, worst])]
            print(str(Slide([current, worst])))
            photo_list.remove(worst)
        photo_list.remove(current)
    else:
        print("Encontrado horizontal primero")
        output = output + [Slide([current])]
        print(str(Slide([current])))
        photo_list.remove(current)
    num_photos = len(photo_list)
    while num_photos > 1:
        j = 1
        current_num_tags = current.get_num_tags()
        max_candidate = photo_list[j]
        print("Elementos:" + str(num_photos))
        while not found_best and j < num_photos:
            candidate = photo_list[j]
            if max_candidate.get_interest(current) < candidate.get_interest(current):
                max_candidate = candidate
            #print("Elementos:" + str(j))
            if current_num_tags > candidate.get_num_tags():
                current_num_tags = current_num_tags - 1
            if candidate.get_interest(current) == current_num_tags / 2:
                if candidate.position == 'V':
                    worst = find_worst_vertical(photo_list, candidate)
                    if (worst != None):
                        print("Encontrado vertical")
                        output = output + [Slide([candidate, worst])]
                        photo_list.remove(worst)
                        found_best = True
                        j = 1
                    photo_list.remove(candidate)
                else:
                    print("Encontrado horizontal")
                    found_best = True
                    output = output + [Slide([candidate])]
                    photo_list.remove(candidate)
                    j = 1
            else:
                j = j + 1
        if not found_best:
            if max_candidate.position == 'V':
                worst = find_worst_vertical(photo_list, max_candidate)
                if (worst != None):
                    print("Encontrado vertical maximo")
                    output = output + [Slide([max_candidate, worst])]
                    print(str(Slide([max_candidate, worst])))
                    photo_list.remove(worst)
                photo_list.remove(max_candidate)
            else:
                print("Encontrado horizontal maximo")
                output = output + [Slide([max_candidate])]
                print(str(Slide([max_candidate])))
                photo_list.remove(max_candidate)
                current = max_candidate
        current = candidate
        num_photos = len(photo_list)
        found_best = False
    return output

inputs = Input('b_lovely_landscapes.txt')
slideshow = Slideshow()
#print(inputs.photos)
final = search(inputs.photos)
for slide in final:
    slideshow.add_slide(slide)
slideshow.write_solution('output_b.txt')