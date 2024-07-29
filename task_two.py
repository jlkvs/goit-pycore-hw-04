def get_cats_info(path):
    cats_info = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line: 
                id_, name, age = line.split(',')
                cat = {
                "id": id_, "name": name, "age": age
                }
                cats_info.append(cat)
    return cats_info

cats_info = get_cats_info("/Users/julia/goit-pycore-hw-04/cats_file.txt")
print(cats_info)


