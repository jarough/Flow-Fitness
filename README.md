# Flow-Fitness

## Table of Contents

### UX Design
* Project Goals
* Design Choices
* User Stories
* Database Schema


### Features

### Technologies Used
### Testing
### Deployment
### Credits
* Content
* Media
* Code
* Acknowledgements

## UX Design

### Project Goals
My goal from this project is to establish a gym management system for a local business to utilise. This system will include various features such as user profiles and a text wall to post about individual successes, as well as subscription models to name a few.

The goals for the site user are:
* Have the ability to join a create an account and join a fitness group.
* To be able to review and join personalised exercise plans for a subscription fee.
* To have the option to purchase merchandise and gym equipment for use at home.

The goals for the site owner are:
* To be able to generate fitness groups based on how many people subscribe to a certain model.
* To be able to sell exercise plans depending on the type of person and their needs.
* To be able to sell exercise equipment through an in-site payment system.

### User Stories
As a recently registered member of the site, I want:
* The ability to login and view my personal profile.
* The ability to browse the equipment store and sort the products by specific categories.
* The ability to post success stories to a feed for other members to see.
* The ability to purchase a subscription plan through the use of credit card payment.

### Database Schema
The database will consist of several tables for each specific aspect of the site:
* **Users**
    * User ID
    * Name
    * Password
    * Email
    * Current Membership
* **Memberships/Subscriptions**
    * Membership ID
    * Name
    * Description
    * Price
* **Equipment**
    * Equipment ID
    * Name
    * Price
* **Payments**
    * User ID
    * Payment Date
    * Price
    * Payment Method

## Features

### Existing Features
* Navigation System
* Message Wall
* User Profiles
* Testimonials Section
* Subscription Payments
* Store Payments
* Login authentication for registered users and admin users

### Features to be implemented
* A gallery of videos and photos of the gym.



## Technologies Used
* HTML
* CSS
* Bootstrap v5.2
* Python 3.8.6
* Django 3.2
* JavaScript

## Deployment
This project was developed using Visual Studio Code IDE with commits to git and pushed to GitHub using Source Control.

To deploy this page to GitHub Pages, these steps were taken:
1. Log into GitHub
2. Select repository **"jarough/Flow-Fitness"**
3. Click on settings at the top of repository page
4. Find the GitHub Pages section
5. Under **Source** select the branch 'Master Branch' instead of 'None'
6. The page is refreshed and the website is now live.

To clone this project:
1. Follow the [link](https://github.com/jarough/Flow-Fitness) to the repository
2. Click on the green **Code** button above the file list
3. Make sure **HTTPS** is highlighted and copy the link below it
4. Open Git Bash
5. Change the working directory to the location you want the cloned directory
6. Type 'git clone' followed by the URL you copied
7. Press **Enter** to create the clone.



## Credits

### Content/Media
* Images featured in this site were sourced from:
    * [Freepik](https://www.freepik.com/)
    * [Vecteezy](https://www.vecteezy.com/)

### Code
* Code for the navbar taken and modified from [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) documentation.
* Code for initially setting up the Django system sourced from the Code Institute Boutique Ado walkthrough project.
https://getbootstrap.com/docs/5.2/components/card/#titles-text-and-links