![(assets/image/Amiresponsive.PNG)](assets/image/MeetEcoresponsive.PNG)


# **MeetEco**

MeetEco is an easy event creator based on ecological concerns.




## **User Experience**

 The navigation bar is at the head of the page easily visible. 
 The "Home" button and the logo will take you right back to the landing with hero image and website motto.   
 "How it works" tab will take you to short explanation about how to use the website.
 "See the events" tab will take you to the events created.    
 "Create an event" will take you to a form in order to create the event
 In the footer you can find the email to contact me and navigation link to the pages, also a link to send the user to top of the page.

#### **User Stories**


As a user I would like  
* to have clear understanding what is the purpose of the website.
* to see how can I use the website.  
* to be able to create an event
* to be able to edit or delete the event when I need to.
* to see the created events and if I am interested, to be able to attend.
* to be able to contact someone when I need to.


As a owner I would like
* to make sure users will understand how to interact with the website.
* to make sure the user create ecological concern based events.
* to make sure only the creator is able to change or delete the event.
* to ensure the user can contact me if they see any fault or suggestion to improve the website.


### **Strategy**

I wanted to answer users common questions such as "Is this what I expected to see?", "Does it offer what I want?",
"Is it valuable enough for me to return?". 
For this website I aimed to create an user friendly, intiuitive structure. To do that I tried to create a simple but visually appealing website

### **Scope**

This website scope are those people who would like to create events based on ecological concerns, therefore I limited the event categories.   


### **Structure**

The website is built in home, create and edit sections:  
Home page has 4 sections:  
"Landing" has hero image and website motto sharing the screen large and medium sizes. 
"How it works" gives the short details about how to use the website.
"See the events" displays all the events to the website visitors anyone can see the any events happening with details in materialized card and can show their interest by providing their details.  
Also the creator can edit their events with the id provided when they created the event. This will take the user to edit page.
"Footer" is a responsive footer, pinned to the bottom of the page, with Contact Details, links to the navigation for the website.


"Create an Event" page allow user to create event. I kept the events limited so user will only create climate concern based events. As the user  
create an event there will be an modal screen that informs the user about the event id and that they can change or delete it with this unique code.




### **Skeleton**

I tried to give as many information as I can with minimal choices. Navigation has "home", "how it works" and "see the events" and "create an event" sections.  
The website prototype I have designed is [here](wireframe/MeetEco.pdf).  
### **Surface**

The colors I used in this project were:  


![(assets/image/MeetEcopallete.png)](static/images/pallete.png)  


I used Google fonts for the website; font *"Monoton"* for the website motto , font *"Oswald"* for the headings and, *"Lato"* for the paragraphs and contents. 

## **Features**
### **Existing Features**


User can
** navigate through the site with Navbar, they can go to how it works and see the event section.
** get more information about the events on the events section.
** create an event based on solutions to world's ecological problems.
** see the event id as soon as they created.
** show interest by providing user details.
** creator can update or delete the event once they provided the given id number.


### **Features Left to Implement**
* At the moment in order to edit or delete the event, user has to provide the unique event id 
  this is not secure or user friendly option so in the future I would like to set login page  
  for user to register and login to Create an user account to control event creation, edit and delete options.  
* I would like to add a filter option for the events based on location so user can see nearby events.
* Make user able to add more event categories to widen the event options.
* Make user able to add pictures they choose.


## **Technologies Used**

  * HTML


  * CSS


  * Javascript 


  * [Bootstrap](https://getbootstrap.com/)


  * [Google Fonts](https://fonts.google.com/) *Lato*, *Oswald*, *Monoton*


  
  * [Fontawsome](https://fontawesome.com/) for the event categories icon.


  * [Materializecss](https://materializecss.com/) for the designing the card and footer.

  
### Back-End Technologies
* Flask - Used as the microframework.
* Jinja - Used for templating with Flask.
* Heroku - Used to host the application
* Python - The back-end programming language.
* Pymongo - Used to connect the python with the database.
* MongoDB Atlas - Used to store the database.

### Database Schema
The application uses MongoDB for data storage. MongoDB was chosen as the database to use due to the unstructured format of the data that will be stored within it.  
The data stored in the database are the following:

...* Object  
...* String  
...* Array  
### Data structure  

#### Event_categories  
| Title         | 	Key in db	    |  Data type |  
| ------------- |:-----------------:|-----------:|
| event_id      |      _id          |ObjectId    | 
| event_name    | Event name        |String      | 
| event_picture | path to the image |String      |

#### Events

| Title             | Key in bd         | Data     |
| -------------     |:-----------------:| --------:|
| event_id          | _id               | ObjectId |
| organiser_name    | Name              |   String |
| event_description | Event description |   String |
| event_date        | Event date        | String   |
| guests            | attenders details | Array    |
## **Testing**
To test the website I have used Google developer tools during and after creating the site to check CSS elements and website responsiveness,  
"console" to see API and function errors, "source" for js function and typing errors and "network" tab to test APIs responding correctly.  
I tested the responsivenes between different mobile devices using Google developer tools. I also tested it in most common browsers such as Chrome, Mozilla,  
Safari, Opera.  
I tested my html code with [W3C HTML Validator](https://validator.w3.org/). I fixed the erros and warnings accordingly.  
I tested my CSS code with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).I fixed the errors and warnings accordingly.
I tested my Javascript code with [JSHint](https://jshint.com/) there was typing error such as missing semicolon and undefined variables, these were also fixed accordingly.

## **Deployment**

In order to deploy the repository from GitHub I follow these steps.
1. From GitHub repositories dashboard I selected "MeetEco".
2. I went to Settings and "GitHub Pages" heading.
3. I chose the "master branch" option from the "source" dropdown menu.
4. This action refreshed the page and a ribbon appeared saying "Your site is published at  (https://ozluna.github.io/MeetEco/ ) with the the live link which indicated me that deployment was successful.

#### To run locally:
Save a copy of the github repository located at https://github.com/ozluna/MeetEco by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder.  
If you have Git installed on your system, you can clone the repository with the following steps:  

* Open Git Bash.

* Change the current working directory to the location where you want the cloned directory.

* Type git clone, and then paste the URL you copied earlier.

  `git clone https://github.com/ozluna/MeetEco`  

* Press Enter to create your local clone.


## **Credits**
I used Google Places Documentation and [codelabs developers](https://codelabs.developers.google.com/) when I created the code to find the user's location 
script and I found some help on ["stackoverflow"](https://stackoverflow.com/questions/29734251/google-places-js-api-show-reviews) for the script to call the reviews.  SendEmail function was created with help of documentation from EmailJs and code institute lessons.  


All the images are created on [Canva](https://www.canva.com/)  
Social link icons are taken from [Fontawsome](https://fontawesome.com/)  
Animation on the greeting is from [Animista](https://animista.net/)  
For responsiveness I used [Boostrap](https://getbootstrap.com/)  
For fonts I used [Google Fonts](https://fonts.google.com/)  


## **Acknowledgements**

In the process of finishing this website I used many resources mainly, Google Places documentation, MDN web docs, W3Schools, Stack Overflow.  
Youtube channels such as Travers media, online resources [goalkicker](https://goalkicker.com), code institute videos and last but not least my mentor and tutors help.




