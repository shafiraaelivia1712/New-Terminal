import os
import sys
import time
import random
import subprocess

# Kode ANSI untuk warna terminal
HIJAU = "\033[1;32m"
RESET = "\033[0m"

def cetak_pelan(teks, jeda=0.03):
    """Menampilkan teks seperti diketik oleh mesin tik"""
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(jeda)
    print()

def efek_matrix():
    """Menampilkan animasi teks jatuh secara acak"""
    karakter = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
    print(HIJAU)
    try:
        # Menampilkan 50 baris karakter acak
        for _ in range(50):
            baris = "".join(random.choice(karakter) if random.randint(0, 4) > 1 else " " for _ in range(80))
            print(baris)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass # Hentikan animasi jika user menekan Ctrl+C
    print(RESET)

def simulasi_scan():
    """Menampilkan teks palsu seolah sedang memindai jaringan"""
    cetak_pelan(f"{HIJAU}[*] Memulai bypass firewall target...{RESET}")
    time.sleep(1)
    for i in range(1, 4):
        cetak_pelan(f"{HIJAU}[+] Menemukan kerentanan pada port 192.168.1.{10 + i}... [BERHASIL]{RESET}", 0.02)
        time.sleep(0.5)
    cetak_pelan(f"{HIJAU}[!] Koneksi terenkripsi terjalin. Mengamankan log...{RESET}")

def jalankan_hacker_shell():
    # Membersihkan layar saat pertama kali dibuka
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{HIJAU}=======================================")
    print("      SYSTEM BREACHED - ROOT OK        ")
    print(f"======================================={RESET}")
    cetak_pelan(f"{HIJAU}Selamat datang di HackNet v2.0. Ketik 'help' untuk daftar perintah.{RESET}")

    while True:
        cwd = os.getcwd()
        try:
            # Tampilan prompt kustom
            user_input = input(f"\n{HIJAU}root@hacknet:{cwd} # {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{HIJAU}Menghapus jejak... Disconnected.{RESET}")
            break

        if not user_input:
            continue

        args = user_input.split()
        command = args[0].lower()

        # 1. PERINTAH KUSTOM (ELEMEN HACKER)
        if command in ["exit", "keluar"]:
            cetak_pelan(f"{HIJAU}Memutuskan koneksi dan menghapus log...{RESET}")
            break
        elif command == "help":
            cetak_pelan(f"{HIJAU}Perintah internal: help, clear, matrix, scan{RESET}")
            cetak_pelan(f"{HIJAU}Perintah sistem  : cd, ping, dir/ls, dll (tergantung OS){RESET}")
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command == "matrix":
            efek_matrix()
        elif command == "scan":
            simulasi_scan()
        
        # 2. PERINTAH SISTEM ASLI
        elif command == "cd":
            try:
                if len(args) > 1:
                    os.chdir(args[1])
                else:
                    os.chdir(os.path.expanduser("~"))
            except Exception as e:
                print(f"{HIJAU}[ERROR] {e}{RESET}")
        else:
            # Eksekusi perintah komputer asli dengan balutan warna hijau
            try:
                print(HIJAU, end="") # Warnai output sistem jadi hijau
                subprocess.run(args)
                print(RESET, end="")
            except FileNotFoundError:
                print(f"{HIJAU}[!] Perintah '{command}' tidak ditemukan.{RESET}")
            except Exception as e:
                print(f"{HIJAU}[!] Gagal mengeksekusi: {e}{RESET}")

if __name__ == "__main__":
    jalankan_hacker_shell()