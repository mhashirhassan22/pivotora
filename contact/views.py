from django.views import View
from .models import *
from django.shortcuts import render, redirect,reverse
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.utils.dateparse import parse_datetime
import calendar
from .models import *
from .utils import Calendar
from contact.forms import EventForm


# Create your views here.
class PivotoraIndex(View):
    template_name = "index.html"

    def get(self, request):
        web_content = WebContent.objects.filter().first()
        portfolio = Portfolio.objects.all()
        context = {
            'content': web_content,
            'portfolio': portfolio

        }
        return render(request, self.template_name, context)





class CalendarView(generic.ListView):
    model = Event
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        web_content = WebContent.objects.filter().first()
        portfolio = Portfolio.objects.all()
        context = {
            'content': web_content,
            'portfolio': portfolio

        }
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contact:calendar'))
    web_content = WebContent.objects.filter().first()
    portfolio = Portfolio.objects.all()
    context = {
        'content': web_content,
        'portfolio': portfolio,
        'form': form

    }
    return render(request, 'index.html', context)



class MessageView(View):
    template_name = "index.html"


    def get(self, request):
        web_content = WebContent.objects.filter().first()
        portfolio = Portfolio.objects.all()
        context = {
            'content': web_content,
            'portfolio': portfolio,

        }
        return redirect('/')

    def post(self, request):
        web_content = WebContent.objects.filter().first()
        portfolio = Portfolio.objects.all()
        context = {
            'content': web_content,
            'portfolio': portfolio,

        }
        msg = Message()
        msg.name = request.POST['name']
        msg.email = request.POST['email']
        msg.message = request.POST['message']
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['done'] = 'success'
        msg.save()
        return render(request, self.template_name, context)


class EventView(View):
    template_name = "index.html"


    def get(self, request, d):
        selected_date = d.split('-')
        curr_date = datetime.now().date()
        web_content = WebContent.objects.filter().first()
        portfolio = Portfolio.objects.all()
        context = {
            'content': web_content,
            'portfolio': portfolio,

        }
        dt = date(int(selected_date[2]),int(selected_date[1]),int(selected_date[0]))
        if(curr_date>dt):
            d = get_date(self.request.GET.get('month', None))
            cal = Calendar(d.year, d.month)
            html_cal = cal.formatmonth(withyear=True)
            context['calendar'] = mark_safe(html_cal)
            context['prev_month'] = prev_month(d)
            context['next_month'] = next_month(d)
            context['wrong_date'] = 'Please select future day for appointment!'
            return render(request, self.template_name, context)
        context['date'] = d
        return render(request, self.template_name, context)

    def post(self, request, d):
        web_content = WebContent.objects.filter().first()
        portfolio = Portfolio.objects.all()
        context = {
            'content': web_content,
            'portfolio': portfolio,

        }
        curr_date = get_date(self.request.GET.get('month', None))
        cal = Calendar(curr_date.year, curr_date.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(curr_date)
        context['next_month'] = next_month(curr_date)

        e = Event()
        e.email = request.POST['email']
        e.start_time = request.POST['start_time']
        e.end_time = request.POST['end_time']
        x = d.split('-')
        e.date = datetime(int(x[2]), int(x[1]), int(x[0]))


        # check if event collides

        all_events = Event.objects.filter(date=e.date, start_time__lte=e.end_time, end_time__gte=e.start_time)
        if(all_events):
            context['fail'] = 'fail'
        else:
            context['booked'] = 'success'
            e.save()

        return render(request, self.template_name, context)





def index(request):
    return redirect('admin:index')
