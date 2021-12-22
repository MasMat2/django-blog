add app to installed app list for django to get the templates
template inheritence

Part 7
user built in managment system
    user.is_authenticated
    @login_required decorator
    add settings to configure built in managment system

Part 8
One to one relationsips
Manage static files:
    Media root
    Media url
    Url pattern
Signals:
    Sender, receiver
Reverse for 'admin-site' not found. 'admin-site' is not a valid view function or pattern name.

Part 9
merge forms
File upload handling:
    add encoding type for files #enctype="multipart/form-data"
    files located at request.FILES on POST
    https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/
Create a form to edit an existing Article, but use POST data to populate the form. # request.POST, instance=request.user