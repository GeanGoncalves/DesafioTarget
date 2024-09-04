

# Resolução de Problemas

## 3) Observe o trecho de código abaixo:

```c
int INDICE = 12, SOMA = 0, K = 1;
while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}
printf("%d", SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?

**Resposta:** O valor da variável SOMA será 77.

## 4) Descubra a lógica e complete o próximo elemento:

a) **Sequência:** 1, 3, 5, 7, ___

**Resposta:** A sequência é uma ordem de números ímpares. O próximo termo após 7 é: 9.

b) **Sequência:** 2, 4, 8, 16, 32, 64, ____

**Resposta:** A sequência é uma progressão geométrica onde cada termo é o dobro do termo anterior. O próximo termo após 64 é: 128.

c) **Sequência:** 0, 1, 4, 9, 16, 25, 36, ____

**Resposta:** A sequência é formada pelos quadrados dos números naturais: 0², 1², 2², 3², 4², 5², 6². O próximo termo é: 49.

d) **Sequência:** 4, 16, 36, 64, ____

**Resposta:** A sequência é formada pelos quadrados dos números pares: 2², 4², 6², 8². O próximo termo é: 100.

e) **Sequência:** 1, 1, 2, 3, 5, 8, ____

**Resposta:** A sequência é a sequência de Fibonacci, onde cada termo é a soma dos dois termos anteriores. O próximo termo após 8 é: 13.

f) **Sequência:** 2, 10, 12, 16, 17, 18, 19, ____

**Resposta:** A sequência parece seguir um padrão onde a maioria dos números é consecutiva, mas há alguns números "saltados". Observando o padrão, o próximo número consecutivo após 19 é: 20.

## 5) Identificação dos Interruptores

Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas?

**Resposta:**

**Primeira Ida:**
1. Ligue o primeiro interruptor (Interruptor A) e deixe-o ligado por alguns minutos.
2. Desligue o Interruptor A e imediatamente ligue o segundo interruptor (Interruptor B).
3. Deixe o Interruptor B ligado e vá até as salas das lâmpadas.

**Verificação das Lâmpadas:**
1. Na primeira sala de lâmpada que você verificar, toque na lâmpada:
   - Se a lâmpada estiver acesa, então ela é controlada pelo Interruptor B (aquele que estava ligado quando você entrou na sala).
   - Se a lâmpada estiver apagada, toque nela:
     - Se a lâmpada estiver quente, então ela é controlada pelo Interruptor A (aquele que estava ligado por um tempo antes de ser desligado).
     - Se a lâmpada estiver fria, então ela é controlada pelo Interruptor C (o que nunca foi ligado).
