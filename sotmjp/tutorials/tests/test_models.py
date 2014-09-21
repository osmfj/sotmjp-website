from django.contrib.auth.models import User
from django.test import TestCase

from sotmjp.tests.factories import SotMTutorialProposalFactory

from ..models import SotMTutorialMessage


class SotMTutorialMessageModelTest(TestCase):
    def test_one(self):
        """Can create the application object"""
        SotMTutorialMessage()

    def test_reverse_relation(self):
        user = User.objects.create_user("Foo")
        tutorial = SotMTutorialProposalFactory.create()
        self.assertFalse(tutorial.tutorial_messages.all())

        # Just the minimum required fields
        x = SotMTutorialMessage.objects.create(
            tutorial=tutorial,
            user=user,
            message="Foo",
        )
        # the reverse relation works
        self.assertEqual(x, tutorial.tutorial_messages.all()[0])
