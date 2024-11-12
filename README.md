# Projeto: Extração de Texto de Imagens

**Descrição:**

Este projeto Python tem como objetivo extrair texto de imagens utilizando as bibliotecas OpenCV e PyTesseract. O código processa imagens em um diretório especificado, extrai o texto e salva o resultado em arquivos de texto.

**Funcionalidades:**

* **Extração de texto:** Utiliza o PyTesseract para extrair texto de imagens.
* **Pré-processamento de imagens:** Converte imagens para tons de cinza e aplica limiarização para melhorar a extração de texto.
* **Geração de arquivos de texto:** Salva o texto extraído em arquivos de texto individuais.
* **Gerenciamento de erros:** Utiliza o módulo `logging` para registrar erros e informações detalhadas sobre a execução do programa.

**Requisitos:**

* Python (versão 3.6 ou superior)
* Bibliotecas:
  * OpenCV
  * PyTesseract
  * NumPy (dependência do OpenCV)

**Instalação:**

1. **Criar um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate  # Para Windows
   ```
2. **Instalar as dependências:**
   ```bash
   pip install opencv-python pytesseract numpy
   ```
   **Observação:** A instalação do PyTesseract pode exigir a instalação adicional do Tesseract OCR. Consulte a documentação do PyTesseract para mais informações.

**Estrutura do Projeto:**

```
project/
├── images/  # Diretório com as imagens de entrada
├── output/  # Diretório para salvar os arquivos de texto
└── play2.py  # Script principal
```

**Uso:**

1. **Coloque as imagens a serem processadas no diretório `images`.**
2. **Execute o script:**
   ```bash
   python play2.py
   ```

**Configuração do Log:**

* **Nível de log:**
  * **DEBUG:** Detalhes muito detalhados para depuração.
  * **INFO:** Informações gerais sobre a execução do programa.
  * **WARNING:** Condições que podem indicar problemas futuros.
  * **ERROR:** Erros que interrompem a execução normal do programa.
  * **CRITICAL:** Erros críticos que podem levar à falha do sistema.
* **Formato da mensagem:**
  O formato da mensagem pode ser personalizado no início do script para incluir informações como data, hora, módulo, linha do código, etc.

**Personalização:**

* **Linguagem:** Altere o parâmetro `lang` na função `extract_text_from_image` para especificar a linguagem do texto nas imagens.
* **Diretórios:** Modifique os caminhos dos diretórios `image_dir` e `output` para atender às suas necessidades.
* **Pré-processamento:** Experimente diferentes técnicas de pré-processamento de imagens para melhorar a qualidade da extração de texto.
* **Configuração do log:** Ajuste o nível de log e o formato da mensagem para obter informações mais detalhadas ou menos detalhadas sobre a execução do programa.

**Considerações Futuras:**

* **Interface gráfica:** Criar uma interface gráfica para facilitar o uso do programa.
* **Processamento em lote:** Permitir o processamento de múltiplos diretórios de imagens.
* **Integração com outras ferramentas:** Integrar com ferramentas de OCR mais avançadas ou com sistemas de gerenciamento de documentos.

**Contribuições:**

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver alguma sugestão de melhoria, por favor, abra um issue no repositório do projeto.

**Licença:**

Este projeto está licenciado sob a [Licença MIT](LICENSE).
