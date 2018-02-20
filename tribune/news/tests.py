from django.test import TestCase
from .models import Editor,tags,Article
# Create your tests here.


class EditorTestClass(TestCase):
    # set up method
    def setUp(self):
        self.evans=Editor(first_name='evans',last_name='mwenda',email='evanmwenda@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.evans,Editor))

        # testing save method
    def test_save_method(self):
        self.evans.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def 