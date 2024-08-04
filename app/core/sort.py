import random

def sort_choices(data, from_name):
    
    work_lists = {work_name: [] for work_name in data[from_name]["option_name"]}  # 工作名稱列表
    worker_dict = { worker_name: 0 for worker_name in data[from_name]["people"]}  # { 人名: 現在是他的第幾志願-1 }
    
    total_work_num = sum(data[from_name]["option_name"].values())
    total_worker_num = len(data[from_name]["people"])
    round_num = (total_work_num // total_worker_num) + 1
    
    over = False
    
    for i in range(round_num):  #每個人第i個工作
        people_names = list(data[from_name]["people"].keys())
        random.shuffle(people_names) # 隨機
        
        for name in people_names:
            choice_work_name = data[from_name]["people"][name][ worker_dict[name] ]
            
            #while need == have:
            while int(data[from_name]["option_name"][choice_work_name]) == len(work_lists[choice_work_name]):
                worker_dict[name] += 1
                #他排了幾個志願                             @現在在他的第幾個志願
                if len(data[from_name]["people"][name]) < worker_dict[name] + 1 :
                    over = True
                    break
                choice_work_name = data[from_name]["people"][name][ worker_dict[name] ]
            
            if over:
                break
            
            work_lists[choice_work_name].append(name)  
            worker_dict[name] += 1
    
    return work_lists

       
