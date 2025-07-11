import random

def sort_choices(data, from_name):
    work_lists = {work_name: [] for work_name in data[from_name]["option_name"]}
    worker_dict = {worker_name: 0 for worker_name in data[from_name]["people"]}

    # 👇 修正這行，加上 int() 做型別轉換
    total_work_num = sum(int(v) for v in data[from_name]["option_name"].values())
    total_worker_num = len(data[from_name]["people"])
    round_num = (total_work_num // total_worker_num) + 1

    for i in range(round_num):
        people_names = list(data[from_name]["people"].keys())
        random.shuffle(people_names)

        for name in people_names:
            if worker_dict[name] >= len(data[from_name]["people"][name]):
                continue

            choice_work_name = data[from_name]["people"][name][worker_dict[name]]

            # 如果人數滿了就跳下一個志願
            while int(data[from_name]["option_name"][choice_work_name]) == len(work_lists[choice_work_name]):
                worker_dict[name] += 1
                if worker_dict[name] >= len(data[from_name]["people"][name]):
                    break
                choice_work_name = data[from_name]["people"][name][worker_dict[name]]
            else:
                work_lists[choice_work_name].append(name)
                worker_dict[name] += 1

    return work_lists


       
