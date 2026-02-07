from datetime import date
from django.test import TestCase
from django.db import IntegrityError
from .models import Category, Task


class CategoryModelTest(TestCase):
    def test_str_returns_name(self):
        category = Category.objects.create(name="Work")
        self.assertEqual(str(category), "Work")

    def test_name_is_unique(self):
        Category.objects.create(name="Work")
        with self.assertRaises(IntegrityError):
            Category.objects.create(name="Work")


class TaskModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Work")

    def test_defaults_and_str(self):
        task = Task.objects.create(
            title="Test Task",
            category=self.category,
            due_date=date.today(),
        )
        self.assertEqual(str(task), "Test Task")
        self.assertFalse(task.completed)

    def test_category_relationship_and_reverse(self):
        task = Task.objects.create(
            title="Test Task",
            category=self.category,
            due_date=date.today(),
        )
        self.assertEqual(task.category, self.category)
        self.assertIn(task, self.category.tasks.all())

    def test_cascade_delete(self):
        task = Task.objects.create(
            title="Test Task",
            category=self.category,
            due_date=date.today(),
        )
        task_id = task.id
        self.category.delete()
        self.assertFalse(Task.objects.filter(id=task_id).exists())
