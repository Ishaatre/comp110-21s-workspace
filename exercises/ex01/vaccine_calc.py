"""A vaccination calculator."""

__author__ = "730393785"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population:"))
doses_administered: int = int(input("Doses Administered:"))
doses_per_day: int = int(input("Doses per day:"))
target_percent: int = int(input("Target percent vaccinated:"))

already_vaccinated: int = round(doses_administered / 2)
target_population: int = round(population *(target_percent / 100))
remaining_population: int = target_population - already_vaccinated
num_of_days_to_vaccinate_remaining_population: int = round(2*(remaining_population / doses_per_day))




today: datetime = datetime.today()
days_to_vaccinate_target_percent: timedelta = timedelta(num_of_days_to_vaccinate_remaining_population)
calculated_date: datetime = today + days_to_vaccinate_target_percent


final_answer: str = "We will reach " + str(target_percent) + "%" + " vaccination in " + str(int(num_of_days_to_vaccinate_remaining_population)) + " days, which falls on " + (calculated_date.strftime("%B %d, %Y")) + "."

print(final_answer)