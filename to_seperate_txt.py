import os

# 输入和输出目录
input_file = 'all_except_nodata_test.txt'
output_dir = 'test'

# 获取图像尺寸 (假设所有图像尺寸相同，可以从文件中获取实际尺寸)
image_width = 1242  # 根据实际图像尺寸调整
image_height = 375  # 根据实际图像尺寸调整

# 确保输出目录存在

def convert_to_yolo(bbox_left, bbox_top, bbox_right, bbox_bottom):
    # 计算YOLO格式的边界框参数
    x_center = (bbox_left + bbox_right) / 2.0 / image_width
    y_center = (bbox_top + bbox_bottom) / 2.0 / image_height
    bbox_width = (bbox_right - bbox_left) / image_width
    bbox_height = (bbox_bottom - bbox_top) / image_height
    return x_center, y_center, bbox_width, bbox_height

with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()
        
        # 提取图像路径和标注信息
        image_path = parts[0]
        image_name = image_path[-10:-4]

        # 写入YOLO格式的标注文件
        with open(output_dir+"/"+image_name+".txt", 'w') as outfile:  # 使用'a'模式以追加标注到文件中
            
        
            for box in parts[1:]:
                bbox_info = box.split(',')
            
                # 提取边界框和类别ID
                bbox_left = int(bbox_info[0])
                bbox_top = int(bbox_info[1])
                bbox_right = int(bbox_info[2])
                bbox_bottom = int(bbox_info[3])
                class_id = int(bbox_info[4])
                distance = float(bbox_info[5])
            
            

                # 转换为YOLO格式
                x_center, y_center, bbox_width, bbox_height = convert_to_yolo(bbox_left, bbox_top, bbox_right, bbox_bottom)
                outfile.write(f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f} {distance}\n")
        
        outfile.close()
        
