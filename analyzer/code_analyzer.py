file_path = input()
with open(file_path, mode='r') as file:
    for (num, line) in enumerate(file, 1):
        prepared_line = line.strip()
        if len(prepared_line) > 79:
            print(f'Line {num}: S001 Too long line')
