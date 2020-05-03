class BlogPost:
    def __init__(self, title, content, blogDict = {}):
        self.title = title
        self.content = content
        self.blogDict = blogDict
        
    def addToDict(self):
        stripTitle = self.title.lower().strip()
        self.blogDict[stripTitle] = self.content
        
    def __repr__(self):
        return "{0}    \n\n\n{1}".format(self.title, self.content)
    
    def getBlog(self):
        getTitle = input("What is the title of the blog post?")
        key = getTitle.lower().strip()
        blogContent = self.blogDict.get(key)
        return key, blogContent
        
    def viewBlog(self):
        print(self)
        
    def editBlogPost(self):
        print (self.content)
        editedPost = input("This is the current blog post content, please rewrite post as you want it edited.\nEdits:")
        self.content = editedPost
        print(self.content)
        confirm = input("Would you like to make any more changes? Enter 'Y' for yes.")
        confirm.strip()
        if confirm == "Y":
            self.editBlogPost()
        else:
            print("Thank you for the changes!\n\n\n")
    
    def deleteBlogPost(self):
        key, blogContent = self.getBlog()
        if key in self.blogDict.keys():
            confirm = input("Are you sure you want to delete '{}'? Respond with 'Y' to continue.".format(key))
            confirm.strip()
            if confirm == "Y": 
                self.blogDict.pop(key)
                self.title = None
                self.content = None
                print("You have successfully deleted the post.")
            else:
                self.deleteBlogPost()
        else:
            print("This is not a valid post title. Please try again.")
            self.deleteBlogPost()

class Comment:
    def __init__(self, commentContent):
        self.commentContent = commentContent
        
    def __repr__(self):
        return "{0}".format(self.commentContent)
        
    def viewComment(self):
        print(self)
    
    def editComment(self):
        print (self.commentContent)
        editedComment = input ("This is the current comment, please rewrite the comment as you want it edited.")
        self.commentContent = editedComment 
    
    def deleteComment(self):
        self.commentContent = None 

