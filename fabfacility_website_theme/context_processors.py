from .forms import SubscripForm


def theme_context(self):
    context = {
        'subscription_form': SubscripForm()
    }
    return context
