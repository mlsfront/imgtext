import os
import cv2
import pytesseract
import logging
import logging.handlers

# Configurar o logging
logging.basicConfig(level=logging.DEBUG)

# Criar um logger
logger = logging.getLogger(__name__)

# Criar um handler para o console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Criar um handler para um arquivo de log
file_handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Adicionar os handlers ao logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def extract_text_from_image(image_path, lang='por'):
    try:
        # Carregar a imagem
        img = cv2.imread(image_pat)

        # Converter para tons de cinza e aplicar limiarização
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Extrair o texto da imagem
        text = pytesseract.image_to_string(thresh, lang=lang)
        return text
    except cv2.error as e:
        logging.error(f"Erro do OpenCV ao processar {image_path}: {e}")
        return None
    except pytesseract.TesseractError as e:
        logging.error(f"Erro do PyTesseract ao processar {image_path}: {e}")
        return None
    except OSError as e:
        logging.error(f"Erro do sistema operacional ao processar {image_path}: {e}")
        return None
    except Exception as e:
        logging.error(f"Erro inesperado ao processar {image_path}: {e}")
        return None

# Criar o diretório de saída, se não existir
if not os.path.exists("output"):
    os.makedirs("output")

# Diretório com as imagens
image_dir = "images"

# Iterar sobre as imagens
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_dir, filename)

        try:
            text = extract_text_from_image(image_path)
            if text:
                with open(f"output/{filename}.txt", "w") as f:
                    f.write(text)
            else:
                print(f"Nenhum texto foi extraído da imagem {filename}")
        except Exception as e:
            print(f"Erro ao processar a imagem {filename}: {e}")

# Exemplo de uso do logger
# logger.debug('Esta é uma mensagem de depuração')
# logger.info('Esta é uma mensagem informativa')
# logger.warning('Esta é uma mensagem de aviso')
# logger.error('Ocorreu um erro!')