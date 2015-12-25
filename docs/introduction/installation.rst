############
Installation
############


*******************
Installing packages
*******************

We'll assume you have a django CMS (version 3.x) project up and running.

If you need to set up a new django CMS project, follow the instructions in the `django CMS tutorial
<http://docs.django-cms.org/en/develop/introduction/install.html>`_.

Then run either::

    pip install aldryn-events

or to install from the latest source tree::

    pip install -e git+https://github.com/aldryn/aldryn-events.git#egg=aldryn-events


********************
Edit ``settings.py``
********************

In your project's ``settings.py`` make sure you have all of::

    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_translation_tools',
    'aldryn_reversion',
    'aldryn_common',
    'aldryn_events',
    'appconf',
    'bootstrap3',
    'django_tablib',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'extended_choices',
    'filer',
    'parler',
    'sortedm2m',
    'standard_form',

listed in ``INSTALLED_APPS``, *after* ``'cms'``.

.. note::
   If you are using Django 1.6, add ``south`` to  ``INSTALLED_APPS``.

   If you are using Python 2.6 please remove ``django_tablib`` from
   ``INSTALLED_APPS`` because this package does not supports both
   Python 2.6 and Django 1.6.


Filer
=====

Aldryn Events also depends on Filer, be sure to follow
`Filer's installation instructions <http://django-filer.readthedocs.org/en/latest/installation.html>`_.
To get up and running quickly, make sure you adapt your settings to include the
``filer.thumbnail_processors.scale_and_crop_with_subject_location`` thumbnail processor: ::

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        # 'easy_thumbnails.processors.scale_and_crop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )


****************************
Prepare the database and run
****************************

Now run ``python manage.py migrate`` to prepare the database for the new
application, then ``python manage.py runserver``.


****************
For Aldryn users
****************

On the Aldryn platform, the Addon is available from the `Marketplace
<http://www.aldryn.com/en/marketplace>`_.

You can also `install Aldryn Events into any existing Aldryn project
<https://control.aldryn.com/control/?select_project_for_addon=aldryn-events>`_.
