import os
import shutil
from datetime import datetime

class MiniFileSystem:
    def __init__(self):
        self.current_dir = "/"
        self.files = {}
        self.directories = {"/": {}}
        
    def mkdir(self, dir_name):
        path = os.path.join(self.current_dir, dir_name)
        if path in self.directories:
            print(f"Diretório {path} já existe")
            return False
        
        parent_dir = self.directories
        for part in path.split("/")[1:-1]:
            parent_dir = parent_dir.get("/" + part, {})
        
        parent_dir[path] = {}
        self.directories[path] = {}
        print(f"Diretório {path} criado")
        return True
    
    def cd(self, path):
        if path == "..":
            self.current_dir = os.path.dirname(self.current_dir) or "/"
        elif path.startswith("/"):
            if path in self.directories:
                self.current_dir = path
            else:
                print(f"Diretório {path} não encontrado")
        else:
            new_path = os.path.join(self.current_dir, path)
            if new_path in self.directories:
                self.current_dir = new_path
            else:
                print(f"Diretório {new_path} não encontrado")
    
    def ls(self):
        contents = []
        for d in self.directories[self.current_dir]:
            contents.append(d + "/")
        
        for f in [f for f in self.files if os.path.dirname(f) == self.current_dir]:
            contents.append(os.path.basename(f))
        
        print("\n".join(contents) if contents else "Diretório vazio")
    
    def touch(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        if file_path in self.files:
            print(f"Arquivo {file_path} já existe")
            return False
        
        self.files[file_path] = {
            "content": "",
            "created": datetime.now(),
            "modified": datetime.now(),
            "size": 0
        }
        print(f"Arquivo {file_path} criado")
        return True
    
    def write(self, file_name, content):
        file_path = os.path.join(self.current_dir, file_name)
        if file_path not in self.files:
            self.touch(file_name)
        
        self.files[file_path]["content"] = content
        self.files[file_path]["modified"] = datetime.now()
        self.files[file_path]["size"] = len(content)
        print(f"Conteúdo escrito em {file_path}")
    
    def read(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        if file_path not in self.files:
            print(f"Arquivo {file_path} não encontrado")
            return None
        
        return self.files[file_path]["content"]
    
    def rm(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        if file_path in self.files:
            del self.files[file_path]
            print(f"Arquivo {file_path} removido")
            return True
        else:
            print(f"Arquivo {file_path} não encontrado")
            return False
    
    def mv(self, src, dest):
        # Implementação básica de mover/renomear
        if src in self.files:
            content = self.files[src]["content"]
            self.rm(src)
            self.write(dest, content)
            print(f"Arquivo {src} movido/renomeado para {dest}")
            return True
        else:
            print(f"Arquivo {src} não encontrado")
            return False
    
    def stat(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        if file_path in self.files:
            info = self.files[file_path]
            print(f"Nome: {file_name}")
            print(f"Tamanho: {info['size']} bytes")
            print(f"Criado em: {info['created']}")
            print(f"Modificado em: {info['modified']}")
            return True
        else:
            print(f"Arquivo {file_path} não encontrado")
            return False

# Exemplo de uso
if __name__ == "__main__":
    fs = MiniFileSystem()
    
    print("=== Mini Sistema de Arquivos ===")
    print("Comandos disponíveis: mkdir, cd, ls, touch, write, read, rm, mv, stat, exit")
    
    while True:
        command = input(f"{fs.current_dir} $ ").strip().split()
        if not command:
            continue
        
        cmd = command[0].lower()
        
        try:
            if cmd == "exit":
                break
            elif cmd == "mkdir" and len(command) > 1:
                fs.mkdir(command[1])
            elif cmd == "cd" and len(command) > 1:
                fs.cd(command[1])
            elif cmd == "ls":
                fs.ls()
            elif cmd == "touch" and len(command) > 1:
                fs.touch(command[1])
            elif cmd == "write" and len(command) > 2:
                fs.write(command[1], " ".join(command[2:]))
            elif cmd == "read" and len(command) > 1:
                print(fs.read(command[1]))
            elif cmd == "rm" and len(command) > 1:
                fs.rm(command[1])
            elif cmd == "mv" and len(command) > 2:
                fs.mv(command[1], command[2])
            elif cmd == "stat" and len(command) > 1:
                fs.stat(command[1])
            else:
                print("Comando inválido ou argumentos faltando")
        except Exception as e:
            print(f"Erro: {str(e)}")