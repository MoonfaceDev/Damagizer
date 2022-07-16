class EnchantmentTypeMeta(type):
    def __call__(cls, min_level: int = 1, max_level: int = 5) -> type:
        return type('EnchantmentTypeValue', (EnchantmentType,), {'min_level': min_level, 'max_level': max_level})


class EnchantmentType(metaclass=EnchantmentTypeMeta):
    min_level: int
    max_level: int

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: int):
        if not isinstance(v, int):
            return False
        return v == 0 or cls.min_level <= v <= cls.max_level
