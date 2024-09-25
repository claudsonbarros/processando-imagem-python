from PIL import Image
import os

class ImageProcessor:
    def __init__(self, image_path):
        """
        Inicializa a classe carregando a imagem do caminho especificado.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Imagem não encontrada no caminho: {image_path}")

        self.image = Image.open(image_path)

    def resize(self, width, height):
        """
        Redimensiona a imagem para a largura e altura especificadas.
        
        Parametros:
        -width: Nova largura da imagem.
        -height: Nova altura da imagem.
        """
        try:
            self.image = self.image.resize((width, height))
        except Exception as e:
            raise ValueError(f"Erro ao redimensionar a imagem: {e}")
        
        return self

    def convert(self, mode):
        """
        Converte a imagem para o modo de cor especificado (ex: 'L' para escala de cinza, 'RGB' para colorido).
        
        Parametros:
        -mode: Modo de cor desejado (ex: 'L', 'RGB').
        """
        try:
            self.image = self.image.convert(mode)
        except ValueError as e:
            raise ValueError(f"Erro ao converter a imagem: {e}")
        
        return self

    def save(self, output_path):
        """
        Salva a imagem processada no caminho especificado.

        -output_path: Caminho completo para salvar a imagem processada.
        """
        try:
            directory = os.path.dirname(output_path)
            if not os.path.exists(directory) and directory != "":
                os.makedirs(directory)
            
            self.image.save(output_path)
            print(f"Imagem salva com sucesso em: {output_path}")
        except Exception as e:
            raise IOError(f"Erro ao salvar a imagem: {e}")

    def show(self):
        """
        Exibe a imagem no visualizador padrão do sistema.
        """
        self.image.show()

