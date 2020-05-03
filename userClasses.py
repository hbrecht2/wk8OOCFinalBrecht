from blogContentClasses import *

class Admin:
    def deleteBlogPost(self):
        BlogPost('title', 'content').deleteBlogPost()
    
    def deleteComment(self):
        Comment().deleteComment()
    
    def deleteAccount(self):
        userDelete = input("What is the username of the account you want to delete?") 
        User.deleteAccount(userDelete)
    
    
class User:
    def __init__(self, username = None, password = None, email = None, users = {}):
        self.username = username
        self.password = password
        self.email = email
        self.users = users
        
    def createAccount(self):
        self.username = input("Enter a username: ")
        if self.username in self.users.keys():
            print ("That username is already taken. Please choose a different one.")
            self.createAccount()
        else:
            self.password = input("Enter a password: ")
            self.users.update({self.username : self.password})
            self.email = input("Enter a good email to reach you at if needed: ")
            return self.username, self.password, self.email
            
    def returnInfo(self):
        return self.username, self.password, self.email 
            
    def deleteAccount(self, username):
        print(self.users)
        self.users.pop(username)
        print(self.users)
    
class Member(User):
    def __init__(self, username, password, email, loginStatus=False):
        self.loginStatus = loginStatus
        User.__init__(self, username, password, email)
        
    def getUsername(self):
        username = input ('Enter username:')
        return username
    
    def getPassword(self):
        password = input ('Enter password:')
        return password
    
    def verifyLogin(self): 
        username = self.getUsername()
        password = self.getPassword()
        if password == self.password:
            self.loginStatus = True 
            print ("You have successfully logged in.\n")
            
        else:
            print ("Password incorrect. Please try again.\n")
            self.verifyLogin()
            
    def logout(self):
        #change whatever at logged in back to logged out
        self.loginStatus = False
        print("You have successfully logged out.")
    
    def createComment(self):
        commentContent = input("Enter comment here..")
        comment = Comment(commentContent)
        return comment
    
    def editComment(self):
        comment.editComment()
        
    def deleteComment(self):
        comment.deleteComment

class memGuest(Member):
    def __init__ (self, memberType="guest"):
        self.memberType = memberType
        
class memBlogger(Member):
    def __init__ (self, memberType="blogger"):
        self.memberType = memberType
        
    def createBlogPost(self):
        postTitle = input("What is the tile of your blog post?")
        postContent = input("Please enter the content of your blog post..")
        
        post = BlogPost(postTitle, postContent)
        return post
    
    def editBlogPost(self):
        post.editBlogPost()
    
    def deleteBlogPost(self):
        post.deleteBlogPost()
    