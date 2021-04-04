with open("nginx_logs.txt", "r", encoding="utf-8") as file:
    final_list = []
    for line in file:
        ip = line.split(" ")[0]
        act = line.split(" ")[5][1:]
        path = line.split(" ")[6]
        final_list.append((ip, act, path))

    print(final_list)
