#前提：from_YOLO内存有图片
#功能：根据图片信息，从val数据集中，复制原始图片和标签文件到指定目录
import os

def get_file_names(directory, extension):
    """获取指定目录下特定扩展名的文件名列表，并去掉扩展名"""
    try:
        return {file.rsplit('.', 1)[0] for file in os.listdir(directory) if file.endswith(extension)}
    except FileNotFoundError:
        print(f"目录不存在: {directory}")
        return set()

img_path="human_select\\from_YOLO"
val_img_path="data_process\\finded_image"
val_lable_path="data_process\\txt"

place_img_path="human_select\\find_in_val\\imgs"
place_lable_path="human_select\\find_in_val\\lables"

img_names=get_file_names(img_path,".jpg")
val_img_name=get_file_names(val_img_path,".jpg")
val_lable_name=get_file_names(val_lable_path,".txt")

os.makedirs(place_img_path, exist_ok=True)
os.makedirs(place_lable_path, exist_ok=True)

print(f"图片总数: {len(img_names)}")
print(f"val标签文件总数: {len(val_lable_name)}")
#复制
not_found_img=[]
not_found_lable=[]
for name in img_names:
    if name in val_img_name:
        try:
            #复制图片到目录下
            scr_path=os.path.join(val_img_path,f"{name}.jpg")
            dst_path=os.path.join(place_img_path,f"{name}.jpg")
            os.system(f"copy {scr_path} {dst_path}")
        except:
            print(f"复制图片失败: {name}")
    else:
        not_found_img.append(name)
    
    if name in val_lable_name:
        try:
            #复制标签文件到目录下
            scr_path=os.path.join(val_lable_path,f"{name}.txt")
            dst_path=os.path.join(place_lable_path,f"{name}.txt")
            os.system(f"copy {scr_path} {dst_path}")
        except:
            print(f"复制标签文件失败: {name}")
    else:
        not_found_lable.append(name)

print(f"未找到图片: {not_found_img}")
print(f"未找到标签文件: {not_found_lable}")