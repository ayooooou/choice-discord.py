import random

def sort_choices(data, from_name):
    last_round_fail = []
    work_lists = {work_name: [] for work_name in data[from_name]["option_name"]}  # 工作名稱列表
    worker_dict = { worker_name: 0 for worker_name in data[from_name]["people"]}  # 人名列表
    for round in range(data[from_name]["option_num"]):  # 第i輪
        people_names = list(data[from_name]["people"].keys())
        random.shuffle(people_names) # 隨機
        
        # 上一輪沒選到的人優先
        for name in last_round_fail:  
            people_names.remove(name)
        random.shuffle(last_round_fail)
        people_names = last_round_fail  + people_names 
        last_round_fail = []
        
        for name in people_names:
            choice_work_name = data[from_name]["people"][name][round] 
            
            if int(data[from_name]["option_name"][choice_work_name]) > len(work_lists[choice_work_name]):
                work_lists[choice_work_name].append(name)  # 加入工作列表
                worker_dict[name] += 1
            else:
                last_round_fail.append(name) # 加入落選列表
    print(worker_dict)
    return work_lists

       
