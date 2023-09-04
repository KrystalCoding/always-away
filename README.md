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
- [_Agile Methodology_](#agile)
- [_User Stories_](#user-stories)
  - [_Users_](#users)
  - [_Admin_](#admin)
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

### <span id="agile"></span>Agile Methodology:
The principles of agile methodology were implemented during the project. By assigning user stories to issues and utilizing the GitHub Kanban board, the necessary project goals could be easliy prioritized. Labels were used to fine tune the priority of each user story.

## <span id="user-stories"></span>User Stories
### <span id="users"></span>Users:
- I can **register an account** so that **I can comment and like**
- I can **log in to my account and see my messages** so that **keep track of conversations with admin**
- I can **view a paginated list of pages** so that **I can easily select a page to view**
- I can **view a list of posts** so that **I can select one to read**
- I can **click on a post** so that **I can read the full text**

- I can **leave comments on a post** so that **I can be involved in the conversation**
- I can **view comments on an individual post** so that **I can read the conversation**
- I can **edit my comments** so that **I can more deeply interact with the community**
- I can **delete my own comments** so that **change my mind about a comment**

- I can **like or unlike a post** so that **I can interact with the content**
- I can **view the number of likes on each post** so that **I can see which is the most popular or viral**

- I can **create a draft message and save without sending** so that **I can take my time formulating a message over more than one site visit/login**
- I can **send a message to the admin** so that **I can interact with the creator of the blog**
- I can **delete messages** so that **I can clean out my inbox**

- I can **access the README.md file** so that **I can thoroughly read the appropriate documentation**

*Disclaimer: The following User stories have not yet been implemented. They have been left on the project for the purpose of organizing future goals and projects to expand and enhance the blog site.

- I can **make a blog post**
- I can **utilize a search capability** so that **I can easily locate specific topics or posts**
- I can **organize messages by category** so that **I can quickly search for a message I want to find**
- I can **upvote on comments** so that **earn Karma points, eventually rewarding me with badges or digital trophies**
- I can **mark a message as read** so that **my account can keep track for me if I have read a message or not**
- I can **use a reply function on messages** so that **I can continue a string of messages with admin**

### <span id="admin"></span>Admin:
- I can **view comments on an individual post** so that **I can read the conversation**
- I can **leave comments on a post** so that **I can be involved in the conversation**
- I can **approve or disapprove comments** so that **I can filter out objectionable comments**

- I can **delete messages** so that **I can clean out my inbox**
- I can **view the number of likes on each post** so that **I can see which is the most popular or viral**

- I can **create draft posts** so that **I can finish writing the content later**
- I can **create, read, update, and delete posts** so that **I can manage my blog content**

*Disclaimer: The following User stories have not yet been implemented. They have been left on the project for the purpose of organizing future goals and projects to expand and enhance the blog site.

- I can **utilize a search capability** so that **I can easily locate specific topics or posts**
- I can **categorize posts into sub-threads** so that **keep multiple posts organized**
- I can **send message to Users from admin panel** so that **I can more personally interact with site Users**
- I can **receive notifications** so that **I can see when someone likes or comments on my post**

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


| Validator  |  Pass  |  Fail  |
| :---  |    :----:   | :----: |
| HTML  |  &check;  |  0  |
| W3 CSS  |  &check;  |  0  |
| JavaScript  |   &check;   |  0  |
| Lighthouse  |  &check;  |  &check;  |
| Grammarly  |  &check;  |  0  |


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
