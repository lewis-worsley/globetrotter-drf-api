# Testing

Any bugs identified are listed below.

Full details of manual testing can be found on this page.

<br>

## Bugs

During the course of writing the code for the back-end of the Globetrotters application, these are the following bugs I discovered.

<br>

### Bug fixes
<Hr>
​
The following bugs were identified during user testing:

- Bug 🐞 - Database became corrupted and would no longer accept new changes to models, therefore failing to migrate
- Cause ⚒️ - Removing a 'unique_together' field on one of the models
- Resolution ✅ - Code Institute advised I delete all migration files other than the init.py file

<br>

- Bug 🐞 - Not deploying on Heroku
- Cause ⚒️ - Procfile not set up correctly regarding 'web' and 'ALLOWED_HOSTS' not added to Heroku config vars correctly
- Resolution ✅ - Procfile amended to the correct variable and 'ALLOWED_HOSTS' added to Heroku Config Vars. The project was deployed afterwards 

<br>

- Bug 🐞 - Couldn't view the API data in the admin panel
- Cause ⚒️ - Connected to the local database in my workspace
- Resolution ✅ - Commented out DEV mode so I could access the API data in the admin panel

<br>

### Unfixed bugs or issues
<hr>

- is_admin field on profile:
    - This boofield (default set to 'False'), whilst acknowledged in the admin panel, does not set a profile to 'True' on the front-end despite the boolean field being ticked to 'True' in the admin panel. Does NOT effect the function of the website.

<br>

## Manual testing

To ensure the application is working as expected, I performed some manual tests.

Followers do not appear in the admin panel as users are in control who they do and don't follow.

Likes do not appear in the admin panel as users are in control in regards to which posts they do and don't like

<br>

### Site admin
<hr>

- User story 📖: Post new news articles from the admin panel to display on the frontend to the visitor
- Test 🧪: Used the admin panel to create a new news article
- Result 🏆: Upon inputting valid data into the form, the news article appeared at the top of the most recent results on each respective news component (excluding unique news page) on the website
- Verdict ✅: Test passed

<br>

- User story 📖: Can add, update and remove profiles
- Test 🧪: Used the admin panel to add, edit and remove test profiles
- Result 🏆: Upon pressing delete, the subsequent profile was deleted
- Verdict ✅: Test passed

<br>

- User story 📖: Can update and remove journey and blog posts if content is found to be inappropriate 
- Test 🧪: Used the admin panel to update and delete content
- Result 🏆: Upon pressing save, the post was updated; on delete, the post was deleted
- Verdict ✅: Test passed

<br>

- User story 📖: Can remove comments from journeys and blogs if content is found to be inappropriate 
- Test 🧪: Used the admin panel to remove comments
- Result 🏆: Upon pressing delete, the comment was removed from both respective components
- Verdict ✅: Test passed

<br>

### Authorised user
<hr>

- User story 📖: Be able to sign in to my account
- Test 🧪: When signed out, I navigated to the navbar, as well as used links and buttons that are present across the site that push vistors to the sign in page, and filled the form to sign in
- Result 🏆: Entered my details and clicked the submit button to be redirected to the  home page. In subsequent visits, the form auto-filled the sign in fields which as a user made my life easier
- Verdict ✅: Test passed

<br>

- User story 📖: Follow or unfollow another account
- Test 🧪: Navigated to a profile page account and pressed follow and unfollow
- Result 🏆: The function captured the click which increased and decreased followers and following count 
- Verdict ✅: Test passed

<br>

- User story 📖: Like or unlike another post
- Test 🧪: Navigated to a unique post which I didn't own and liked and unliked a post
- Result 🏆: The like count increased and decreased
- Verdict ✅: Test passed

<br>

- User story 📖: Can't like my own post
- Test 🧪: Navigated to a unique post that I own and clicked the like icon
- Result 🏆: The like ignored the my request as I own the post. A Tooltip message is flagged to the user informing them it's not possible to like one's own post
- Verdict ✅: Test passed

<br>

- User story 📖: Comment on one's own post, as well as others
- Test 🧪: Navigated to my own post as well as another user's and submitted a comment
- Result 🏆: The comment appeared in both cases
- Verdict ✅: Test passed

<br>

- User story 📖: View a list of journeys, blogs and news
- Test 🧪: Added test posts for each component and navigated to list view URL to check they are displayed
- Result 🏆: Instances were displayed as intended
- Verdict ✅: Test passed

<br>