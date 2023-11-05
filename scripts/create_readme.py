with open('markdowns/TABLE_OF_CONTENT.md', 'r') as file:
    table_of_content = file.read()

with open('markdowns/INTRODUCTION.md', 'r') as file:
    introduction = file.read()

with open('markdowns/VIDEOS.md', 'r') as file:
    videos = file.read()

with open('markdowns/BLOGS.md', 'r') as file:
    blogs = file.read()

with open('markdowns/BUILD.md', 'r') as file:
    build = file.read()

with open('markdowns/DAO.md', 'r') as file:
    dao = file.read()

with open('markdowns/CONTRIBUTION.md', 'r') as file:
    contribution = file.read()

with open('markdowns/SOCIAL.md', 'r') as file:
    social = file.read()

with open('README.md', 'w') as file:
    file.write(table_of_content + '\n\n')
    file.write(introduction + '\n\n')
    file.write(videos + '\n\n')
    file.write(blogs + '\n\n')
    file.write(build + '\n\n')
    file.write(dao + '\n\n')
    file.write(contribution + '\n\n')
    file.write(social)