# Django bulk insert test

This is a test of the bulk_create method of the Django ORM.

Versions:
python 3.7.1
Django 2.1.5

In the official Django documentation, the bulk_create method is described with the limitation:

> If the model’s primary key is an AutoField it does not retrieve and set the primary key attribute, as save() does, unless the database backend supports it (currently PostgreSQL).

Yet with MySQL and sqlite backends, the current version of Django _does_ create a primary key. This is very nice.

`python3 manage.py bulk_insert`

before bulk_create:
```
[<Item: (None) 714893>, <Item: (None) 871190>, <Item: (None) 871068>, <Item: (None) 206753>, <Item: (None) 249027>]
```

getting the newly created items:
```
<QuerySet [<Item: (1) 714893>, <Item: (2) 871190>, <Item: (3) 871068>, <Item: (4) 206753>, <Item: (5) 249027>]>
```

see the code in `inserter/management/commands/bulk_insert.py`
