import subprocess, threading, json
from colorama import Fore, Back, Style, init


class Messenger:
    freinds_id: list

    def terminal(self, command: str) -> subprocess.Popen:
        return subprocess.Popen(command.split(sep=' '),
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         text=True, shell=True)


    def listen(self, port: int):
        return self.terminal(f'ncat -l {port}').communicate()


    def connect(self, ip: str, port: int):
        self.terminal(f'ncat {ip} {port}')


    def check_lib(self):
        pass


    @staticmethod
    def open_friends_id_txt_file() -> list:
        try:
            data = []
            with open('friendsId.txt', 'r', encoding='utf-8') as file:
                for el in file.read().split('\n'):
                    data.append(el)
            return data
        except:
            return []


    @staticmethod
    def write_to_file(filename: str, data: list) -> str:
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for el in data:
                    file.write(el + '\n')
            return f"success to write to {filename}"
        except:
            return f"failed to write to {filename}"


    def test(self):
        in_terminal:str = 'echo Hi Hi!'
        stdout, stderr = self.terminal(in_terminal).communicate()
        print(stdout)


def init_info():
    messanger_commands = {'terminal': 'command: str',
                          'listen': 'port: int',
                          'connect': 'ip: str, port: int',
                          'check_lib': 'pass',
                          'open_friends_id_txt_file': None,
                          'write_to_file': 'filename: str, data: list'}
    out = '\n0 / exit / quit - Close program'
    i=0
    for key, val in messanger_commands.items():
        i+=1
        out += f'\n{i} - {Fore.CYAN}{key} {Style.RESET_ALL}values: '
        if val == 'pass':
            out += Fore.RED + "func don't work" + Style.RESET_ALL
        elif val:
            out += Fore.GREEN + val + Style.RESET_ALL
        else:
            out += Fore.RED + "not arguments" + Style.RESET_ALL
    # abc = (f'\n1 - terminal(command: str)'
    #         f'\n2 - listen(port: int)'
    #         f'\n3 - connect(ip: str, port: int)'
    #         f'\n4 - open_friends_id_txt_file'
    #         f'\n5 - write_to_file(filename: str, data: list)')
    return out


def cycle(is_on,messenger):
    action = input('RO >>>')
    if action == '0' or action == 'quit' or action == 'exit':
        is_on = False
    match action:
        case '1':
            action = action[2::]
            messenger.terminal(action)
        case '2':
            action = action[2::]
            messenger.listen(action)
        case '3':
            action = action[2::].split(sep=' ')
            messenger.connect(action[0], action[1])
        case '4':
            messenger.check_lib()
            print('Поздравляю, ты выиграл 100 тысяч долларов!')
        case '5':
            print('count your friends: ' + messenger.open_friends_id_txt_file().count())
        case '6':
            if action.count() <= 2:
                messenger.write_to_file('friendsId.txt', messenger.friends_id)
            else:
                action = action[2::].split(sep=' ')
                if action.count == 1:
                    messenger.write_to_file(action, messenger.friends_id)
                else:
                    print('неа, не туда целишься')


def start():
    proc = Messenger()
    proc.freinds_id = proc.open_friends_id_txt_file()
    proc.check_lib()

    init(autoreset=True)
    manual = init_info()
    print(manual)
    cycle(is_on=True,messenger=proc)


if __name__ == '__main__':
    start()
