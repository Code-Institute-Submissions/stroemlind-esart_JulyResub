# E.Stromlind Art (ESART)
amiresponisive image

ES Art is the name of the web application for E.Strömlind art & posters. 
E.Strömlind takes the colorful and vibrant moments in life and makes them abstract and easy for the eye. The inspiration for the posters comes from different types of photos, like concert pictures, fashion editorials from magazines, or random everyday life pictures. All the posters are handmade on acrylic paper, drawn with pen and different types of markers.
This web application exists to display and get the customer a view and an easy way to purchase posters directly or make a request. 
Note: The creator of this web application is the owner of all the images used.

## User Stories

* As a Shopper, I want to get an overview of all the products.
* As a Shopper, I want to be able to see poster all the posters depending on the poster's motive.
* As a Shopper, I want to be able to view a product detail for each product on the page. 
* As a Shopper, I want to be able to like different posters/products and see them on my user page.
* As a Shopper, I want to be able to request a customized poster.
* As a Shopper, I want to be able to create a user profile page for smoother checkouts and be able to edit information when needed.
* As a Shopper, I want to be able to see my order history on my user page.
* As a Shopper, I want to be able to manage the shopping cart by adding, editing, and deleting products in the bag.
* As a Shopper, I want to get confirmation that it went through after purchase.
* As a Shopper, if something goes wrong during the shopping process, I want to get a notification about it.
* As a Store Manager, I want to be able to manage products through the admin page.

## UX
The website design is minimalistic, focusing on the main product, handmade posters. The typography and colors' main point is to create an atmosphere that gives the user a feeling of being in the drawing process of the posters. 

### SEO and KeyWords
### Colour Scheme
The website's primary colors are:
* Black (#000001)
* Cultured white (#F5F5F5)
* Light green color (#E9EFE7)
* Red (#FF0000)

![Colorpallet](documentation/images/colorpallet.png)

[Coolors.co](https://coolors.co/000001-f5f5f5-e9efe7-ff0000) to create the color pallet for the project. The green and white colors give the web application a soft and minimalistic feel to highlight the contrasts of the posters and the logo's diamond edges.
The red color highlights errors or messages to catch the user's attention.
The black color is to connect and contrast the primary colors of the posters. 

![Colors](documentation/images/color.png)

### Typography
#### Fonts
The fonts for this project comes from [Google fonts](https://fonts.google.com/), and are the following ones:
* [Amatic SC](https://fonts.google.com/specimen/Amatic+SC?query=amatic): for h3 headings and the display of poster names. 
* [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montse): The base font family for the project. Used when no other specifications are said.
* [Rock 3D](https://fonts.google.com/specimen/Rock+3D?query=rock+3): This font is for the h1 and h2 heading.

The use of fonts Amatic SC and Rock 3D gives the web application a feeling of hand-drawn letters and connects it to the shop's core product.

#### Icons
For this project, the different icons for the navbar are:
* [hamburger-menu](https://fontawesome.com/v5/icons/align-justify?s=solid)
* [search](https://fontawesome.com/v5/icons/search?s=solid)
* [heart](https://fontawesome.com/v5/icons/heart?s=regular)
* [user](https://fontawesome.com/v5/icons/user?s=regular)
* [shopping-cart](https://fontawesome.com/v5/icons/shopping-cart?s=solid )

, for the pages, like poster-detail.html are: 
* [heart-regular](https://fontawesome.com/v5/icons/heart?s=regular)
* [heart-solid](https://fontawesome.com/v5/icons/heart?s=solid)
* [arrow-left](https://fontawesome.com/v5/icons/angle-double-left?s=solid)

And for the footer:
* [facebook-icon](https://fontawesome.com/v5/icons/facebook-f?s=brands)
* [instagram-icon](https://fontawesome.com/v5/icons/instagram?s=brands)
* [pinterest-icon](https://fontawesome.com/v5/icons/pinterest-square?s=brands)

### Wireframes

#### Mobile

![wireframe1](documentation/wireframes/wireframe1.png)
![wireframe2](documentation/wireframes/wireframe2.png)
![wireframe3](documentation/wireframes/wireframe3.png)
![wireframe4](documentation/wireframes/wireframe4.png)

## Features
### Existing Features
### Features Left to Implement

* A feature left to implement for the future would be to wire up the application to Amazon AWS3 and create a front-end feature to add new posters to the shop and website.

## Technologies Used
These are the following technologies and packages used to develop this project:

* [HTML](https://html.spec.whatwg.org/): HTML5 are used to build the core structure of the web application.

* [CSS](https://www.w3.org/TR/css/): CSS is used to style the web application with colors, fonts, placement of elements, etc.

* [JavaScript](https://www.javascript.com/): JavaScript are used to make the web application more interactive for the User.

* [jQuery](https://releases.jquery.com/): jQuery is a fast, small, and feature-rich JavaScript library to make the web application more interactive for the User.

* [Python](https://www.python.org/): Python is used to build the core structure and code for the project.

* [Heroku](https://www.heroku.com/home): Heroku is the deployment environment used to deploy the project and connected with the GitHub repository.

* [Gitpod](https://gitpod.io/): Gitpod is the development environment used for developing all the code during this project.

* [GitHub](https://github.com/): GitHub are used to store the repository for this project.

* [Git](https://atlassian.com/git/): Git is used to create backups of the project and ensure that all versions of the project is pushed to GitHub.

* [Canva](https://www.canva.com/): Canva is a web application used to create the wireframes for this project.

* [Bootstrap5](https://www.getbootstrap.com/): Bootstrap is a front-end open source toolkit to quickly design and customize responsive mobile-first web application. Bootstrap5 is used to create the base for all the templates in the project.

* [DevTools](https://developer.chrome.com/docs/devtools/): Dev Tools is used to look over the development of the website, debugging problems, and try different approaches to issues that would occur during the process. 

* [Auto Prefixer](https://autoprefixer.github.io/): Auto Prefixer is an application used at the end of the project to give the CSS code some extra properties when used on different browsers.

* [Django Framework](https://www.djangoproject.com/): Django is a free and open source Python web framework for rapid development and clean, pragmatic design. Django is used as the base framework for this project.

### Django packages
To build this project the following packages needs to be installed:
<details><summary>CLICK HERE to expand the full requirements.txt file details</summary>

| Package  | Version | Description |
| ------------- | ------------- | ------------- |
| [Django](https://www.djangoproject.com/) | 3.2 | The Django Framework|
| dj_database_url | 0.5.0 | Utilizes the 12factor inspired DATABASE_URL environment variable to configure Django apps  |
| [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) | 0.48.0 | An integrated Django application for addressing authentication, registration, account management, and social account authentication. |
| [django-countries==7.2.1](https://pypi.org/project/django-countries/) | 2.9.3 | A Django application that provides country choices for use with forms, flag icons static files, and a country field for models (Text from website). |
| [django-crispy-forms==1.14.0](https://django-crispy-forms.readthedocs.io/en/latest/) | 2.9.3 | A way to control the rendering behavior of your Django forms in a very elegant and DRY way. |
| [Gunicorn](https://gunicorn.org/)  | 20.1.0 | Gunicorn is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The server is compatible with various web frameworks and light in server resources |
| [Pillow](https://pillow.readthedocs.io/en/stable/) | 9.1.0 | Pillow is a Python Imaging Library that adds image processing capabilities to the Python interpreter. |
| [Psycopg2](https://www.psycopg.org/docs/) | 2.9.3 | A PostgreSQL database adapter for the Python programming language |
| [stripe==2.74.0](https://stripe.com/se) | 2.9.3 | A workframe to bring together everything needed to build websites and apps that can receive and send payments worldwide.  |
| [Whitenoise](https://whitenoise.evans.io/en/stable/django.html) | 6.0.0 | Whitenoise allows the web app to serve its own static files |


The [requirements.txt](requirements.txt) command for the installed packages is:
- `pip3 install -r requirements.txt`

</details>

## Testing
To view all tests for this project, please refer to the [TESTING.md](TESTING.md) file.

## Deployment
The site was deployed to Heroku. The steps to deploy are as follows:
* Go to the [Heroku](https://www.heroku.com/home) site, [sign up](https://signup.heroku.com/login) for free if you do not already have an account.
    * If creating an account, fill in the signup form with name.
* On the dashboard page, navigate to the Create New App button and click.
* Give the app a unique name; it can not have the same name as another app, choose the region you are currently located in and select Create app.
* Go to the Resources tab and select add a database. In the add-ons box, search for Postgres. Select Heroku Postgres and click Submit Order Form.
* On the apps dashboard page, navigate to the Settings tab.
* On the Settings page, go down to the config vars section. 
* Create the following config vars:
  * Set the key to `DATABASE_URL`, value to `Provided-postgres-link`, and click add. 
  * Set the key to `SECRET_KEY`, value to `Your-SECRET_KEY`, and click add. 
  * Set the key to `DEBUG`, value to `True`, and click add. 
  * Set the key to `DISABLE_COLLECTSTATIC`, value to `1`, and click add.
  * Set the key to `STRIPE_PUBLIC_KEY`, value to `Your-STRIPE_PUBLIC_KEY_API`, and click add.
  * Set the key to `CLIENT_SECRET`, value to `Your-STRIPE_SECRET_KEY_API`, and click add.

Note: Remove DEBUG and DISABLE_COLLECTSTATIC before the final deployment. Also remember to have the env.py file in the **.gitignore** file before the first deployment. So no value information will be visible after deployment.

* To obtain a Stripe key (For this project Stripe is set in Test mode)
  * Go to the [Stripe](https://www.stripe.com/home) site, [sign up](https://dashboard.stripe.com/register) for free if you do not already have an account. 
    * If creating an account, fill in the signup form with email, name, country and password.
  * On the dashboard page, navigate to the Developer button and click. Make sure that the test-mode is on.
  * On the Developer menu, navigate to the API-Keys button and click.
  * Retrive the Publishable key api code.
  * Retrive the Secret Key API by clicking on the reveal Test Key.
    * Make sure that the API keys begins with 'pk_test_...' and 'sk_test_...'.

Note: Remember to have the env.py file and have it in the **.gitignore** file before the first deployment. So no value information will be visible after deployment. Add the Stripes API Keys to the env.py file and set the variables from the env.py file in the settings.py file. 

* To obtain a PostgreSQL DATABASE_URL 
  * Install the supporting libraries by typing in the command 'pip3 install dj_database_url pyscopg2'
  * When done, type in the command `pip3 freeze --local > requirements.txt` in the terminal
  * In the env.py file, import os. 
  *  Setup the following environment variable: 
      DATABASE_URL and paste in the DATABASE_URL from Heroku.
      ```os.environ['DATABASE_URL'] = 'postgres://***************'```

  * In the settings.py file, import os dj_database_url.
    So scroll down to the DATABASES section and comment out the entire section. 
    Below the comment out section, add in the following code: 
    ```DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}```

* Navigate to the Deploy tab and down to the section called Deployment method. 
* Select GitHub and confirm the connection between Heroku and GitHub.
* Search for the project's repository name on GitHub and click "connect" to link GitHub with Heroku.
* On the same page, scroll down and choose how to deploy the app. For this project, automatic deploys are selected and enabled.
* Create a **Procfile** for Heroku, inside the file insert the following line:
    - `web: gunicorn cosmos.wsgi`
    * Note that cosmos is the name for this app.
    
* Create a **requirements.txt** file for Heroku, using the following command:
    - `pip3 freeze --local > requirements.txt`

The live link can be found here - [https://es-art.herokuapp.com/](https://es-art.herokuapp.com/)

### Local Deployment
In order to make a local copy of this project, you can type the following into your IDE Terminal to clone this repository:

- `git clone https://github.com/stroemlind/esart.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/stroemlind/esart)
## Credits
### Content
Color choose: 
[Coolors.co](https://coolors.co/)

Fonts:
[Google fonts](https://fonts.google.com/)

Icons:
[FontAwesome](https://fontawesome.com/)

List in footer for icons:
[Unused-css](https://unused-css.com/blog/css-horizontal-lists/)

Secret Key generator:
[Miniwebtool](https://miniwebtool.com/django-secret-key-generator/)

Round Menu Button:
[W3school](https://www.w3schools.com/howto/howto_css_round_buttons.asp)

Menu Button:
[Codepen](https://codepen.io/seme332/pen/reJOwo)
[Getcssscan](https://getcssscan.com/css-box-shadow-examples) nr.9
[W3school](https://www.w3schools.com/cssref/tryit.asp?filename=trycss_position2)

White Noise:
[White Noise](http://whitenoise.evans.io/en/stable/index.html)
[Devcenter](https://devcenter.heroku.com/articles/django-assets)

mobile wireframe base:
[imockups](https://imockups.com/iphone-xs-wireframe-template_3884)

Canva for wireframe design:
[Canva](https://www.canva.com)

Remove item from cart
[Devdreamz](https://devdreamz.com/question/533451-remove-an-unique-item-from-shopping-cart-in-django)

Django countries:
[Django Countries](https://pypi.org/project/django-countries/)
[Django Countries get countries](https://pypi.org/project/django-countries/#get-the-countries-from-python)

Toasts help:
[Stackoverflow](https://stackoverflow.com/questions/56503954/bootstrap-toast-does-not-show-up)

Newsletter:
[YouTube](https://www.youtube.com/watch?v=TBVsILIt4HM&list=PLGzru6ACxEAKtb29AeyHbVGUh2-0r891H&index=20) Video 20 - 26.
[Stackoverflow](https://stackoverflow.com/questions/66371279/how-to-create-a-simple-form-in-the-base-html-template-django)

Request form image:
[GeeksforGeeks](https://www.geeksforgeeks.org/imagefield-django-forms/)

Stripe
[Stripe Card](https://stripe.com/docs/payments/cards/overview)
[Stripe Elements](https://stripe.com/docs/payments/elements)
[Stripe Create Payment Element](https://stripe.com/docs/js/elements_object/create_payment_element)
[Stripe JS Docs](https://stripe.com/docs/js)
[Stripe Testing](https://stripe.com/docs/testing)

Customer like page
[Stackoverflow](https://stackoverflow.com/questions/63547411/django-filter-liked-posts-by-user )

jQuery for index request poster form:
[jQuery](https://api.jquery.com/submit/ )

Bootstrap:
[Bootstarp5](https://https://getbootstrap.com/docs/5.1/getting-started/introduction/)


[](https://)
[](https://)
### Media
### Acknowledgements (edited) 
