import seaborn as sns 
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", palette="pastel")

# obtendo dados
tips = sns.load_dataset("tips")
#print(tips.sample(3).T)
print(tips.columns)

# desenhando um boxplot para mostrar pagamentos por dia e horário
#fig = plt.figure(figsize=(50,50))
ax =sns.boxplot(
    data=tips,
    x="day", 
    y="total_bill",
    hue="time",
    palette=["m", "g"],
)
sns.despine(offset=10, trim=True)
plt.title("Boxplot Gorgedas por dias/horário")
ax.set_xlabel("Dia da Semana")
ax.set_ylabel("Total de Gorjetas")

plt.savefig("lixo.png")
