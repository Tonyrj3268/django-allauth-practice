# Django Third-Party Authentication Practice

## Overview

This project aims to practice third-party authentication in Django using Django-allauth. For a more refined UI, the project employs `django-allauth-ui`.

## Version Compatibility

**Note**: Use `django-allauth = "0.57.0"` for compatibility with `django-allauth-ui`.

## Important Reminder

**Ordering in `INSTALLED_APPS`**: It's crucial to place `allauth_ui` before `allauth` in the `INSTALLED_APPS` section of your Django settings to properly override the default allauth templates.

For example, your `INSTALLED_APPS` should look something like this:

```
INSTALLED_APPS = [
    ...
    # prettier allauth templates
    "allauth_ui",
    "widget_tweaks",
    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    ...]
```

## Further Reading

For additional details and configurations, you can refer to the [allauth documentation](https://docs.allauth.org/en/latest/).
