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
6. La migrazione di alcuni tasks può avvenire se e solo se una frazione $`n_b`$ di tutte le CPU sta eseguendo in *HI-crit* mode.
7. Qualora questa frazione $`n_b`$ venisse superata, allora il sistema MCS dovrà abbandonare certe prestabilite attività.
   
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

La **prima** si chiama *period transformation*, ovvero una tecnica che permette di intervallare task di diversa criticità con più frequenza, migliorando, come lui dimostra, la schedulabilità. In breve: se un task $`\tau_j`$ ad alta criticità ha un periodo $`T_j`$ più lungo di un task a bassa criticità $`\tau_i`$, allora $`T_j`$ e $`C_j`$ vengono divisi per un numero intero $`n`$ sufficientemente grande tale che $`T_j \leq T_i`$.

La **seconda**, riguarda l'assegnamento di priorità ai tasks tramita una modifica dell'algoritmo di Audsley. La sua versione originale  è così formulata: 
1. all'inizio, nessun task ha priorità assegnata;
2. le priorità sono assegnata partendo dalla più bassa e terminando con la più alta;
3. ad ogni step, viene selezionato quel task che può essere schedulato con quelli ai quali è già stata assegnata una priorità;

La versione modificata di Vestal S. aggiunge un vincolo alla selezione del task, ovvero di essere quello con il *critical scaling factor* $`\Delta^*`$ più alto.

Il *critical scaling factor* $`\Delta^*`$ è il più grande valore tale per cui tutti i tempi di esecuzione dei task, fino ad ora selezionati, possono essere moltiplicati preservando la loro *feasibility*.

### *Adaptive Mixed Criticality di Baruah, Burns & Davis*
[[Baruah et al., 2011]](https://ieeexplore.ieee.org/document/6121424), sempre in un contesto single-core,  propongono il seguente algoritmo di scheduling run-time:
1. esiste un *criticality level indicator* $`\Gamma`$, inizializzato a $`LO`$;
2. fintantoché $`\Gamma \equiv LO`$, viene selezionato per l'esecuzione il job ready a priorità più alta;
3. se il job che sta eseguendo eccede il suo *LO-criticality WCET*, allora $`\Gamma \leftarrow HI`$;
4. se $`\Gamma \equiv HI`$, allora i jobs con *criticality level* $\equiv LO`$ non possono essere selezionati per l'esecuzione.
5. Quando possibile, ripristinare $`\Gamma \equiv LO`$. Gli autori non argomentano molto questo punto, ma suggeriscono che questo potrebbe avvenire qualora non ci fossero jobs *HI-criticality* pronti per eseguire.

Questo implica il disporre di un *run-time monitoring* che si preoccupa di rilevare se un task eccede il suo *LO-criticality WCET*.

La RTA che propongono si compone di tre distinte fasi:
1. verificare la schedulabilità nel caso che $`\Gamma \equiv LO`$;
2. verificare la schedulabilità nel caso che $`\Gamma \equiv HI`$;
3. verificare la schedulabilità nel momento di transizione dalla modalità $`LO`$ a $`HI`$. Quest'ultimo punto è molto importante, in quanto nel momento in cui $`\Gamma \leftarrow HI`$, i jobs *HI-criticality* potrebbero aver subito, fino a quel momento, interferenza dai jobs *LO-criticality* a priorità più alta.

#### Fase 1: $`\Gamma \equiv LO`$
```math
R_i(LO) = C_i(LO) + \sum_{j \in hp(i)} \lceil R_i(LO)/T_j \rceil  C_j(LO)
```
#### Fase 2: $`\Gamma \equiv HI`$
```math
R_i(HI) = C_i(HI) + \sum_{j \in hpH(i)} \lceil R_i(HI)/T_j \rceil  C_j(HI)
```
#### Fase 3: $`\Gamma \leftarrow HI`$
```math
R_i(HI)^* = C_i(HI) + \sum_{j \in hpH(i)} \lceil R_i(HI)^*/T_j \rceil  C_j(HI) + \sum_{k \in hpL(i)} \lceil R_i(LO)/T_k \rceil  C_k(LO)
```

### *Il problema dell'allocazione di CPUs e assegnamento di priorità ai tasks*
[[Kelly et al., 2011]](https://ieeexplore.ieee.org/abstract/document/6120937) affrontano il problema di:
1. allocare i tasks alle CPUs disponibili;
2. assegnare ai tasks i valori di priorità.

Si spostano quindi in un contesto *multi-core*, analizzando come diversi:
1. ordinamenti dei tasks,
2. metodi di allocazione e 
3. assegnamento di priorità

possano determinare o meno la schedulabilità di un certo taskset.

## **Semi-partitioned model**

Il modello che Xu & Burns propongono, vuole garantire la schedulabilità dell'intero taskset qualora il numero di core in *HI-crit mode* sia al più $`n_b = \lceil log_2(n) \rceil`$, dove $`n`$ è il numero totale dei core. Nel caso di piattaforma dual-core, allora $`n = 2 \implies n_b = 1`$. L'idea fondante che rende questo possibile è il permettere ad alcuni tasks, in caso di necessità, di migrare su di un altro core. Le proprietà di questo modello sono:
1. se tutti i tasks eseguono entro il loro *LO-crit* budget, allora nessun task migra e tutti rispetteranno la propria deadline;
2. a nessun *LO-crit* è concesso eccedere il suo *LO-crit* budget;
3. se un *HI-crit* task eccede il suo *LO-crit* budget e, fino a prima di quel momento, il numero di core in *HI-crit* mode $`n_{HI} < n_b`$, allora alcuni *LO-crit* tasks migreranno, ma l'intero tasket rimane schedulabile;
4. se un *HI-crit* task eccede il suo *LO-crit* budget e, fino a prima di quel momento, il numero di core in *HI-crit* mode $`n_{HI} \geq n_b`$, allora alcuni *LO-crit* tasks saranno abbandonati, ma tutti gli *HI-crit* tasks rimangono schedulabili.

L'algoritmo di scheduling, nel caso di piattaforma dual-core, presenta i seguenti passi:

1. ad ogni core è associato *criticality level indicator* $`\Gamma`$, inizializzato a $`LO`$;
2. fintantoché $`\Gamma \equiv LO`$, viene selezionato per l'esecuzione il task ready a priorità più alta;
3. se un *LO-crit* task eccede il suo *LO-crit* budget, il suo job corrente deve essere terminato;
4. se un *HI-crit* task eccede il suo *LO-crit* budget, allora $`\Gamma \leftarrow HI`$;
5. Se $`\Gamma \equiv HI`$ solo su di un core ($`c_A`$), allora sul core ($`c_B`$) con $`\Gamma \equiv LO`$ vengono spostati alcuni prestabiliti *LO-crit* tasks di $`c_A`$, mentre gli *HI-crit* task sul core $`c_A`$ inizieranno ad eseguire secondo il loro *HI-crit* budget;
6. se $`(\Gamma\_c_A \equiv HI) \wedge (\Gamma\_c_B \leftarrow HI)`$, allora sul core $`c_B`$ vengono abbandonati tutti i *LO-crit* tasks, mentre i suoi *HI-crit* tasks inizieranno ad eseguire secondo il loro *HI-crit* budget.

## **Metodo**

## **Risultati**