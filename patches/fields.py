from decimal import Decimal
from haystack.exceptions import SearchFieldError

class SearchField:
    def prepare(self, value):
        raise NotImplementedError("Subclasses must implement the `prepare` method.")

class CharField(SearchField):
    def prepare(self, value):
        if not isinstance(value, str):
            raise SearchFieldError(f"Cannot convert {value} to a string.")
        return value

class DateField(SearchField):
    def prepare(self, value):
        if not value:
            return None

        if isinstance(value, datetime):
            return value.date()
        elif isinstance(value, str):
            parsed_date = parse_date(value)
            if not parsed_date:
                raise SearchFieldError(f"Invalid date format: {value}")
            return parsed_date
        else:
            raise SearchFieldError(f"Cannot convert {value} to a date.")

class DateTimeField(SearchField):
    def prepare(self, value):
        if not value:
            return None

        if isinstance(value, datetime):
            return value
        elif isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                raise SearchFieldError(f"Invalid datetime format: {value}")
        else:
            raise SearchFieldError(f"Cannot convert {value} to a datetime.")

class BooleanField(SearchField):
    def prepare(self, value):
        if value in [True, False]:
            return value
        if isinstance(value, str):
            if value.lower() in ["true", "1"]:
                return True
            if value.lower() in ["false", "0"]:
                return False
        raise SearchFieldError(f"Cannot convert {value} to a boolean.")

class DecimalField(SearchField):
    def prepare(self, value):
        if isinstance(value, Decimal):
            return value
        if isinstance(value, str):
            try:
                return Decimal(value)
            except ValueError:
                raise SearchFieldError(f"Invalid decimal format: {value}")
        raise SearchFieldError(f"Cannot convert {value} to a decimal.")
