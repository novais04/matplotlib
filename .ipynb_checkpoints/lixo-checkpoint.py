import seaborn as sns 
sns.set_theme(style='whitegrid')

#obter base de dados
penguins = sns.load_dataset("penguins")

# Desenhando um barplot de especies e sexo
fig = sns.catplot(
    data=penguins,
    x='species',
    y='body_mass_g',
    hue='sex'
)

