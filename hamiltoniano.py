from objetos import *
import heapq

def join_transitions(list_of_transitions, new_transition):
    if list_of_transitions[0] == new_transition[0]:
        new_transition.reverse()
        return new_transition + list_of_transitions[1:]

    if list_of_transitions[0] == new_transition[-1]:
        return new_transition + list_of_transitions[1:]

    if list_of_transitions[-1] == new_transition[0]:
        return list_of_transitions[:-1] + new_transition

    if list_of_transitions[-1] == new_transition[-1]:
        new_transition.reverse()
        return list_of_transitions[:-1] + new_transition


def join_lists(list_of_lists, transition):
    current_index = -1
    first_join_index = -1
    second_join_index = -1
    for transition_list in list_of_lists:
        current_index = current_index + 1
        if len(set(transition_list[1:-1]).intersection(transition)) != 0:
            return list_of_lists
        head_tile_intersection = len(set([transition_list[0]] + [transition_list[-1]]).intersection(transition))
        
        if head_tile_intersection == 2:
            return list_of_lists
        
        elif head_tile_intersection == 1:
            if first_join_index == -1:
                first_join_index = current_index
            else:
                second_join_index = current_index
                break
    
    if first_join_index == -1 and second_join_index == -1:
        # No se puede unir y añadimos transición
        return list_of_lists + [transition]
    elif second_join_index == -1:
        # Se añade unión simple
        new_list = join_transitions(list_of_lists[first_join_index], transition)
        list_of_lists[first_join_index] = new_list
        return list_of_lists
    else:
        # Se añade unión doble
        new_list = join_transitions(list_of_lists[first_join_index], transition)
        second_new_list = join_transitions(new_list, list_of_lists[second_join_index])
        list_of_lists[second_join_index] = second_new_list
        del list_of_lists[first_join_index]
        return list_of_lists
                      

def organizar_verticales(photo_list):
    slide_list = []
    already_sorted = []
    last_sorted_photo = 0
    last_checked_photo = len(photo_list) - 1
    for photo in photo_list:
        if photo.position == 'V':
            if last_sorted_photo not in already_sorted:
                while last_sorted_photo < last_checked_photo:
                    if photo_list[last_checked_photo].position == 'V' and last_checked_photo not in already_sorted:
                        slide_list.append(Slide([photo, photo_list[last_checked_photo]]))
                        already_sorted.append(last_checked_photo)
                        break
                    else:
                        last_checked_photo = last_checked_photo - 1
        else:
            slide_list.append(Slide([photo]))
        last_sorted_photo = last_sorted_photo + 1
    return slide_list

def generate_best_transitions(slide_list):
    heap = []
    current_slide = 0
    for slide in slide_list:
        current_slide_2 = current_slide + 1
        for slide_2 in slide_list[current_slide + 1:]:
            heapq.heappush(heap, (slide.get_interest(slide_2), [current_slide, current_slide_2]))
            current_slide_2 = current_slide_2 + 1
        current_slide = current_slide + 1
    return heap

def generate_list_of_lists(slide_heap, number_of_slides):
    final_slideshow = [heapq.heappop(slide_heap)[1]]
    i = 0
    while len(heap) > 0 and len(max(final_slideshow,key=len)) < number_of_slides:
        current_transition = heapq.heappop(slide_heap)
        final_slideshow = join_lists(final_slideshow, current_transition[1])
        i = i + 1
        if i%10000 == 0:
            print('Slide nº ' + str(i))
    return max(final_slideshow,key=len)
    

inputs = Input('b_lovely_landscapes.txt')
sorted_slides = organizar_verticales(inputs.get_photos())
heap = generate_best_transitions(sorted_slides)
print("Generado montículo")
final_slideshow = generate_list_of_lists(heap, len(sorted_slides))
print('Max len: ' + str(len(set(final_slideshow))))
s = Slideshow()
for seq in final_slideshow:
    s.add_slide(sorted_slides[seq])
s.write_solution('nuevoB.txt')
