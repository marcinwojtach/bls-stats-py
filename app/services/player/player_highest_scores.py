from matplotlib.figure import Figure
import numpy as np
from app.shared import state


class PlayerHighestScores:
    def __init__(self):
        self.all_columns_values = state['headers'].all()
        self.default_params = [
            self.all_columns_values['apct']['label'],
            self.all_columns_values['dpct']['label'],
        ]

    def get_chart(self, all_time_stats, latest_match_stats, params):
        """
        Returns chart figure
        :param all_time_stats: List({ label, value })
        :param latest_match_stats: List({ label, value })
        :param params: List(string)
        :return: Figure
        """
        params_to_use = (self.default_params, params)[bool(params)]

        all_time_stats = self.__create_stats_scope_by_params(all_time_stats, params_to_use)
        latest_match_stats = self.__create_stats_scope_by_params(latest_match_stats, params_to_use)

        labels = [obj['label'] for obj in all_time_stats]
        all_time_values = [obj['value'] for obj in all_time_stats]
        last_match_values = [obj['value'] for obj in latest_match_stats]

        width = 0.35
        figure = Figure()
        ax = figure.add_subplot()

        def add_labels(labels_list, values, bar_no):
            for i in range(len(labels_list)):
                x_offset = i + width if bar_no > 1 else i
                ax.text(x_offset, values[i] // 2, values[i], ha='center')

        all_time_bar = ax.bar(np.arange(len(labels)), all_time_values, width, label='Rekordy / Kariera', color='tab:blue')
        last_match_bar = ax.bar(np.arange(len(labels)) + width, last_match_values, width, label='Ostatni mecz', color='tab:green')

        add_labels(labels, all_time_values, 1)
        add_labels(labels, last_match_values, 2)

        ax.set_xlabel('Kategoria')
        ax.set_ylabel('Wartość')
        ax.set_xticks(np.arange(len(labels)) + width / 2)
        ax.set_xticklabels(labels)
        ax.legend()
        return figure

    def __create_stats_scope_by_params(self, stats, params):
        scope = []

        for stat in stats:
            for param in params:
                if stat['label'] == param:
                    scope.append(stat)

        return scope
