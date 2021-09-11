import re

def process_message(message, response_array, response):
   
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

 
    # print(score, response)
    return [score, response]

def get_response(message):
   
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there!'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        process_message(message, ['your', 'name'], 'My name is Maggi, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you!'),
        process_message(message, ['what','is','your', 'age'], 'I am 20 decades old '),
        process_message(message, ['any', 'hobbies'], 'chatting with you '),
        process_message(message, ['can', 'i' ,'help' ,'others'], 'make tea for others:) ')
     
    ]
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])
        
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

