from utils.DateFormat import DateFormat


class Movie():

    def __init__(self, id, title=None, duration=None, released=None) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': DateFormat.convert_date(self.released)
        }
