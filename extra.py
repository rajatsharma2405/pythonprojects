spy = {
    'name' : 'Rajat',
    'salutation' : 'Dr',
    'age' : 19,
    'rating' : 4.7,
    'is_online' : True
}

STATUS_MESSAGES = ["unAvailable" , "ready to chat", "go on", "driving"]

friends = [
    {
        'name' : 'tarun',
        'salutation' : 'mr',
        'age' : 39,
        'rating' : 5.9,
        'chats'  : []

    },

    {
        'name' : 'charu',
        'salutation' : 'ms',
        'age' : 39,
        'rating' : 5.9,
        'chats'  : []


    }
]
print "Hello!! Let's get started."
#This will simply print a message "Hello!! Let's get started."

question = "Do you want to continue as " +spy['salutation'] +" " +spy['name'] +".(Y/N)"
existing = raw_input(question)