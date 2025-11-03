def get_input():
    with open(r"C:\Users\habib\PycharmProjects\Adven_code_practice\2015\Day2\Day2_input.txt") as f:
        dimension=[tuple(map(int,line.strip().split('x'))) for line in f]
        #print("Read dimensions:", dimension)
        return dimension

def calculate_area(l,w,h):
    return 2*(l*w+w*h+h*l)

def calculate_volume(l,w,h):
    return l*w*h

def calculate_exess(l,w,h):
    sort_dimension= sorted([l,w,h])
    return  sort_dimension[0]* sort_dimension[1]

def calculate_length(l,w,h):
    sort_dimension= sorted([l,w,h])
    return  2*(sort_dimension[0]+ sort_dimension[1])



if __name__ == "__main__":
    d=get_input()
    #areas= [ calculate_area(l,w,h)  + calculate_exess(l,w,h) for l,w,h in d  ]
    #print(sum(areas))
    ribb_length=[ calculate_length(l,w,h)  + calculate_volume(l,w,h) for l,w,h in d  ]
    print(sum(ribb_length))

