# <span id="overview"></span>Always Away

![picture of responsive design](/media/gallery/responsiveness.png)

Always Away is a blog site, with the intention to create a community. The author is a long-term expatriot who wishes to create a safe space for users to share stories and feel a sense of camaraderie. Whether a fellow willing wanderer, displaced person, dreaming of the adventures, or simply intrigued by the stories of the migrating life - all are welcome.

View the live site by clicking [HERE](https://always-away-227aba88ca4e.herokuapp.com/).


# <span id="contents-menu"></span>Contents menu
- [_Always Away_](#overview)
- [_Contents menu_](#contents-menu)
- [_UX_](#ux)
  - [_Site Purpose_](#purpose)
  - [_Site Goal_](#site-goal)
  - [_Target Audience_](#audience)
  - [_Modern Community_](#communication)
  - [_New User Goals_](#new-user-goals)
  - [_Current User Goals_](#current-user-goals)
  - [_Future User Goals_](#future-goals)
- [_Accessibility_](#accessibility)
- [_Agile Methodology_](#agile)
- [_User Stories_](#user-stories)
- [_Wireframes_](#wireframes)
- [_Features_](#features)
  - [_Navbar_](#navbar)
  - [_Footer/Social Media_](#footer)
  - [_Homepage_](#homepage)
  - [_Post Detail_](#post-detail)
  - [_Sign Up_](#signup)
  - [_Sign In_](#signin)
  - [_Log Out_](#logout)
  - [_Upvote/Downvote_](#likes)
- [_C.R.U.D._](#crud)
  - [_Commenting_](#comments)
    - [_Create_](#c)
      - [_Post Comment_](#post-comment)
    - [_Read_](#r)
      - [_View Comment_](#view-comment)
    - [_Update_](#u)
      - [_Edit Comment_](#edit-comment)
    - [_Delete_](#d)
      - [_Delete Comment_](#delete-comment)
  - [_Messaging_](#messaging)
    - [_Create_](#c)
      - [_Send Message_](#send-message)
    - [_Read_](#r)
      - [_Read Message_](#read-message)
    - [_Update_](#u)
      - [_Edit Message_](#edit-message)
    - [_Delete_](#d)
      - [_Delete Message_](#delete-message)
- [_Technologies_](#tech)
  - [_Main Languages_](#languages)
  - [_Frameworks, Libraries, and Programs_](#frameworks)
  - [_Installed Packages_](#packages)
- [_Deployment_](#deployment)
  - [_Forking in Github_](#forking)
  - [_Running Local Environment_](#local)
  - [_Deploying to Heroku_](#heroku)
- [_Bugs_](#bugs)
  - [_Fixed Bugs_](#fixed)
  - [_Remaining Bugs_](#remaining)
- [_Testing_](#testing)
  - [_Validator Testing_](#validator)
- [_Credits_](#credits)
- [_Media_](#media)
- [_Team Members_](#team)

Always Away is a community blog site, written with the intention of sharing experiences and engaging with like-minded individuals. Here, I'll be sharing my personal journey and experiences as a long-term expatriot. Whether you're a fellow willing wanderer, displaced person, dreaming of the adventures in your own future, or simply intrigued by the stories of the migrating life, you are invited to join in to create an online community.

## <span id="ux"></span>UX

### <span id="purpose"></span>Site Purpose:
This site's intention is to create an online society. [Always Away](https://always-away-227aba88ca4e.herokuapp.com/) is meant to convey understanding, create community, and inspire a feeling of camaraderie amongst both strangers and friends.

### <span id="site-goal"></span>Site Goal:
The goal is to create a platform for online communication. The site intents to create an engaging experience to provide a modern sense of community in a growing and ever-alienating world. Where one neighborhood disappears in person, the site can provide digitally.

### <span id="audience"></span>Target Audience:
For citizens of the world with a thirst for adventure, the restless and onlookers alike. By having this avenue of online interaction, users will be able to get a taste of each other's experiences -  hopes, dreams, struggles, heartache...everything that compiles the life of a modern-day nomad or immigrant.

### <span id="communication"></span>Modern Community:
The worldwide web is a vital avenue of communication for modern day travelers, nomads, displaced persons, those left behind, or for any reason long-distance relationships. Without this form of computer-generated interaction, we would still be sending snail mail that may be lost after months in transit.

### <span id="new-user-goals"></span>New User Goals:
To intuitively navigate the site content, create account, and begin to engage with all there is to explore.

### <span id="current-user-goals"></span>Current User Goals:
Engage in the online community via comments or messaging to the site's author. For travellers to share their experiences
and possibly make a new friend along the way.

### <span id="future-goals"></span>Future Goals:
- To create a profile page for each user to have expanded capacity for sharing and interacting. 
- To implement functionality for users to post their own blog posts, including photos and text.
- To allow the site's admin to message individual users in response to their messages.
- To expand site's useability by categorizing posts and comments for users to easily be able to search for a spcific word or topic.

### <span id="accessibility"></span>Accessibility and Design:

This Django blog project prioritizes functionality and a positive user experience. The decision to use the standard Django template was deliberate, with a focus on providing a reliable and efficient platform for users. The choice of a standard template ensures consistency across the site, making navigation intuitive and straightforward.

### Key Points:

- **Functionality First:** The primary goal was to build a blog that meets user needs, ensuring a seamless and efficient experience.
  
- **Usability and Accessibility:** Attention was given to usability, accessibility, and responsiveness to enhance the overall user experience.

- **Standard Template for Consistency:** The use of the standard Django template was intentional, providing a clean and uniform design throughout the site.

- **Color Contrast and Design:** Careful consideration was given to color contrast, and the overall color scheme contributes to a visually pleasing interface.

- **Future Customization:** The standard template sets the stage for future updates or customization without compromising the existing design.

- **Efficiency in Development:** Opting for the standard template allowed for efficient development, emphasizing core features without unnecessary complexity.

This approach reflects a balance between a user-centric design philosophy and efficient development practices.



### <span id="agile"></span>Agile Methodology:
The principles of agile methodology were implemented during the project. By assigning user stories to issues and utilizing the GitHub Kanban board, the necessary project goals could be easliy prioritized. Labels were used to fine tune the priority of each user story.

## <span id="user-stories"></span>User Stories
## Epics

1. **User Account Management**
- [X] I can register an account so that I can comment and like.
- [X] I can log in to my account and see my messages so that keep track of conversations with admin.
- [X] I can edit my comments so that I can more deeply interact with the community.
- [X] I can delete my own comments so that change my mind about a comment.

2. **Content Viewing and Interaction**
- [X] I can view a paginated list of pages so that I can easily select a page to view.
- [X] I can view a list of posts so that I can select one to read.
- [X] I can click on a post so that I can read the full text.
- [X] I can leave comments on a post so that I can be involved in the conversation.
- [X] I can view comments on an individual post so that I can read the conversation.
- [X] I can like or unlike a post so that I can interact with the content.
- [X] I can view the number of likes on each post so that I can see which is the most popular or viral.

3. **Messaging System**
- [X] I can create a draft message and save without sending so that I can take my time formulating a message over more than one site visit/login.
- [X] I can send a message to the admin so that I can interact with the creator of the blog.
- [X] I can delete messages so that I can clean out my inbox.

4. **Content Creation and Management (Admin)**
- [X] Admin can view comments on an individual post so that they can read the conversation.
- [X] Admin can leave comments on a post so that they can be involved in the conversation.
- [X] Admin can approve or disapprove comments so that they can filter out objectionable comments.
- [X] Admin can delete messages so that they can clean out their inbox.
- [X] Admin can view the number of likes on each post so that they can see which is the most popular or viral.
- [X] Admin can create draft posts so that they can finish writing the content later.
- [X] Admin can create, read, update, and delete posts so that they can manage blog content.

*Disclaimer: The following User stories have not yet been implemented. They have been left on the project for the purpose of organizing future goals and projects to expand and enhance the blog site.

- I can **make a blog post**
- I can **utilize a search capability** so that **I can easily locate specific topics or posts**
- I can **organize messages by category** so that **I can quickly search for a message I want to find**
- I can **upvote on comments** so that **earn Karma points, eventually rewarding me with badges or digital trophies**
- I can **mark a message as read** so that **my account can keep track for me if I have read a message or not**
- I can **use a reply function on messages** so that **I can continue a string of messages with admin**
- I can **utilize a search capability** so that **I can easily locate specific topics or posts**
- I can **categorize posts into sub-threads** so that **keep multiple posts organized**
- I can **send message to Users from admin panel** so that **I can more personally interact with site Users**
- I can **receive notifications** so that **I can see when someone likes or comments on my post**

## <span id="wireframes"></span>Wireframes:
The combination of a textual mindmap and a Lucidchart flowchart strikes a balance between clarity and visual representation. The textual mindmap ensures a quick, accessible overview, while the Lucidchart flowchart adds depth to user flows, fostering a comprehensive understanding of the blog's structure and interactions.

- Admin Panel
  - **Blog Management**
    - Create Blog
    - Edit Blog
    - Publish Blog
    - Save as Draft
    - Delete Blog
  - **Comment Supervision**
    - View Comments
  - **Message Reading**
    - Inbox
    - Draft Inbox
    - Sent Messages

![screenshot of Admin Wireframe](/media/gallery/admin-panel-wireframe.png)

- Front-End User Interaction
  - **Home Page**
    - Scrollable List of Published Blogs
  - **Navbar**
    - Register/Sign Up
    - Login
    - Logout
    - Home Page Navigation
  - **Authenticated User**
    - Inbox
    - Draft Message Inbox
    - Sent Messages Inbox
    - **Message Actions**
      - Send to Admin
      - Save as Draft
      - View Sent Messages
      - Delete Messages

![screenshot of UX Wireframe](/media/gallery/ux-wireframe.png)

## <span id="features"></span>Features
### <span id="navbar"></span>Navbar:
Desktop View while user is logged out/unregistered:
![screenshot of logged out Navbar](/media/gallery/navbar.png)
Mobile View while user is authenticated and logged in:
![screenshot of logged in Navigation](/media/gallery/navigation.png)

### <span id="footer"></span>Footer/Social Media:
![screenshot of Footer/Social Media Icons](/media/gallery/footer.png)

### <span id="homepage"></span>Homepage:
![screenshot of Homepage](/media/gallery/homepage.png)

### <span id="post-detail"></span>Post Detail View:
![screenshot of Post Detail View](/media/gallery/post-detail.png)

### <span id="signup"></span>Sign Up:
![screenshot of Sign Up Form](/media/gallery/sign-up.png)

### <span id="signin"></span>Sign In:
![screenshot of Sign In Form](/media/gallery/sign-in.png)

### <span id="logout"></span>Sign out:
![screenshot of Sign Out Form](/media/gallery/sign-out.png)

### <span id="likes"></span>Liking/Unliking:
![screenshot of Like Function](/media/gallery/likes.png)

## <span id="crud"></span>C.R.U.D.
### <span id="comments"></span>Commenting:
#### <span id="c"></span>Create:
##### <span id="post-comment"></span>Post Comment:
![screenshot of Post Comment Form](/media/gallery/post-comment-form.png)
#### <span id="r"></span>Read:
##### <span id="view-comment"></span>View Comment:
![screenshot of Comment Form](/media/gallery/comment-form.png)
#### <span id="u"></span>Update:
##### <span id="edit-comment"></span>Edit Comment:
![screenshot of Edit Comment Form](/media/gallery/edit-comment-form.png)
#### <span id="d"></span>Delete:
##### <span id="delete-comment"></span>Delete Comment:
![screenshot of Delete Comment Form](/media/gallery/delete-comment-form.png)
### <span id="messaging"></span>Messaging:
#### <span id="c"></span>Create:
##### <span id="send-message"></span>Send Message:
![screenshot of Send Message Form](/media/gallery/send-message-form.png)
#### <span id="r"></span>Read:
##### <span id="read-message"></span>Read Message:
![screenshot of Read Message Form](/media/gallery/view-message.png)
#### <span id="u"></span>Update:
##### <span id="edit-message"></span>Edit Message:
![screenshot of Draft Inbox](/media/gallery/draft-inbox.png)
![screenshot of Edit Message Form](/media/gallery/edit-message-form.png)
#### <span id="d"></span>Delete:
##### <span id="delete-message"></span>Delete Message:
![screenshot of Delete Message Button](/media/gallery/view-message.png)

## <span id="tech"></span>Technologies
### <span id="languages"></span>Main Languages:
- Python
- Javascript
- HTML5
- CSS3 + SVG

### <span id="frameworks"></span>Frameworks, Libraries, and Programs:
- [Python Built-in "os" Modules](https://docs.python.org/3/library/os.html)
- [Django](https://pypi.org/project/Django/3.2.14/)
- [Bootstrap + jQuery](https://getbootstrap.com/)
- [ElephantSQL](https://www.elephantsql.com/)
- [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gad=1&gclid=Cj0KCQjwgNanBhDUARIsAAeIcAunN7Ty8U3gZ7QFYnOuxM59Z22YZb6_bVmSwDBKKpWY2BvyYmsZHlUaAmkeEALw_wcB)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/icons/instagram?s=solid&f=brands)
- [GitHub:](https://github.com/)
- [GitPod:](https://gitpod.io/)
- [Am I Responsive?](https://ui.dev/amiresponsive?url=https://krystalcoding.github.io/antisocial-dog-meetups/)
- [Favicon.io](https://favicon.io/)
- [Figma Wireframing](https://www.figma.com/wireframe-tool/?utm_source=google&utm_medium=cpc&utm_campaign=20335659807&utm_term=online%20wireframe%20tool&utm_content=664692216843&gclid=Cj0KCQjwgNanBhDUARIsAAeIcAt2VbuxIVbr5x1CH3hQsz0lcVeZaaVpQApMCS4M4wz0oNr2kHjJDAkaAtI7EALw_wcB)

### <span id="packages"></span>Installed Packages:
- 'django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote
- django-allauth
- django-crispy-forms

## <span id="deployment"></span>Deployment
### <span id="forking"></span>Forking in Github:
1. Navigate to the [project repository](https://github.com/KrystalCoding/always-away)
2. Top Right menu > "Fork"
3. Clicking the Fork button automatically saves a copy of the repo on your own, logged-in Github page

### <span id="local"></span>Running locally:
1. Navigate to the [project repository](https://github.com/KrystalCoding/always-away)
2. Click on the top right, green "Code" button
3. Choose one of the three options (HTTPS, SSH or GitHub CLI) and then click copy
4. Open the terminal in your IDE program
5. Type git clone into your terminal and paste the URL that was copied in step 3
6. Hit Enter and your local clone will be created.

Alternatively - Use Gitpod:
1. Navigate to the [project repository](https://github.com/KrystalCoding/always-away
2. Hit the green "Gitpod" button and the project will automatically open up for you

### <span id="heroku"></span>Deploying to Heroku:
1. Create [Heroku](https://dashboard.heroku.com/) account
2. Install Django & Gunicorn via terminal command: ```pip3 install 'django<4' gunicorn```
3. Install Django database & psycopg:
```pip3 install dj_database_url psycopg2```
4. Install Cloudinary:
```pip3 install dj3-cloudinary-storage```
5. Creating the requirements.txt file with the following command:
```pip3 freeze --local > requirements.txt```
6. My django project was created using: ```django-admin startproject always-away .```
7. The blog app was then created with: ```python3 manage.py startapp blog```
8. This was then added to the" "settings.py" file within the project directory
9. The changes were then migrated using:
```python3 manage.py migrate```
10. Navigate to [Heroku](www.heroku.com) & created a new app called "always-away"
11. Add the Heroku Postgres database to the Resources tab
12. Navigate to the Settings tab and add the following key/value pairs to the configvars:

- key: SECRET_KEY | value: randomkey
- key: PORT | value: 8000
- key: CLOUDINARY_URL | value: API environment variable
- key: DATABASE_URL | value: value supplied by Heroku

13. Create an "env.py" file
14. Add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the "env.py" file
15.added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the "settings.py" file
16. Add the "import os" command at the top of the "env.py" file
17. Add Heroku to the ALLOWED_HOSTS in "settings.py"
18. Create a "Procfile"
19. Push the project to GitHub using commands ```git add .``` , ```git commit-m "Commit message"``` , ```git push```
20. Use the Deploy tab in Heroku to connect to the github repository
21. Click "Deploy"


## <span id="bugs"></span>Bugs
### <span id="fixed"></span>Fixed Bugs:
* At first, I tried to connect posting, editing, and deleting messages to the comment Model and View. Once I realized this was stupid, I learned some things and re-focused the project.
* Static Files were not included and set up properly on deployment, but that was sorted.

### <span id="remaining"></span>Remaining Bugs:
* Footer is not sticking to the bottom of the screen below the forms.
* Message to ask user if they are sure they want to delete a message is not function. Code was removed from the repo for the sake of submitting the project, but it will be implemented eventually.
* Confirmation messages to let user know their messages were saved as a draft or sent successfully are not functioning. Again, code was removed temporarily.
* Unique photo upload to the blog posts via admin panel is not functioning and I do not currently know why, though the default image is being uploaded correctly.
*I ran out of time before deadline to finish testing procedures, but have run everything through validators to make sure it functions. It received a poor score on Lighthouse due to Largest Contentful Paint. Future fix will be to decrease the size of the photos and reupload them to Cloudinary and then to the site.

## <span id="testing"></span>Testing
### <span id="validator"></span>Validator Testing:

1. Manual testing
2. Automated testing

### Manual testing

1. As a site User I can view a paginated list of pages so that I can easily select a page to view

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the links (or hamburger icon on smaller screens) to intuitively access pagination via navigation bar | Nav bar drop down will open on smaller screens, and links will open to their associated pages. (See below for specific link functions) | Works as expected |
| Click on the Social Media icons link in the footer | Associated social media icons will load in a separate tab | Works as expected |
| Click on the 'Code Institute' or 'Django Framework' logos in the side panel | External tabs with associated websites will load | Works as expected |

<details><summary></summary>
<img src="">
<img src="">
<img src="">
<img src="">
</details>

9. As an Admin / Authorised User I can log in so that I can access the back end of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the admin page (ENTER LINK HERE)| Enter admin login credentials, gain access to back end | Works as expected |


<details><summary></summary>
<img src="">
<img src="">


</details>

3. As a Site Owner I can create and save draft blog posts, publish new blog posts, and edit formerly published posts.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on Create new post | New Post form will appear | Works as expected |
| Click on save post as draft | Post is saved in admin panel for further updates | Works as expected |
| Click on publish post | New Post is published on front end for public viewing | Works as expected |
| Click on edit post in admin panel | Updates are published on front end for public viewing | Works as expected |


<details><summary></summary>
<img src="">

</details>

4. As a site User, I can register a personal account, access inbox, compose messages and save as drafts for further editing, and send messages to site admin.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Register' link in the navigation bar | Sign up page will load| Works as expected |
| Click on the 'Sign in' link in the navigation bar | Login page will load| Works as expected |
| Click on the 'Contact' link in the navigation bar | Send Message to Admin form will load| Works as expected |
| Click on the 'Inbox' link in the navigation bar, or 'Primary Inbox' button in the Draft Inbox page | Inbox page will load | Works as expected |
| Click on the 'Draft Inbox' link in the navigation bar, or from the button in the Inbox page | Draft Inbox page will load| Works as expected |
| Click on the 'Logout' link in the navigation bar | Logout page will load| Works as expected |

<details><summary></summary>
<img src="">
<img src="">

</details>

2. As a site User, I can view blog post homepage, access individual posts for viewing content, comments, and likes. When logged in as a registered user, I can post my own comments and like posts.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | Click on 'Blog Home' and scroll to footer at bottom of page | View blog home page in full length, all the way to the footer | Works as expected |
 | Click on individual posts to view content, including comments and likes | Opens individual post with scrolling function | Works as expected |
 | Click on like button | Page refreshes and updates icon via user's action of either liking or unliking a post | Works as expected |
 | Write comment and post with button | Page refreshes with comment + ability for user to edit or delete their own comment | Works as expected |

<details><summary></summary>
<img src="">
<img src="">

</details>

5. As a site Owner, I can approve or delete user comments from blog posts.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on 'Comments' in admin panel| Choose to approve or delete user comments | Works as expected |

<details><summary></summary>
<img src="">
<img src="">

</details>

### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report


<details><summary>Bar & Grill App, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-models.PNG">
</details>

<details><summary>Bar & Grill App, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-views.PNG">
</details>

<details><summary>Bar & Grill App, test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-urls.PNG">
</details>

<details><summary>Bar & Grill App, Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/coverage-bar-and-grill.PNG">
</details>

<details><summary>Bookings App, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bookings-test-models.PNG">
</details>

<details><summary>Bookings App, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bookings-test-views.PNG">
</details>

<details><summary>Bookings App, test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bookings-test-urls.PNG">
</details>

<details><summary>Bookings App, Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/coverage-bookings.PNG">
</details>


### Device Testing & Browser compatibility

The site uses to test on various real world devices was [BrowserStack](https://ci-pp4-the-diplomat.herokuapp.com/)  

This allowed me to test on real devices and not just device emulators.

The following devices were used to test my site:

<details><summary>Samsung Galaxy S22 Ultra</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-samsung-s22-ultra.PNG">
</details>

<details><summary>Apple iPhone 13</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-iphone-13.PNG">
</details>

<details><summary>Google Pixel 5</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-google-pixel-5.PNG">
</details>

<details><summary>Mozilla Firefox (v105 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-firefox.PNG">
</details>

<details><summary>Google Chrome (v106 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-chrome.PNG">
</details>

<details><summary>Safari (Monteray v15.3 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/device-test-safari-monteray-15.3.PNG">
</details>


##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| css not loading| the css folder was created in uppercase as CSS, renamed and fixed |
| While logged in as a user, on edit bookings page, if you changed the url booking number and if the number was a valid booking for another user it would access the booking | Defensive programming to make sure that only bookings made by the user would be visible |
| Double bookings | Adjusted code to check that the date, time and table were unique together and to give an error to indicate to the user that the booking was unavailable for that date, time and table combination |
| Food item description not showing on menu | A "p" element was used to encase the jinja code, once removed the food item description was then visible |
| Foods not listing by type, starters, manins and desserts | I needed to fix the database loop for the food items to specify the food type had to be a starter to display in the starter section of the menu, and the same for mains and desserts |
| Drinks not listing by type, wines, beers and cocktails | I needed to fix the database loop for the drinks item to specify the drink type had to be a wine to display in the wine section of the menu, and the same for beers and cocktails |
| Card links not working on home page for book a table, food menu and drinks menu | The links were not set within urls.py so just needed to be wired up to load each relevant page |
| Booking form accepting phone number that are too short | I used Django PhoneNumberField to ensure only valid phone formats were accepted |



## <span id="credits"></span>Credits
* Martina Terlevic: Code Institute Mentor and center of sanity.
* OpenAI for the cheesy content of my fake blog posts.
* Code Institute's walkthrough Django project, called [_I think therefore I blog_](https://github.com/Code-Institute-Solutions/Django3blog/tree/master), for basic repository set up and starter Django project code.
* Clueless Biker's github project ["print(STATEMENTS)"](https://github.com/CluelessBiker/project4-print-statements) for the README.md inspiration.
* ErikHgm's github project ["FireHouse Restaurant"](https://github.com/ErikHgm/FireHouse-Restaurant-Project) for README.md inspiration.
* Code Institute's tutors, and fellow students on Slack for degugging
* [Stack Overflow](https://try.stackoverflow.co/explore-teams?utm_source=adwords&utm_medium=ppc&utm_campaign=kb_teams_search_brand_emea-dach&_bt=657236278306&_bk=stack+overflow&_bm=p&_bn=g&gclid=Cj0KCQjwgNanBhDUARIsAAeIcAt8RyvjI8QiLAj3kyl-W8hBXwtXekioNxfa6XQ9uT2fIyg7jq52MJMaAqKQEALw_wcB) for coding solutions when I was terribly stuck.

## <span id="media"></span>Media

* [_Pexels_](https://www.pexels.com/)
    - Photos by: 
      - Alex Azabache
      - Cottonbro Studio
      - Adrian Vieriu
      - James Wheeler
      - Krampus Production
      - Ketut Subiyanto
      - Matt Barnard

*  [_Cloudinary_](https://cloudinary.com/) photo hosting platform

## <span id="team"></span>Team Members

| Name                | LinkedIn                                                                                    | GitHub                                                                                    |
|---------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Krystal Juvrud | [<img src="https://skillicons.dev/icons?i=linkedin" height="20px" alt="LinkedIn" />](https://www.linkedin.com/in/krystal-juvrud/)             | [<img src="https://skillicons.dev/icons?i=github" height="20px" alt="GitHub" />](https://github.com/KrystalCoding)               |
