# Як граматики породжують мови?

%% Insert text %%
## Відношення виведення

Граматика $G=(\Sigma,\Mu,H,\mathcal{P})$ визначає ***відношення виведення*** $G\models\alpha\Rightarrow\beta$
для $\alpha\in(\Sigma\cup\Mu)^\ast\setminus\Sigma^\ast$ та $\beta\in(\Sigma\cup\Mu)^\ast$ у такий спосіб:

 >$G\models\alpha\Rightarrow\beta$, якщо
 >
> - $\alpha\rightarrow\beta\in\mathcal{P}$;
> - $\alpha\rightarrow\gamma\in\mathcal{P}$ та $\gamma\Rightarrow\beta$.

## Мова, яка породжується граматикою

Породжуюча граматика $G=(\Sigma,\Mu,H,\mathcal{P})$ визначає підмножину

>$$L(G)=\{u\in\Sigma^\ast\mid G\models[H]\Rightarrow u\}\subset\Sigma^\ast,$$

яку називають ***мовою, що породжується граматикою $G$***.
