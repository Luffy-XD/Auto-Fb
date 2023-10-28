import ctypes
import os

def main():
    print("MENU DECOMPILER")
    print("1. Decompile .so file")
    print("2. Exit")

    choice = input("Pilih menu (1/2): ")

    if choice == '1':
        file_name = input("Masukkan nama file (.so): ")
        decompile_so_file(file_name)
    elif choice == '2':
        print("Goodbye!")
    else:
        print("Input tidak valid, silakan pilih menu 1 atau 2.")
        main()

def decompile_so_file(file_name):
    if not file_name.endswith('.so'):
        print("File harus berformat .so.")
        return

    if not os.path.exists(file_name):
        print("File tidak ditemukan.")
        return

    lib = ctypes.cdll.LoadLibrary(file_name)
    functions = [f for f in dir(lib) if not f.startswith('__')]

    if not functions:
        print("Tidak ada fungsi yang dapat didecompile.")
        return

    for function in functions:
        print(f"\nFunction: {function}")
        try:
            decompiled_code = disassemble_function(lib, function)
            print(decompiled_code)
        except Exception as e:
            print(f"Error: {e}")

def disassemble_function(lib, function_name):
    function = getattr(lib, function_name)
    return dis.dis(function)

if __name__ == "__main__":
    main()
