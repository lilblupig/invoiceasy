# **InvoicEasy**

# Testing

A plan and log for testing the website, this is primarily a manual testing plan due to the limitations of the developer at this time.

# Index
1. [Validation Testing](#validation-testing)
1. [Automated Testing](#automated-testing)
1. [Logic Error Testing](#logic-error-testing)
1. [Client Stories Testing](#client-stories-testing)
1. [Manual Testing](#manual-testing)
    * [Common Elements](#common-elements)
    * [Page Specific Sections](#page-specific-sections)
    * [Accessibility](#accessibility)
1. [Bugs](#bugs)

## Validation Testing
The project code has been passed through the following code validators:
* [HTML Code Validator](https://validator.w3.org/) Public facing pages were tested by url, and restricted pages were tested by copying the page source code of the deployed site from the browser and pasting into the validator.
<br>Validator results (PDF):
  * [Home](html-validation/home.pdf)
  * [About](html-validation/about.pdf)
  * [Pricing](html-validation/products-pricing.pdf)
  * [Pricing Detail](html-validation/products-pricing-detail.pdf)
  * [Contact](html-validation/contact.pdf)
  * [Register](html-validation/accounts-register.pdf)
  * [Login](html-validation/accounts-login.pdf)
  * [Dashboard](html-validation/invoices-dashboard.pdf)
  * [New/Manage Customer](html-validation/invoices-new-customer.pdf)
  * [New/Manage Invoice](html-validation/invoices-new-invoice.pdf)
  * [Profile](html-validation/profile.pdf)
<br><br>
* [CSS Code Validator](https://jigsaw.w3.org/css-validator/) (one warning - external stylesheets are not checked)
![CSS Validator result](assets/readme-images/css-validation.png)
![CSS Validator warning](assets/readme-images/css-validation-warning.png)

* [JS Hint](https://jshint.com/)

* The project has been assessed throughout development using [Lighthouse](https://developers.google.com/web/tools/lighthouse).
![Lighthouse Ratings](assets/readme-images/lighthouse-XXXX.png)

## Logic Error Testing
1. Check that script to determine form validation and success feedback has no errors.

1. Check all pages for appropriate Bootstrap grid component ordering.

## Client Stories Testing
1. As a new user, I want to 
    1. 
    1. 
    ![User story 1 screenshot](assets/readme-images/user-story-1.png)
1. As a new user, I want to 
    1. 
    1. 
    ![User story 2 screenshot](assets/readme-images/user-story-2.png)
1. As a new user, I want to l
    1. 
    ![User story 3 screenshot](assets/readme-images/user-story-3.png)
1. As a returning user, I want to 
    1. 
    ![User story 4 screenshot](assets/readme-images/user-story-4.png)
1. As a returning user, I want to 
    1. 
    1. 
    ![User story 5 screenshot](assets/readme-images/user-story-5.png)
1. As a frequent user, I want to 
    1. 
    ![User story 6 screenshot](assets/readme-images/user-story-6.png)

## Manual Testing

### **Common Elements**

These components are present on every page, and each page has been tested.

---

#### Navigation Bar

**Intent** - a navbar which collapses to hamburger on mobile.

* All links are valid and link to the appropriate page.
* Logo alt displays on hover (added title attribute).
* Hover effect occurs correctly for each navigation section.
* Active class is applied correctly for current page.
* Resize to mobile/tablet and check that navigation bar collapses to hamburger.
* Expand hamburger menu and check all sections present, and displaying correctly.

**Result** - `Text here to explain what happened when tested`

**Verdict** - XXXX

---

#### Hero Images

**Intent** - a full width image relevant to the page content, different for each page.  Primary purpose, to elicit a positive emotional response from the user.  The image should display correctly on all device sizes.  The image should display XXX% height on the home page and XXX% on the 404 page to display redirect information.

* Image fills the viewport as expected depending on page.
* Resize to mobile/tablet and check that image still displays without distortion.
* Text remains centered with no overflow at mobile/tablet.

**Result** - `Text here to explain what happened when tested`

**Verdict** - XXXX

---

#### Footer

**Intent** - The footer should be reflective of the design of the nav to bookend each page and provide familiarity to the user.  This helps with intuitive learning.  Any external links should open in new tabs and provide user feedback when hovered over.

* Footer appears in XXX sections.
* Social media icons display correctly, and show feedback behaviour on hover.
* Social links open in new tabs to correct locations.
* Resize to tablet and check for text overflow issues.
* Resize to mobile and check that sections wrap neatly below one another.

**Result** - `Text here to explain what happened when tested`

**Verdict** - XXXX

---

### **Page Specific Sections**

These items are specific to each individual page.

#### Basic Plan for Body Sections
* Check all areas of text align appropriately, horizontally and vertically.
* Check that behaviour is correct for mobile/tablet.
* Check that any links, buttons or fields show feedback behaviour on hover.
* Check that any links navigate to correct pages.
* Check that any external links open in a new tab, to the correct place.
* Check that any icons do not overflow into text on mobile/tablet.

---

#### Contact Us

**Intent** - Encourage the user to get in touch with the owners, and make it as easy as possible to do so.

* All text sections display correctly across tested device widths.
* All buttons display user feedback on hover.
* All internal links navigate to the correct page.

Contact Us Form
* Form contents align nicely and that there is no overflow of content.
* Fields display correctly on mobile/tablet and PC.
* Placeholder text displays in fields.
* Fields and submit button display feedback on hover.
* Fields display feedback on focus.
* Try to submit blank form, error messages display with information.
* Try to submit email in incorrect format, error message displays with information.
* Try to submit form without question, error message displays with information.
* Submit correctly completed form, receive success modal.
* Modal information centers correctly with no overflow on all device widths.

**Result** - `Text here to explain what happened when tested`

**Verdict** - XXXX

---
#### 404

**Intent** - Catch users who would normally encounter a browser generated 404 page, and redirect them back to the website as cleanly as possible.

* All text sections display correctly across tested device widths.
* All buttons and links display user feedback on hover.
* All internal links navigate to the correct page.
* User is guided back to the home page.
* Mistyped url for website to ensure 404 page displays in such situations.
* Deliberately broke page link to ensure 404 page will display in this instance too.

**Result** - `Text here to explain what happened when tested`

**Verdict** - XXXX

---

### **Accessibility**

The colourblind feature on Coolors was used to check that the colours appeared sufficiently different, and not jarring for these users.
![Colourblindness assessment via Coolors](assets/readme-images/colourblindness.png)

As well as the use of the Lighthouse assessments of accessibility, the website was browsed at intervals by two users who may experience difficulty.  A dyslexic user with ASD and a colourblind user both XXXXX.

## Bugs

Details of any persistent or difficult bugs, and any bugs which remain unresolved.

### **Fixed Bugs**


### **Remaining Bugs**



Testing first completed XX/XX/2021 - AKH
Testing repeated XX/XX/2021 - AKH

[Return to Top](#title)