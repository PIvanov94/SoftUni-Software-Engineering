import os


def get_files_extensions(files):
    files_info = {}
    for file in files:
        file_name, file_extension = file.split(".")
        if file_extension not in files_info:
            files_info[file_extension] = []
        files_info[file_extension].append(file_name)
    return files_info


files_in_directory = [file for file in os.listdir() if os.path.isfile(file)]
group_files = get_files_extensions(files_in_directory)
result_in_string = ""
for files_extensions, files_names in sorted(group_files.items(), key=lambda x: x[0]):
    result_in_string += f".{files_extensions}\n"
    for names in files_names:
        result_in_string += f"- - - {names}.{files_extensions}\n"
    # print(*[f"- - - {name}.{files_extensions}" for name in files_names], sep="\n")

with open("C:\\Users\\User\\Desktop\\my_first_report.txt", "w") as file:
    file.write(result_in_string)