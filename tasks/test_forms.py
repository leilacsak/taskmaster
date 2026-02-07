from datetime import date
from django.test import TestCase

from .forms import TaskForm
from .models import Category


class TaskFormTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Work")

    def test_form_valid_data(self):
        form = TaskForm(data={
            "title": "Buy milk",
            "due_date": date.today(),
            "category": self.category.id,
        })
        self.assertTrue(form.is_valid())

    def test_form_missing_title_invalid(self):
        form = TaskForm(data={
            "title": "",
            "due_date": date.today(),
            "category": self.category.id,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_form_missing_due_date_invalid(self):
        form = TaskForm(data={
            "title": "Buy milk",
            "due_date": "",
            "category": self.category.id,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("due_date", form.errors)

    def test_form_missing_category_invalid(self):
        form = TaskForm(data={
            "title": "Buy milk",
            "due_date": date.today(),
            "category": "",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("category", form.errors)

    def test_form_title_too_long_edge_case(self):
        form = TaskForm(data={
            "title": "a" * 201,   # if max_length=200
            "due_date": date.today(),
            "category": self.category.id,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
