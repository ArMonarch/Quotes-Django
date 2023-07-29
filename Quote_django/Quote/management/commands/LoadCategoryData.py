from csv import DictReader
from django.core.management.base import BaseCommand
from Quote.models import Category

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    #show this when user types help
    help = "Load Data from Data.csv"
    
    def handle(self, *args, **options):
        # Show this if the data already exist in the database
        if Category.objects.exists():
            print("Category Data Already Loaded \nExiting the System......")
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        
        #Show This Before Loading The Data into the Database
        print("Loading Data Into The DataBase..........")
        
        #Code to Load Data into The DataBase
        for row in DictReader(open("./static/Data/Data.csv")):
            category = Category(Name = row["Name"], Description = row["Description"])
            category.save()    