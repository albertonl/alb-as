# ALB AulesScraper (ALB-AS)

![test coverage 79%](https://img.shields.io/badge/test%20coverage-79%25-yellow.svg) ![build failing](https://img.shields.io/badge/build-failing-red.svg) ![current version 0.1.1](https://img.shields.io/badge/current%20version-0.1.1-blue.svg) ![stage beta](https://img.shields.io/badge/stage-beta-blue.svg)

![python version 3.6.9](https://img.shields.io/badge/python%20version-3.6.9-orange.svg) ![database engines SQLite PostgreSQL MySQL](https://img.shields.io/badge/database%20engines-SQLite%2c%20PostgreSQL%2c%20MySQL-orange.svg)

ALB AulesScraper is a web scraper and automatic emailer for Aules written in Python. It will notify you of any new courses or tasks added to your profile.

## Setup

1. Make sure you have installed a copy of Python (at least 3.6.8) on your machine.

2. Create a virtual environment for this project. To accomplish this, run `$ virtualenv <NAME-OF-YOUR-ENV>`. If `virtualenv` is not installed on your machine, run `$ pip install virtualenv` first.

3. Activate your virtual environment: `$ source <NAME-OF-YOUR-ENV>/bin/activate`

4. Install all required dependencies via pip: `$ pip install -r requirements.txt`

5. Move to the `src/` directory and run `createdb.py` (`$ python createdb.py`). This script will create an SQLite3 database that will store your courses and tasks data. Please refer to "[DB setup and alternative database engines](https://github.com/albertonl/alb-as/blob/master/src/README.md)" to learn how to set up your database, or in case you prefer using another database engine, such as MySQL or PostgreSQL, for further information.

6. Add your Aules and Gmail credentials to a new file called `auth.py` inside the `src/util/` directory. Refer to "[Authentication setup](https://github.com/albertonl/alb-as/blob/master/src/util/README.md)" for instructions on how to do this.

7. Move back to the `src/` directory and run `scraper.py` (`$ python scraper.py`) and get your update right into your inbox.

## Testing

If you want to help us by testing this application, follow the steps 1 to 4 described in the section "Setup" above.

Now, export the `DATABASE_URL` environment variable to the relative path of your database (in case it is a database in your filesystem). For instance, if your database is an SQLite3 database called `db.sqlite3`, and stored inside the `src/` directory, `DATABASE_URL` should hold the value `sqlite:///src/db.sqlite3`. Refer to "[DB setup and alternative database engines](https://github.com/albertonl/alb-as/blob/master/src/README.md)" for further instructions on how to do this.

To run all tests, run, from this directory (same for Windows):

```bash
$ pytest
```

Optionally, if you want to run only a specific group of tests (they are grouped by files), proceed to run this instead:

```bash
$ pytest test/<FILENAME>
```

Of course, replacing `<FILENAME>` by the corresponding name of the tests file. As of now, there are two testing files available (the filenames you can replace `<FILENAME>` by):
- `test_general.py`: test the main function, `src.scraper.main()`.
- `test_tools.py`: test the tools defined in `src.util.course_scraper` and `src.util.emailer`.

## Version History

- **v0.1-beta** (April 2020): ALB-AS for basic scraping of courses and tasks. Email support Gmail only.
  - **v0.1.1-beta** (May 2020): Added support for Aules4, improved test coverage to 79%. **Build failing**. Bug fixes and improvements.

## Compatibility

### Aules compatibility

The last supported version of Aules is Aules4, the latest available version as of May 5 2020.

### Python compatibility

This application has been tested in Python 3.6.8 and 3.6.9.

### Database engine compatibility

The application has been tested with the SQLite and PostgreSQL database engines, and the SQL syntax is valid for at least MySQL as well.

## Contact and bug report

If you have any questions, please email us at <albertonl.dev@gmail.com> or open an issue here.
