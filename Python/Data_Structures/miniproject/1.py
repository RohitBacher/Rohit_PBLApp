dict_ = {
    'Jeff': 'Is afraid of Dogs.',
    'David': 'Plays the piano.',
    'Jason': 'Can fly anairplane.'
}

for i in dict_ :
    print(i, ":", dict_[i])
print("Next Output")

dict_['Jeff'] = 'Is afraid of heights.'
dict_['Jill'] =  'Can hula dance.'

for i in dict_ :
    print(i, ":", dict_[i])
