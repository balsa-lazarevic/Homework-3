# 1. zadatak

#Storage of all articles
articles = []

def validateTitle(title):
    if(len(title) > 50):
        print('The title is too long, max input is 50 characters')
        return False
    if(title.replace(' ','').isalnum() == False):
        print('The title must contain only alphanumeric characters')
        return False
    
    for article in articles:
        if(title == article.getTitle()):
            return False

    return True

def validateAuthor(author):
    if(len(author) > 100):
        print('The author is too long, max input is 100 characters')
        return False
    if(author.replace(' ','').isalpha() == False):
        print('The author must contain only alphanumeric characters')
        return False
    if ' ' not in author:
        print('You must provide both first name and last name for the author')
        return False

    return True

def validateDescription(description):
    if(len(description) > 300):
        print('The description is too long, max input is 300 characters')
        return False
    return True

def validateCategory(category):
    if(len(category) > 20):
        print('The category is too long, max input is 20 characters')
        return False
    return True

def validateCommentTitle(title):
    if(len(title) > 50):
        print('The comment title is too long, max input is 50 characters')
        return False
    return True

def validateCommentAuthor(author):
    if(len(author) > 50):
        print('The comment author is too long, max input is 50 characters')
        return False
    return True

def validateCommentDescription(description):
    if(len(description) > 120):
        print('The comment description is too long, max input is 120 characters')
        return False
    return True

class Article:
    def __init__(self, title, author, description, category, views = 0, comments = []):
        if(validateTitle(title) == False):
            return False
        if(validateAuthor(author) == False):
            return False
        if(validateDescription(description) == False):
            return False
        if(validateCategory(category) == False):
            return False

        self.__title = title
        self.__author = author
        self.__description = description
        self.__category = category
        self.__views = views

        validatedComments = []
        if(comments != []):
            for comment in comments:
                if(validateCommentTitle(comment[0]) == False):
                    continue
                if(validateCommentAuthor(comment[1]) == False):
                    continue
                if(validateCommentDescription(comment[2]) == False):
                    continue

                validatedComments.append(comment)

        self.__comments = validatedComments

    def __str__(self):
        return f'Title: {self.__title}, Autor: {self.__author}, Opis: {self.__description}, Kategorija: {self.__category}, Pregledi: {self.__views}, Broj komentara: {len(self.__comments)}'

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        if(validateTitle(title) == False):
            print('Title not set')
            return False
        self.__title = title

    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        if(validateAuthor(author) == False):
            print('Author not set')
            return False
        self.__author = author
        print('Author updated')

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        if(validateDescription(description) == False):
            print('Description not set')
            return False
        self.__author = author
        print('Author updated')

    def getCategory(self):
        return self.__category

    def setCategory(self, category):
        print('set')

    def getViews(self):
        return self.__views
    
    def setViews(self, views):
        print('set')

    def incViews(self, increment = 1):
        self.__views = self.__views + increment

    def getComments(self):
        return self.__comments

    def getCommentsNum(self):
        return len(self.__comments)

    def get_comments_by_title(self, title):
        return_comment = []
        for comment in self.__comments:
            if(title == comment[0]):
                return_comment.append(comment)
        return return_comment
    
    def delete_comment_by_title(self, title):
        new_comments = []
        for comment in self.__comments:
            if(title != comment[0]):
                new_comments.append(comment)
        self.__comments = new_comments
        print('Comment deleted')

    def get_comments_by_author(self, author):
        return_comments = []
        for comment in self.__comments:
            if(author == comment[1]):
                return_comments.append(comment)
        return return_comments

    def delete_comment_by_author(self, author):
        new_comments = []
        for comment in self.__comments:
            if(author != comment[1]):
                new_comments.append(comment)
        self.__comments = new_comments
        print('Comment deleted')

    def insert_new_comment(self, title, description, author = 'anonim'):
        new_comments = []
        for comment in self.__comments:
            new_comments.append(comment)
            if(title == comment[0]):
                print('Comment has already been added')
                return False

        new_comments. append((title, author, description))
        self.__comments = new_comments
        print('Comment Added')

# 2. i 3. zadatak
class TechArticle(Article):
    def __init__(self, title, author, description, creation_date, lang, views = 0, comments = []):
        super().__init__(title, author, description, 'tech', views, comments)
        self.__creation_date = validateCreationDate(creation_date)
        self.__lang = lang

    def get_comments_by_term(self, term):
        return_comments = []
        for comment in self.getComments():
            if(comment[0].find(term) == 0):
                return_comments.append(comment)
        return return_comments

    def __str__(self):
        return f'Title: {self.getTitle()}, Autor: {self.getAuthor()}, Opis: {self.getDescription()}, Kategorija: {self.getCategory()}, Pregledi: {self.getViews()}, Broj komentara: {self.getCommentsNum()}, Datum kreiranja: {self.__creation_date}, Jezik: {self.__lang}'

def validateCreationDate(creation_date):
    currentInput = creation_date.split('/')
    returnDate = ''
    if(len(currentInput[0]) == 1):
        currentInput[0] = '0' + currentInput[0]
    if(len(currentInput[1]) == 1):
        currentInput[1] = '0' + currentInput[1]
    if(len(currentInput[2]) == 1):
        currentInput[2] = '0' + currentInput[2]
    
    returnDate = currentInput[0] + '/' + currentInput[1] + '/' + currentInput[2]
    return returnDate
    
def create_article():
    current_articles = len(articles)
    print('Welcome to BBC Article Creation System')
    print('Currently you have', current_articles, ' articles')
    print('We are now going to create a new article\n')
    title = ''
    author = ''
    description = ''
    category = ''
    views = ''

    while(title == ''):
        newTitle = input('Please provide a title: ')
        if(validateTitle(newTitle)):
            title = newTitle

    while(author == ''):
        newAuthor = input('Please provide an author: ')
        if(validateAuthor(newAuthor)):
            author = newAuthor

    while(description == ''):
        newDescription = input('Please provide a description: ')
        if(validateDescription(newDescription)):
            description = newDescription

    while(category == ''):
        newCategory = input('Please provide a category: ')
        if(validateCategory(newCategory)):
            category = newCategory

    while(views == ''):
        newViews = input('Please provide number of views: ')
        views = int(newViews)

    article = Article(title, author, description, category, views)
    articles.append(article)

def create_tech_article():
    current_articles = len(articles)
    print('Welcome to BBC Article Creation System')
    print('Currently you have', current_articles, ' articles')
    print('We are now going to create a new Tech article\n')
    title = ''
    author = ''
    description = ''
    creation_date = ''
    lang = ''
    views = ''

    while(title == ''):
        newTitle = input('Please provide a title: ')
        if(validateTitle(newTitle)):
            title = newTitle

    while(author == ''):
        newAuthor = input('Please provide an author: ')
        if(validateAuthor(newAuthor)):
            author = newAuthor

    while(description == ''):
        newDescription = input('Please provide a description: ')
        if(validateDescription(newDescription)):
            description = newDescription
    
    while(creation_date == ''):
        newCreationDate = input('Please provide a date in the form of d/m/y: ')
        if(validateCreationDate(newCreationDate)):
            creation_date = newCreationDate

    while(lang == ''):
        newLang = input('Please provide article language (example: en, fr, es): ')
        lang = newLang

    while(views == ''):
        newViews = input('Please provide number of views: ')
        views = int(newViews)

    article = TechArticle(title, author, description, creation_date, lang, views)
    articles.append(article)

def show_all_articles():
    for article in articles:
        print(article)

def filter_by_category(category):
    return_articles = []
    for article in articles:
        if article.getCategory == category:
            return_articles.append(article)
    return return_articles

'''
Kreirati 4 Article i 2 Tech Article
'''
for x in range(0,4):
    create_article()

if()
for x in range(0,2):
    create_tech_article()

create_tech_article()
create_tech_article()
print('-----')
print(filter_by_category('tech'))
print('-----')
