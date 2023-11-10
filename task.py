import os
from random import randint


def main():
    dicts = {}
    for i in range(1, 31):
        dicts[str(i)] = {
            "name": i,
            "age": randint(0, 101),
            "num": randint(0, 11),
        }

    task1(dicts)
    print('----------------------------------------------------------------')
    task2(dicts)
    print('----------------------------------------------------------------')
    task3(dicts)
    print(task3(dicts))
    print('----------------------------------------------------------------')
    print(task4())


def task1(dicts):
    # for sub in sorted(dicts): # 这样是按照键的迭代器排序
    for key in sorted(dicts, key=lambda x:dicts[x]['name']):
        val = dicts[key]
        if val['age'] > 50 and val['num'] > 5:
            print(val['name'])


def task2(dicts):
    for key in sorted(dicts, key=lambda x:dicts[x]['name']):
        val = dicts[key]
        if val['age'] < 50 and val['num'] >= 5:
            print(val['name'])


def task3(dicts):
    statistic = [0] * 12
    for key in dicts:
        val = dicts[key]
        id = int(val['age'] / 10)
        statistic[id] += 1

    res = {}
    for i in range(0, 11):
        res['[{}, {}]'.format(str(i * 10), str(i * 10 + 9))] = statistic[i]
    return res


def task4():
    current_working_directory = os.getcwd()
    filename_list = os.listdir('./')
    jpg_filename_list = []
    for filename in filename_list:
        t = filename.split('.')
        if len(t) > 0 and t[-1] == 'jpg' and os.path.isfile(filename):
            tmp = os.path.join(current_working_directory, filename)
            jpg_filename_list.append(os.path.abspath(tmp))
            # jpg_filename_list.append('{}\{}'.format(current_working_directory, filename))
    return jpg_filename_list


if __name__ == '__main__':
    main()