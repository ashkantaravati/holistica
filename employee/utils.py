class EventMapper:
    @classmethod
    def map_employee_birthday_to_event(cls, birthday):
        full_name = birthday.full_name
        return {
            "type": "Birthday",
            "subject": f"{full_name}'s Birthday",
            "time": "All Day",
        }

    @classmethod
    def map_all_employee_birthdays_to_event(cls, birthdays):
        events = []
        for birthday in birthdays:
            events.append(cls.map_employee_birthday_to_event(birthday))
        return events
