# Demonstrating abstraction by exposing a simple interface while hiding implementation details

class DataProcessor:
    def __init__(self, data):
        self._data = data

    def process(self):
        '''Public method that hides the implementation details.'''
        cleaned = self._clean_data()
        return self._summarize(cleaned)

    def _clean_data(self):
        return [item for item in self._data if item is not None]

    def _summarize(self, cleaned_data):
        return {
            'count': len(cleaned_data),
            'max': max(cleaned_data) if cleaned_data else None,
            'min': min(cleaned_data) if cleaned_data else None,
        }

processor = DataProcessor([10, None, 20, 5, None, 15])
print(processor.process())
