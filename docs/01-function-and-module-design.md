# Function and Module Design

## 0.1 FrontPage

### 0.1.1 Index Page

- header : logo + login/register | image/name
- nav : All Topics + Search + Filter? + New Topic
- main : topics + pagination
- footer : ??

- This page is accessed to users unlogged

### 0.1.2 Detail Page

- main : subject + content + replies
- user who has not login cannot reply
- This page is unaccessed to users unlogged

### 0.1.3 Form Page

## 1.1 Topic and Post Module

### DP101 Create a topic

- login required

### DP102 Delete a topic

- login required
- user can only delete topic that was created by themselves
- once topic is deleted, the replies about it will be deleted

### DP103 Update a topic

- login required
- user can only update topic that was created by themselves

### DP104 Search topics

- pagination
- search topic subject according to the input words

## 1.2 User Module

### DP201 Register a user

### DP202 Login a user

### DP003 Logout a user