import os
import shutil
from tkinter import Tk, filedialog

# extensiones de archivos
TIPOS_ARCHIVOS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".avif", ".webp", ".svg", ".bmp", ".tiff", ".ico", ".heic",
    ".raw", ".psd", ".ai", ".eps", ".indd", ".dwg", ".dxf", ".dwf", ".jpg", ".jpeg", ".png", ".gif", ".avif", ".webp",
    ".svg", ".bmp", ".tiff", ".ico", ".heic", ".raw",],
    
    "documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".odt", ".ods",
    ".odp", ".rtf", ".csv", ".md", ".xml", ".json", ".yml", ".yaml", ".log", ".ini",
    ".cfg", ".sql", ".psd", ".ai", ".eps", ".indd", ".dwg", ".dxf", ".dwf", ".dwg", ".dxf",
    ".dwf", ".doc", ".xls", ".ppt", ".odt", ".ods", ".odp", ".rtf", ".csv", ".md", ".xml",
    ".json", ".yml", ".yaml", ".log", ".ini", ".cfg", ".sql", ".psd", ".ai", ".eps", ".indd",
    ".dwg", ".dxf", ".dwf", ".html", ".htm", ".xhtml", ".shtml", ".xml", ".rss", ".atom",
    ".svg", ".webp", ".avif", ".heic"],
    
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm", ".mpeg", ".mpg",
    ".wmv", ".m4v", ".3gp", ".vob", ".ogv", ".ts", ".m2ts", ".mkv", ".mp4", ".avi",
    ".mov", ".flv", ".webm"],
    
    "comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso",
    ".dmg", ".cab", ".arj", ".lzh", ".z", ".tar.gz", ".tar.bz2", ".tar.xz"],
    
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".opus", ".wma",
    ".alac", ".aiff", ".pcm", ".dsd", ".dff", ".dsf", ".tak", ".tta", ".wv",
    ".ape", ".mac", ".ofr", ".ofs", ".shn"],
    
    "ejecutables": [".exe", ".msi", ".bat", ".sh", ".app", ".deb", ".rpm", ".apk",
    ".dmg", ".iso", ".bin", ".cmd", ".com", ".cpl", ".gadget", ".inf", ".ins", ".isp",
    ".jse", ".lnk", ".msc", ".msp", ".mst", ".pif", ".reg", ".scr", ".sct", ".vb", ".vbe",
    ".vbs", ".ws", ".wsc", ".wsf", ".wsh", ".xnk", ".xps", ".zip", ".rar", ".7z", ".tar",
    ".gz", ".bz2", ".xz", ".iso", ".dmg", ".cab", ".arj", ".lzh", ".z", ".tar.gz", ".tar.bz2",
    ".tar.xz", ".exe", ".msi", ".bat", ".sh", ".app", ".deb", ".rpm", ".apk", ".dmg", ".iso",
    ".bin", ".cmd", ".com", ".cpl", ".gadget", ".inf", ".ins", ".isp", ".jse", ".lnk",
    ".msc", ".msp", ".mst",], 
}

def seleccionar_carpeta():

    root = Tk()
    root.withdraw()

    carpeta = filedialog.askdirectory(
        title="Selecciona la carpeta que deseas organizar"
    )

    return carpeta

def organizar_archivos(ruta):

    if not os.path.exists(ruta):
        print("Ruta inválida")
        return

    archivos = os.listdir(ruta)

    for archivo in archivos:

        ruta_archivo = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_archivo):

            extension = os.path.splitext(archivo)[1].lower()

            for categoria, extensiones in TIPOS_ARCHIVOS.items():

                if extension in extensiones:

                    carpeta_destino = os.path.join(ruta, categoria)

                    os.makedirs(carpeta_destino, exist_ok=True)

                    shutil.move(
                        ruta_archivo,
                        os.path.join(carpeta_destino, archivo)
                    )

                    print(f"{archivo} → {categoria}")


def main():

    carpeta = seleccionar_carpeta()

    if carpeta:
        print("Carpeta seleccionada:", carpeta)
        organizar_archivos(carpeta)
    else:
        print("No se seleccionó ninguna carpeta.")


if __name__ == "__main__":
    main()