keys_list, total_h = [], []
with open("text_6.txt", encoding="UTF-8") as schedule:
    for items in schedule:
        keys_list.append(items.split()[0][:len(items.split()[0]) - 1])
        count = 0
        for i in items.split():
            if i.endswith('(л)'):
                count += int(i.replace('(л)', ''))
            elif i.endswith('(пр)'):
                count += int(i.replace('(пр)', ''))
            elif i.endswith('(лаб)'):
                count += int(i.replace('(лаб)', ''))
            else:
                continue
        total_h.append(count)
    lessons_dict = dict(zip(keys_list, total_h))

print(lessons_dict)