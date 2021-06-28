# DeepLearninCovid_Lucas_Leticia
Repositório do trabalho final da matéria Deep Learning desenvolvido pelos alunos Lucas Lampier e Letícia Araújo

# Relatório do trabalho 
Relatorio_LucasLampier_LeticiaAraujo.pdf

# Codigo do treinamento de cada um dos testes 
- Notebooks/Teste1_VGG_arch.ipynb ---
Treina uma arquitetura baseada na VGG na tarefa de identificar frames de CT contendo infecção por COVID de frames de pulmões saudáis. O arquivo usado para pré-processar está em: Extras/pre_processamento_treino_teste.ipynb. Os resultados não foram bons.

- Notebooks/Teste 2-1 _ Unet_Pulmao_Segmentacao.ipynb---
Treina e uma U-Net para segmentar a região dos pulmões dos frames de CT. As regiõs foram  
- Notebooks/Teste_2-2_VGG_pulmao_segmentado.ipynb
- Notebooks/Teste 3_ Unet_mascaras_covid.ipynb

# Exemplo de utilização da rede treinada
- Notebooks/

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
MOROZOV, S. P. et al. Mosmeddata: Chest ct scans with covid-19 related findings dataset. arXiv preprint arXiv:2005.06465, 2020.
