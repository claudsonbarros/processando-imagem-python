from image_processing.processor import ImageProcessor
from dotenv import load_dotenv
import os 

def main():
    #Carrega variavei do arquivo .env
    load_dotenv()

    # Caminho da imagem original
    image_path =os.getenv("INPUT_PATH")

    # Criação do processador de imagem
    processor = ImageProcessor(image_path)

    # Processamento: Redimensionar a imagem e convertê-la para escala de cinza
    processor.resize(300, 400).convert('L')

    # Salvar a imagem processada
    output_path = "output/minha_imagem_processada.jpg"
    processor.save(output_path)

    # Exibir a imagem processada (opcional)
    processor.show()

if __name__ == "__main__":
    main()
