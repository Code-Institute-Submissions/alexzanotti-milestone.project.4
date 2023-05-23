# Purpose

In this project, a full-stack site based around business logic used to control a centrally-owned dataset. An authentication mechanism is setup, providing access to the site's data. A donation mechanism is also setup for users who'd like to contribute.

[Click Here to View the Website!](https://milestone-project-4.herokuapp.com/)

# Value provided:
1. By authenticating on the site, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
2. The site owner is able to make money by providing a donation mechanism to the users.
3. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

# Project Requirements

In order to pass this milestone project, the following requirements must be met:

## Main Technologies

* HTML
* CSS
* JavaScript
* Python+Django
* Relational database
* Stripe payments
* Additional libraries and APIs

## Mandatory Requirements 

1. Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
2. Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
3. Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course (changing the field names of the miniproject models is not customisation)
4. User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
5. User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
6. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout or single payments, or donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.
7. Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
8. Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
9. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
10. Version Control: Use Git & GitHub for version control.
11. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
10. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
11. Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.

# UX

## User Stories

### Index
1. As a user, I want to visit the home page of the website so that I can learn about the website's purpose and content.

### Contact
2. As a user, I want to be able to fill out a contact form so that I can communicate with the website administrators.
3. As a website administrator, I want to manage the contact forms that have been submitted so that I can respond to user inquiries.
4. As a website administrator, I want to update and delete contact forms so that I can manage the information received from users.

### Donate
5. As a user, I want to be able to make a donation to the website so that I can support its operation and development.
6. As a site administrator, I want to be able to display information about how the users donation has helped the running of the website

### Community
7. As a user, I want to view posts in the community section so that I can engage with the content and discussions.
8. As a user, I want to comment on posts so that I can participate in discussions and share my thoughts.
9. As a user, I want to create my own posts so that I can start discussions and share information with the community.
10. As a user, I want to have a "My Posts" page where I can see all my posts and comments so that I can easily manage and review my contributions to the community.
11. As a user, I want to edit my own posts and comments so that I can correct mistakes as needed.
12. As a user, I want to delete my own posts and comments so that I can remove content as needed.
13. As a site administrator, I want to view all categories in the community section so that I can oversee the topics being discussed.
14. As a site administrator, I want to add, edit, or delete categories in the community section so that I can manage the structure and organization of discussions.
15. As a site administrator, I want to view all posts and comments from users so that I can monitor the content being shared in the community.
16. As a site administrator, I want to edit or delete posts and comments from users when necessary so that I can ensure the content aligns with community guidelines and standards.

### Plans
17. As a user, I want to view plans in the plans section so that I can explore and learn from other users' strategies.
18. As a user, I want to view comments from other users so that I can learn from different thoughts and ideas.
19. As a user, I want to comment on plans so that I can provide feedback, ask questions, or share my thoughts.
20. As a user, I want to create my own plans so that I can structure my strategies and share them with the community.
21. As a user, I want to have a "My Plans" page where I can see all my plans and comments so that I can easily manage and track my contributions.
22. As a user, I want to edit and delete my own plans and comments so that I can update my strategies or remove content as needed.
23. As a site administrator, I want to view all categories in the plans section so that I can oversee the variety of strategies being shared.
24. As a site administrator, I want to add, edit, or delete categories in the plans section so that I can manage the structure and organization of strategies.
25. As a site administrator, I want to view all plans and comments from users so that I can monitor the strategies and feedback being shared in the community.
26. As a site administrator, I want to edit or delete plans and comments from users when necessary to ensure that the content aligns with community guidelines and standards.

### Profile
27. As a user, I want to be able to register an account so that I can participate in the community, create posts, plans, and comments.
28. As a registered user, I want to be able to log in to my account so that I can access my personalized features such as "My Profile", "My Posts" and "My Plans".
29. As a user, I want the website to provide error messages if I enter incorrect login information so that I can correct my input and successfully log in.

30. As a registered user, I want to log out from my account to ensure that my account is secure when I'm not using the site.

## User Story Images 

### User Story 1
![alt text](media/user_story_1.png "User Story 1")
### User Story 2
![alt text](media/user_story_2.png "User Story 2")
### User Story 3
![alt text](media/user_story_3.png "User Story 3")
### User Story 4
![alt text](media/user_story_4.png "User Story 4")
### User Story 5
![alt text](media/user_story_5_1.png "User Story 5 - First")
![alt text](media/user_story_5_2.png "User Story 5 - Second")
### User Story 6
![alt text](media/user_story_6.png "User Story 6")
### User Story 7
![alt text](media/user_story_7_1.png "User Story 7 - First")
![alt text](media/user_story_7_2.png "User Story 7 - Second")
![alt text](media/user_story_7_3.png "User Story 7 - Third")
### User Story 8
![alt text](media/user_story_8_1.png "User Story 8 - First")
![alt text](media/user_story_8_2.png "User Story 8 - Second")
### User Story 9
![alt text](media/user_story_9.png "User Story 9")
### User Story 10
![alt text](media/user_story_10.png "User Story 10")
### User Story 11
![alt text](media/user_story_11.png "User Story 11")
### User Story 12
![alt text](media/user_story_12.png "User Story 12")
### User Story 13
![alt text](media/user_story_13.png "User Story 13")
### User Story 14
![alt text](media/user_story_14_1.png "User Story 14 - First")
![alt text](media/user_story_14_2.png "User Story 14 - Second")
![alt text](media/user_story_14_3.png "User Story 14 - Third")
### User Story 15
![alt text](media/user_story_15.png "User Story 15")
### User Story 16
![alt text](media/user_story_16_1.png "User Story 16 - First")
![alt text](media/user_story_16_2.png "User Story 16 - Second")
### User Story 17
![alt text](media/user_story_17_1.png "User Story 17 - First")
![alt text](media/user_story_17_2.png "User Story 17 - Second")
![alt text](media/user_story_17_3.png "User Story 17 - Third")
### User Story 18
![alt text](media/user_story_18.png "User Story 18")
### User Story 19
![alt text](media/user_story_19.png "User Story 19")
### User Story 20
![alt text](media/user_story_20_1.png "User Story 20 - First")
![alt text](media/user_story_20_2.png "User Story 20 - Second")
### User Story 21
![alt text](media/user_story_21.png "User Story 21")
### User Story 22
![alt text](media/user_story_22_1.png "User Story 22 - First")
![alt text](media/user_story_22_2.png "User Story 22 - Second")
### User Story 23
![alt text](media/user_story_23.png "User Story 23")
### User Story 24
![alt text](media/user_story_24_1.png "User Story 24 - First")
![alt text](media/user_story_24_2.png "User Story 24 - Second")
![alt text](media/user_story_24_3.png "User Story 24 - Third")
### User Story 25
![alt text](media/user_story_25_1.png "User Story 25 - First")
![alt text](media/user_story_25_2.png "User Story 25 - Second")
### User Story 26
![alt text](media/user_story_26_1.png "User Story 26 - First")
![alt text](media/user_story_26_2.png "User Story 26 - Second")
![alt text](media/user_story_26_3.png "User Story 26 - Third")
### User Story 27
![alt text](media/user_story_27_1.png "User Story 27 - First")
![alt text](media/user_story_27_2.png "User Story 27 - Second")
![alt text](media/user_story_27_3.png "User Story 27 - Third")
![alt text](media/user_story_27_4.png "User Story 27 - Fourth")
![alt text](media/user_story_27_5.png "User Story 27 - Fifth")
### User Story 28
![alt text](media/user_story_28.png "User Story 28")
### User Story 29
![alt text](media/user_story_29.png "User Story 29")
### User Story 30
![alt text](media/user_story_30.png "User Story 30")

## Development Planes

### Strategy Plane
The strategy incorporates the user story needs. This website will focus on the following target audience, divided into two main categories:

* Fitness Enthusiasts who would like to view, contribute to and start discussions with the community
* Fitness Enthusiasts who would like to view, contribute to and share fitness plans with the community

#### Personality
* Bright
* Thoughtful
* Diligent
* Persistent
* Rational

#### Demographic
* Age - 18-60
* Gender - Male/Female
* Education - Some College

### Scope Plane

The scope of this website is to create an engaging, interactive, and helpful online community for fitness enthusiasts. The website offers a set of functionalities that allow users to share and gain knowledge, create and follow fitness plans, and engage with other community members. 

#### Functional Requirements

1. **User Authentication:** Users can create accounts, log in, and manage their profiles. This feature ensures a personalized and secure user experience.
2. **Community Posts:** Users have the ability to create, view, edit, and delete their own posts. They can also view posts made by others, fostering an environment of sharing and learning.
3. **Fitness Plans:** Users can create and manage their own fitness plans. They also have the option to view fitness plans shared by other users, promoting mutual growth and inspiration within the community.
4. **Commenting and Interaction:** Users can comment on posts and fitness plans, allowing for interaction and discussions. This fosters a sense of community and active engagement.
5. **Search / Forum Categorisation Functionality:** Users can search for fitness plans, making it easier to find relevant content. Community posts are structured in tables, allowing categories to be easily selected

#### Content Requirements

1. **Profiles:** Information about the user, including their plans, posts, comments
2. **Community Posts:** A variety of posts on topics related to fitness, health, diet, exercise routines, personal experiences, etc. 
3. **Fitness Plans:** Detailed plans centred around the topic of health and fitness
4. **Interactive Elements:** Comment sections to increase user engagement and interaction.
5. **Contact Form** A contact form allows users to submit a query to the site administrators 
6. **Donation Page** A donation page allows users to contribute to the running of the site.

The scope of this website is to offer a user-friendly, engaging, and informative platform for fitness enthusiasts to learn, share, and grow together in their fitness journey. 

### Structure Plane
The structure of the website will be as follows:

#### Home 
#### Community
##### Community Category
###### Community Post
###### Community Post Comment
#### Plans
##### Plans Description
##### Plans Description Comment
#### Profile
##### Plan Management
##### Post Management
##### Community Management
##### My Profile
##### My Plans
##### My Posts
##### Register
##### Login
##### Logout
##### Forgotten Password
#### Donate
#### Donate Success


### Skeleton Plane

### Balsamiq Wireframe Images
Below are the Wireframes created in Balsamiq for this project:
* Home Page Wireframe
![alt text](media/wireframe-home.png "Home Page Wireframe")
* Community Wireframe
![alt text](media/wireframe-community.png "Community Page Wireframe")
* Plans Wireframe
![alt text](media/wireframe-plans.png "Plans Page Wireframe")
* Profile Page Wireframe
![alt text](media/wireframe-profile.png "profile Page Wireframe")
* Contact Page Wireframe
![alt text](media/wireframe-contact.png "Contact Page Wireframe")
* Donate Page Wireframe
![alt text](media/wireframe-donate.png "donate Page Wireframe")


#### Home
The Home page is the landing page for your website, providing an overview of what the website is about and guiding users to the main features of the site.

#### Community
The Community page is a central hub where users can interact with each other. It includes the following:

#### Community Category
Each category in the Community section represents a different topic or area of interest. Clicking on a category takes the user to a list of posts in that category.

#### Community Post
Each post in a Community Category page represents a discussion or sharing of information about the category's topic. Clicking on a post takes the user to the post's page.

#### Community Post Comment
The comments on a Community Post page allow users to interact with the post, adding their own thoughts or responding to others.

#### Plans
The All Plans page lists all fitness plans available on the website.

#### Plans Description
Each plan in a Plans page includes a description of the plan and its details. Clicking on a plan takes the user to the plan's page.

#### Plans Description Comment
The comments on a Plans Description page allow users to share their experiences with the plan, ask questions, or provide feedback.

#### Profile
The Profile page is a personal hub for each user, including the following:

#### Plan Management
Allows administrators to manage the plans.

#### Post Management
Allows administrators to manage the community posts.

#### Community Management
Allows administrators to manage the contact forms submitted.

#### My Profile
Allows users to view and edit their personal information.

#### My Plans
Allows users to view the plans they've created or comments they've made

#### My Posts
Allows users to view the community posts they've created or comments they've made

#### Register
Allows new users to create an account.

#### Login
Allows existing users to log into their account.

#### Logout
Allows logged-in users to log out of their account.

#### Donate
The Donate page allows users to make a donation to support the website.

#### Donate Success
This page confirms that a user's donation was successful and thanks them for their support.

### Surface Plane
#### Colour Schemes
#### Graphics

# Features

## Head
- Each page of the website contains a relevant title
- Meta Tags: It includes three meta tags that set the character encoding (UTF-8), the browser compatibility (edge version for Internet Explorer), and the viewport (width=device-width, initial-scale=1).
- Static CSS File: There's a reference to a static CSS file named 'base.css' for defining the styles used across the website.
- Bootstrap: It includes Bootstrap 4.6.2 for responsive design, grid layout and CSS components.
- Google Fonts: There are preconnect links to the domains fonts.googleapis.com and fonts.gstatic.com, which are used to establish a network connection in advance, optimizing load times. A link to a specific Google Fonts stylesheet is also included, which is used to load various weights and styles of the Roboto font.
- Font Awesome: It includes a script for loading Font Awesome, which is a toolkit for adding vector icons and social logos to a website.
- Stripe: It includes a script for loading Stripe.js, a library provided by Stripe for handling online payments.

## Header
- Bootstrap is used to construct the header
- It will be clear what page the user is on, as the color of the list item will be different
- When hovering over a different list item, the color will change
- Clicking on the brand name takes the user to the home page
- For smaller screens, a vertical navbar (hamburger) is used, displaying the nav items in block
- There is a image at the top of each page, which is fitness related and holds the page title.

## Footer
- Bootstrap is used to contruct the footer
- About information is held on the left side of the page
- Site Links are held on the right of the page
- The site link change color when hovering
- For smaller screens, the about section is displayed in block (From top to bottom: About, Site Links)

## Home
- The home page contains introductory text, describing the website and it's purpose
- There are cards displayed for each section of the website, that provide an image and a brief summary and a button to click (taking the user to that section of the website).
- a responsive design ensures that as the screen size is reduced, the number of cards held on the horizontal axis also reduces.

## Community
- The community page contains an introduction to the purpose of the page and how the sub-pages within the community page is structured
- A table is presented, which indicated the category of post, the number of posts for the category and the latest post date/time
- When the user clicks into a row, it will take the user to the relevant Community Category page.
- Title: The title for the page is set to "Community" using the title block from the base template.
- Image: Similarly, the image block from the base template is set to display "Community".
- Community Active: The "community" block is set to "active", enabling the current active class in the navigation menu.
- An introductory section describing the content of the page.
- A responsive table which displays categories of posts. If the user is authenticated, they are provided with a button to add a post.
- The columns within the table are: category name, description, number of posts, latest post
- A JavaScript script is included which makes entire table rows clickable, redirecting to a URL determined by a data-href attribute.

### Community Category
- Title: The title for the page is set to "Category Posts" using the title block from the base template.
- Image: Similarly, the image block from the base template is set to display "Category Posts". The specific usage of this block will depend on how it's defined in "base.html".
- Community Active: The "community" block is set to "active", enabling the current active class in the navigation menu.
- A paragraph describing the posts for a specific category.
- A responsive table which displays posts in the selected category. Each row corresponds to a post, displaying its title, author, number of comments, and the date it was posted. 
- If no posts are available in the category, a message indicating this is displayed. 
- If the user is authenticated, they are provided with a button to add a post.
- A JavaScript script is included which makes entire table rows clickable, redirecting to a URL determined by a data-href attribute.

### Community Post
- Title: The title of the page is set to "Post".
- Image: The image block is set to "Post". Its specific use depends on how it's defined in the base template.
- Community Active: The "community" block is set to "active", enabling the current active class in the navigation menu.
- Details of the post: This includes the post's title, the category of the post, and the author's name, and the date it was posted.
- Post Content: This section includes the content of the post.
- Comments: This section includes an interactive comments section that collapses and expands when clicked. For each comment, it shows the author and the date it was created. If no comments are available, it shows a message "No comments yet".
- Add Comment: If the user is authenticated, they will see a button allowing them to add a comment to the post.

### Community Management
- This template extends base.html, with the title, image, and profile blocks set to "Community Management", "Community Management", and "active", respectively.
- In the content block, it presents management interfaces for categories, posts, and comments. Administrators can add, edit, and delete categories; view post details, edit, and delete posts; view comment details, edit, and delete comments. Note that some columns in these tables will not display for small and medium screen sizes to optimize for mobile viewing.
- At the end of the template, it includes a script that allows table rows to be clickable by assigning a URL to them.

### My Posts
- This template extends base.html, with the title, image, and profile blocks set to "My Posts", "My Posts", and "active", respectively.
- In the content block, it displays a list of posts and comments made by the current user. For each post and comment, it shows relevant details (like title, category, date, etc.) and options to edit or delete. Similar to the previous tables mentioned, some columns in these tables will not display for small and medium screen sizes.
- At the end of the template, it includes a script that allows table rows to be clickable by assigning a URL to them.

### Community Forms
- This template extends base.html, with the title, image, and profile blocks set to "Add Category", "Add Category", and "active", respectively.
- In the content block, it provides a form to enable CRUD functionality, such as adding or edits posts/comments/categories. Django's form system automatically handles much of this (the form.as_p line), including rendering form fields for all the fields in the category model.

## Plans
- This webpage is titled "Plans" and it extends from the base layout. It contains introductory text about the fitness plans offered on the site, along with details on how to use search and sorting functionalities.
- If the user is logged in, they will see an "Add Plan" button, otherwise they'll be prompted to login or register to contribute. 
- There is a search bar for searching plans and a dropdown for sorting them. 
- All the available fitness plans are listed in a row-based card layout with an image, name, category and the author. If no image is provided for a plan, a default image is used.
- the number of cards decreases horizontally as the screen size reduces, to enable a more responsive design

## Plans Description
- This webpage is titled "Plan" and it extends from the base layout. 
- It provides detailed information about a single fitness plan, including its name, category, author, and the date it was posted. 
- If there's an image associated with the plan, it's displayed on the page.
- There's a section for the plan's description, and another collapsible section for displaying comments about the plan. 
- If there are no comments, a message saying "No comments yet." is displayed. 
- If the user is logged in, they can see an "Add Comment" button for adding comments to the plan.

## Plan Management 
- This webpage is titled "Plan Management" and it extends from the base layout. It's a page intended for administrators, containing tables for managing categories, plans, and comments.
- For each category, administrators can see its name and description, and buttons for editing and deleting the category. 
- Similar details are provided for plans, along with an accordion feature to view more information about a plan. 
- The comments table displays the content of each comment, the plan it's associated with, and the author. Administrators can also edit and delete comments.
- At the start of each section, there's a "Add" button for adding new categories, plans, and comments. 
- There's also a jjquery script included at the end of the page that makes table rows clickable, taking the administrator to the appropriate edit page when clicked.

## My Plans

- The {% load static %} tag loads the static template tags which are a collection of template tags for serving static files.
- {% block title %}My Plans{% endblock %} specifies the title of the page as "My Plans".
- {% block image %}My Plans{% endblock %} sets the title in the image header
- {% block profile %}active{% endblock %} This block indicates the currently active page in the navigation bar.
- The content block contains two sections, one for "Plans" and one for "Comments". 
- In each section, there's an explanatory paragraph and a table. 
- The table lists the respective items (plans/comments) and provides "Edit" and "Delete" buttons for each one. 
- If there are no items to list, it displays a message to that effect.
- A small jQuery script that adds a click event to any element with a "data-href" attribute, which makes the entire element clickable, redirecting the user to the URL specified in "data-href". 

### Plans Forms
- These template extends base.html, with the title, image, and profile blocks set to "Add Category", "Add Category", and "active", respectively.
- In the content block, it provides a form to enable CRUD functionality, such as adding or edits plans/comments/categories. Django's form system automatically handles much of this (the form.as_p line), including rendering form fields for all the fields in the category model.

## My Profile
- This contains a form for updating the user profile name. 
- The form includes a single field rendered by {{ form.as_p }}.
- This is then displayed when the user creates/comments on a plan/post.

## Contact
- The contact page contains a form that the user is able to complete. It asked for their Name, Email and Message.
- The "Submit" button is disabled until the user completes all fields. The color of the "Submit" button will slightly change when this occurs

## Contact Management
- The page title and image block are set to "Contact Management".
- The content block of the page contains a header, some descriptive text, and a table showing all submitted contact forms.
- Each row in the table corresponds to a single contact form.
- Columns include "Name", "Email", "Created", "Updated", "Status", and "Action".
- Each row is also a link to an update page for the respective contact form.
- There's also a delete button in the "Action" column that can stop the event propagation when clicked to avoid triggering the row's click event.
- The page also includes a script at the end (inside the "endscripts" block). This script makes each row in the table clickable, redirecting to the URL stored in the "data-href" attribute of the row when clicked.

## Contact Update 
- The page title and image block are set to "Update Contact Form".
- The content block of the page contains:
1. A form to update the contact form.
2. A link to return to the "Contact Management" page.
3. A list of comments associated with the contact form.
4. A form to add a new comment to the contact form.

## Donate
- The page title and image block are set to "Donate".
- The content block of the page contains:
1. A message thanking users who have donated.
2. A donation form for users who have not donated yet.
3. Instructions to login or register for users who are not authenticated.
4. The page includes an additional CSS file located at 'donate/css/donate.css' and a JavaScript file located at 'donate/js/donate.js'.
5. There are a few conditional blocks within the content that check the authentication and donation status of the user. These blocks render different HTML content depending on the user's status.

## Donate Success
- The page title and image block are set to "Donate Success".
- The content block of this page contains:
1. A thank you message for the users who have made a donation.
2. A list of how their donation helps the website.
3. A button that redirects users to the homepage of the website.

# Technologies Used

## Main Technologies Used
### HTML5
### CSS3
### Javascript
### Python+Django
### PostgreSQL
### Stripe

## Frameworks, Libraries & Programs Used
### Amazon Web Services
Amazon Web Services was used to serve media and static files in the production environment of this project.
### Bootstrap
Bootstrap was used in the media page to assist with enabling a responsive design
### jQuery 
jQuery was sparingly used within the project
### Google Fonts
Google fonts was used to import the fonts Barlow, Chivo Mono, Lato, Oswald & Quantico into the style.css file.
### Font Awesome
Font Awesome was used to assist with the styling of the website, such as providing a caret icon for the comments section, to denote that there was a dropdown.
### GitPod
GitPod was used for writing code, commiting, and then pushing to GitHub.
### GitHub
GitHub was used as the repository for the code.
### Balsamiq
Balsamiq was used to create the wireframes during the design of the project.

## Testing Procedure
For the implementation of both automated and manual testing, an explanation is provided for each sub-section of testing, followed by a table of the test results.
### Manual Testing Procedure

#### Browser testing
In this test, the application is tested on various web browsers to ensure that it is working properly across different browsers and their versions. Testers check for compatibility issues with different browsers and ensure that the application's functionalities are consistent across different browsers.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|-----------------|--------|
| 1       | Automated Cross-Browser Testing | The website should function correctly and display as intended on all tested browsers (Safari, Edge, Chrome, Explorer) |   Pass |
| 2       | Manual Functionality Testing on Safari, Edge, Chrome, Explorer | All website features (forms, buttons, links, navigation, etc.) should work as expected. |  Pass |
| 3       | Manual Layout and Design Testing on Safari, Edge, Chrome, Explorer | The website's layout and design (text, images, colors, styles, responsive design, etc.) should appear correctly. |  Pass |

#### Data Management
This test type ensures that the application's data management functions work correctly. Testers verify that the data is being stored, retrieved, and manipulated properly. They also check that the CRUD functionality is working correctly. 

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | Data Storage, Retrieval, and Manipulation | The application's data should be properly stored, retrieved, and manipulated. | Pass |
| 2       | CRUD Functionality for Applicants/Applications and Listings | The application should correctly implement Create, Read, Update, and Delete functionality for each of the various data schemas | Pass |

#### Functionality/Usability/Interactvity 
This test type assesses the application's functionality, usability, and interactivity. Testers check if all features and functionalities are working as intended, if the application is user-friendly, and if user interaction is smooth, as specified in the features section of the README.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | Functionality Test | All features and functionalities should work as intended. | Pass |
| 2       | Usability Test | The application should be user-friendly. | Pass |
| 3       | Interactivity Test | User interaction with the application should be smooth. | Pass |

#### Heroku Deployment
This test type focuses on the deployment of the application on the Heroku platform. Testers check if the application is successfully deployed and accessible on the Heroku platform. They also ensure that this matches the development version.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | Heroku Deployment Test | The application should be successfully deployed and accessible on the Heroku platform, matching the development version. | Pass |

#### Lighthouse
This test type uses Google's Lighthouse tool to assess the application's performance, accessibility, best practices, and SEO. Testers use the tool to generate a report and check for any issues or recommendations.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | Lighthouse Performance, Accessibility, Best Practices, and SEO Test | The Lighthouse tool should generate a report without any major issues | Pass |

#### PEP8 Compliance
PEP 8 is a set of guidelines and recommendations for writing clean, readable, and maintainable Python code. It covers topics such as naming conventions, code layout, function and class design, and documentation. Adhering to PEP 8 helps improve the consistency and quality of Python code, making it easier to understand, debug, and collaborate on.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | PEP 8 Compliance Test | The Python code in the application should adhere to the guidelines and recommendations in PEP 8. | Pass |

#### Responsiveness
This test type checks the application's responsiveness across different screen sizes and devices. Testers ensure that the application's layout adjusts correctly to different screen sizes and that all features are accessible on different devices, as specified in the features section of the README.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | Responsiveness Test Across Different Screen Sizes | The application's layout should adjust correctly to different screen sizes. | Pass |
| 2       | Responsiveness Test Across Different Devices | The application's layout should adjust correctly for different devices (e.g. Mac and Windows Laptops). | Pass |

#### User Story Validation
This test type ensures that the application meets the requirements of the user stories. Testers verify that all user stories are addressed and implemented correctly. They also ensure that the application's functionalities are in line with the user's needs and expectations.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | User Story Validation Test | All user stories should be addressed and implemented correctly. The application's functionalities should align with the user's needs and expectations. | Pass |


### Automated Testing Procedure

#### HTML Validator
This automated test type checks the HTML code for errors and warnings. The HTML Validator tool (validator.w3.org) checks for proper markup, syntax errors, and other issues that can cause problems with the rendering of web pages. It provides a detailed report of errors and warnings, allowing developers to fix them quickly. NOTE: the validator contain warning, derived from the Django templating language.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | HTML Validation Test | The HTML Validator tool should return a report with no errors | Pass |

#### CSS Validator
This automated test type checks the CSS code for errors and warnings. The CSS Validator tool (jigsaw.w3.org/css-validator/) checks for syntax errors, compliance with CSS standards, and other issues that can cause problems with the appearance and layout of web pages. It provides a detailed report of errors and warnings, allowing developers to fix them quickly.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | CSS Validation Test | The CSS Validator tool should return a report with no errors or warnings. | Pass |

#### Javascript Validator
This automated test type checks the JavaScript code for errors and warnings. The JSHint tool (JSHint) checks for syntax errors, potential bugs, and other issues that can cause problems with the functionality of web pages. It provides a detailed report of errors and warnings, allowing developers to fix them quickly.

| Test ID | Test Description | Expected Outcome | Status |
|---------|------------------|------------------|--------|
| 1       | JavaScript Validation Test | The JSHint tool should return a report with no errors or warnings. | Pass |


# Deployment

## ElephantSQL Database hosting
1. Log in to ElephantSQL.com to access your dashboard
2. Click “Create New Instance”
3. Set up your plan (Free)
4. Select “Select Region”
5. Select a data center near youThen click “Review”
6. Check your details are correct and then click “Create instance”
7. Return to the ElephantSQL dashboard and click on the database instance name for this project
8. In the URL section, clicking the copy icon will copy the database URL to your clipboard
9. The URL is then used when setting up the Heroku App


## Deployment on Heroku
1. To deploy on Heroku, the following steps were taken:
2. Set Up A New Heroku App
3. Give your app a name and select the region closest to you
4. In the setting tab, add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL.
5. Connect Git Remote
6. Add A Requirements.txt file
7. Add A Procfile file
8. Connect App to Github
9. Set Up The Environment Variables in Heroku
10. Enable The Automatic Deployment

## Project preparation in your IDE
1. In the terminal, install dj_database_url and psycopg2
2. Update your requirements.txt file
3. In your settings.py file, import dj_database_url underneath the import os
4. Connect to the new ElephantSQL database in the settings.py file
5. Run the Makemigrations and Migrate commands in the terminal

## Amazon Web Services Setup
1. create AWS account
2. AWS management console
3. Search for S3 service
4. Create new bucket
5. Select Region
6. Allow bucket to be public
7. Ensure settings are configured: 
    * Enable static website hosting
    * Cross-origin resource sharing (CORS) Configuration
    * Bucket Policy
    * Access control list (ACL) 
8. Setup Identify and Access Management (IAM)
    * Create group
    * Create policy
    * Attach policy
    * Create User
    * Download CSV, containing keys
    * Add user to Group
9. Django to S3, by adding config vars to Heroku and adding to settings.py file (including media and static urls).

# Credits

The following sites were used:
* Bootstrap
* Code Institute
* Font Awesome
* https://beautifier.io/
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* https://peps.python.org/pep-0008/
* Jquery
* JSHint
* Stack Overflow
* W3Schools
* www.freeformatter.com
* Youtube

# Acknowledgements
I would like to thank all parties within the credits section

I would also like to thank my mentor, Koko, for her invaluable help and guidance throughout the project.