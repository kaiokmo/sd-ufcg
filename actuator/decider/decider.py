# -*- coding: utf-8 -*-
""" module decider
        decicdes over received metrics.
"""
class Decider(object):
    """ class Decicder
        encapsulates tolerance and decision parameters.
    """
    def __init__(self, tolerance):
        self._tolerance = tolerance

    @property
    def tolerance(self):
        """ tolerance()
            return saved tolerance.
        """
        return self._tolerance

    def process_metric(self, metric):
        """ process_metric(metric)
                analyses passed metric and deccides workload balancing.
        """
        pass
