from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.conf import settings
from rest_framework.reverse import reverse_lazy

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Construct the reset password URL
    reset_password_url = "{}?token={}".format(
    instance.request.build_absolute_uri(reverse_lazy('password_reset:reset-password-confirm')),
    reset_password_token.key
)

    # Construct the email content
    email_message = f"Click the following link to reset your password: {reset_password_url}"

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for School Finder",
        # message:
        email_message,
        # from:
        settings.DEFAULT_FROM_EMAIL,
        # to:
        [reset_password_token.user.email]
    )
    msg.send()
