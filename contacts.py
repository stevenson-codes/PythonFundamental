contacts = {
    'number': 4,
    'students':
        [
            {'name':'Stevenson Yan', 'email':'stevenson@example.com'},
            {'name':'Linda Han', 'email':'linda@example.com'},
            {'name':'Tony Yan', 'email':'tony@exmaple.com'}
        ]
}

print('Student emails:')
for students in contacts['students']:
    print(students['email'])