import random

def sort(data, from_name):
    work_lists = {work_name: [] for work_name in data[from_name]["option_name"]}  # 工作列表的字典
     
    for i in range(data[from_name]["num"]):  # 第i輪
        last_round_fail = []  
        people_names = list(data[from_name]["people"].keys())
        random.shuffle(people_names) # 隨機
        
        for name in last_round_fail:
            people_names.remove(name)  # 移除上一輪失敗的人
        
        random.shuffle(last_round_fail) # 隨機
        people_names = last_round_fail + people_names  # 上一輪失敗的人優先
        
        for name in people_names:
            choice_work_name = data[from_name]["people"][name][i] 
            
            if data[from_name]["option_name"][choice_work_name].value < len(work_lists[choice_work_name]):
                work_lists[choice_work_name].append(name)  # 加入工作列表
            else:
                last_round_fail.append(name) # 加入失敗名單
                
    return work_lists

       
