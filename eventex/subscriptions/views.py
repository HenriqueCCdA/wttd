from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription
from django.views.generic import DetailView


new = EmailCreateView.as_view(model=Subscription,
                      form_class=SubscriptionForm,
                      email_subject='Confirmação de inscrição')


detail = DetailView.as_view(model=Subscription)
