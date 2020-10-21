# Introduzione

I sistemi aderenti al paradigma TSP (*Time and Space Partitioning*), come ad esempio [XtratuM](https://fentiss.com/products/hypervisor/), differiscono profondamente da quelli aderenti al paradigma MCS (Mixed Criticality Systems) nella [versione di Xu e Burns](https://www.sciencedirect.com/science/article/abs/pii/S0164121219300020).

## **TSP**

1. Ogni partizione viene staticamente assegnata ad una CPU.
2. Durante l'esecuzione, una partizione può eseguire solo ed esclusivamente su quella CPU.
3. Ad ogni partizione viene staticamente assegnato un intervallo temporale, che corrisponde al tempo che la partizione ha a disposizione per eseguire sulla CPU.
4. Questo lasso di tempo, è dimensionato al tempo di esecuzione nel caso peggiore di quella partizione.
5. Quando un sovraccarico viene rilevato, esso viene trattato come un guasto grave che porta ad abbandonare certe prestabilite attività.
   
Il punto 4), essendo il caso peggiore un evento con bassa probabilità di occorrenza, porta ad un ingente spreco di risorse (cicli di CPU).

## **MCS secondo Xu & Burns**

1. Ogni task viene staticamente assegnato ad una CPU.
2. Ad ogni task viene staticamente assegnato un *LO-crit* budget, che corrisponde al tempo che un job di un task ha a disposizione per eseguire e completare sulla CPU.
3. Per alcuni tasks (*HI-crit* task) viene staticamente assegnato un *HI-crit* budget, che corrisponde al tempo che un job di un *HI-crit* task ha a disposizione per eseguire e completare sulla CPU in caso sia stato rilevato un sovraccarico.
4. Un sovraccarico si verifica quando un *HI-crit* task eccede il suo *LO-crit* budget. In tal caso, **alcuni** task fra quelli **non** HI-crit vengono migrati su di un'altra CPU, anzichè essere abbandonati.
5. Al verificarsi di un sovraccarico su di una CPU, si dice che essa eseguirà in *HI-crit mode*, per poi tornare ad eseguire in *LO-crit mode* non appena possibile .
6. La migrazione di alcuni tasks può avvenire se e solo se una frazione $`w`$ di tutte le CPU sta eseguendo in *HI-crit* mode.
7. Qualora questa frazione $`w`$ venisse superata, allora il sistema MCS dovrà abbandonare certe prestabilite attività.
   
L'aspettativa è che un sistema MCS possa, grazie al punto 4), reggere più carico utile di un sistema TSP: quando un sistema TSP sceglie di scartare delle attività, un sistema MCS, invece, le sposta su di un'altra CPU (posto che ne esista una disponibile ad accettare nuove attività).

Quello che si vuole e deve fare è:
- realizzare una implementazione del modello MCS Xu & Burns;
- vedere se il carico utile è simile alle predizioni favorevoli del lavoro, [nella versione dual-core](https://dl.acm.org/doi/10.1145/2834848.2834865), di Xu & Burns;
- confrontare le prestazionI con XtratuM.

# Il lavoro di Xu & Burns

## **Lavori precedenti**
### *L'algoritmo di Vestal*
[Vestal S.](https://ieeexplore.ieee.org/document/4408308), nel contesto *single-core*, formula una prima idea che getta le basi per i posteri modelli MCS. L'idea è basata sul fatto che maggiore è il livello di criticità di un task, maggiore sarà il tempo d'esecuzione che viene allocato per quel task.

Con "*maggiore è il livello di criticità di un task*" si intende che:
- una *deadline miss* è sempre meno tollerata;
- c'è bisogno di essere molto sicuri che il tempo d'esecuzione di quel task non superi il tempo per lui allocato.

Vestal S. associa ad ogni task più livelli di criticità e, per ognuno di essi, una quantità temporale da allocare: maggiore è la criticità, maggiore sarà il tempo allocato.

L'equazione che propone per fare RTA è:
```math
R_i = C_i(L_i) + \sum_{j \in hp(i)} \lceil R_i/T_j \rceil  C_j(L_i)
```
Cioè l'interferenza dei tasks a priorità più alta è data dal tempo di esecuzione, di questi tasks, **in funzione** del loro livello di criticità.
Vestal S. chiama questo *multi-criticality analysis*.

Vestal propone altre due cose, che possono essere combinate o usate come alternative reciproce.

La **prima** si chiama *period transformation*, ovvero una tecnica che permette di intervallare task di diversa criticità con più frequenza migliorando, come lui dimostra, la schedulabilità. In breve: se un task $`\tau_j`$ ad alta criticità ha un periodo $`T_j`$ più lungo di un task a bassa criticità $`\tau_i`$, allora $`T_j`$ e $`C_j`$ vengono divisi per un numero intero $`n`$ sufficientemente grande tale che $`T_j \leq T_i`$.

La **seconda**, riguarda l'assegnamento di priorità ai tasks tramita una modifica dell'algoritmo di Audsley. La sua versione originale  è così formulata: 
1. all'inizio, nessun task ha priorità assegnata;
2. le priorità sono assegnata partendo dalla più bassa e terminando con la più alta;
3. ad ogni step, viene selezionato quel task che può essere schedulato con quelli ai quali è già stata assegnata una priorità;

La versione modificata di Vestal S. aggiunge un vincolo alla selezione del task, ovvero di essere quello con il *critical scaling factor* $`\Delta^*`$ più alto.

Il *critical scaling factor* $`\Delta^*`$ è il più grande valore tale per cui tutti i tempi di esecuzione dei task, fino ad ora selezionati, possono essere moltiplicati preservando la loro *feasibility*.

### *RTA per MCS di Baruah, Burns & Davis*

## **Metodo**

## **Risultati**