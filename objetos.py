class Photo:
    tags = None
    position = None
    id = None

    # Pre:  id es entero, position 'v'/'h' y tags una lista
    # Post: genera la foto
    def __init__(self, id, position, tags):
        self.id = id
        self.position = position
        self.tags = tags
    
    def get_num_tags(self):
        return len(self.tags)
    
class Slide:
    photos = None
    # Pre: photos es lista con una o dos fotos
    def __init__(self, photos):
        self.photos = photos

    def __str__(self):
        result = ""
        for photo in self.photos:
            result = result + str(hotos.id) + " "
        return result

    def get_tags(self):
        result = []
        for photo in self.photos:
            result.append(photo.tags)
        return set(salida)

    def get_interest(self, second_slide):
        n_tags_first = len(self.get_tags())
        n_tags_second = len(second_slide.get_tags())
        n_tags_intersection = len([value for value in self.get_tags() if value in second_slide.get_tags()])
        return min(n_tags_first, n_tags_second, n_tags_intersection)

class Slideshow:
    slides = None

    def __init__(self):
        slides = []
    
    def __str__(self):
        result = str(len(slides)) + '\n'
        for slide in slides:
            result = result + str(slide) + '\n'

    def add_slide(self, slide):
        slides.append(slide)

    def write_solution(self, file_name):
        output = open(file_name, 'w')
        output.write(str(self))
