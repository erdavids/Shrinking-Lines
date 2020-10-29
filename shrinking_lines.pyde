w, h = 1000, 1000

colors = [(188, 216, 193), (214, 219, 178), (227, 217, 133), (229, 122, 68)]
colors = [(219, 177, 188), (211, 196, 227), (143, 149, 211), (137, 218, 255)]
#colors = [(), (), (), ()]
lines = []
line_groups = []

possible_line_length = 130
possible_line_start_diff = 700

base_line_size = 610
base_line_increment = 15
black_outline_size = 10

def get_random_element(l):
    return l[int(random(len(l)))]

def setup():
    size(w, h)
    pixelDensity(2)

    background(*get_random_element(colors))
    number_of_lines = 40
    number_of_groups = 1
    
    for j in range(number_of_groups):
        line_groups.append([])
        for l in range(number_of_lines):
            line_start = [w/2 - random(-possible_line_start_diff, possible_line_start_diff), h/2 - random(-possible_line_start_diff, possible_line_start_diff)]
            line_groups[j].append([line_start[0] - random(-possible_line_length, possible_line_length), line_start[1] - random(-possible_line_length, possible_line_length), line_start[0] - random(-possible_line_length, possible_line_length), line_start[1] - random(-possible_line_length, possible_line_length)])
                     

    current_stroke = base_line_size
    strokeWeight(current_stroke)
    outline = True
    last_color = get_random_element(colors)
    while(current_stroke >= base_line_increment):
        
        for g in range(number_of_groups):
            if (outline == True):
                stroke(0)
            else:
                next_color = get_random_element(colors)
                while(next_color == last_color):
                    next_color = get_random_element(colors)
                stroke(*next_color)
                last_color = next_color
                
            for l in line_groups[g]:
                line(l[0], l[1], l[2], l[3])
        
        if (outline == True):
            current_stroke -= black_outline_size
            outline = False
        else:
            current_stroke -= base_line_increment
            outline = True
        
        strokeWeight(current_stroke)
    
    save("Examples/" + str(int(random(10000))) + ".png")
