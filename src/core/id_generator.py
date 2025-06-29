class IDGenerator:
    """
    Thread-safe ID generator for entities
    """

    def __init__(self) -> None:
        self._counters = {}

    def get_next_id(self, entity_type: str) -> int:
        if entity_type not in self._counters:
            self._counters[entity_type] = 0

        self._counters[entity_type] += 1
        return self._counters[entity_type]

    def set_counter(self, entity_type: str, value: int) -> None:
        self._counters[entity_type] = value


id_generator = IDGenerator()
