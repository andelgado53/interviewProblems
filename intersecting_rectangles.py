from pprint import pprint
rectangle1 = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}

rectangle2 = {
    'left_x':  5,
    'bottom_y': 2,
    'width'    : 3,
    'height'   : 6,
}

def get_xs(rectangle):
    x = set()
    for value in range(rectangle['left_x'], rectangle['left_x'] + rectangle['width'] + 1):
        x.add(value)
    return x

def get_ys(rectangle):
    y = set()
    for value in range(rectangle['bottom_y'], rectangle['bottom_y'] + rectangle['height'] + 1):
        y.add(value)
    return y

def find_intersecting(rectangle1, rectangle2):
    pass
    

r1_x = get_xs(rectangle1)
r1_y = get_ys(rectangle1)

r2_x = get_xs(rectangle2)
r2_y = get_ys(rectangle2)

interscecting = {
    'left_x':  None,
    'bottom_y': None,
    'width'    : None,
    'height'   : None,
}

# print(r1_x)
# print(r1_y)
# print(r2_x)
x_inter = r1_x & r2_x
y_inter = r1_y & r2_y
print(y_inter)

interscecting['left_x'] = min(x_inter)
interscecting['width'] = max(x_inter) -  min(x_inter)
interscecting['bottom_y'] = min(y_inter)
interscecting['height'] = max(y_inter) - min(y_inter)

pprint(interscecting)

