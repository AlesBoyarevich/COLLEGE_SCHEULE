from django.urls import reverse_lazy
from copy import copy


class BaseMixin:
    active:str = 'not set'
    breadcramps:dict[str:str] = {'not set': ...}
    extra_context = {
        'email': 'alesboyarevich@gmail.com',
        'phone': '+375 25 500 58 93',
        'license': '© 2024 MRC-schedule. This project is distributed under the MIT license and is open for anyone to use.',
        'social_telegram': 'https://t.me/mrkchannelofficial',
        'social_instagram': 'https://www.instagram.com/mrk_bsuir.by/',
        'social_youtube': 'https://www.youtube.com/@user-jw9pb7kx1f',
        'social_wk': 'https://vk.com/offmrc',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = self.active
        context['breadcramps'] = copy(self.breadcramps)
        return context
    

class CoreMixin(BaseMixin):
    active = 'index'
    breadcramps = {'main': reverse_lazy('index')}

class TeachersMixin(BaseMixin):
    active = 'teachers'
    breadcramps = {'teachers': reverse_lazy('teachers')}

class SubjectsMixin(BaseMixin):
    active = 'subjects'
    breadcramps = {'subjects': reverse_lazy('subjects')}

class GroupsMixin(BaseMixin):
    active = 'groups'
    breadcramps = {'groups': reverse_lazy('groups')}

class ScheduleMixin(BaseMixin):
    active = 'schedule'
    breadcramps = {'schedule': reverse_lazy('schedule')}
