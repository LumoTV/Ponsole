import cmd
import os

class MaConsole(cmd.Cmd):
    prompt = '>> '
    variables = {}  # Simulation de variables
    color_codes = {
        'reset': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    def do_hello(self, args):
        """Affiche un message de salutation."""
        print("Salut !")

    def do_quit(self, args):
        """Quitte la console."""
        print("Au revoir !")
        return True

    def do_add(self, args):
        """Additionne les nombres fournis en arguments."""
        try:
            numbers = [float(arg) for arg in args.split()]
            result = sum(numbers)
            print(f"Résultat de l'addition : {result}")
        except ValueError:
            print("Erreur : veuillez fournir des nombres valides.")

    def do_multiply(self, args):
        """Multiplie les nombres fournis en arguments."""
        try:
            numbers = [float(arg) for arg in args.split()]
            result = 1
            for num in numbers:
                result *= num
            print(f"Résultat de la multiplication : {result}")
        except ValueError:
            print("Erreur : veuillez fournir des nombres valides.")

    def do_echo(self, args):
        """Répète le texte fourni en arguments."""
        print(args)

    def do_del(self, args):
        """Supprime un fichier du système de fichiers."""
        for file_path in args.split():
            try:
                os.remove(file_path)
                print(f"Fichier '{file_path}' supprimé.")
            except FileNotFoundError:
                print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier '{file_path}': {e}")

    def do_dir(self, args):
        """Affiche la liste des fichiers dans le répertoire actuel."""
        try:
            files = os.listdir(os.getcwd())
            print("Fichiers dans le répertoire actuel:", ', '.join(files))
        except Exception as e:
            print(f"Erreur lors de l'affichage des fichiers : {e}")

    def do_color(self, args):
        """Change la couleur du texte dans la console."""
        color = args.lower()
        if color in self.color_codes:
            print(f"{self.color_codes[color]}La couleur a été changée en {color.upper()}{self.color_codes['reset']}")
        else:
            print(f"Erreur : La couleur '{color}' n'est pas prise en charge.")

    def do_duck(self, args):
        """Affiche un canard en ASCII art."""
        duck_art = """
  _
>(.)__
 (___/  
        """
        print(duck_art)

if __name__ == '__main__':
    ma_console = MaConsole()
    ma_console.cmdloop("Bienvenue dans Ponsole.")