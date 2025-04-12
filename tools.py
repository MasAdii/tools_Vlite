import subprocess
import platform
import os
import sys
import time 


def print_header():
    
    clear_screen()
    
    print(r"""
_____       .___.__  ___________           .__          
  /  _  \    __| _/|__| \__    ___/___   ____ |  |   ______
 /  /_\  \  / __ | |  |   |    | /  _ \ /  _ \|  |  /  ___/
/    |    \/ /_/ | |  |   |    |(  <_> |  <_> )  |__\___ \ 
\____|__  /\____ | |__|   |____| \____/ \____/|____/____  >
        \/      \/                                      \/ 

    """)
    print("=" * 70)
    print("              Ethical Hacking Toolkit Launcher")
    print("                        Versi: 1.1")
    print("=" * 70)
    print(" [!] Penting: Gunakan tool ini secara BERTANGGUNG JAWAB dan LEGAL [!]")
    print(" [!] Hanya gunakan pada sistem yang Anda MILIKI IZIN untuk diuji. [!]")
    print("-" * 70)
    
    time.sleep(1)


def display_information():
    
    clear_screen()
    print("=" * 60)
    print("                  Informasi Toolkit")
    print("=" * 60)
    print("Nama Skrip      : Ethical Hacking Toolkit Launcher")
    print("Versi           : 1.1")
    print("Dibuat oleh     : Adi Tools (berdasarkan permintaan)") 
    print("Bahasa          : Python 3")
    print("-" * 60)
    print("Tujuan          :")
    print("  Skrip ini berfungsi sebagai antarmuka baris perintah (CLI)")
    print("  untuk memudahkan pemanggilan tool ethical hacking populer")
    print("  seperti Nmap, Nikto, SQLMap, Hydra, dan Metasploit.")
    print("  Skrip ini TIDAK membuat ulang fungsionalitas tool tersebut,")
    print("  melainkan hanya menjalankan tool yang sudah terinstal.")
    print("-" * 60)
    print("Prasyarat       :")
    print("  Anda HARUS menginstal tool berikut secara terpisah agar")
    print("  skrip ini berfungsi:")
    print("    * Nmap (nmap.org)")
    print("    * Nikto (cirt.net)")
    print("    * SQLMap (sqlmap.org)")
    print("    * Hydra (github.com/vanhauser-thc/thc-hydra)")
    print("    * Metasploit Framework (metasploit.com)")
    print("  Pastikan tool tersebut dapat diakses dari terminal/command prompt")
    print("  (biasanya berarti mereka ada di PATH sistem Anda).")
    print("-" * 60)
    print("DISCLAIMER PENTING:")
    print("  Pengembang skrip ini TIDAK bertanggung jawab atas penyalahgunaan")
    print("  tool ini. Aktivitas hacking tanpa izin adalah ilegal dan")
    print("  dapat dikenakan sanksi hukum. Gunakan hanya untuk tujuan")
    print("  edukasi atau pengujian penetrasi yang sah dan diizinkan.")
    print("=" * 60)
    input("\nTekan Enter untuk kembali ke menu...")




def clear_screen():
    
    os.system('cls' if platform.system() == "Windows" else 'clear')

def check_tool_installed(tool_name):
    
    print(f"[INFO] Memeriksa keberadaan '{tool_name}'...")
    try:
        if platform.system() == "Windows":
            cmd = ["where", tool_name]
            if tool_name in ["sqlmap", "nikto"]:
                print(f"[WARN] Di Windows, '{tool_name}' mungkin perlu dijalankan via python/perl.")
                print(f"[WARN] Pastikan '{tool_name}' bisa diakses atau sesuaikan skrip.")
        else:
            cmd = ["which", tool_name]

        process = subprocess.run(cmd, capture_output=True, text=True, check=False, encoding='utf-8', errors='ignore')

        if process.returncode == 0 and process.stdout.strip():
            print(f"[ OK ] '{tool_name}' ditemukan.")
            return True
        else:
            
            if platform.system() != "Windows":
                try:
                    cmd_alt = ["command", "-v", tool_name]
                    process_alt = subprocess.run(cmd_alt, capture_output=True, text=True, check=False, encoding='utf-8', errors='ignore')
                    if process_alt.returncode == 0 and process_alt.stdout.strip():
                        print(f"[ OK ] '{tool_name}' ditemukan (via command -v).")
                        return True
                except FileNotFoundError:
                    pass 

            print(f"[FAIL] '{tool_name}' tidak ditemukan di PATH.")
            print(f"[FAIL] Silakan instal '{tool_name}' terlebih dahulu.")
            return False
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan saat memeriksa '{tool_name}': {e}")
        print(f"[WARN] Mungkin '{'where' if platform.system() == 'Windows' else 'which/command'}' tidak tersedia?")
        print(f"[WARN] Atau '{tool_name}' tidak ada di PATH.")
        return False

def run_command(command_list):
    
    print("\n" + "="*20 + " Output Perintah " + "="*20)
    command_str = ' '.join(command_list)
    print(f"[CMD] Menjalankan: {command_str}")
    print("-" * (40 + len(" Output Perintah ")))
    try:
        
        
        process = subprocess.run(command_list, check=False, encoding='utf-8', errors='ignore')
        print("-" * (40 + len(" Output Perintah ")))
        print(f"[INFO] Perintah selesai dengan kode keluar: {process.returncode}")
    except FileNotFoundError:
        print(f"[ERROR] Perintah '{command_list[0]}' tidak ditemukan.")
        print("[ERROR] Pastikan tool sudah terinstal dan ada di PATH sistem.")
    except KeyboardInterrupt:
        print("\n[INFO] Proses dihentikan oleh pengguna (Ctrl+C).")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan saat menjalankan perintah: {e}")
        
        if hasattr(e, 'stderr') and e.stderr:
            print(f"[ERROR Detail] {e.stderr}")
        if hasattr(e, 'stdout') and e.stdout:
            print(f"[ERROR Detail] {e.stdout}")

    print("=" * (40 + len(" Output Perintah ")) + "\n")
    input("Tekan Enter untuk kembali ke menu...")




def run_nmap():
    
    if not check_tool_installed("nmap"):
        input("Tekan Enter untuk kembali...")
        return
    
    print("\n--- Nmap Scan ---")
    target = input("Masukkan Target (IP/Hostname/Range): ")
    if not target:
        print("[ERROR] Target tidak boleh kosong.")
        time.sleep(1)
        return

    print("Pilih jenis scan Nmap:")
    print("  1) Scan Cepat (-F)")
    print("  2) Scan Port Umum & Deteksi Versi (-sV)")
    print("  3) Scan Agresif (-A)")
    print("  4) Scan Semua Port TCP (-p-)")
    print("  5) Scan UDP (membutuhkan root/admin) (-sU)")
    print("  6) Kustom (masukkan argumen sendiri)")
    choice = input("Pilihan (1-6): ")

    cmd = ["nmap"]
    needs_sudo = False

    if choice == '1':
        cmd.extend(["-F", target])
    elif choice == '2':
        cmd.extend(["-sV", target])
    elif choice == '3':
        cmd.extend(["-A", target])
    elif choice == '4':
        cmd.extend(["-p-", target])
    elif choice == '5':
        if platform.system() != "Windows" and os.geteuid() != 0: 
            print("[INFO] Scan UDP biasanya memerlukan hak akses root/sudo.")
            use_sudo = input("Gunakan sudo? (y/n, default n): ").lower()
            if use_sudo == 'y':
                needs_sudo = True
        elif platform.system() == "Windows":
            print("[WARN] Scan UDP di Windows mungkin terbatas/tidak berfungsi seperti di Linux.")
        cmd.extend(["-sU", target])
    elif choice == '6':
        custom_args_str = input("Masukkan argumen Nmap (setelah 'nmap', pisahkan spasi): ")
        custom_args = custom_args_str.split()
        cmd.extend(custom_args)
        
        if target not in custom_args_str:
            cmd.append(target)
        
        if platform.system() != "Windows" and os.geteuid() != 0:
            if any(opt in custom_args for opt in ['-O', '-sS', '-sU']):
                print("[INFO] Opsi yang dipilih mungkin memerlukan hak akses root/sudo.")
                use_sudo = input("Gunakan sudo? (y/n, default n): ").lower()
                if use_sudo == 'y':
                    needs_sudo = True
    else:
        print("[ERROR] Pilihan tidak valid.")
        time.sleep(1)
        return

    
    if needs_sudo:
        
        if check_tool_installed("sudo"):
            cmd.insert(0, "sudo")
        else:
            print("[WARN] Perintah 'sudo' tidak ditemukan. Menjalankan tanpa sudo.")
            print("[WARN] Scan mungkin gagal jika memerlukan hak akses lebih tinggi.")
            time.sleep(2)


    run_command(cmd)


def run_nikto():
    
    tool_name = "nikto"
    tool_cmd_base = []
    nikto_found = False

    
    if check_tool_installed(tool_name):
        tool_cmd_base = [tool_name]
        nikto_found = True
    
    else:
        print(f"[INFO] '{tool_name}' tidak di PATH, mencoba mencari 'nikto.pl'...")
        try:
            
            if platform.system() == "Windows":
                find_cmd = ["where", "nikto.pl"]
            else:
                find_cmd = ["which", "nikto.pl"]
            process = subprocess.run(find_cmd, capture_output=True, text=True, check=False, encoding='utf-8', errors='ignore')

            if process.returncode == 0 and process.stdout.strip():
                nikto_script_path = process.stdout.strip().splitlines()[0] 
                print(f"[ OK ] Menemukan skrip Nikto di: {nikto_script_path}")
                
                perl_executable = "perl"
                if not check_tool_installed("perl"):
                    print("[WARN] 'perl' tidak ditemukan di PATH. Nikto mungkin gagal.")
                    
                tool_cmd_base = [perl_executable, nikto_script_path]
                nikto_found = True
            else:
                print("[FAIL] 'nikto.pl' juga tidak ditemukan via 'which'/'where'.")

        except Exception as e:
            print(f"[ERROR] Gagal mencari nikto.pl: {e}")

    
    if not nikto_found:
        print("[INFO] Tidak dapat menemukan Nikto secara otomatis.")
        use_manual_path = input("Apakah Anda ingin menentukan path manual ke nikto/nikto.pl? (y/n): ").lower()
        if use_manual_path == 'y':
            manual_path = input("Masukkan path lengkap ke 'nikto' atau 'nikto.pl': ").strip()
            if os.path.exists(manual_path):
                if manual_path.endswith("nikto.pl"):
                    perl_executable = input("Masukkan path ke perl.exe (kosongkan jika 'perl' di PATH): ").strip() or "perl"
                    tool_cmd_base = [perl_executable, manual_path]
                else: 
                    tool_cmd_base = [manual_path]
                nikto_found = True
                print("[INFO] Menggunakan path manual.")
            else:
                print(f"[ERROR] Path manual tidak valid: {manual_path}")

    
    if not nikto_found:
        print("[ERROR] Gagal menemukan instalasi Nikto yang bisa dijalankan.")
        print("[ERROR] Pastikan Nikto terinstal dan bisa diakses.")
        input("Tekan Enter untuk kembali...")
        return

    print("\n--- Nikto Web Scanner ---")
    target_url = input("Masukkan Target URL (contoh: http://example.com atau https://example.com:8443): ")
    
    if not target_url.startswith(("http://", "https://")):
        print("[ERROR] URL harus diawali dengan http:// atau https://")
        time.sleep(1)
        return
    
    target_url = target_url.rstrip('/')

    
    cmd = tool_cmd_base + ["-h", target_url]

    
    add_opts_str = input("Tambahkan opsi Nikto lain? (misal: -Tuning x -o output.txt. Kosongkan jika tidak): ")
    if add_opts_str:
        cmd.extend(add_opts_str.split())

    run_command(cmd)


def run_sqlmap():
    
    tool_name = "sqlmap"
    tool_cmd_base = []
    sqlmap_found = False

    
    if check_tool_installed(tool_name):
        tool_cmd_base = [tool_name]
        sqlmap_found = True
    
    else:
        print(f"[INFO] '{tool_name}' tidak di PATH, mencoba mencari 'sqlmap.py'...")
        try:
            if platform.system() == "Windows":
                find_cmd = ["where", "sqlmap.py"]
            else:
                find_cmd = ["which", "sqlmap.py"]
            process = subprocess.run(find_cmd, capture_output=True, text=True, check=False, encoding='utf-8', errors='ignore')

            if process.returncode == 0 and process.stdout.strip():
                sqlmap_script_path = process.stdout.strip().splitlines()[0]
                print(f"[ OK ] Menemukan skrip SQLMap di: {sqlmap_script_path}")
                
                python_executable = "python" 
                if check_tool_installed("python3"):
                    python_executable = "python3"
                elif not check_tool_installed("python"):
                    print("[WARN] 'python' atau 'python3' tidak ditemukan di PATH. SQLMap mungkin gagal.")
                tool_cmd_base = [python_executable, sqlmap_script_path]
                sqlmap_found = True
            else:
                print("[FAIL] 'sqlmap.py' juga tidak ditemukan via 'which'/'where'.")

        except Exception as e:
            print(f"[ERROR] Gagal mencari sqlmap.py: {e}")

    
    if not sqlmap_found:
        print("[INFO] Tidak dapat menemukan SQLMap secara otomatis.")
        use_manual_path = input("Apakah Anda ingin menentukan path manual ke sqlmap/sqlmap.py? (y/n): ").lower()
        if use_manual_path == 'y':
            manual_path = input("Masukkan path lengkap ke 'sqlmap' atau 'sqlmap.py': ").strip()
            if os.path.exists(manual_path):
                if manual_path.endswith("sqlmap.py"):
                    python_executable = input("Masukkan path ke python/python3 (kosongkan jika di PATH): ").strip()
                    if not python_executable:
                        python_executable = "python3" if check_tool_installed("python3") else "python"
                    tool_cmd_base = [python_executable, manual_path]
                else: 
                    tool_cmd_base = [manual_path]
                sqlmap_found = True
                print("[INFO] Menggunakan path manual.")
            else:
                print(f"[ERROR] Path manual tidak valid: {manual_path}")

    if not sqlmap_found:
        print("[ERROR] Gagal menemukan instalasi SQLMap yang bisa dijalankan.")
        print("[ERROR] Pastikan SQLMap terinstal dan bisa diakses.")
        input("Tekan Enter untuk kembali...")
        return

    print("\n--- SQLMap SQL Injection Tool ---")
    target_url = input("Masukkan Target URL dengan parameter (contoh: \"http://test.com/vuln.php?id=1\"): ")
    if not target_url:
        print("[ERROR] URL tidak boleh kosong.")
        time.sleep(1)
        return
    
    if '&' in target_url and not (target_url.startswith('"') and target_url.endswith('"')):
        print("[WARN] URL mengandung '&'. Sebaiknya masukkan URL di dalam tanda kutip (\").")

    print("Pilih mode SQLMap:")
    print("  1) Deteksi Dasar + Banner (--banner --batch)")
    print("  2) Dump Nama Database (--dbs --batch)")
    print("  3) Dump Tabel dari DB tertentu (--dump -D dbname --batch)")
    print("  4) Dump Semua DB (--dump-all --batch) - HATI-HATI! BISA LAMA!")
    print("  5) Kustom (masukkan argumen sendiri)")
    choice = input("Pilihan (1-5): ")

    cmd = tool_cmd_base + ["-u", target_url]

    if choice == '1':
        cmd.extend(["--banner", "--batch"])
    elif choice == '2':
        cmd.extend(["--dbs", "--batch"])
    elif choice == '3':
        db_name = input("Masukkan nama database yang akan di-dump: ")
        if not db_name:
            print("[ERROR] Nama database tidak boleh kosong.")
            time.sleep(1)
            return
        cmd.extend(["-D", db_name, "--dump", "--batch"])
    elif choice == '4':
        confirm = input("[PERINGATAN] Dump semua database bisa memakan waktu sangat lama dan sumber daya. Lanjutkan? (y/n): ").lower()
        if confirm == 'y':
            cmd.extend(["--dump-all", "--batch"])
        else:
            print("[INFO] Operasi dibatalkan.")
            return
    elif choice == '5':
        custom_args_str = input("Masukkan argumen SQLMap (setelah '-u <url>', pisahkan spasi): ")
        cmd.extend(custom_args_str.split())
        
        if "--batch" not in custom_args_str.split() and "-v" not in custom_args_str: 
            add_batch = input("Jalankan dalam mode batch (otomatis)? (y/n, default y): ").lower()
            if add_batch != 'n':
                cmd.append("--batch")
            else:
                print("[INFO] Menjalankan SQLMap dalam mode interaktif.")
    else:
        print("[ERROR] Pilihan tidak valid.")
        time.sleep(1)
        return

    run_command(cmd)


def run_hydra():
    
    if not check_tool_installed("hydra"):
        input("Tekan Enter untuk kembali...")
        return

    print("\n--- Hydra Password Cracker ---")
    target = input("Masukkan Target (IP/Hostname): ")
    service = input("Masukkan Nama Service (ssh, ftp, smb, http-post-form, dll.): ")
    if not target or not service:
        print("[ERROR] Target dan Service tidak boleh kosong.")
        time.sleep(1)
        return

    
    user_arg = []
    while not user_arg:
        user_opt = input("Gunakan satu username (-l) atau file daftar username (-L)? (l/L): ").lower()
        if user_opt == 'l':
            username = input("Masukkan Username: ")
            if username:
                user_arg = ["-l", username]
            else:
                print("[ERROR] Username tidak boleh kosong jika memilih -l.")
        elif user_opt == 'L':
            userlist = input("Masukkan Path ke File Daftar Username: ")
            if os.path.exists(userlist):
                user_arg = ["-L", userlist]
            else:
                print(f"[ERROR] File userlist tidak ditemukan: {userlist}")
        else:
            print("[ERROR] Pilihan username tidak valid (masukkan 'l' atau 'L').")

    
    pass_arg = []
    while not pass_arg:
        pass_opt = input("Gunakan satu password (-p) atau file daftar password (-P)? (p/P): ").lower()
        if pass_opt == 'p':
            password = input("Masukkan Password: ")
            
            pass_arg = ["-p", password]
        elif pass_opt == 'P':
            passlist = input("Masukkan Path ke File Daftar Password: ")
            if os.path.exists(passlist):
                pass_arg = ["-P", passlist]
            else:
                print(f"[ERROR] File passlist tidak ditemukan: {passlist}")
        else:
            print("[ERROR] Pilihan password tidak valid (masukkan 'p' atau 'P').")

    
    extra_opts_str = input("Masukkan opsi Hydra tambahan (misal: -t 4 -V -f. Kosongkan jika tidak): ")
    extra_opts = extra_opts_str.split()

    
    target_full = target 
    if "http-" in service: 
        print(f"[INFO] Untuk service web ({service}), Anda mungkin perlu menentukan path atau detail form.")
        print("       Contoh http-post-form: example.com/login.php:user=^USER^&pass=^PASS^:F=Login Failed")
        print("       Contoh http-get: example.com/admin/")
        target_web_detail = input(f"Masukkan detail path/form untuk target (kosongkan jika hanya hostname/IP): ")
        if target_web_detail:
            
            if ':' in target_web_detail or '/' in target_web_detail: 
                target_full = target_web_detail
            else: 
                target_full = f"{target}/{target_web_detail.lstrip('/')}"
            print(f"[INFO] Menggunakan target Hydra: {target_full}")
        else:
            print(f"[INFO] Menggunakan target dasar: {target}")


    service_args = []

    cmd = ["hydra"] + user_arg + pass_arg + extra_opts + [target_full, service] + service_args
    run_command(cmd)


def run_metasploit():
    
    tool_name = "msfconsole"
    if not check_tool_installed(tool_name):
        
        check_tool_installed("msfdb")
        input("Tekan Enter untuk kembali...")
        return

    print("\n--- Metasploit Framework Console ---")
    print("[INFO] Memulai msfconsole...")
    print("[INFO] Ini mungkin memerlukan waktu (terutama saat pertama kali atau update DB).")
    
    run_msfdb_init = input("Jalankan 'msfdb init' untuk memastikan database siap? (y/n, default n): ").lower()
    if run_msfdb_init == 'y':
        if check_tool_installed("msfdb"):
            print("[INFO] Menjalankan 'msfdb init'...")
            try:
                needs_sudo = False
                if platform.system() != "Windows" and os.geteuid() != 0:
                    print("[WARN] 'msfdb init' mungkin memerlukan sudo.")
                    sudo_ask = input("Gunakan sudo untuk 'msfdb init'? (y/n, default n):").lower()
                    if sudo_ask == 'y': needs_sudo = True

                msfdb_cmd = ["msfdb", "init"]
                if needs_sudo and check_tool_installed("sudo"):
                    msfdb_cmd.insert(0, "sudo")

                subprocess.run(msfdb_cmd, check=True)
                print("[ OK ] 'msfdb init' selesai.")
            except Exception as e:
                print(f"[ERROR] Gagal menjalankan 'msfdb init': {e}")
                print("[WARN] Melanjutkan untuk membuka msfconsole, tapi DB mungkin tidak berfungsi.")
                time.sleep(2)
        else:
            print("[WARN] 'msfdb' tidak ditemukan. Tidak dapat inisialisasi database.")
            time.sleep(1)


    print("[INFO] Meluncurkan console Metasploit. Anda akan berinteraksi di jendela baru/terminal ini.")
    print("[INFO] Ketik 'exit' di dalam msfconsole untuk kembali ke toolkit ini.")

    try:
        print("\n" + "="*20 + " Output Metasploit Console " + "="*20)
        
        process = subprocess.run([tool_name])
        print("\n" + "="*20 + " Metasploit Console Ditutup " + "="*20)
        print(f"[INFO] msfconsole ditutup (Kode keluar: {process.returncode}).")
    except FileNotFoundError:
        print(f"[ERROR] Perintah '{tool_name}' tidak ditemukan.")
        print("[ERROR] Pastikan Metasploit Framework terinstal dan msfconsole ada di PATH.")
    except KeyboardInterrupt:
        print("\n[INFO] Permintaan keluar diterima (mungkin saat msfconsole loading).")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan saat menjalankan msfconsole: {e}")

    input("Tekan Enter untuk kembali ke menu...")




def main_menu():
    
    while True:
        clear_screen() 
        print_header() 
        print(" Menu Utama:")
        print("  1. Nmap       (Network Mapper)")
        print("  2. Nikto      (Web Server Scanner)")
        print("  3. SQLMap     (SQL Injection Tool)")
        print("  4. Hydra      (Password Cracker)")
        print("  5. Metasploit (Framework Console)")
        print("------------------------------------")
        print("  9. Informasi Tool")
        print("  0. Keluar")
        print("=" * 70) 

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            run_nmap()
        elif choice == '2':
            run_nikto()
        elif choice == '3':
            run_sqlmap()
        elif choice == '4':
            run_hydra()
        elif choice == '5':
            run_metasploit()
        elif choice == '9': 
            display_information()
        elif choice == '0':
            print("\nTerima kasih telah menggunakan Adi Tools Toolkit. Keluar...")
            time.sleep(1)
            clear_screen()
            sys.exit(0)
        else:
            print("[ERROR] Pilihan tidak valid, silakan coba lagi.")
            time.sleep(1) 



if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n[INFO] Program dihentikan oleh pengguna (Ctrl+C). Keluar.")
        sys.exit(0)
    except Exception as e:
        
        print("\n[FATAL ERROR] Terjadi kesalahan tak terduga dalam skrip:")
        print(e)
        
        input("Tekan Enter untuk keluar...")
        sys.exit(1)