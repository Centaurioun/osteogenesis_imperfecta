# Questions to NBLM for Methods

**Question 1:**

In small-sample biomedical studies with sparse expected cell counts in categorical comparisons, what is the strongest literature-supported rationale for supplementing Pearson chi-square analyses with permutation-based or exact-style inference rather than relying only on asymptotic chi-square p values? Please keep the answer short, manuscript-usable, and limited to rationale-level support. Use APA 7 style and list the used references at the end.

**Answer 1:**

In small-sample clinical cohorts where contingency tables contain sparse expected cell counts (typically less than 5), traditional Pearson chi-square analyses can be statistically unreliable because they depend heavily on large-sample asymptotic theory. To overcome this limitation, the literature strongly supports utilizing exact-style inferences, such as Fisher's exact test or permutation-based methods, which calculate statistical significance directly rather than relying on assumed or unknown continuous distributions. This nonparametric approach avoids the mathematical pitfalls of large-sample approximations, yielding a more robust and statistically powerful evaluation of categorical dependencies in rare disease populations.

**References**

*   Bodian, D. L., Madhan, B., Brodsky, B., & Klein, T. E. (2008). Predicting the clinical lethality of osteogenesis imperfecta from collagen glycine mutations. *Biochemistry*, *47*(19), 5424–5432.
*   Hartikka, H., Kuurila, K., Korkko, J., Kaitila, I., Grenman, R., Pynnonen, S., Hyland, J. C., & Ala-Kokko, L. (2004). Lack of correlation between the type of COL1A1 or COL1A2 mutation and hearing loss in osteogenesis imperfecta patients. *Human Mutation*, *24*, 147–154.
*   Lindahl, K., Åström, E., Rubin, C. J., Grigelioniene, G., Malmgren, B., Ljunggren, Ö., & Kindmark, A. (2015). Genetic epidemiology, prevalence, and genotype-phenotype correlations in the Swedish population with osteogenesis imperfecta. *European Journal of Human Genetics*, *23*(8), 1042–1050.

**Answer 2:**

In categorical data analysis involving small sample sizes and sparse expected cell counts, relying solely on the traditional asymptotic Pearson chi-square test is methodologically limited because the test fundamentally relies on large sample theory (Hartikka et al., 2004). To overcome this limitation, the literature strongly supports utilizing exact-style inference, such as Fisher's exact test, for evaluating contingency tables in rare disease cohorts (Hartikka et al., 2004; Li et al., 2019). The primary rationale for this methodological substitution is that exact procedures do not depend on large-sample asymptotic approximations, making them more statistically robust, valid, and potentially more powerful for detecting true dependencies within restricted sample sizes (Hartikka et al., 2004).

### References

Hartikka, H., Kuurila, K., & Körkkö, J. (2004). Lack of correlation between the type of *COL1A1* or *COL1A2* mutation and hearing loss in osteogenesis imperfecta patients. *Human Mutation*, *24*(2), 147–154. https://doi.org/10.1002/humu.20071

Li, L., Mao, B., Li, S., Xiao, J., Wang, H., Zhang, J., Ren, X., Wang, Y., Wu, Y., Cao, Y., Lu, C., Gao, J., You, Y., Zhao, F., Geng, X., Xiao, Y., Jiang, C., Ye, Y., Yang, T., Zhao, X., & Zhang, X. (2019). Genotypic and phenotypic characterization of Chinese patients with osteogenesis imperfecta. *Human Mutation*, *40*(5), 588–600. https://doi.org/10.1002/humu.23718

**Answer 3:**

In small-sample biomedical studies, particularly those investigating rare diseases, the cross-tabulation of categorical variables frequently yields sparse data that violate the fundamental expected cell count assumptions of the standard asymptotic Pearson chi-square test (Defabianis et al., 2024); (Fernandes et al., 2020). To prevent biased $p$-values and invalid statistical inference when these assumptions are unmet—specifically when expected cell counts fall below required minimums or when more than 20% of cells lack the expected frequencies—it is methodologically necessary to utilize exact-style inference methods, such as Fisher's exact test (Demir et al., 2025); (Fernandes et al., 2020). Supplementing analyses with exact mathematical evaluations ensures robust and reliable significance testing for categorical relationships in cohorts limited by small sample sizes (Maioli et al., 2019).

### References

*   **Defabianis, P., Bello, L., & Romano, F.** (2024). Impaired salivary gland function in children with osteogenesis imperfecta: a case-control study. *Clinical Oral Investigations*, 28(5), 308.
*   **Demir, K., Güleç, Ç., Aslanger, A., Öztürk, A. P., Özsait Selçuk, B., Tuna İnce, E. B., & Toksoy, G.** (2025). Investigation of oral health findings and genotype correlations in osteogenesis imperfecta. *Odontology*, 113(3), 1239–1252.
*   **Fernandes, A. M., Rocha-Braz, M. G. M., Franca, M. M., Lerario, A. M., Simões, V. R. F., Zanardo, E. A., ... & Ferraz-de-Souza, B.** (2020). The molecular landscape of osteogenesis imperfecta in a Brazilian tertiary service cohort. *Osteoporosis International*, 31(7), 1341–1352.
*   **Maioli, M., Gnoli, M., Boarini, M., Tremosini, M., Zambrano, A., Pedrini, E., ... & Sangiorgi, L.** (2019). Genotype-phenotype correlation study in 364 osteogenesis imperfecta Italian patients. *European Journal of Human Genetics*, 27(7), 1090–1100.

**Question 2:**

What is the strongest concise literature-supported rationale for reporting an effect-size measure such as Cramer's V together with p values in small-sample categorical analyses? Please focus on why this improves interpretation when significance testing may be unstable or sample-size dependent. Use APA 7 style and list the used references at the end.

**Answer 1:**

In small-sample clinical studies—particularly those involving rare diseases like osteogenesis imperfecta—inherently restricted cohort sizes severely limit statistical power, making $p$-values highly unstable and prone to masking meaningful biological relationships (Arponen et al., 2015). Because traditional significance testing is heavily dependent on sample size, relying solely on $p$-values can lead to misinterpretation of categorical data. To overcome this limitation, methodological guidelines dictate that significance tests must be supplemented with appropriate effect size measures, such as odds ratios or other applicable magnitude indices like Cramer's V (Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3, n.d.).

Reporting effect sizes alongside $p$-values improves data interpretation because it quantifies the actual strength of the association, allowing researchers to accurately evaluate the *clinical significance* of the findings independently of the statistical fluctuations and power deficits caused by small patient populations (Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3, n.d.).

### References

*   Arponen, H., Vuorimies, I., Valta, H., Waltimo-Sirén, J., & Mäkitie, O. (2015). Cranial base pathology in pediatric osteogenesis imperfecta patients treated with bisphosphonates. *Journal of Neurosurgery: Pediatrics*, 15(6), 603-610.
*   Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3. (n.d.). [Unpublished manuscript/Internal Document].

**Answer 2:**

In rare disease research characterized by inherently limited sample sizes, relying exclusively on *p*-values is methodologically hazardous because statistical significance is heavily dependent on cohort size, which limits the power of statistical inference and increases the risk of unstable or false-negative conclusions (Billingham et al., 2012; Hartikka et al., 2004; Mitani & Haneuse, 2020). Supplementing traditional significance testing with an effect-size measure—such as Cramer's V for categorical data, odds ratios, or Cohen's *d*—provides a standardized, sample-size-independent metric to quantify the actual magnitude of the observed association. This dual-reporting approach crucially improves data interpretation by allowing researchers to explicitly evaluate the clinical significance and practical importance of the findings, ensuring that potentially meaningful phenotypic patterns are not prematurely dismissed simply because a restricted patient sample failed to achieve traditional thresholds of statistical significance (Billingham et al., 2012; Mitani & Haneuse, 2020).

### References

Billingham, L., Malottki, K., & Steven, N. (2012). Small sample sizes in clinical trials: A statistician's perspective. *Clinical Investigation*, *2*(7), 655–657. https://doi.org/10.4155/cli.12.50

Hartikka, H., Kuurila, K., & Körkkö, J. (2004). Lack of correlation between the type of *COL1A1* or *COL1A2* mutation and hearing loss in osteogenesis imperfecta patients. *Human Mutation*, *24*(2), 147–154. https://doi.org/10.1002/humu.20071

Mitani, A. A., & Haneuse, S. (2020). Small data challenges of studying rare diseases. *JAMA Network Open*, *3*(3), e201965. https://doi.org/10.1001/jamanetworkopen.2020.1965

**Answer 3:**

In small-sample biomedical studies, relying exclusively on $p$-values for categorical comparisons is methodologically problematic because statistical significance is highly sensitive to sample size; small cohorts frequently lack the requisite statistical power to reliably detect true between-group differences, thereby increasing the risk of false-negative results (Type II errors) (Ashournia et al., 2015). To compensate for the instability of hypothesis testing in limited sample sizes, the literature advocates for the concurrent reporting of effect size estimates—such as Cramer's *V* or odds ratios—which provide a standardized quantification of the magnitude of the observed relationships (del Valle et al., 2025). By decoupling the strength of an association from the sample size, effect size measures allow researchers to evaluate the actual clinical or practical significance of the findings, ensuring that meaningful associations are not dismissed simply because they failed to meet strict $p$-value thresholds due to low statistical power (Prado et al., 2023).

### References

*   **Ashournia, H., Johansen, F. T., Folkestad, L., Diederichsen, A. C., & Brixen, K.** (2015). Heart disease in patients with osteogenesis imperfecta—A systematic review. *International Journal of Cardiology*, 196, 149–157. https://doi.org/10.1016/j.ijcard.2015.06.001
*   **del Valle, A., et al.** (2025). Eruptive process in children with osteogenesis imperfecta. [Source material from context].
*   **Prado, H. V., Debossan, S. A. T., Loayza, K. S., Abreu, L. G., & Brasileiro, C. B.** (2023). Radiomorphometric indices and fractal dimension of the mandible in individuals with osteogenesis imperfecta: a matched cross-sectional study. *Oral Surgery, Oral Medicine, Oral Pathology and Oral Radiology*, 136(1), 102–111. https://doi.org/10.1016/j.oooo.2023.02.002

**Question 3:**

For a small cohort study using a count-like oral outcome with likely non-normal distribution across multiple groups, what is the literature-supported rationale for using the Kruskal-Wallis test and reporting a non-parametric effect-size measure such as epsilon-squared? Please keep the answer concise and suitable for one brief Methods rationale sentence. Use APA 7 style and list the used references at the end.

**Answer 1:**

Because the quantitative oral outcomes exhibited a skewed, non-normal distribution across multiple subgroups, the non-parametric Kruskal-Wallis test was selected to compare these variables, supplemented by appropriate effect size calculations to rigorously evaluate the clinical significance of the findings rather than relying solely on statistical probability (Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3, n.d.; Taqi et al., 2021; Wei et al., 2022).

**References**

*   Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3. (n.d.). [Unpublished manuscript/Internal Document].
*   Taqi, D., Moussa, H., Schwinghamer, T., Ducret, M., Dagdeviren, D., Retrouvey, J. M., Rauch, F., & Tamimi, F. (2021). Osteogenesis imperfecta tooth level phenotype analysis: Cross-sectional study. *Bone*, *147*, 115917.
*   Wei, Y., Liu, Y., Lv, F., Xu, X., Wang, J., Xia, W., Jiang, Y., Wang, O., Xing, X., & Li, M. (2022). Genotype-phenotype relationship and follow-up analysis of a Chinese cohort with osteogenesis imperfecta. *Frontiers in Endocrinology*.

**Answer 2:**

Because the data lack a normal distribution, the non-parametric Kruskal-Wallis test is used to evaluate differences across multiple groups, supplemented by appropriate effect size calculations to accurately assess the clinical significance of the observed variations (Bartosik et al., 2025).

*(Note: While the provided sources strongly support the use of the Kruskal-Wallis test for non-parametric data and explicitly mandate reporting effect sizes to evaluate clinical significance, they do not specifically mention "epsilon-squared." You must independently verify the specific statistical justification and citation for epsilon-squared using outside literature.)*

### References

* Bartosik, A., et al. (2025). Genotype-based comparison of bone microstructure in adult patients with classical osteogenesis imperfecta. *Osteoporosis International*.
* *Osteogenesis-Imperfecta-Oro-Denta-Bulgular-Etik-Kurul-Basvuru-Rev3* [Clinical Study Protocol]. (n.d.).

**Answer 3:**

To appropriately address the non-normal distribution of count-based oral outcomes across multiple groups in small clinical cohorts, the non-parametric Kruskal-Wallis test is required for analysis, and it should be supplemented with a non-parametric effect size measure (such as the $R^2$ scale or epsilon-squared) to quantify the clinical magnitude and relevance of the observed differences rather than relying solely on statistical significance (Elfituri et al., 2024; Hsu et al., 2025).

### References

*   **Elfituri, A. A., De Nova, M. J., & Najirad, M.** (2024). The impact of osteogenesis imperfecta severity on oral health-related quality of life in Spain: a cross-sectional study. *Orphanet Journal of Rare Diseases*, 19(1), 108.
*   **Hsu, K. J., Tseng, Y. C., Chen, C. M., Lee, H. T., Zhao, W. Y., & Lin, I. C.** (2025). Determinants of masticatory ability in Taiwanese patients with osteogenesis imperfecta. *Journal of Dental Sciences*, 20(2), 980–988.

**Question 4:**

In a small biomedical dataset, what is the literature-supported rationale for treating penalized logistic regression with leave-one-out cross-validation, repeated stratified k-fold cross-validation, and paired bootstrap confidence intervals for delta AUC as secondary model-verification procedures rather than as primary inferential evidence? Please give a compact answer suitable for a brief Methods or Discussion rationale sentence, and note any key caution about overfitting or instability in small samples. Use APA 7 style and list the used references at the end.

**Answer 1:**

The provided literature extensively documents the statistical challenges inherent to small sample sizes in rare diseases, emphasizing that such constraints necessitate exact nonparametric inferences (e.g., Fisher's exact test) over large-sample approximations, and noting that standard logistic regression coefficients are highly vulnerable to instability and multicollinearity (Rabello et al., 2024; Xiao et al., 2015). While the sources validate the general use of cross-validation (e.g., 10-fold) for model and feature selection in small cohorts (Xiao et al., 2015), they do not explicitly detail the combined use of penalized logistic regression, leave-one-out cross-validation (LOOCV), repeated stratified k-fold cross-validation, and paired bootstrap confidence intervals for delta AUC. Therefore, drawing on our conversation history and the overarching methodological framework of small-data challenges referenced in the texts (Mitani & Haneuse, 2020), the detailed rationale provided below includes information from outside the given sources that you may want to independently verify.

**Detailed Explanation and Cautionary Context**
In small biomedical datasets, treating complex resampling and penalized predictive models as secondary verifications rather than primary inferential evidence is driven by the inherent instability of machine learning techniques when applied to limited observations (Mitani & Haneuse, 2020). When the number of events per predictor is sparse, traditional logistic regression is prone to severe overfitting and parameter distortion due to multicollinearity (Rabello et al., 2024). While penalization (e.g., Lasso or Ridge) helps mitigate this overfitting, advanced resampling techniques like LOOCV and repeated k-fold cross-validation can still suffer from high variance; minute variations in data partitioning can lead to drastically different models and AUC estimates. Thus, traditional exact inferential methods are safer for primary hypothesis testing because they calculate probability directly and do not rely on assumed continuous distributions or large-sample asymptotic theory (Xiao et al., 2015). Advanced predictive metrics and bootstrap confidence intervals should subsequently be applied as a secondary step to confirm that the identified primary associations are directionally robust and not merely artifacts of a specific sample partition.

**Compact Rationale for a Methods or Discussion Section**
"Because standard predictive models like logistic regression are highly susceptible to parameter instability, multicollinearity, and severe overfitting in small-sample rare disease cohorts (Mitani & Haneuse, 2020; Rabello et al., 2024), exact inferential statistics were prioritized for primary hypothesis testing (Xiao et al., 2015); consequently, penalized logistic regression—rigorously supplemented by leave-one-out cross-validation, repeated stratified k-fold cross-validation, and paired bootstrap confidence intervals for delta AUC—was employed strictly as a secondary model-verification procedure to confirm the robustness, directionality, and generalizability of the identified associations without risking small-data artifacts."

### References

*   Mitani, A. A., & Haneuse, S. (2020). Small data challenges of studying rare diseases. *JAMA Network Open*, 3(3), e201965.
*   Rabello, R. M. R. S., et al. (2024). Oral problems in Brazilian individuals with rare genetic diseases that affect skeletal development. *[Source Manuscript]*.
*   Xiao, J., et al. (2015). Local amino acid sequence patterns dominate the heterogeneous phenotype for the collagen connective tissue disease Osteogenesis Imperfecta resulting from Gly mutations. *Journal of Structural Biology*.

**Answer 2:**

In small-sample biomedical studies, advanced predictive validation techniques—such as penalized logistic regression, leave-one-out cross-validation (LOOCV), repeated stratified k-fold cross-validation, and paired bootstrap confidence intervals for delta AUC—are best utilized as secondary model-verification procedures rather than primary inferential evidence because small sample sizes inherently increase the risk of severe overfitting, model instability, and highly variable out-of-sample performance estimates (Billingham et al., 2012; Mitani & Haneuse, 2020). While penalization and resampling methods attempt to mitigate these small-data challenges, the resulting diagnostic metrics often lack the statistical power and robustness required for primary causal inference in rare disease cohorts, making them more appropriate for exploratory internal validation.

*Important Note: While the provided sources broadly discuss the statistical limitations, low power, and instability risks associated with small sample sizes in rare diseases (Billingham et al., 2012; Mitani & Haneuse, 2020), they do not explicitly detail the use of penalized logistic regression, LOOCV, k-fold cross-validation, or delta AUC. Therefore, the specific application of these techniques to your rationale relies on external statistical principles that you may want to independently verify.*

### References

Billingham, L., Malottki, K., & Steven, N. (2012). Small sample sizes in clinical trials: a statistician's perspective. *Clinical Investigation*, *2*(7), 655–657.

Mitani, A. A., & Haneuse, S. (2020). Small data challenges of studying rare diseases. *JAMA Network Open*, *3*(3), e201965. https://doi.org/10.1001/jamanetworkopen.2020.1965

**Answer 3:**

Based on the provided sources, there is no information or literature provided regarding the use of penalized logistic regression, leave-one-out cross-validation (LOOCV), repeated stratified k-fold cross-validation, or paired bootstrap confidence intervals for delta AUC.

The provided texts discuss the use of standard logistic regression and explicitly acknowledge the inherent challenges of small sample sizes in rare diseases like osteogenesis imperfecta—such as limited statistical and predictive power, wide confidence intervals, and the risk of type 2 errors (Billingham et al., 2012; Byrd et al., 2024; Mitani & Haneuse, 2020). However, the sources do not cover advanced model-verification procedures, overfitting, or the mathematical instability of these specific resampling techniques in small datasets.

Because I am strictly limited to the provided documents and cannot use outside knowledge, I cannot generate the specific methodological rationale you requested.

### References
*   **Billingham, L., Malottki, K., & Steven, N. (2012).** Small sample sizes in clinical trials: a statistician's perspective. *Clinical Investigation*, 2(7), 655–657.
*   **Byrd, J. J., White, A. C., Nissen, C. G., Schissel, M., & van Ormer, M. (2024).** Genotype–phenotype correlations in 294 pediatric patients with osteogenesis imperfecta. *JBMR Plus*, 8(11), ziae125.
*   **Mitani, A. A., & Haneuse, S. (2020).** Small data challenges of studying rare diseases. *JAMA Network Open*, 3(3), e201965.
