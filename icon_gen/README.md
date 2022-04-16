Script para geração automatica de thumbnails(icones) de vinyl para o NFS World

- Requisitos: Python3, modulo Pillow(PIL) e imagemagick instalado e adicionado ao PATH do Windows
- Ao iniciar o script vai pedir o local da pasta do vinyl, e obviamente voce devera colar/escrever o local
 
- O Padrão da pasta/arquivos do vinyl deve ser:
    - Pasta com nome do vinyl (ex: ADDON_PETRONAS, ADDON_AMG)
    - Dentro da pasta deve ter os layers do vinyl em PNG (ex: petronas_0.png, petronas_1.png/amg_0.png...)
    - O NOME DOS PNGs DEVE CONTER "_0.png, _1.png, _2.png ou _3.png" NO FINAL DO NOME. De acordo com o numero de layers que o vinyl tiver:
      - Vinyl com 1 layer deve ter um arquivo [xxxx_0.png]
      - Vinyl com 2 layers deve ter arquivos os [xxxx_0.png, xxxxx_1.png]
      - Vinyl com 3 layers deve ter arquivos os [xxxx_0.png, xxxxx_1.png, xxxxx_2.png]
      - Vinyl com 4 layers deve ter arquivos os [xxxx_0.png, xxxxx_1.png, xxxxx_2.png, xxxxx_3.png]
      - Por enquanto o script só trabalhar com 4 camadas de imagens
      - Arquivos adicionais fora dos padrões serão ignorados. como um .txt, um .png ou qualquer outra coisa do tipo. caso seja necessario ter um arquivo a mais dentro da pasta do vinyl
- Exemplo de um padrão **VALIDO**:
    
    > **Pasta:** ADDON_PETRONAS / ADDON_PETRONAS_LOGO / ADDON_PETRONAS_VINYL / ADDON_PETRONAS1
    >> **Arquivos:** 
    >> - petronas_0.png, petronas_1.png, petronas_2.png, petronas_3.png
    >> - PETRONAS_0.png, PETRONAS_1.png ....
    >> - vinyl_0.png, vinyl_1.png ....
    >> - petronas_vinyl_0.png .....
    >> - petronas_0.png ....
    >> - aaaaa_0.png .....
    >> - 123456_0.png ....
- Exemplo de um padrão **INVALIDO**:
    > **Pasta:** vinyl petronas / petronas / addon-petronas / addon petronas
    >> **Arquivos:** 
    >> - petronas_1.png, petronas_2.png ... (começando do _1 ao inves do _0)
    >> - petronas 0.png, petronas 1.png ... (espaço no lugar do _)
    >> - petronas0.png, petronas2.png ... (falta do _ antes do numero do layer)
    >> - petronas_00.png ... (dois digitos no numero do layer)
    >> - petronas-0.png ... (- no lugar do _)
    >> - petronas.png ... (ausencia total do _0/_1/_2/_3)
