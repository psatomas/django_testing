from django.test import TestCase
from unittest.mock import patch
from products.models import User

class UserSignalTests(TestCase):
    
    @patch('products.signals.send_mail')
    def test_welcome_email_sent_on_user_creation(self, mock_send_mail):
        """Test that a welcome email is sent when a new user is created."""
        User.objects.create_user(username='john', email='john@example.com', password='password123')

        mock_send_mail.assert_called_once_with(
            'Welcome!',
            'Thanks for signing up!',
            'admin@django.com',
            ['john@example.com'],
            fail_silently=False,
        )

    @patch('products.signals.send_mail')
    def test_no_email_sent_on_user_update(self, mock_send_mail):
        user = User.objects.create_user(username='john', email='john@example.com', password='password123')

        mock_send_mail.reset_mock()

        user.email = 'john_new@example.com'
        user.save()

        mock_send_mail.assert_not_called()

