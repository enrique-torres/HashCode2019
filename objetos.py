class Photo:
    tags = []
    position = None
    id = None
    n_tags = None

    # Solo para test
    def __str__(self):
        result = str(self.id) + " "
        for tag in self.tags:
            result = result + " " + tag
        return result

    # Pre:  id es entero, position 'V'/'H' y tags una lista
    # Post: genera la foto
    def __init__(self, id, position, tags):
        self.id = id
        self.position = position
        self.tags = tags
        self.n_tags = len(tags)
    
    def get_num_tags(self):
        return self.n_tags

    def get_interest(self, second_photo):
        n_tags_first = len(self.get_num_tags())
        n_tags_second = len(second_photo.get_num_tags())
        n_tags_intersection = len([value for value in self.tags if value in second_photo.tags()])
        return min(n_tags_first, n_tags_second, n_tags_intersection)
    
class Slide:
    photos = []
    # Pre: photos es lista con una o dos fotos
    def __init__(self, photos):
        self.photos = photos

    def __str__(self):
        result = ""
        for photo in self.photos:
            result = result + str(photo.id) + " "
        return result

    def get_tags(self):
        result = []
        for photo in self.photos:
            result = result + photo.tags
        return set(result)

    def get_interest(self, second_slide):
        n_tags_first = len(self.get_tags())
        n_tags_second = len(second_slide.get_tags())
        n_tags_intersection = len([value for value in self.get_tags() if value in second_slide.get_tags()])
        inter = min(n_tags_first-n_tags_intersection, n_tags_second-n_tags_intersection, n_tags_intersection)
        return -1*(inter / max(n_tags_first, n_tags_second))

class Slideshow:
    slides = []

    def __init__(self):
        slides = []
    
    def __str__(self):
        result = str(len(self.slides)) + '\n'
        for slide in self.slides:
            result = result + str(slide) + '\n'
        print(result)
        return result

    def add_slide(self, slide):
        self.slides.append(slide)

    def write_solution(self, file_name):
        output = open(file_name, 'w')
        result = str(len(self.slides)) + '\n'
        for slide in self.slides:
            result = result + str(slide) + '\n'
        output.write(result)
        output.close()

class Input:
    photos = []

    def __init__(self, file_name):
        lines = [line.rstrip('\n') for line in open(file_name)]
        self.photos = []
        id = 0
        for line in lines[1:]:
            elements = line.split(' ')
            self.photos.append(Photo(id, elements[0], elements[2:]))
            id+= 1
        self.photos.sort(key= lambda x: x.get_num_tags(), reverse=True)
    
    def get_photos(self):
        return self.photos