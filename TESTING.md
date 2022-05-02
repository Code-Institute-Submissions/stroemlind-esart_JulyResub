# Testing
There was always a tab open for testing with the website preview through Gitpod port 8000. To check up on my code and see if it worked as I wanted. I used DevTools to see how the code would respond if I added or changed properties or values with CSS or Bootstrap. I also took help from DevTools to check the responsiveness when decreasing or increasing the screen size. To see and test the website's performance, I used Lighthouse, for both mobile and desktop usage, which gave me an updated report to see how well my performance, accessibility, and SEO were for the website.

To see that the JavaScript code in the project worked without any bugs, I used the console section of DevTools to know that it rendered as it should.

Several internet browsers, like Chrome, Mozilla Firefox, Microsoft Edge, and Safari, were used during all the testing. It works on all the mentioned internet browsers and mobile devices.
## Code Validation

### HTML
There are no errors form the offical [W3C Validatior](https://validator.w3.org/)
   ![HTML-validation](documentation/testing/html1.png)

   ![HTML-validation](documentation/testing/html8.png)
    
  Link to the validation for the home page: [W3C Validatior](https://validator.w3.org/nu/?doc=https%3A%2F%2Fes-art.herokuapp.com%2F)

Except for the customer profile page and the liked poster page, which gave an Error 500. See unfixed bugs for more infromation. 

### CSS
There are no major errors form the offical [Jigsaw validator](https://jigsaw.w3.org/css-validator/), except for on the customer and liked poster page, where an error occur. The warning for the valid pages am I aware of.
Note: See Unfixed bugs for more infromation.

  ![Css-validation](documentation/testing/css1.png)

  ![Css-validation-warning](documentation/testing/css-warning.png)

  ![Css-validation-warning](documentation/testing/css-error.png)
    
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

  ![Chrome](documentation/testing/chrome.png)

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
### Tablet 
### Mobile 

## Tested User Stories
### Overview of all the products.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### See poster all the posters depending on the poster's motive.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### View a product detail for each product on the page.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### Like different posters/products and see them on my user page.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

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
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### View order history on my user page.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### Manage the shopping cart by adding, editing, and deleting products in the bag.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### Confirmation that the payment went through.
![](documentation/testing/)
![](documentation/testing/)

### Something goes wrong during the shopping process, I want to get a notification about it.
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

### Manage products through the admin page.
![](documentation/testing/)
![](documentation/testing/)

## Tested Features
Test existing web application features that are not related to a User Story.

### Menu/Navbar
#### Hidden Menu/Navbar
![](documentation/testing/)
![](documentation/testing/)

Home
![](documentation/testing/)

Login
![](documentation/testing/)

Sign Up
![](documentation/testing/)

Profile
![](documentation/testing/)

Sign out
![](documentation/testing/)

All Posters
![](documentation/testing/)

Customize/Request Poster
![](documentation/testing/)

Categories
![](documentation/testing/)

#### Visable icon Menu/Navbar
Search function
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

Liked Posters Page
![](documentation/testing/)
![](documentation/testing/)

Profile
![](documentation/testing/)
![](documentation/testing/)

Shopping Cart
![](documentation/testing/)
![](documentation/testing/)
![](documentation/testing/)

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
![Send hello mail in inbox](documentation/testing/hello3.png)


#### Social Media platforms
When users click on one of the Social Media icons in the footer, they get redirected to the given web application. The link opens in a new tab in the browser window.
![Facebook](documentation/testing/facebook.png)
![Instagram](documentation/testing/instagram.png)
![Pinterest](documentation/testing/)

## Unfixed Bugs
* Remove text from the request Poster Form 
![Code for forms with Crispy FormHelper1](documentation/testing/crispyformhelper1.png)
![Code for forms with Crispy FormHelper2](documentation/testing/crispyformhelper2.png)

* A bug that I can not figure out how to solve correctly is the Add to cart button not changing when a user adds a poster to the shopping cart. To fix this in the meantime, I implemented an Error message letting the user know that the poster was already in the shopping cart.

* This project took shape with two different computers and screen sizes. Depending on which computer, the d in the heading "E.Stromlind posters and art" disappears into the image to the right. I have lowered the pixel size from 60px to 55px to make it look better on both computers, but it is something to look over in more detail.