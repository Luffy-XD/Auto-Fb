import subprocess

def decompile_so_file(input_file, output_file):
    if not input_file.endswith('.so'):
        print("File harus berformat .so.")
        return

    # Menggunakan uncompyle6 untuk mencoba decompile
    try:
        output = subprocess.check_output(['uncompyle6', input_file], universal_newlines=True)
        with open(output_file, 'w') as f:
            f.write(output)
        print(f"File berhasil didecompile dan disimpan sebagai {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Gagal decompile: {e}")

def main():
    while True:
        print("MENU DECOMPILER")
        print("1. Decompile .so file")
        print("2. Exit")
    
        choice = input("Pilih menu (1/2): ")
    
        if choice == '1':
            input_file = input("Masukkan nama file (.so) untuk decompile: ")
            output_file = input("Masukkan nama file keluaran: ")
            decompile_so_file(input_file, output_file)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Input tidak valid, silakan pilih menu 1 atau 2.")

if __name__ == "__main__":
    main()
