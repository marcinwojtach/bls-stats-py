from matplotlib.figure import Figure
import numpy as np


class PlayerHighestScores:
    def get_chart(self, all_time_stats, latest_match_stats):
        labels = [obj['label'] for obj in all_time_stats]
        all_time_values = [obj['value'] for obj in all_time_stats]
        last_match_values = [obj['value'] for obj in latest_match_stats]

        width = 0.35
        figure = Figure()
        ax = figure.add_subplot()

        all_time_bar = ax.bar(np.arange(len(labels)), all_time_values, width, label='Rekordy / Kariera', color='tab:blue')
        last_match_bar = ax.bar(np.arange(len(labels)) + width, last_match_values, width, label='Ostatni mecz', color='tab:green')

        ax.set_xlabel('Kategoria')
        ax.set_ylabel('Wartość')
        ax.set_xticks(np.arange(len(labels)) + width / 2)
        ax.set_xticklabels(labels)
        ax.legend()
        return figure
