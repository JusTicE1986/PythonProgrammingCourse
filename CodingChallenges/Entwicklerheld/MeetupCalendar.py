import datetime


class MeetupCalculator:
    @staticmethod
    def calculate_meetup_date(year, month, week, day_of_week): #-> datetime.date:
        # Implement this
        # 2024, 3, "first", "Monday"
        print(datetime.date.weekday(day_of_week))


if __name__ == "__main__":
    meetup_calendar = MeetupCalculator.calculate_meetup_date(2024, 3, "first", "Montag")