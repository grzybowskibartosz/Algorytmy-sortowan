import csv
import time

def filtering(file):
    with open(file, 'r', encoding='utf-8', newline='') as input_file, \
            open('Project 1 - filtered data.csv', 'w', encoding='utf-8', newline='') as output_file:

        reader_csv = csv.reader(input_file, delimiter=',')
        writer_csv = csv.writer(output_file, delimiter=',')

        for line in reader_csv:
            if len(line) >= 3 and line[2].strip():
                writer_csv.writerow(line)

        return 'Project 1 - filtered data.csv'

def create_list(file_to_sort):
    with open(file_to_sort, 'r', encoding='utf-8', newline='') as file_to_sort:
        read = csv.reader(file_to_sort, delimiter=',')

        list_of_lines = []
        for line in read:
            list_of_lines.append(line)
        return list_of_lines

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = float(lista[1][2])
        smaller = [element for element in lista[2:] if float(element[2]) < pivot]
        equal = [element for element in lista if float(element[2]) == pivot]
        bigger = [element for element in lista[2:] if float(element[2]) > pivot]
        return quicksort(smaller) + equal + quicksort(bigger)

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half = lista[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if float(left_half[i][2]) < float(right_half[j][2]):
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

    return lista

def bucket_sort(lista, num_of_buckets):
    min_val = 1.0
    max_val = 10.0

    bucket_range = (max_val - min_val + 1) / num_of_buckets

    buckets = [[] for _ in range(num_of_buckets)]

    for val in lista:
        bucket_index = int((float(val[2]) - min_val) // bucket_range)
        buckets[bucket_index].append(val)

    sorted_list = []
    for bucket in buckets:
        sorted_bucket = quicksort(bucket)
        sorted_list += sorted_bucket

    return sorted_list

def save(filename, type_of_sort_data):
    with open(filename, 'w', encoding='utf-8', newline='') as sorted_file:
        writer = csv.writer(sorted_file, delimiter=',')
        for line_of_text in type_of_sort_data:
            writer.writerow(line_of_text)

def create_data_structure(filename, max_data):
    data = []
    with open(filename, 'r', encoding='utf-8') as csv_file:
        read = csv.reader(csv_file, delimiter=',')
        j = 0
        for row in read:
            j = j + 1
            if j > max_data:
                break
            data.append(row)
    return data


input_file_name = 'Project 1 - filtered data.csv'

data_10 = create_data_structure(input_file_name, 10)
data_100 = create_data_structure(input_file_name, 100)
data_1000 = create_data_structure(input_file_name, 1000)
data_10000 = create_data_structure(input_file_name, 10000)
data_100000 = create_data_structure(input_file_name, 100000)
data_200000 = create_data_structure(input_file_name, 200000)
data_300000 = create_data_structure(input_file_name, 300000)
data_all = create_list('Project 1 - filtered data.csv')

i = data_all

# start = time.time()
# filtered_file = filtering(input_file_name)
# end = time.time()
# filtering_time = end - start


start = time.time()
quicksort_data = quicksort(i)
end = time.time()
quicksort_time = (end - start)
save('Project 1 - quicksort data.csv', quicksort_data)

# start = time.time()
# merge_sort_data = merge_sort(i)
# end = time.time()
# merge_sort_time = end - start
# save('Project 1 - merge_sort data.csv', merge_sort_data)
#
# start = time.time()
# bucket_sort_data = bucket_sort(i, 5)
# end = time.time()
# bucket_sort_time = end - start
#
# save('Project 1 - bucket_sort data.csv', bucket_sort_data)


# print(filtering_time)
print(quicksort_time)
# print(merge_sort_time)
# print(bucket_sort_time)


