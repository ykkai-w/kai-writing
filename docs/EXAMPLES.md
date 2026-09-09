# 中英文学术写作对照案例

以下为真实稿件的编辑演示。原文仅重排排版，改稿围绕同一组证据调整段落与表达。

## 中文案例

来源论文《基于机器学习的双重动量指数轮动策略——以沪深300与中证1000为例》，第 4.3 节“与基准及基础DMR版本的对比”，表 7 后三段。

### 原文

相较于沪深300基准，DMR-ML策略在收益端实现了119.66%的绝对超额，在风险端将最大回撤从45.60%压缩至12.71%，改善幅度达32.89个百分点。这一结果表明，双重动量机制结合ML风险门禁能够在A股市场获取显著的风险调整超额收益。

相较于基础版DMR策略，DMR-ML在累计收益上提升了49.66个百分点，在最大回撤上改善了6.26个百分点，夏普比率从0.66提升至0.94。这一对比清晰地展示了ML风险门禁模块的增益贡献：通过在高风险时段主动规避市场敞口，策略不仅降低了回撤幅度，还因避开了部分下跌行情而间接提升了累计收益。

ML模块的贡献并非仅仅体现在绝对收益的提升上，更重要的是风险调整效率的改善。夏普比率从0.66提升至0.94，意味着每承担一单位风险所获得的收益补偿提高了42%。对于风险厌恶型投资者而言，这一改善具有实质性的价值。

### 演示改稿

表7以沪深300指数比较策略相对市场的表现，并以不含ML模块的基础版DMR考察风险门禁的增量效果。DMR-ML的累计收益为176.49%，较沪深300的56.83%高119.66个百分点，年化收益分别为15.67%和6.65%；最大回撤幅度则由基准的45.60%降至12.71%，减小32.89个百分点。相较于基础版DMR，加入ML模块后的累计收益由126.84%增至176.49%，提高49.65个百分点，年化收益由12.44%增至15.67%，最大回撤幅度由18.97%降至12.71%，减小6.26个百分点。风险门禁在高风险时段主动规避市场敞口，在控制回撤的同时，避开部分下跌行情也有助于保留累计收益。对风险厌恶型投资者而言，ML模块的收益改善还体现在单位风险的收益补偿上，夏普比率由0.66升至0.94，增幅约42%。

### 主要修改

将连续三段合为一段，按市场基准、基础版 DMR 和风险调整收益展开比较，保留风险门禁的解释。补入同一表 7 的累计收益、年化收益及最大回撤数值，用具体比较替代评价性措辞；按 176.49% − 126.84% 将收益差更正为 49.65 个百分点，并将相对沪深300的累计收益差统一表述为百分点。原文引文保留原数值，供对照辨认。

## English example

Source paper, Forecasting Clean Vehicle Adoption and Market Substitution Dynamics in China's Automotive Transition, Section III.C, “Identification of Substitution Dynamics,” final paragraph on page 5.

### Original

The variance decomposition further reveals that penetration shocks account for 25.2% of the forecast error variance of CFV sales at the 12-period horizon, confirming that penetration is a substantively important, though not the sole, driver of CFV sales dynamics. The VECM error correction coefficient remains significantly negative across lag orders 2 to 5, confirming the stability of the long-run equilibrium result. Taken together, the Granger test establishes unidirectional temporal precedence from penetration to CFV sales, the VECM confirms a stable long-run equilibrium with rapid error correction, and the variance decomposition quantifies the magnitude of this influence. These results provide convergent evidence that the NEV-to-CFV substitution dynamic is not merely a statistical correlation but a directional, self-correcting process.

### Demonstration revision

At the 12-period horizon, NEV penetration shocks account for 25.2% of the forecast error variance of CFV sales. The four-lag Granger test indicates that changes in NEV penetration help predict subsequent changes in log CFV sales, with a Wald statistic of 16.30 and a p-value of 0.003. The reverse test is not significant, with a Wald statistic of 2.78 and a p-value of 0.595. In the VECM, the error correction coefficient in the CFV sales equation is −1.349, with p < 0.001, indicating overcorrection within one period and rapid, oscillatory adjustment toward the long-run equilibrium. The coefficient remains significantly negative across lag orders 2 to 5, so the estimated adjustment pattern persists under these alternative lag specifications.

### Main changes

The paragraph develops the variance decomposition, predictive direction, and equilibrium adjustment in sequence. It incorporates the Granger test statistics and p-values, and the estimated VECM coefficient with its p-value, from the preceding paragraphs of Section III.C. These reported results replace repeated summary claims while retaining the distinction between prediction and causal interpretation.
