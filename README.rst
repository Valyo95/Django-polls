=====
Polls
=====

Polls is simple Django app to condict Web-based polls. Fore each
question, visitors can choose between a fixed numver of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS settings like this::

   INSTALLED_APPS = [
        ...
        'polls'
   ]

2. Include the polls URLconf in your project urls.py like this::

   path('polls/', include(('polls.urls')),

3. Run 'python manage.py migrate' to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
