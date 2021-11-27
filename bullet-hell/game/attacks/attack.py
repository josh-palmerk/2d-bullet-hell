class Attack:
    """A code template for an attack. 
    
    Stereotype:
        Controller

    Attributes: ???
        _tag (string): The action tag (input, update or output).
    """

    def spawn_attack(self, cast, attacker):
        """Executes the attack.

        Args:
            cast (dict): The game actors {key: tag, value: list}. 
        """
        raise NotImplementedError("spawn_attack not implemented in superclass")