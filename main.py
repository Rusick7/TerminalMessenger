import json
import subprocess, threading


def terminal(command: str) -> subprocess.Popen:
    return subprocess.Popen(command.split(sep=' '),
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     text=True, shell=True)


def listen(port: int):
    terminal(f'ncat -l {port}')


def connect(ip: str, port: int):
    terminal(f'ncat {ip} {port}')


def check_lib():
    pass


def open_friends_id_txt_file():
    try:
        data = []
        with open('friendsId.txt', 'r', encoding='utf-8') as file:
            for el in file.read().split('\n'):
                data.append(el)
        return data
    except:
        return []


def write_to_file(filename: str, data: list):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for el in data:
                file.write(el + '\n')
    except:
        return f"failed to write to {filename}"


def start():
    # print('Hi!')
    in_terminal:str = 'echo Hi Hi!'
    stdout, stderr = terminal(in_terminal).communicate()
    print(stdout)
    # friends_data = open_friends_id_txt_file()
    # friends_data.append()
    # write_to_file('friendsId.txt', friends_data)


if __name__ == '__main__':
    start()
