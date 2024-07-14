import random as rd
import numpy as np
boxes = []

# tạo mảng và random ngẫu nhiên 100 array 4 phần tử. 1000x4
for i in range(100):
    boxes.append([i+1, i+1, i+1, i+1])

boxes = np.array(boxes)
# print(boxes)

# slicing lấy tất cả phần tử x nhỏ nhất trong 100 hình chữ nhật và
# cho vào một array.
x0 = boxes[:, 0]

# tương tự cho y nhỏ nhất, (x,y) lớn nhất
y0 = boxes[:, 1]
x1 = boxes[:, 2]
y1 = boxes[:, 3]

# tính các area của 100 hình, lưu vào array.
area = (x1 - x0 + 1)*(y1 - y0 + 1)

# tính tọa độ của những điểm chung A và B (A,B là array)
# lưu ý: x0[0] là điểm target thực tế, đem so sánh nó với từng predict.
# tức là so sánh x0[0] với x0[1], x0[2], x0[3] .... trở đi. sử dụng broadcasting
# như phía dưới. tương tự cho các tọa độ khác
xA = np.maximum(x0[0], x0[1:])
yA = np.maximum(y0[0], y0[1:])
xB = np.minimum(x1[0], x1[1:])
yB = np.minimum(y1[0], y1[1:])

# tính toán giá trị intersect. chú ý fix overfitting bằng maximum và 1.
inter = np.maximum(0, xB - xA + 1) * np.maximum(0, yB - yA + 1)

# trả về list IoU:
iou = inter / (area[0] + area[1:] - inter)

print(iou)
