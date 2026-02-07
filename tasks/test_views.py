from datetime import date
from django.test import TestCase
from django.urls import reverse

from .models import Category, Task


class HomeViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Test Task",
            due_date=date.today(),
            completed=False,
            category=self.category,
        )

    def test_home_view_status_code_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "tasks/index.html")

    def test_home_view_contains_tasks_and_form_in_context(self):
        response = self.client.get(reverse("home"))
        self.assertIn("form", response.context)
        self.assertIn("active_tasks", response.context)
        self.assertIn(self.task, response.context["active_tasks"])

    def test_home_view_no_tasks_edge_case(self):
        Task.objects.all().delete()
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("active_tasks", response.context)
        self.assertEqual(len(response.context["active_tasks"]), 0)

    def test_home_view_post_valid_creates_task(self):
        data = {
            "title": "New Task",
            "due_date": date.today(),
            "category": self.category.id,
        }
        response = self.client.post(reverse("home"), data)

        self.assertTrue(Task.objects.filter(title="New Task").exists())

        # Accept either redirect or re-render, depending on your view
        self.assertIn(response.status_code, [200, 302])

    def test_home_view_post_invalid_does_not_create_task(self):
        # Missing title should be invalid
        data = {
            "title": "",
            "due_date": date.today(),
            "category": self.category.id,
        }
        response = self.client.post(reverse("home"), data)

        self.assertFalse(Task.objects.filter(title="").exists())
        # usually re-renders with errors
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertTrue(response.context["form"].errors)

