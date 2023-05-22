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
28. As a user, I want the website to provide error messages if I enter incorrect login information so that I can correct my input and successfully log in.
29. As a registered user, I want to be able to log in to my account so that I can access my personalized features such as "My Profile", "My Posts" and "My Plans".
30. As a registered user, I want to log out from my account to ensure that my account is secure when I'm not using the site.