import abc
from typing import Dict

import numpy as np

from ossm_base.types import Observable
from ossm_base.types import Stimulus


class OSSMModel(abc.ABC):
    """ Interface for sensorimotor models. Implements the OSSM modeling standards.

    The interface standardizes the initialization and operation of models within the standards. The implementation
    itself is left to the specific model.

    Multiple extensions of the interface will exist for different autodifferentiation frameworks,
    e.g. PyTorch or TensorFlow.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def initialize(self) -> "OSSMModel":
        """ Initialize the model before starting a simulation. Returns itself. """
        pass

    @abc.abstractmethod
    def simulate(self, stimulus: Stimulus) -> "OSSMModel":
        """ Run a single timestep of the model simulation. Returns itself.

        This method should only simulate the internal dynamics of the model. It does not handle the simulation of the
        task environment or the recording of observables.
        """
        pass

    @abc.abstractmethod
    def record(self) -> Dict[Observable, np.ndarray]:
        """ Measure the observables of the model. """
        pass