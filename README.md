# pCMS

pCMS is an example project and shows how we can easily make django's FlatPages a little more better. By subclassing the original FlatPages and adding some fields of our own. We added description and keywords fields which are needed for SEO.
Added extra fields for scripts and css giving the opportunity to the designer of the page to add his own. Added also a published flag for each page giving the designer the ability to publish or not a page at will.
We can take advantage of the registration required field and display pages only to logged in users and use it also for the menus.

It contains an automatic grouping of flatpages under the same starting url and constructs an appropriate menu for them. Menus also have a registration required field to be shown only to logged in users.

Comments can be enabled for a particular page. Only logged in users can comment. Th user can delete his own comments and admin can delete everybody's.

There is also a search function which searches for text at the context of every page. The search algorithm is done with normalizing queries and searches directly the db. A quick hack provided by [Julien Phalip](http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap).

It provides the [tinymce](http://www.tinymce.com/) editor at the admin interface to edit the contents of the page and it's integrated with the [elFinder](http://elrte.org/elfinder) filemanager to upload and manage images and scripts.

The css provided with the project is [bootstrap](http://twitter.github.com/bootstrap/). A highly customizable and complete css framework suitable even for mobile devices.

The SecureRequiredMiddleware used is responsible for securing, with https, specified urls of the site. By changing:

    HTTPS_SUPPORT = False

to True and including the desired urls at:

    SECURE_REQUIRED_PATHS = (
        '/login/',
    )


### Installation

Clone or fork this repository. Go to project's root and issue:

    ./manage.py syncdb
    
This will create the db needed and load some startup example pages and a menu.

After creating the database delete or rename the file *initial_data.json* because it will be loaded every time you do *syncdb*.

Run the server as always with:

    ./manage.py runserver

### Usage

Go to the admin interface and add pages and menus. For example:

* Add a menu with the url */services/*
* Add pages with urls starting with the above: */services/design/* , */services/hosting/*
* All this pages will be grouped under the same menu.


