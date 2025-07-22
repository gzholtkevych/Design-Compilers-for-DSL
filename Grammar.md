----
<font size="+1">Перейти до [[0 Про курс|ЗМІСТУ]]</font>

----
<H1>Породжуюча граматика</H1>

***Породжуюча граматика*** є стандартним інструментом специфікації синтаксису формальної мови.

>[!info] Що таке породжуюча граматика?
> Породжуюча граматика це четвірка $(\Sigma,\Mu,H,\mathcal{P})$, що складається з
> - алфавіту $\Sigma$ ***термінальних символів***;
> - алфавіту $\Mu$ ***нетермінальних символів***;
> - виділеного термінального символу $H\in\Mu$, який називається ***головним***;
> - непорожньої скінченної підмножини $\mathcal{P}\subset((\Sigma\cup\Mu)^\ast\setminus\Sigma^\ast)\times(\Sigma\cup\Mu)^\ast$, елементи якої називають ***синтаксичними правилами***.
> 
> Ця четвірка має задовольняти умові $\Sigma\cap\Mu=\emptyset$.

Граматика $G=(\Sigma,\Mu,H,\mathcal{P})$ визначає відношення $G\models\alpha\rightarrow\beta$ для $\alpha,\beta\in(\Sigma\cup\Mu)^\ast$ у такий спосіб:$$
G\models\alpha\rightarrow\beta\iff\alpha=\gamma_1\alpha_1\gamma_2\land\beta=\gamma_1\beta_1\gamma_2\land(\alpha_1,\beta_1)\in\mathcal{P}.
$$Транзитивне замкнення цього відношення позначається $G\models\alpha\rightarrow^+\beta$, рефлексивно-транзитивне замкнення - $G\models\alpha\rightarrow^*\beta$.

>[!info] Яку мову породжує граматика?
> Породжуюча граматика $G=(\Sigma,\Mu,H,\mathcal{P})$ визначає підмножину$$
L(G)=\{u\in\Sigma^\ast\mid G\models[H]\rightarrow^+u\}\subset\Sigma^\ast,
$$яку називають мовою, що породжується граматикою $G$.

