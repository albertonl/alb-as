# Alternative database engines

If you want to check your own database engine's compatibility with ALB-AS, please refer to the section "Compatibility" in the [main README.md](https://github.com/albertonl/alb-as/blob/master/README.md) and see whether or not it is listed as compatible.

By default, ALB-AS uses SQLite as the default database engine. When you run `createdb.py`, an SQLite database will be created in this directory under the name `db.sqlite3`. However, you may want to use your own database engine (e.g. MySQL, PostgreSQL). To accomplish this, we have two options:

## Option A: URI via environment variable

This is a better way to do this if you plan on changing engines quickly, but it may be a little tricky to set up. If you want to use this method, follow these steps:

1. Import the `os` module in both `createdb.py` and `scraper.py`. To do this, add this line on top of both files:

```python
import os
```

2. Replace any occurrences of `'sqlite:///db.sqlite3'` in both files by:

```python
os.getenv("DATABASE_URL")
```

Or, if you prefer:

```python
os.environ.get("DATABASE_URL")
```

3. **Every time** you want to run either `createdb.py` or `scraper.py`, remember to export the value of your `$DATABASE_URL` environment variable by running on the Bash console:

```bash
$ export DATABASE_URL=<YOUR-DATABASE-URI-GOES-HERE>
```

If you are using a Windows machine, instead run:

```batch
> set DATABASE_URL=<YOUR-DATABASE-URI-GOES-HERE>
```

If you don't know what your database URI, it usually looks something like this:

```
<DATABASE-ENGINE>:///<DATABASE-NAME>
```

Examples: `sqlite:///db.sqlite3`, `postgresql:///mydatabase`.

Make sure you always do this **before** running any other file. Otherwise, SQLAlchemy will not know what database to refer to. Additionally, you can, with the help of some module like `python-dotenv` automatically export the DATABASE_URL environment variable every time you run a file within this directory.

## Option B: hardcoded URI

This is, in my opinion, the best method if you are using a local database, and not planning to change it in a long time. In case you are using a **database hosting service**, such as Heroku Postgres, I strongly recommend choosing **option A** as to avoid anyone who has access to the code on your machine being able to control your remote database.

If you stick with this option, there is one simple step to do. Simply replace all ocurrences of `'sqlite:///db.sqlite3'` inside both `createdb.py` and `scraper.py` by your database URI.

