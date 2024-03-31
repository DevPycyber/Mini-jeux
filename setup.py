from cx_Freeze import setup, Executable

setup(
    name = "morpion contre une IA niveau 1",
    version = "1.0",
    description = """vous devez aligner 3 pion en ligne colonne ou diagonale\n
    vous avez face à vous une IA qui choisit aléatoirement la position de son pion parmi les cases\n 
    qui ne sont pas prises""",
    executables = [Executable("morpion_niveau1.py")]
)


