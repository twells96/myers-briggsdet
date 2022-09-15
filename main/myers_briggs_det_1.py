import math

def word_counter(word_to_check, words_list):
    word2count = {}
    for word in words_list:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
    res = [word2count[key] for key in [word_to_check]]
    return res

def i_bag_of_words(words):
    vector = []
    list_of_squared_values = []
    temp_bag = ['actually', 'way', 'feeling', 'dream', 'found', 'everything', 'problem', 'language', 'always', 'two', 'day', 'need', 'already', 'one', 'still', 'beautiful', 'fe', 'many', 'look', 'reading', 'ever', 'around', 'keep', 'never', 'feel', 'think', 'different', 'person', 'type', 'though', 'good', 'thread', 'help', 'kind', 'see', 'say', 'try', 'sure', 'seem', 'someone', 'example', 'probably', 'like', 'yes', 'maybe', 'usually', 'little', 'find', 'alone', 'even', 'want', 'relate', 'believe', 'take', 'made', 'time', 'family', 'really', 'ni', 'live', 'come', 'happy', 'go', 'show', 'make', 'function', 'much', 'without', 'well', 'enough', 'used', 'music', 'mean', 'year', 'back', 'test', 'love', 'people' 'rant', 'going', 'friend', 'seems', 'lot', 'best', 'yet', 'others']
    amateur_match = set(words) & set(temp_bag)
    for i in amateur_match:
        word_count = word_counter(i, words)
        vector.append(word_count)
    for i in vector:
        a = i[0]*i[0]
        list_of_squared_values.append(a)
        sum_of_squared_values = sum(list_of_squared_values)
    if amateur_match.__len__() == 0:
        magnitude = 0
    else:
        magnitude = math.sqrt(sum_of_squared_values)
    print(magnitude)
    return magnitude

def e_bag_of_words(words):
    vector = []
    list_of_squared_values = []
    temp_bag = ['idea', 'mean', 'pretty', 'actually', 'always', 'person', 'question', 'love', 'ne', 'need', 'people', 'entp', 'rather', 'fucking', 'go', 'good', 'friends', 'best', 'say', 'never', 'agree', 'know', 'interesting', 'see', 'word', 'little', 'im', 'wrong', 'done', 'well', 'win', 'thing', 'nt', 'really', 'tell', 'big', 'way', 'guy', 'take', 'want', 'feel', 'te', 'life', 'talk', 'fun', 'much', 'often', 'yeah', 'like', 'maybe', 'experience', 'entj', 'work', 'said', 'read', 'find', 'stupid', 'new', 'look', 'every', 'start', 'think', 'quite', 'lot', 'show', 'reason', 'year', 'still', 'shit', 'thought', 'time', 'fi', 'intelligence', 'lol', 'come', 'yes', 'many', 'first', 'usually', 'kill', 'usually', 'sex', 'problem', 'test', 'woman', 'thread', 'talking', 'make', 'anything', 'happy', 'even', 'thinking', 'smart', 'sense', 'one', 'street', 'going', 'friend']
    amateur_match = set(words) & set(temp_bag)
    for i in amateur_match:
        word_count = word_counter(i, words)
        vector.append(word_count)
    for i in vector:
        a = i[0] * i[0]
        list_of_squared_values.append(a)
        sum_of_squared_values = sum(list_of_squared_values)
    if amateur_match.__len__() == 0:
        magnitude = 0
    else:
        magnitude = math.sqrt(sum_of_squared_values)
    print(magnitude)
    return magnitude

def myers_briggs_generation(post):
    myers_briggs_type = []
    introverted = i_bag_of_words(post.split())
    extroverted = e_bag_of_words(post.split())
    if introverted > extroverted:
        myers_briggs_type.append("I")
        print ("Post made by an Introvert")
    if extroverted > introverted:
        myers_briggs_type.append("E")
        print ("Post made by an Extrovert")
    if introverted == extroverted:
        # do something to decide between the two maybe later
        print ("First fourth could not be determined")

myers_briggs_generation('')
