import os
import shutil

# extensiones de archivos
TIPOS_ARCHIVOS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".avif", ".webp", ".svg"],
    "documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm"],
    "comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "ejecutables": [".exe", ".msi", ".bat", ".sh", ".app"], 
}


def organizar_archivos(ruta):

    archivos = os.listdir(ruta)

    for archivo in archivos:

        ruta_archivo = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_archivo):

            extension = os.path.splitext(archivo)[1].lower()

            for categoria, extensiones in TIPOS_ARCHIVOS.items():

                if extension in extensiones:

                    carpeta_destino = os.path.join(ruta, categoria)

                    os.makedirs(carpeta_destino, exist_ok=True)

                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

                    print(f"{archivo} movido a {categoria}")


if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpeta = os.path.join(base_dir, "test_folder")

    organizar_archivos(carpeta)