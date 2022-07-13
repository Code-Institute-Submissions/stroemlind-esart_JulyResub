# Testing
There was always a tab open for testing with the website preview through Gitpod port 8000. To check up on my code and see if it worked as I wanted. I used DevTools to see how the code would respond if I added or changed properties or values with CSS or Bootstrap. I also took help from DevTools to check the responsiveness when decreasing or increasing the screen size. To see and test the website's performance, I used Lighthouse, for both mobile and desktop usage, which gave me an updated report to see how well my performance, accessibility, and SEO were for the website.

To see that the JavaScript code in the project worked without any bugs, I used the console section of DevTools to know that it rendered as it should.

Several internet browsers, like Chrome, Mozilla Firefox, Microsoft Edge, and Safari, were used during all the testing. It works on all the mentioned internet browsers and mobile devices.
## Code Validation

### HTML
There are no errors form the offical [W3C Validatior](https://validator.w3.org/).

   ![HTML-validation](documentation/testing/html1.png)
    
  Link to the validation for the home page: [W3C Validatior](https://validator.w3.org/nu/?doc=https%3A%2F%2Fes-art.herokuapp.com%2F)

### CSS
There are no major errors form the offical [Jigsaw validator](https://jigsaw.w3.org/css-validator/). I am aware of the warnings.

  ![Css-validation](documentation/testing/css1.png)

  ![Css-validation-warning](documentation/testing/css-warning.png)
    
  Link to the validation: [Jigsaw validator](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Fes-art.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)

### JavaScript
No errors where found when going through the offical [Jshint validator](https://jshint.com/).
* There are 4 functions in this file.
* Function with the largest signature take 1 arguments, while the median is 1.
* Largest function has 8 statements in it, while the median is 4.5.
* The most complex function has a cyclomatic complexity value of 3 while the median is 1.5.
I am aware of the warning about the Stripe element, but to setup this code I followed the lessons and Strip documentation. Do not cause an issue with the functionality of the code. 

    ![script.js](documentation/testing/jshint.png)

### Python
The code passed through [PEP8 linter](http://pep8online.com/). The result confirmed there are no problems with the code.

![PEP8](documentation/testing/pep8forms.png)

## Browser Compatibility
### Google Chrome
The website runs without any issues in the Google Chrome browser

  ![Chrome](documentation/testing/desk-posterdetail1.png)

### Mozilla Firefox
The website runs without any issues in the Mozilla Firefox browser

  ![Firefox](documentation/testing/firefox.png)

### Microsoft Edge
The website runs without any issues in the Microsoft Edge browser

  ![Edge](documentation/testing/edge.png)

### Safari
The website runs without any issues in the Safari browser

  ![Safari](documentation/testing/safari.png)

## Responsiveness
This section provides images of the tests for responsiveness on different screen sizes.

### Desktop
#### Home
![Home page](documentation/testing/desk-home.png)

#### Menu/Navbar
![Menu/Navbar](documentation/testing/desk-menu.png)

#### Sign Up/Login/Sign Out/Profile page
![Signup](documentation/testing/desk-signup.png)

![Login](documentation/testing/desk-login.png)

![Signout](documentation/testing/desk-signout.png)

![Profile page](documentation/testing/desk-profile.png)

#### Posters view, category and detail view
![All Posters](documentation/testing/desk-posters.png)

![Category page](documentation/testing/desk-categorypage.png)

![Poster detail view](documentation/testing/desk-posterdetail1.png)

#### Add, Edit and Delete Posters
![Add Poster 1](documentation/testing/desk-addposter.png)

![Add Poster 2](documentation/testing/desk-addposter1.png)

![Edit Poster 1](documentation/testing/desk-editposter1.png)

![Edit Poster 2](documentation/testing/desk-editposter2.png)

![Delete Poster](documentation/testing/desk-deleteposter.png)

#### Request Poster Form
![RequestPosterForm](documentation/testing/requestform1.png)

#### Liked Posters page
![Liked posters page](documentation/testing/desktop-likedpage.png)

![Liked posters page](documentation/testing/desktop-likedposters.png)

#### Shopping Cart
![Cart No free](documentation/testing/desk-checkout.png)

![Cart free](documentation/testing/desk-cartfree.png)

![Cart empty](documentation/testing/desk-emptycart.png)

#### Checkout/Checkout Success
![Checkout page](documentation/testing/desk-checkout1.png)

![Checkout payment](documentation/testing/desk-checkout2.png)

![Checkout Success](documentation/testing/desk-successbuy.png)

#### Footer/About Us/Terms & Conditions
![Whole footer](documentation/testing/footer1.png)

![About Us](documentation/testing/aboutus.png)

![Terms & Cond](documentation/testing/terms.png)

### Tablet
#### Home
![Home page 1](documentation/testing/tablet-home.png)

![Home page 2](documentation/testing/tablet-home2.png)

![Request Form](documentation/testing/tablet-requestform.png)

#### Menu/Navbar
![Menu/Navbar](documentation/testing/tablet-menu1.png)

![Menu/Navbar](documentation/testing/tablet-menu2.png)

![Menu/Navbar](documentation/testing/tablet-menu3.png)

#### Sign Up/Login/Sign Out/Profile page
![Signup](documentation/testing/tablet-signup.png)

![Login](documentation/testing/tablet-login.png)

![Signout](documentation/testing/tablet-signout.png)

![Profile page 1](documentation/testing/tablet-profile1.png)

![Profile page 2](documentation/testing/tablet-profile2.png)

#### Posters view, category and detail view
![All Poster view](documentation/testing/tablet-posters.png)

![Category page](documentation/testing/tablet-category.png)

![Poster detail view](documentation/testing/tablet-posterdetail.png)

#### Add, Edit and Delete Poster view
![Add Poster](documentation/testing/tablet-addposterpage.png)

![Edit Poster](documentation/testing/tablet-editposterpage.png)

![Delete Poster](documentation/testing/tablet-deleteposter.png)

#### Liked Posters page
![Liked posters page with likes](documentation/testing/tablet-likedposters.png)

![Liked posters page without likes](documentation/testing/tablet-nolikedposters.png)

#### Shopping Cart
![Cart No free](documentation/testing/tablet-cart2.png)

![Cart free](documentation/testing/tablet-cart1.png)

![Cart empty](documentation/testing/tablet-emptycart.png)

#### Checkout/Checkout Success
![Checkout 1](documentation/testing/tablet-checkout1.png)

![Checkout 2](documentation/testing/tablet-checkout2.png)

![Success 1](documentation/testing/tablet-success1.png)

![Success 2](documentation/testing/tablet-success2.png)

#### Footer/About Us/Terms & Conditions
![Whole footer](documentation/testing/tablet-footer.png)

![About Us](documentation/testing/tablet-aboutus.png)

![Terms & Cond](documentation/testing/tablet-terms.png)

### Mobile
#### Home
![Home page](documentation/testing/mobile-home.png)

#### Request Poster Form
![Request Form 1](documentation/testing/mobile-requestform1.png)

![Request Form 2](documentation/testing/mobile-requestform2.png)

#### Menu/Navbar
![Menu/Navbar](documentation/testing/mobile-menu1.png)

![Menu/Navbar](documentation/testing/mobile-menu2.png)

#### Sign Up/Login/Sign Out/Profile page
![Signup](documentation/testing/mobile-signup.png)

![Login](documentation/testing/mobile-login.png)

![Signout](documentation/testing/mobile-signout.png)

![Profile page 1](documentation/testing/mobile-profile1.png)

![Profile page 2](documentation/testing/mobile-profile2.png)

![Profile page 3](documentation/testing/mobile-profile3.png)

#### Posters view, category and detail view
![All Posters](documentation/testing/mobile-posters.png)

![Category page](documentation/testing/mobile-category.png)

![Poster detail view 1](documentation/testing/mobile-posterdetail1.png)

![Poster detail view 2](documentation/testing/mobile-posterdetail2.png)

#### Add, Edit and Delete Poster view
![Add poster 1](documentation/testing/mobile-addposter1.png)

![Add poster 2](documentation/testing/mobile-addposter2.png)

![Add poster 3](documentation/testing/mobile-addposter3.png)

![Edit poster 1](documentation/testing/mobile-editposter1.png)

![Edit poster 2](documentation/testing/mobile-editposter2.png)

![Edit poster 3](documentation/testing/mobile-editposter3.png)

![Delete poster](documentation/testing/mobile-deleteposter.png)

#### Liked Posters page
![Liked posters page with likes](documentation/testing/mobile-likedposter1.png)

![Liked posters page without likes](documentation/testing/mobile-likedposter2.png)

#### Shopping Cart
![Cart No free](documentation/testing/mobile-cart1.png)

![Cart free](documentation/testing/mobile-cart2.png)

![Cart empty](documentation/testing/mobile-emptycart.png)

#### Checkout/Checkout Success
![Checkout 1](documentation/testing/mobile-checkout1.png)

![Checkout 2](documentation/testing/mobile-checkout2.png)

![Checkout 3](documentation/testing/mobile-checkout3.png)

![Success 1](documentation/testing/mobile-success1.png)

![Success 2](documentation/testing/mobile-success2.png)

![Success 3](documentation/testing/mobile-success3.png)

#### Footer/About Us/Terms & Conditions
![Footer 1](documentation/testing/mobile-footer1.png)

![Footer 2](documentation/testing/mobile-footer2.png)

![About Us](documentation/testing/mobile-aboutus.png)

![Terms & Cond](documentation/testing/mobile-terms.png)

### Tested Code
This section go through the Django testing done to the project code.

#### The test codes from home.tests_models.py:
```python
<from django.test import TestCase
from .models import RequestPoster


class TestRequestPosterModel(TestCase):
    """
    Test the PostModel
    """
    @classmethod
    def setUpTestData(cls):
        RequestPoster.objects.create(
            full_name='Test Out',
            email='test@mail.com',
            phone_number='123949596',
            date='2022.05.03',
            motive='I want to request',
            image='placeholder',
        )

    def test_full_name_max_length(self):
        """ test full_name max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 70)

    def test_email_max_length(self):
        """ test email max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('email').max_length
        self.assertEqual(max_length, 200)

    def test_phone_number_max_length(self):
        """ test email max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_motive_max_length(self):
        """ test email max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('motive').max_length
        self.assertEqual(max_length, 500)
>
```

#### The test code from posters.tests_views.py:
```python
<
from django.test import TestCase
from .models import Poster


class TestViews(TestCase):
    """ Test the code for the views """
    @classmethod
    def setUpTestData(cls):

        Poster.objects.create(
            name='Test Name',
            description='Test and test',
            size=True,
            quantity=1,
            price=50.00,
            image='placeholder'
        )

    def test_get_posters_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/posters/posters/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'posters/posters-page.html',
            'base.html'
        )
>
```

The tests run results:

![Tested Code](documentation/testing/tested-code.png)

## Tested User Stories
### Overview of all the posters
A user can quickly check all the posters available in the shop on a single page. 

![Poster page 1 desk](documentation/testing/posterpage1.png)

![Poster page 2 tablet](documentation/testing/tablet-posters.png)

![Poster page 3 mobile](documentation/testing/mobile-posters.png)

### See poster all the posters depending on the poster's motive/category
When users select to view posters by category, they get redirected to a page that displays all the posters for the selected category.

![Category page desk](documentation/testing/desk-categorypage.png)

![Category page tablet](documentation/testing/tablet-category.png)

### View a product detail for each product on the page.
The user gets a detailed view of the poster. The name, price, stock info, and like button are visible. The accordion works accordingly and displays the given information below each subject. The terms and conditions page button takes the user to the right page.

![Product detail page](documentation/testing/desk-posterdetail1.png)

![Product detail info](documentation/testing/posterdetail1.png)

![Product detail info to Terms](documentation/testing/terms.png)


### Like different posters and see them on my user page
An authenticated user can like and unlike the posters through a heart-shaped button. The button works accordingly. 
The user should see the liked poster on a separate page instead of the profile page. If the user is not authenticated, the heart button is not visible on the poster detail page or the navbar.
Unfortunately, the code to render the page is not fully developed yet and has a text with a message about it. Please see the unfixed bugs section.

![Unliked Poster button](documentation/testing/posterdetail1.png)

![Liked Poster button](documentation/testing/posterlike.png)

![Liked Poster page](documentation/testing/desktop-likedposters.png)

![No Like button](documentation/testing/posterdetail2.png)

![No Liked Posters](documentation/testing/desktop-likedpage.png)

### Request a customized poster.
A user can fill out a form on the index page with a request to get a customized poster. 
The Full name, email, Phone number, and Description fields are required. If a user tries to submit the form with one or more of these fields empty, they get a notification letting them know that the field is required or missing valid characters, for example, the email field. 

Submit form with empty Full Name field

![RequestForm1](documentation/testing/requestform2.png)

Submit form with empty Email field or submit email whitout an "@"
![RequestForm](documentation/testing/request3.png)

![RequestForm](documentation/testing/requestform3.png)

Submit form with empty Phone number field
![RequestForm](documentation/testing/requestform4.png)

Submit form with empty Description field
![RequestForm](documentation/testing/requestform5.png)

Submit form with correct input in fields
![RequestForm](documentation/testing/requestform7.png)

Submit form Success message and conformation
![RequestForm](documentation/testing/requestform6.png)

Submitted form stored on the Admin page
![RequestForm](documentation/testing/requestform8.png)

### Create a user profile page for smoother checkouts and be able to edit information when needed.
#### Sign Up
The sign-up function works accordingly. A user can sign-up with a username, email, and password. The email field is only optional in the user does not want to give it for the sign-up. 
If the user does not provide a valid input or an empty input to the required fields, a message gets displayed, letting the user know why the sign-up process did not go through. The user gets redirected to the home page with a successful sign-up.

![Sign Up username](documentation/testing/signup7.png)

![Sign Up email](documentation/testing/signup2.png)

![Sign Up Password 1](documentation/testing/signup3.png)

![Sign Up Password 2](documentation/testing/signup4.png)

![Sign Up Password 3](documentation/testing/signup5.png)

![Sign Up success](documentation/testing/signup6.png)

#### Login
The login function works accordingly. A user can log in with given account details from sign up. If the user does not provide a valid input or an empty input to the required fields, a message gets displayed, letting the user know why the login process did not go through. The user gets redirected to the home page with a successful log in.

![Login required 1](documentation/testing/login2.png)

![Login required 2](documentation/testing/login3.png)

![Login incorrect input](documentation/testing/login4.png)

![Login Success](documentation/testing/successlogin.png)

#### Edit Profile information
A user can prefill out the delivery form for purchases or update it after purchase. The information given during the buying process gets saved if the user checks the box for it.

![Before purchase update](documentation/testing/profileinfobefore.png)

![After purchase update](documentation/testing/infoafterupdate.png)


### View order history on my user page
An authenticated user who makes a purchase can view their order history on their designated profile page. When clicking on the order number, it takes the user to a page to view the information about that specific order.

![Order History section](documentation/testing/order1.png)

![Full Order conf.](documentation/testing/orderconf.png)

### Manage the shopping cart by adding, editing, and deleting products in the bag.
A user can manage the shopping cart by adding products and removing products to update the cart. When adjusting the shopping cart, the user gets a message of success. There is only one of each poster in stock, and the sizes are the ones given; the user can not update the shopping cart with the size or quantity of the posters.

![Add poster to cart](documentation/testing/desk-checkout.png)

![Add posters to cart](documentation/testing/shoppingcart.png)

![Remove poster from cart](documentation/testing/successremovecart.png)

![Remove all posters from cart](documentation/testing/successremovecart2.png)

![Success add poster](documentation/testing/successaddcart.png)

![Success add poster](documentation/testing/successaddcart2.png)

![Error add poster](documentation/testing/erroraddcart.png)

### Confirmation that the payment went through.
After purchase, the user gets confirmation displayed on their browser window with a message and redirected to a success checkout page. Here the user can see the complete order information about the purchase. If the user is an authenticated user for the web application, they can go to their profile page and review the order confirmation. A confirmation email is sent to the given email.

![Confirmation message](documentation/testing/successbuy.png)

![Confirmation page authenticated](documentation/testing/orderconf.png)

![Confitmation page non-authenticated](documentation/testing/orderconf-noauth.png)

![Confirmation email](documentation/testing/mail-conf.png)

### Something goes wrong during the shopping process, I want to get a notification about it
If something happens during the payment process, the user gets notified with error messages displayed for them. For example, suppose the card account does not have a sufficient amount, or the user needs to authenticate the card during the process. In that case, a message will appear with the error, and an authentication pop-up will appear on the screen. If the user does not fill out the delivery form with valid and required information, the user will get a notification about the invalid input and get a chance to fix it. For the Full Name, Email and Phone number field, they only get highlighted and if the user hovers over the field they get the infromation about what the problem is.

![Card failure amount](documentation/testing/paymentfail-card.png)

![Card authentication popup](documentation/testing/cardauth1.png)

![Card failure authentication](documentation/testing/cardauth2.png)

![Checkoutform fail 1](documentation/testing/checkout6.png)

![Checkoutform fail 2](documentation/testing/checkout5.png)

![Checkoutform fail 3](documentation/testing/checkout7.png)

![Checkoutform fail 4](documentation/testing/checkout4.png)

![Checkoutform fail 5](documentation/testing/checkout3.png)

![Checkoutform fail 6](documentation/testing/checkout2.png)

![Checkoutform fail 7](documentation/testing/checkout1.png)

### Add, edit and delete poster through the web application's front-end as Admin/Superuser
An admin or Superuser for the web application can add, edit and delete posters to the shop through frontend applications. The User gets a notification each time they successfully add, edit, or delete a poster. The User also receives a message about which poster they are editing.

* Add a poster to the shop
![Add Poster](documentation/testing/addposter-test.png)

![Success message add poster](documentation/testing/info-add.png)

* Edit a poster to the shop
![Edit Poster](documentation/testing/tablet-editposterpage.png)

![Information about edit poster](documentation/testing/info-editposter.png)

![Success message edit poster](documentation/testing/info-updatesuccess.png)

* Delete a poster from the shop
![Delete Poster](documentation/testing/tablet-deleteposter.png)

![Success message delete poster](documentation/testing/info-delete.png)


### Manage posters through the admin page
An admin or superuser for the web application can add, edit and delete posters to the shop by the admin panel. The events get displayed on a message board on the admin panel.

![Manage Posters](documentation/testing/posteractions.png)

## Tested Features
Test existing web application features that are not related to a User Story.

### Menu/Navbar
#### Hidden Menu/Navbar
All the navbar links in the offcanvas navbar work accordingly if the user is authenticated or not and redirect the user to the right page.

![Hidden out](documentation/testing/hiddenmenu2.png)
![Hidden in](documentation/testing/hiddenmenu4.png)

Home
![Home](documentation/testing/tablet-home.png)

Login

![Login page](documentation/testing/desk-login.png)

Sign Up

![Sign up page](documentation/testing/signup1.png)

Profile
![Profile page](documentation/testing/desk-profile.png)

Sign out

![Sign Out page](documentation/testing/desk-signout.png)

All Posters

![Poster page](documentation/testing/posterpage1.png)

Customize/Request Poster

![Request Poster Form](documentation/testing/requestform1.png)

Categories
![Categories](documentation/testing/tablet-menu2.png)

#### Visable icon Menu/Navbar
Icon menu row depending if authenticated User or not.

![No Authenticated User](documentation/testing/tablet-home.png)

![Authenticated User](documentation/testing/mobile-menu2.png)

![Superuser/Admin](documentation/testing/menuiconssuper.png)

Serach bar
The search function works accordingly. If a user tries to search with an empty field or invalid form, an error message appears on their browser window.

![Searchbar](documentation/testing/searchbar1.png)

![Search input](documentation/testing/searchbar2.png)

![Search result](documentation/testing/searchbar3.png)

![Search result other input](documentation/testing/searchbar4.png)

![Search no input](documentation/testing/errorsearch.png)

Liked Posters Page

![Liked Posters page without likes](documentation/testing/tablet-nolikedposters.png)

![Liked Posters page with likes](documentation/testing/tablet-likedposters.png)

Add Poster Page, if Superuser

![Add poster](documentation/testing/tablet-addposterpage.png)

Profile

![Profile 1](documentation/testing/mobile-profile1.png)

![Profile 2](documentation/testing/mobile-profile2.png)

![PRofile 3](documentation/testing/mobile-profile3.png)

Shopping Cart

![Shopping cart free](documentation/testing/tablet-cart1.png)

![Shopping cart no](documentation/testing/tablet-cart2.png)

![Shopping cart empty](documentation/testing/tablet-emptycart.png)

### Footer
The results for testing the existing features in the footer. 

#### Newsletter Sign Up
A user can quickly sign up for a newsletter. The user gets a notification success message displayed on their screen when sign-up is complete.
If the user tries to add an invalid email or an existing email on the subscription list, an error message will be displayed o their screen.
![Newsletter sign up](documentation/testing/newsletter4.png)

![Newsletter sign up success](documentation/testing/newsletter5.png)

![Newsletter empty field](documentation/testing/newsletter2.png)

![Newsletter missing "@"](documentation/testing/newsletter4.png)

![Newsletter exist](documentation/testing/newsletter6.png)

#### About Us page
When users click on the About Us link in the footer, they get redirected to the About Us page.
![About Us page](documentation/testing/aboutus.png)

#### Posters
When users click on the Posters link in the footer, they get redirected to the All Posters page.
![Poster page](documentation/testing/posterpage1.png)

#### Terms and Conditions
When users click on the Terms and Conditions link in the footer, they get redirected to the Terms and Conditions page.
![Terms & Conditions page](documentation/testing/terms.png)

#### Privacy Policy
When users click on the Privacy Policy link in the footer, they get redirected to the Privacy Policy page, and it opens up in a new tab in the browser window.
![Privacy Policy page](documentation/testing/privacy.png)

#### Send a hello email
When users send a mail through the Send Us a Hello link, it opens the user's nearest open email source with a subject prefilled. The mail comes to the given email address.
![Send hello mail open](documentation/testing/hello1.png)

![Send hello mail send](documentation/testing/hello2.png)

![Send hello mail in inbox](documentation/testing/hello4.png)

![Send hello mail in inbox](documentation/testing/hello5.png)


#### Social Media platforms
When users click on one of the Social Media icons in the footer, they get redirected to the given web application. The link opens in a new tab in the browser window.
![Facebook](documentation/testing/facebook.png)

![Instagram](documentation/testing/instagram.png)

![Pinterest](documentation/testing/pinterest.png)

## Unfixed Bugs
* The Request for a customized poster form shows the "This field is required" error message, even though the user has not taken any actions to submit the form. I tried various ways to prevent it by adding Crispy formHelper and jQuery code on the index.html page to prevent eventDefult and trigger the form submit on click events. The form had some formatting errors before using crispy forms, creating tables element on the deployed page, which only showed via the code validation. I believe this bug occurs because the form tries to submit when the page load and my attempts to fix it until now may not be the right way for it. 

Crispy formHelper

![Code for forms with Crispy FormHelper1](documentation/testing/crispyformhelper1.png)

![Code for forms with Crispy FormHelper2](documentation/testing/crispyformhelper2.png)

* A bug that I can not figure out how to solve correctly is the Add to cart button not changing when a user adds a poster to the shopping cart. To fix this in the meantime, I implemented an Error message letting the user know that the poster was already in the shopping cart.

* This project took shape with two different computers and screen sizes. Depending on which computer, the d in the heading "E.Stromlind posters and art" disappears into the image to the right. I have lowered the pixel size from 60px to 55px to make it look better on both computers, but it is something to look over in more detail.

* There was a code validation error with HTML and CSS for the Customer profile page and the liked poster page. Adding Login required decorators to the rendering of the view does templates the validation error got solved.