# DeepLearninCovid_Lucas_Leticia
Repositório do trabalho final da matéria Deep Learning desenvolvido pelos alunos Lucas Lampier e Letícia Araújo

# Relatório do trabalho 
Relatorio_LucasLampier_LeticiaAraujo.pdf

# Codigo do treinamento de cada um dos testes 
- Notebooks/Teste1_VGG_arch.ipynb ---
Treina uma arquitetura baseada na VGG na tarefa de identificar frames de CT contendo infecção por COVID de frames de pulmões saudáis. O arquivo usado para pré-processar está em: Extras/pre_processamento_treino_teste.ipynb. Os resultados não foram bons.

- Notebooks/Teste 2-1 _ Unet_Pulmao_Segmentacao.ipynb---
Treina e uma U-Net para segmentar a região dos pulmões dos frames de CT. As regiõs foram segmentadas manualmente usando o codigo do arquivo  Extras/selecionar_pulmoes.py. Visualmente as regiões do pulmão parecem estar bem segmentadas.
- Notebooks/Teste_2-2_VGG_pulmao_segmentado.ipynb---
Usa a U-Net treinada no Teste 2-1 para eliminar as regiões fora da região do pulmão nos frames da TC. O as imagens do Teste 1 são dadas de entrada na U-Net do teste 2-1 e então o resultadop é usado para treinar uma nova rede baseada na arquitetura VGG. Os resultados continuam aquem do esperado. 
- Notebooks/Teste 3_ Unet_mascaras_covid.ipynb---
O terceiro teste treina uma U-Net para identificar diretamente as regiões do punmões demarcadas como infectadas. As mascaras são as fornecidas pelo dataset Russo [1] (baixado do drive disponibilizado na disciplina). Este teste foi ben sucedido, atingindo uma acurácia superior a 80%.

# Exemplo de utilização da rede treinada
- Notebooks/exemplo_de_utilização_da_rede_final.ipynb---Notebook exemplificando como carregar e utilizar a rede para classificar os frames como frames infectados por covid ou frames "saudáveis". E demarcando a região infectada.

![alt text](https://github.com/lucaslampier/DeepLearninCovid_Lucas_Leticia/blob/main/resultado1.PNG?raw=true)
![alt text](https://github.com/lucaslampier/DeepLearninCovid_Lucas_Leticia/blob/main/resultado2.PNG?raw=true)

# Usabilidade 
Bastra trocar os caminhos dos arquivos de dados e/ ou modelos salvos nos notebooks e rodar:
![alt text](https://github.com/lucaslampier/DeepLearninCovid_Lucas_Leticia/blob/main/caminho.PNG?raw=true)

# Codigo para segmentar a ROI dos pulmões
- Notebooks/selecionar_pulmoes.py

# Visualização da Tomografia Computadorizada.
- Notebooks/Animacao.ipynb

# Arquiteturas salvas em:
saved_DNNs

Link do drive para baixar os dados:
- dados originais: https://drive.google.com/drive/folders/1igi7O3hJe-FOuTqw9CaW0mP0okbK2pLr?usp=sharing
- dados pré-processados: https://drive.google.com/drive/folders/16os2n2rj33GJdK0LJ1zJGY4b2tf2wWC6?usp=sharing

- Referência dos dados: 

[1] MOROZOV, S. P. et al. Mosmeddata: Chest ct scans with covid-19 related findings dataset. arXiv preprint arXiv:2005.06465, 2020.
