class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod 
    def print_test():
        print("Prueba de estilos: ")
        print(tcolors.HEADER+"HEADER")
        print(tcolors.FAIL+"FAIL")
        print(tcolors.BOLD+"BOLD")        
        print(tcolors.OKBLUE+"OKBLUE")
        print(tcolors.OKCYAN+"OKCYAN")
        print(tcolors.OKGREEN+"OKGREEN")
        print(tcolors.WARNING+"WARNING")
        print(tcolors.RESET+"RESET")
        input("Presione ENTER para continuar...")
