# **InvoicEasy**

# Overview
InvoicEasy is to be a simple online invoicing tool which allows small businesses to quickly and easily set up customer accounts and direct their customers to a secure platform to view invoices, without compromising GDPR.


![Am I Responsive Image](documentation/readme-images/am-i-responsive.png)

# Index
1. [UX](#ux)
    * [User Stories](#user-stories)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
1. [Features](#features)
    * [Existing Features](#existing-features)
    * [Features for Future Implementation](#features-for-future-implementation)
1. [Testing](#testing)
1. [Development Life Cycle](#development-life-cycle)
1. [Deployment of the Application](#deployment)
    * [Cloning via GitPod](#cloning-a-project-into-gitpod)
    * [Cloning Locally](#how-to-run-the-code-locally)
1. [Technologies Used](#technologies-used)
1. [Credits](#credits)
    * [Website](#website-credits)
    * [README](#readme-credits)

Note, testing information can be found in a separate document:
* [Testing](TESTING.md)

## UX

### **Overview and Broad Design Choices**


### **User Stories**
1. As a new user, I want to 
1. As a new user, I want to 
1. As a new user, I want to 
1. As a returning user, I want to 
1. As a returning user, I want to 
1. As a frequent user, I want to 

These stories are addressed fully in the [Testing](TESTING.md) document.

### **Strategy**
Who is the website for?
What does the owner of the website need/want?
What do the users of the website need/want?

Broadly, how does the website meet these needs?

Owner aims:
* 
* 
* 
* 
* 

User aims:
* 
* 
* 
* 
* 

### **Scope**
Why does the website exist?  What does it need to meet the user/owner aims?

#### Feature Viability

| # | Feature | Importance | Viability | Comment |
|---| ------- | :--------: | :-------: | ------- |
1.| Feature  | 0 | 0 | Y - Why
2.| Feature  | 0 | 0 | Y - Why
3.| Feature  | 0 | 0 | Y - Why
T.| Total score | 0 | 0 |

#### Feature Plan
First increment:
* 

Second increment:
* 

Third increment:
* 

### **Structure**
* See Information Grouping [mind map here](assets/documents/structure.pdf).

### **Skeleton**
In line with structure planning... 

#### Wireframes

##### Original
1. [Mobile](documentation/documents/XXXXX-mobile.pdf) 375px
1. [Tablet](documentation/documents/XXXXX-tablet.pdf) 768px
1. [PC/Laptop](documentation/documents/XXXXX-pc.pdf) 1200px

##### Final
1. [Mobile](documentation/documents/XXXXX-mobile-final.pdf) 375px
1. [Tablet](documentation/documents/XXXXX-tablet-final.pdf) 768px
1. [PC/Laptop](documentation/documents/XXXXX-pc-final.pdf) 1200px

##### Summary of Changes
* 

### **Surface**

#### Colours
Thought process behind colour choices and palette development.
![Colours option 1](documentation/readme-images/colors-opt-1.png)

Dark grey - #292F38
Orange - #FF4D00

#### Typography
Thought process behind font choices.
1. 
1. 
1. 

![Example fonts](documentation/readme-images/typography.png)

For logo and Headings etc?
https://fonts.google.com/specimen/Flamenco?preview.text=InvoicEasy&preview.text_type=custom

## Features

### **Existing Features**
Features common to all pages/sections:

#### XXXXX

### **Features for Future Implementation**
1. What | Why

## Testing

This information is held in the [Testing](TESTING.md) file.

## Development Life Cycle

This section is to provide an brief insight into how the approach to the code structure of the website was expected to work, what changed and why, and then to summarise how the creator would now approach replicating the project.

Changes to design are documented in the [UX section](#ux) under [wireframes](#wireframes).

The project was deployed using GitHub pages once the basic structure of the page was complete.  This allowed for continuous delivery as each change was made, and pushed and enabled testing of the page during development on different devices.

Commits were made as each section of each page was added and pushed once a section was complete.

### **Reflections on General Approach to Build**
What would be done differently next time?  What went right?  Overall opinion.

### **Lessons Learned**


#### Preparation


#### Build


### **Revised Development Process**

Based on the experience of producing the website, the creator would now take the following approach.

#### Preparation


#### Build

## Deployment

The website was created using [GitPod](https://www.gitpod.io/). Version control was undertaken by committing to [Git](https://git-scm.com/) and pushing to [GitHub](https://github.com/) using the functions within GitPod.  [Heroku]((https://heroku.com/)) was used to deploy the live site.

### **Deployment of the Page**
Continuous deployment via GitHub-Heroku link was utilised for this project.  As such, deployment was amongst the first tasks undertaken.
1. In the IDE, ensure that a small test application exists, and all changes are committed and pushed to GitHub.
1. Create a requirements file, which will be used by Heroku in creation of the deployment.
    * In the terminal, type "pip3 freeze --local > requirements.txt".
    * Commit this to Git.
1. Create a Procfile, which is used by Heroku to determine the language for the app.
    * In the terminal, type "echo web: python app.py > Procfile".
    * This is case sensitive, and should have a capital P, and should have no file extension.
    * Commit this to Git.
1. Push these files to GitHub.
1. [Sign in to Heroku](https://id.heroku.com/login) (or [create a Heroku account](https://signup.heroku.com/) if you do not already have one), and choose "New > Create New App".
![Heroku Dashboard snip](documentation/readme-images/heroku-1.png)
1. Choose an app name, which must be unique, and select the nearest region.  Then click "Create App".
![Heroku new app snip](documentation/readme-images/heroku-2.png)
1. Once generated choose the "Deploy" tab, select "Connect to GitHub" sub-tab and click the "Connect to GitHub" button.
![Heroku Deploy snip](documentation/readme-images/heroku-3.png)
![Heroku GitHub snip](documentation/readme-images/heroku-4.png)
1. Follow the on-screen instructions to link Heroku to your GitHub account.
1. Click the "Settings" tab from the main menu, and scroll down to find "Reveal Config Vars".  This section should be populated with any sensitive data which is not appropriate to send to GitHub, usually in an "env.py" document.
![Heroku GitHub snip](documentation/readme-images/heroku-vars.png)
1. Back on the Deploy tab, once linked, Heroku will prompt for the repository name, complete this and click "Search".
![Heroku GitHub snip](documentation/readme-images/heroku-5.png)
1. The repo listing should appear, click "Connect".
1. Heroku will process the request before showing that the connection has been made successfully, and showing two new options.  Click the first of these, which is to "Enable Automatic Deploys".
![Heroku GitHub snip](documentation/readme-images/heroku-6.png)
1. The second option is to "Deploy Branch".  Click the button and Heroku will process for some time.
![Heroku GitHub snip](documentation/readme-images/heroku-7.png)
1. Once complete, Heroku will display a checklist, followed by a "View" button.  Click this to open the app in a new tab.
![Heroku GitHub snip](documentation/readme-images/heroku-8.png)
1. Celebrate! Your app should now update in line with any changes pushed to GitHub.

### **How to Clone and Run the Code Locally**
There are slightly different approaches should you choose to use GitPod to clone the project, or a local IDE.

#### Cloning a Project into GitPod
1. Use [Google Chrome](https://www.google.com/intl/en_uk/chrome/). *(This can also be undertaken in Firefox)*
1. If you do not already have one, [create a GitHub account](https://github.com/join).
1. Install the [GitPod browser extension for Chrome](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki). *(Or Firefox if appropriate)*
1. Restart Chrome.
1. In GitHub, find the [project repository](https://github.com/ci-14-task-manager).
1. From the repository menu, choose the green GitPod button.
![GitPod button snip](documentation/readme-images/cloning-gitpod.png)
1. A new GitPod workspace will open containing the project code.

#### Cloning a Project into a Local IDE
1. Navigate to the [GitHub Repository](https://github.com/ci-14-task-manager).
1. Choose the Code dropdown menu, and copy the URL.
![GitHub code download snip](documentation/readme-images/clone-local-ide.png)
1. Open your local IDE and then open a terminal.
1. Set the current working directory to your preferred location for the cloned project.
1. Type in "git clone " followed by the copied URL. Be sure to include a space between git clone and the url, then press enter.
1. The cloned project will be created.

You can find more information on cloning a repository from GitHub [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## Technologies Used

### **Languages**
* HTML5 is used to provide the basic structure of the website.
  * About: [HTML5 Wiki](https://en.wikipedia.org/wiki/HTML5)
  * Creator: [W3 Consortium](https://www.w3.org/)
* CSS3 is used to provide most of the styling for the website.
  * About: [CSS3 Wiki](https://en.wikipedia.org/wiki/CSS)
  * Creator: [W3 Consortium](https://www.w3.org/)
* JavaScript is used to provide the interactive nature of such components throughout the website.
  * About: [JavaScript Home](https://www.javascript.com/)
* Python is the primary programming language used to create the application.
  * About: [Python Home](https://www.python.org/)

### **Libraries and Frameworks**
* The [Django](https://www.djangoproject.com/) framework is used to facilitate efficient app building and include basic security.
* [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html) is used for all user account functionality.
* [Crispy Forms](https://pypi.org/project/crispy-bootstrap5/) is used to power forms used on the site.
* [Bootstrap 5](https://getbootstrap.com/) is used to provide the grid functionality for uniform design, responsiveness and to enable the use of modal and hamburger menu.
* [jQuery](https://jquery.com/) is used to simplify the implementation of interactive JavaScript components.
* [Google Fonts](https://fonts.google.com/) are used to provide the typography for the website.
* [Font Awesome](https://fontawesome.com/) is used to provide the icons for the website.
* [PostgreSQL](https://www.postgresql.org/) is used for the production database via the Heroku Add-On Heroku Postgres.
* [DJ Database URL](https://pypi.org/project/dj-database-url/) is used to facilitate PostgreSQL.
* [Psycopg](https://pypi.org/project/psycopg2-binary/) is also used to facilitate PostgreSQL.
* [SQLite3]() is used for the development database.

### **Tools**
* [Git](https://git-scm.com/)/[GitHub](https://github.com/) was used for version control and repository storage.
* [GitPod](https://www.gitpod.io/) was the IDE used to write the project.
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) were used for specific responsiveness testing and drilling down into bug fixing.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse) was used for macro testing and identification of errors for rectification.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to remove any remaining errors in CSS code.
* [W3C HTML Validation Service](https://validator.w3.org/) was used to remove any remaining errors in HTML code.
* [JS Hint Validation Service](https://jshint.com/) was used to check for major errors in JavaScript.
* [Responsively](https://responsively.app/) was used to explore responsiveness across various devices.

### **Other Resources**
* [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used to set up the repository.
* The following projects created by fellow Code Institute students gave great inspiration and were used to benchmark/guide my own project:
  * [Which Way is Up](https://github.com/lemocla/Which-way-is-up) by [Claire](https://github.com/lemocla).
  * [Postfly](https://github.com/Daph1986/postfly_jouw_online_drukkerij) by [Daphne Heimgartner](https://github.com/Daph1986)
  * [Code With Mike](https://github.com/MikeAvgeros/code-with-mike)
  * [Cost Report](https://github.com/dkeddie/MS4-Cost-Report)


## Credits

### **Website Credits**

#### Content
Where did the website content come from?
* [Whitenoise setup](http://whitenoise.evans.io/en/stable/django.html)
* [Stripe Subscritptions](https://testdriven.io/blog/django-stripe-subscriptions/)
* [Django contact mail article](https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend)
* [Dates conversion](https://www.tutorialspoint.com/How-to-convert-an-integer-into-a-date-object-in-Python#:~:text=You%20can%20use%20the%20fromtimestamp,object%20corresponding%20to%20the%20timestamp.)
* [Difference between Static and Media for relative paths](https://stackoverflow.com/questions/37241902/django-joined-path-is-located-outside-of-the-base-path-component-static-img)
* [Save user as foreign key to form](http://www.learningaboutelectronics.com/Articles/How-to-save-the-current-user-logged-in-to-a-database-table-in-Django.php)

#### Media
* The photographs used for the website were obtained from [Pexels.com](https://www.pexels.com/):

* And [Unsplash](https://unsplash.com/):
  * [Bulldog clip of papers](https://unsplash.com/photos/bSkAq6XEYyk)
  * [Artisan office](https://unsplash.com/photos/cWpgJrVgkr0)
  * [Telephone](https://unsplash.com/photos/-0xCCPIbl3M)
  * [Typewriter](https://unsplash.com/photos/jLwVAUtLOAQ)
  * [Stamp](https://unsplash.com/photos/e-CqOxx8oXw)
  * [Coin jar](https://unsplash.com/photos/SoqG9RWd_FA)
  * [Paper list](https://unsplash.com/photos/onP8BIHPkrc)
  * [Padlock](https://unsplash.com/photos/XUJcmgEhpjA)
  * [Enter arrow](https://unsplash.com/photos/J59wWPn09BE)
  * [See you later sign](https://unsplash.com/photos/v_WLk_vNYRA)
  * [Keys](https://unsplash.com/photos/C1P4wHhQbjM)
  * [Hola sign](https://unsplash.com/photos/8MMtYM_3xMY)
  * [Filing boxes](https://unsplash.com/photos/lRoX0shwjUQ)

* The icons used for the website are from [FlatIcon]():
  * [Monitor in Logo - created by DinosoftLabs](https://www.flaticon.com/free-icons/monitor>)

#### Acknowledgements
Thank you in particular to:
* Reuben Ferrante for mentoring the project.

### **README Credits**

#### Content
Structure and content based heavily on:
* [Code Institute Solutions - README Template](https://github.com/Code-Institute-Solutions/readme-template)
* [Daisy McGirr - Code Institute Testing Webinar](https://us02web.zoom.us/rec/play/9FIKllHX2ZiQNFRhYPn_hBh_ZeA8964ZvIDLnhpKGAf1NLVc3_hBJ6zSL8Hv5Hx7ALnPtDmbg8CmFAs.YVsZ9LR_uI7OjEwH)

#### Media
The images for this README are from the following sources:
* Snips taken from GitHub.
* [Am I Responsive](http://ami.responsivedesign.is/).
* Wireframes created with [Balsamiq](https://balsamiq.com/).
* Colour mockups created with [Coolors](https://coolors.co/).
* Snips taken of Google Fonts.

#### Other
* Markdown basic taken from [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

**This website was produced as an educational project for the Code Institute Full Stack Development course.**

**Created by Amy Hacker.**

[Back to Top](#invoiceasy)