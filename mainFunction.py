from userClasses import *
from blogContentClasses import * 

def main():
    username, password, email = createAccount()
    member = login(username, password, email) 
    post = writeBlogPost()
    editBlogPost(post)
    viewBlogPost(post)
    comment = writeComment(member)
    print("\n")
    viewPostComment(post, comment)
    comment = deleteComment(comment)
    deleteBlogPost(post)
    logout(member)

def createAccount():
    user = User()
    username, password, email = user.createAccount()
    print("You have successfully created an account. Please login to continue.\n")
    return username, password, email 
    
def login(username, password, email):
    member = Member(username, password, email)
    member.verifyLogin()
    return member 
    
def writeBlogPost():
    blogger = memBlogger()
    post = blogger.createBlogPost()
    post.addToDict()
    return post

def editBlogPost(post):
    post.editBlogPost()
    
def viewBlogPost(post):
    post.viewBlog()
    
def writeComment(member):
    comment = member.createComment()
    return comment

def viewPostComment(post, comment):
    post.viewBlog()
    print("\nComments:\n")
    comment.viewComment()
    
def deleteComment(comment):
    comment.deleteComment()
    return comment
    
def deleteBlogPost(post):
    post.deleteBlogPost()
    
def logout(member):
    member.logout()
    
    
main()
