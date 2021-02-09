from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django.urls import reverse
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
		events_per_day = events.filter(date__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			date = str(day)+'-'+str(self.month)+'-'+str(self.year)
			url = reverse('contact:event-check', args=(date,))
			return f'<td><a  class="datenum" href="{url}#eve"> {day} </a></td>'
		return '<td> - </td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(date__year=self.year, date__month=self.month)
		monthinteger = self.month

		month = datetime.date(self.year, monthinteger, 1).strftime('%B')
		b1 = f'<tr><th colspan="7" class="month"><a class="btn btn-danger left" id="left" href="#"> < </a>\n'+'<strong style="padding:20px">'+month+' '+str(self.year)+'</strong> '+'<a class="btn btn-danger right sun" id="right" href="#"> > </a></th></tr>'
		test = f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal = f'<table id="cal" style="display:grid">\n'
		cal += b1

		# cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
