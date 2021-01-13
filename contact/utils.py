from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django.utils.html import format_html
import datetime

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			url = "{% url 'contact:event' "+str(day)+'m'+str(self.month)+'y'+str(self.year)+" %}"
			return f"<td><a class='datenum' href="+ '"' + url + '"' + "><span class='date'>" + str(day) +"</span></a></td>"

			# return f"<td><span class='date'><a href="+ '"' + url + '"' + ">" + str(day) +"</a>"
			# return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
		monthinteger = self.month

		month = datetime.date(self.year, monthinteger, 1).strftime('%B')
		b1 = f'<tr><th colspan="7" class="month"><a class="btn btn-danger left" id="left" href="#"> < </a>\n'+'<strong style="padding:20px">'+month+' '+str(self.year)+'</strong> '+'<a class="btn btn-danger right sun" id="right" href="#"> > </a></th></tr>'
		test = f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		print(test)
		cal = f'<table id="cal" style="display:grid">\n'
		cal += b1

		# cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		# print(cal)
		return cal
