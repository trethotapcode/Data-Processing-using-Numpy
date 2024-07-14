# IoU / Insection over Union in Computer Vision.

def iou(box1, box2):
    '''
    box 1, box2 is output and reality of detection image.
    box 1 has coordinates (x1, y1, x2, y2)
    box 2 same.
    '''

    # call variables

    x_a_min = box1[0]
    y_a_min = box1[1]
    x_a_max = box1[2]
    y_a_max = box1[3]

    x_b_min = box2[0]
    y_b_min = box2[1]
    x_b_max = box2[2]
    y_b_max = box2[3]

    # insection has coordinates (x0, y0, xi, yi)
    # insection has min of max dot, max of min dot.
    # x, y min
    x0 = max(x_a_min, x_b_min)
    y0 = max(y_a_min, y_b_min)

    # x, y max
    xi = min(x_a_max, x_b_max)
    yi = min(y_a_max, y_b_max)

    # calculate area of insection.
    width = xi - x0
    height = yi - y0

    area_insection = width*height

    # calculate area of Union: A + B - insection
    area_a = (x_a_max - x_a_min)*(y_a_max - y_a_min)
    area_b = (x_b_max - x_b_min)*(y_b_max - y_b_min)

    union = area_a + area_b - area_insection

    # calculate IoU of image:
    iou = area_insection/union
    return iou

box1 = (21, 11, 14, 13)
box2 = (23, 12, 13, 14) 
print("iou = " + str(iou(box1, box2)))