from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = 'landing.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'    

class HomePage(TemplateView):
    template_name = 'index.html'


class TermsPage(TemplateView):
    template_name = 'tos.html'


class PrivacyPage(TemplateView):
    template_name = 'privacy.html'
