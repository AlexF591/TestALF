import platform
import psutil


def get_system_info():

    system = platform.system()
    architecture = platform.architecture()[0]
    processor = platform.processor()
    ram = psutil.virtual_memory().total / (1024.0 ** 2)

    return {
        "Операционная система": system,
        "Архитектура": architecture,
        "Процессор": processor,
        "Оперативная память (GB)": round(ram, 2)
    }


system_info = get_system_info()
for key, value in system_info.items():
    print(f"{key}: {value}")
