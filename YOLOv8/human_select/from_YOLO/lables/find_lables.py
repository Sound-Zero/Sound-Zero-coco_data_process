#前提：from_YOLO文件内已存有图片
#功能：根据图片从YOLO.detect()的输出中提取lables文件，并复制到指定目录
import os
def get_file_names(directory, extension):
    """获取指定目录下特定扩展名的文件名列表，并去掉扩展名"""
    try:
        return {file.rsplit('.', 1)[0] for file in os.listdir(directory) if file.endswith(extension)}
    except FileNotFoundError:
        print(f"目录不存在: {directory}")
        return set()


lables_path= "runs\\detect\\predict2\\labels"
img_path="human_select\\from_YOLO"
place_lable_path="human_select\\from_YOLO\\lables"
img_name=get_file_names(img_path,".jpg")
lables_name=get_file_names(lables_path,".txt")

not_find_label=[]
print("图片数量：",len(img_name))
# 确保目标目录存在
os.makedirs(place_lable_path, exist_ok=True)

for name in img_name:
    if name in lables_name:
        # 找到了对应的标签文件
        try:
            #复制标签到目录下
            scr_path=os.path.join(lables_path,f"{name}.txt")
            target_path=os.path.join(place_lable_path,f"{name}.txt")
            os.system(f"copy {scr_path} {target_path}")
        except:
            print(f"复制文件失败: {name}")
    else:
        not_find_label.append(name)

print("未找到标签的图片数量：",len(not_find_label))





