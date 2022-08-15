import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from tabulate import tabulate

dataset = pd.read_csv('data.csv')

data = pd.DataFrame(dataset.values, columns=['Ano', 'PIB', 'CredEmpresas', 'CredParticulares', 'JurosEmpresas', 'JurosParticulares',
                    'Inflacao', 'Desemprego'])

#Multiple Regressions and ANOVAs

modelo = ols("CredParticulares ~ PIB + JurosParticulares + Inflacao + Desemprego", data).fit()
print(modelo.summary())

anova_results = anova_lm(modelo)
print(anova_results)


modelo2= ols("CredEmpresas ~ PIB + JurosEmpresas + Inflacao + Desemprego", data).fit()
print(modelo2.summary())

anova_results2 = anova_lm(modelo2)
print(anova_results2)


#Covariances

data["Emprestimo Total"] = data["CredEmpresas"] + data["CredParticulares"]

anos2010_2014 = data.iloc[0:5]
anos2015_2019 = data.iloc[5:]


def covariance(x, y):
    mean_x = sum(x)/(len(x))
    mean_y = sum(y)/(len(y))
    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    denominator = len(x)-1
    cov = numerator/denominator
    return "{:.2f}".format(cov)


cov_1 = covariance(data["Emprestimo Total"], data["PIB"])
cov_2 = covariance(anos2010_2014["Emprestimo Total"], anos2010_2014["PIB"])
cov_3 = covariance(anos2015_2019["Emprestimo Total"], anos2015_2019["PIB"])
cov_4 = covariance(data["CredEmpresas"], data["JurosEmpresas"])
cov_5 = covariance(data["CredParticulares"], data["JurosParticulares"])

covs = [["S (Empréstimo Total, PIB)", cov_1],
     ["S (Empréstimo Total, PIB) 2010-2014", cov_2],
     ["S (Empréstimo Total, PIB) 2015-2019", cov_3],
     ["S (Empréstimo Empresas, Taxa de Juro Empresa)", cov_4],
     ["S (Empréstimo Particulares, Taxa de Juro Particulares)", cov_5]]


print(tabulate(covs, headers=["Covariância", "Valores"]))


#Correlations

def correlation(x, y):
    mean_x = sum(x)/(len(x))
    mean_y = sum(y)/(len(y))
    sub_x = [i-mean_x for i in x]
    sub_y = [i-mean_y for i in y]
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    std_deviation_x = sum([sub_x[i]**2.0 for i in range(len(sub_x))])
    std_deviation_y = sum([sub_y[i]**2.0 for i in range(len(sub_y))])
    denominator = (std_deviation_x*std_deviation_y)**0.5
    corr = numerator/denominator
    return corr



corr_1 = correlation(data["Emprestimo Total"], data["PIB"])
corr_2 = correlation(anos2010_2014["Emprestimo Total"], anos2010_2014["PIB"])
corr_3 = correlation(anos2015_2019["Emprestimo Total"], anos2015_2019["PIB"])
corr_4 = correlation(data["CredEmpresas"], data["JurosEmpresas"])
corr_5 = correlation(data["CredParticulares"], data["JurosParticulares"])

corrs = [["r (Empréstimo Total, PIB)", corr_1],
     ["r (Empréstimo Total, PIB) 2010-2014", corr_2],
     ["r (Empréstimo Total, PIB) 2015-2019", corr_3],
     ["r (Empréstimo Empresas, Taxa de Juro Empresa)", corr_4],
     ["r (Empréstimo Particulares, Taxa de Juro Particulares)", corr_5]]


print(tabulate(corrs, headers=["Correlações", "Valores"]))


corr_6 = correlation(data["CredEmpresas"], data["Inflacao"])
corr_7 = correlation(data["CredEmpresas"], data["Desemprego"])
corr_8 = correlation(data["CredParticulares"], data["Inflacao"])
corr_9 = correlation(data["CredParticulares"], data["Desemprego"])

corrs = [["r (Empréstimo Empresas, Taxa de Inflação)", corr_6],
     ["r (Empréstimo Empresas, Taxa de Desemprego)", corr_7],
     ["r (Empréstimo Particulares, Taxa de Inflação)", corr_8],
     ["r (Empréstimo Particulares, Taxa de Desemprego)", corr_9]]


print(tabulate(corrs, headers=["Correlações", "Valores"]))
