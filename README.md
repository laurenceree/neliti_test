# Neliti

This is Neliti test

## Task 1: Django ORM

Neliti is primarily a website that hosts academic publications. We record views and downloads of these publications in order to give statistics to our customers. This task is about analyzing view and download data to produce some meaningful insights. Here is an excerpt of two models:

```
class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)

class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted
```
A Publication represents a single journal article on our website (example). Each time a user accesses a publication, we create a new Hit instance. A Hit represents either a single view or a single download of a publication. Publications are arranged into collections called journals - a Journal is a collection of publications of similar subject matter.
Your task is to write a function get_journal_statistics() that returns a dict mapping journals to summary statistics:

```
def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    return summary

```

The return value should be a dict giving summary statistics for all journals in the form
{journal_id -> (total_views, total_downloads)}
where
journal_id is the primary key of the journal instance in the Journal table
total_views is the total number of Hit instances for all publications in that journal and all time with action == Hit.PAGEVIEW
total_downloads is the total number of Hit instances for all publications in that journal and all time with action == Hit.DOWNLOAD.
All journals should be present in the result, and your code should correctly handle cases where there are no hits of the given type.


## Task 2: Django services and frontend

The specification of this task is vague - as are most of the tasks in real life. 🙂 
You will need to balance your time and imagination. If you are out of time, feel free to provide a very basic solution, but for bonus points, add any feature, UX or functional.

The task is simple: Create a small weather app in Django. 

The app can use the met.no service to acquire data via a GET call - on the server side: https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25 - you need to pass the coordinates only. In the application you need to create a way to input the location and then use that information to display weather information. The whole UX is up to you. (Hint: you will only use a fraction of the data from this service!)

Please create a git repo and update it with your code - as it develops. Try to commit as frequently as possible - with meaningful comments - just as you would do in a real project. At the end of the task, please share the link to your repo.


## Task3: CSS

Spend no longer than 15-20 minutes on it, we don't expect it to be a perfect match, however please note the different borders or fill colors. Please explain your solutions with comments.

HTML:
```
<html>
  <head>
  </head>
  <body>
    <button>download</button>
  </body>
</html>


CSS:
button {
    Insert your solution here
}

```
