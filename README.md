# UP CEBU UNISO (Unified Student Organizations) Site

#### The UNISO Site is an all-in-one website for recognized student organizations in UP Cebu which serves as an avenue for proper information dissemination among the student-managed organizations in the said institution.

### STEPS in SETTING UP THE WEBSITE in your LOCALHOST

**Important Reminders:**
* Place the folder in your preferred directory path.
* This app is using PostgreSQL for storing significant data so it is important to have such database management system in your computer.
* This app is also using Python and Django in its backend framework so be sure to install necessary files and download important ones such as the psycopg2.
* Another is that this is a web application and is using BootstrapCDN that loads necessary CSS and JS files remotely, from its servers so make sure you have a steady internet connection to not encounter distorted user interface.

**Let's Get Started. **

1. Open the command line and create a database
   a. by entering --> psql --username=<username of your postgresql database> --password <ENTER then enter password>
   b. upon entering, key in --> create database <"orgsite" is preffered> owner postgres <ENTER>
   c. CTRL C once the database is created
   NOTE: change the Databases information in the settings.py according to your own database details
1. Proceed to the directory path of the application's folder.
1. Key in --> python manage.py makemigrations and then python manage.py migrate
1. Once completed, create a superuser/admin --> python manage.py createsuperuser
1. Run the server --> python manage.py runserver
1. Lastly, open 127.0.0.1:8000 to start using the application.
1. Proceed to Django Admin to begin populating the database using the superuser credentials

### **FEATURES AND FUNCTIONS**

**VIEW ORGANIZATION PROFILE** - As a guest, without even logging in, anyone can already view the organization's profile. One can navigate through what the organization is ABOUT and what ACTIVITIES the organization is having. In the ABOUT tab, you can see information about the organization and how you can reach out to its officers via social media. In the ACTIVITIES tab, you can view the list of activities or announcements starting from the recent ones up until the old ones.

**LOGIN AND LOGOUT** - Note: the superuser account can not be used as an account of any organization. If you successfully log into the website, it will let you access your organization's profile. If you failed to get in, it will stay in the homepage where you are told at the Login dropdown that the credentials you inputted are invalid. You can still access your organization's profile but you can only view what's in it. No editing. No adding. No deleting. Just viewing. There is also a logout feature to prevent compromising of data when you are no longer trying to do some additions and modifications in your profile.

**SEARCH ORGANIZATION** - In the section after the UNISO Site cover homepage, the search engine

**VIEW LATEST POSTED ACTIVITIES** - In another section in the homepage, the latest 6 activities, could be events or announcements, posted by the different organizations are placed in a slider for the users to swipe for easy navigation. These 6 activities are arranged in a manner that the latest posted activity is on the first slider followed by the later ones. Beside the slider is a set of basic information about the activity. The name of the organization can be clicked, and it redirects the page to the organization's profile to read more about the event. 

**VIEW LIST OF ACTIVITIES** - Under the slider for the 6 activities, a button can be found so the users can be able to view not just 6 but all the activities posted by the organizations in another page. The list of activities are also arranged in a way that the latest one is found in the beginning followed by the later ones. Similar to the slider, every activity has an organization name which is also clickable that can proceed to the organization's profile to learn more about the event or announcement, and its other activities.

**SEARCH RESERVED VENUES** -

**VIEW FAQs** - We also added a page for Frequently Asked Questions to resolve confusions by providing answers to these. It has a separate page where you can click on the questions and have your answers revealed after clicking.

**VIEW PROFILE** - After loggin in, the user can already view the organization's profile where it can perform certain functions that will be discussed later. There are certain features and functionalities that can only be seen if the user is logged in which can not be seen by those who are not logged in or just guests. The Profile contains the organzation's basic information. You can also view other organization's profile and you will not see buttons that can add, modify and delete information in their profile.

**EDIT PROFILE** - One of the functions that the user can do is to edit the information in the profile page. The Edit Profile Button can be found in under the name of the organization. One can change the organization's name, shorten name, email, phone, description, mission, vision, social media sites, and even with or without the organization logo. This is necessary especially that officers change from year to year.

**VIEW ACTIVITY** - At the ACTIVITY Tab, you may view the Activity  and all its basic information such as when it was posted, the title and content, and also the publicity material, if necessary. Beside it is a dropdown where you may edit or delete such activity. In another organization's Activity Tab, you cannot see this dropdown as you do not have the privilege to do it. 

**ADD ACTIVITY** - Beside the Edit Profile Button is the Add Activity Button where you can add a new activity to be added the organization's list of activities. The activity added can either contain a publicity material or nothing.

**EDIT ACTIVITY** - Another important feature is the Edit Activity which can be found beside each posted activity. It is important as  it can result to a human error which is most of the time, unavoidable and that these errors are need to be resolved without deleting the activity and adding a new one. Moreover, most of the time, activities do not pursue according to what it is scheduled for. Sometimes, it gets cancelled or moved to another venue. That is what it is important to have a feature such as these to resolve these unavoidable errors.

**DELETE ACTIVITY** - Of course, when the organization intends to take down a post, it must be heard therefore the Delete Actvity feature should be available. Deleting an activity can remove the activity fromm organization's profile's Activity Tab, from the Activities on Slider, if it is one of the six activities, and from the List of All Activities. Once deleted, it can not be recovered anymore.