"""tarmar-auth — a small reusable Django login app shared across projects.

Provides a concrete, project-agnostic ``User`` model plus register / login /
logout / profile views, forms, templates, and URLs. A consuming project adds
``"tarmar_auth"`` to ``INSTALLED_APPS``, sets ``AUTH_USER_MODEL =
"tarmar_auth.User"``, and includes :mod:`tarmar_auth.urls`.

The user model is intentionally minimal (a plain ``AbstractUser``); projects
that need extra fields can add their own related model rather than forking this.
"""
