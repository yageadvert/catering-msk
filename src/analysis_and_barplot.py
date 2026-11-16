import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analysis_and_barplot(data, feature):
# Выводим таблицу соотношения
    distribution = pd.DataFrame({
        'count': data[feature]
                .value_counts(),
        
        'percent': (data[feature]
                .value_counts(normalize=True)*100)
                .map(lambda value: f'{value:.1f}%')
    })
    display(distribution)
    
# Визуализируем данные через barplot
    plt.figure(figsize=(7,5))
    
    avg_count=distribution['count'].mean()

    ax=sns.barplot(
        distribution,
        x=distribution.index,
        y='count',
        edgecolor='black'
    )

    plt.axhline(
        y=avg_count,
        color='red',
        linestyle='--',
        linewidth=1,
        label=f'Среднее количество\nзаведений в категории: {avg_count:.0f}'
    )

    percent_labels = distribution['percent']

    ax.bar_label(
    ax.containers[0],
    labels=percent_labels
)

    plt.xticks(rotation=90)
    plt.xlabel('Категория заведений')
    plt.ylabel('Количество заведений')
    plt.grid(axis='y', alpha=0.3)
    plt.legend()
    
    plt.show()