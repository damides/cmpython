import logging


class Particle:
    ''' Parent class with some basic physical quantities'''

    def __init__(self, name, mass, charge, momentum=0.):
        self._name = str(name)

        # value_when_true if condition else value_when_false
        if mass > 0.:
            self._mass = mass
        else:
            logging.error('Particle with mass less than 0 instantiated')

        self._charge = charge  # [e]
        self._momentum = momentum  # [MeV/c]

    def print_info(self):
        print('+++Particle infos+++')
        print('Name: {}, Mass: {:.2f} MeV/c^2, Charge: {}e, '
              'Momentum: {:.3f} MeV/c'.format(self.name, self.mass,
                                              self.charge, self.momentum))
    # Decorator for getter
    @property
    def name(self):
        return self._name

    # Decorator for setter
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
            print('The new name of the particle is: {}'.format(self.name))

        else:
            print('The name of the particle must be a string')

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        if value > 0.:
            self._mass = value
            print('The new mass of the particle is: '
                  '{} MeV/c^2'.format(self.mass))
        else:
            print("No massless particles in this neighborhood")

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        self._charge = value
        print("The new charge of the particle is: {}e".format(self.charge))

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, value):
        if value < 0.:
            print('Particle with momentum less than 0 not allowed')
        else:
            self._momentum = value
            print("New momentum of the particle is: "
                  "{} MeV/c".format(self.momentum))


class Proton(Particle):
    """Child Class describing a Proton"""

    NAME = 'Proton'
    MASS = 938.272  # MeV /c^2
    CHARGE = +1  # e

    def __init__(self, momentum=0.):  # pass an optional momentum argument
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


class Alpha(Particle):
    """ Class describing an Alpha nucleum """

    NAME = 'Alpha'
    MASS = 3727.3  # MeV
    CHARGE = +4.  # e

    def __init__(self, momentum=0.):
        ''' super() is an elegant way to refer to parent class '''
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


if __name__ == '__main__':
    particle = Particle('electron', 50., -1)
    particle.print_info()
    particle.name = 'pippo'
    particle.name = 5
    particle.mass = 34
    particle.mass = -50
    particle.charge = 4
    particle.momentum = 5
    particle.momentum = -50
    protone = Proton(50)
    protone.print_info()
