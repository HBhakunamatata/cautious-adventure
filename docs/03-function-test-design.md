# Function and Module Design

## 0.1 FrontPage

### 0.1.1 Index Page

- header : logo + login/register | image/name
    - logo: link to index page
    - logged user: image/name
    - unlogged user: login/register
- nav : All Topics + Search + Filter? + New Topic
    - new topic : unlogged--login form / logged--new form
- main : topics + pagination
- footer : ??

- This page is accessed to users unlogged  

  
#### Test

- logged:  login --> index   logout --> index  view_topics  click topic --> details
- unlogged: logout --> index

### 0.1.2 Detail Page

- main : subject + content + replies
- user who has not login cannot reply
- This page is unaccessed to users unlogged

#### Test

- unlogged: reply --> login form
- logged: reply --> reply form

### 0.1.3 Form Page

- Login Form
    - have not register
- Register Form
    - redirect to login form
- New Topic Form
    - after: redirect to index

### 0.1.4 Profile Page

- Posts
- Profile Info
- delete post action
- update post action

### 0.1.5 Confirm Page

- confirm message
- button bind action

## 1.1 Topic and Post Module

### DP101 Create a topic

- login required
- success: redirect to index page

#### Test

- unlogged --> login form

### DP102 Delete a topic

- login required
- user can only delete topic that was created by themselves
- once topic is deleted, the replies about it will be deleted
- redirect to index page

#### Test

- unlogged --> login form
- other post --> message about cannot delete

### DP103 Update a topic

- login required
- user can only update topic that was created by themselves
- redirect to index page

#### Test

- unlogged --> login form
- other post --> message about cannot update

### DP104 Search topics

- pagination
- search topic subject according to the input words

## 1.2 User Module

### DP201 Register a user

- Only unlogged user can be access to it
- Avoid the same username is used
- Make a signal to create a user when register a profile
    - When delete a user, the profile will be deleted
    - When prifile is deleted, the user will be deleted
    - Avoid the signal looping
- redirect to login form

#### Test

- The same username registered
- User create
- Profile create

### DP202 Login a user

- Only unlogged user can be access to it
- authenticate the username and password
- login the user
- redirect to the profile page

#### Test

- wrong username and password
- check rookie and session

### DP003 Logout a user

- Only logged user can be access to it
- change the state of user in backend and frontend
- redirect to index page

#### Test

- check the rookie and seesion
- check the state of user in backend and frontend