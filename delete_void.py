import os

# 文件夹路径
images_folder = 'images/test'
labels_folder = 'labels/test'

# 获取labels文件夹中所有的.txt文件名（不带扩展名）
label_files = {os.path.splitext(f)[0] for f in os.listdir(labels_folder) if f.endswith('.txt')}

# 遍历images文件夹中的所有图片
for image_file in os.listdir(images_folder):
    if image_file.endswith('.png'):
        # 获取图片文件名（不带扩展名）
        image_name = os.path.splitext(image_file)[0]
        # 检查是否存在对应的.txt文件
        if image_name not in label_files:
            # 删除没有对应.txt文件的图片
            os.remove(os.path.join(images_folder, image_file))
            print(f"Removed {image_file}")

print("Completed!")
