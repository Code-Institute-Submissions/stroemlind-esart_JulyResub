# Testing
There was always a tab open for testing with the website preview through Gitpod port 8000. To check up on my code and see if it worked as I wanted. I used DevTools to see how the code would respond if I added or changed properties or values with CSS or Bootstrap. I also took help from DevTools to check the responsiveness when decreasing or increasing the screen size. To see and test the website's performance, I used Lighthouse, for both mobile and desktop usage, which gave me an updated report to see how well my performance, accessibility, and SEO were for the website.

To see that the JavaScript code in the project worked without any bugs, I used the console section of DevTools to know that it rendered as it should.

Several internet browsers, like Chrome, Mozilla Firefox, Microsoft Edge, and Safari, were used during all the testing. It works on all the mentioned internet browsers and mobile devices.
## Code Validation
* Validator HTML table elements created 

### HTML
There are no errors form the offical [W3C Validatior](https://validator.w3.org/)
    ![HTML-validation](documentation/testing/html1.png)
    
    Link to the validation for the home page: [W3C Validatior](https://validator.w3.org/nu/?doc=https%3A%2F%2Fes-art.herokuapp.com%2F)

### CSS
There are no major errors form the offical [Jigsaw validator](https://jigsaw.w3.org/css-validator/), except for on the customer and liked poster page, where an error occur. The warning for the valid pages am I aware of.
Note: See Unfixed bugs for more infromation.

  ![Css-validation](documentation/testing/cssvalid.png)

  ![Css-validation-warning](documentation/testing/csswarning.png)

  ![Css-validation-warning](documentation/testing/csswarning.png)
    
  Link to the validation: [Jigsaw validator](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Fes-art.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)

### JavaScript
No errors where found when going through the offical [Jshint validator](https://jshint.com/).
* There are 4 functions in this file.
* Function with the largest signature take 1 arguments, while the median is 1.
* Largest function has 8 statements in it, while the median is 4.5.
* The most complex function has a cyclomatic complexity value of 3 while the median is 1.5.

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
### See poster all the posters depending on the poster's motive.
### View a product detail for each product on the page. 
### Like different posters/products and see them on my user page.
### Request a customized poster.
### Create a user profile page for smoother checkouts and be able to edit information when needed.
### View order history on my user page.
### Manage the shopping cart by adding, editing, and deleting products in the bag.
### Confirmation that it went through after purchase.
### Something goes wrong during the shopping process, I want to get a notification about it.
### Manage products through the admin page.

## Unfixed Bugs
* Remove text from the request Poster Form 
![Code for forms with Crispy FormHelper1](documentation/testing/crispyformhelper1.png)
![Code for forms with Crispy FormHelper2](documentation/testing/crispyformhelper2.png)

* A bug that I can not figure out how to solve correctly is the Add to cart button not changing when a user adds a poster to the shopping cart. To fix this in the meantime, I implemented an Error message letting the user know that the poster was already in the shopping cart.

* This project took shape with two different computers and screen sizes. Depending on which computer, the d in the heading "E.Stromlind posters and art" disappears into the image to the right. I have lowered the pixel size from 60px to 55px to make it look better on both computers, but it is something to look over in more detail.