# Определить, является ли год, который ввел пользователем, високосным или не високосным.

import calendar
print("YES" if calendar.isleap(int(input())) else "NO")