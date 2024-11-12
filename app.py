import psutil

def cpu_info():
    print(f'CPU usage {psutil.cpu_percent(interval=1, percpu=True)}')
    print(f'Logical CPUs: {psutil.cpu_count(logical=True)}')
    print(f'Physical CPUs: {psutil.cpu_count(logical=False)}')


def memory_usage():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    format = 1024**3 # virtual_memory retorna os valores em bytes, por isso converte-se para GB divindo por 1024**3
    print("\nMemory Info:")
    print(f"Total memory: {memory.total/format:.2f} GB")
    print(f"Used memory: {memory.used/format:.2f} GB")
    print(f"Free memory: {memory.available/format:.2f} GB")
    print(f'Disk usage: {disk.total/format:.2f} GB ')

def process_list():
    print("\nProcess List:")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)

def process_pid(id):
    proc = psutil.Process(id)
    try:
        print(f'\nPID: {proc.pid}')
        print(f'Name: {proc.name()}')
        print(f'Username: {proc.username()}')
        print(f'Status: {proc.status()}')
    except psutil.NoSuchProcess:
        print(f'PID not found {id} \n')

def battery_info():
    battery = psutil.sensors_battery()
    print(f'\nBattery level: {battery.percent}%')
def main():
    while True:

        print("\nSystem menu info:")
        print("1 - CPU Info")
        print("2 - Memory Info")
        print("3 - Process Info")
        print("4 - Process Info by ID (PID")
        print("5 - Battery level")
        print("0 - Leave")

        option = int(input("Choose an operation: "))

        match option:
            case 1:
                cpu_info()
            case 2:
                memory_usage()
            case 3:
                process_list()
            case 4:
                pid = int(input("Insert PID: "))
                process_pid(pid)
            case 5:
                battery_info()
            case _:
                print("Shutting down program...")
                break



if __name__ == "__main__":
    main()