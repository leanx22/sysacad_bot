def get_configs(file_path):
    configs = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                pairs = line.strip().split(';')
                for pair in pairs:
                    if pair:
                        key, value = pair.split('=')
                        configs[key.strip()] = value.strip()
        return configs
    except:
        print("El archivo no existe, creando uno nuevo...")
        with open(file_path, 'w') as file:
            file.write("aggro_level=2;\n"
            "navegador=chrome;\n")
        return get_configs(file_path)

def save_configs(configs, file_path="./src/config.txt"):
    configs_copy = configs.copy()
    try:
        if(configs_copy.get("psw")):
            del configs_copy["psw"]
        with open (file_path, 'w') as file:
            for key, value in configs_copy.items():
                file.write(f"{key}={value};\n")
        return True
    except:
        return False