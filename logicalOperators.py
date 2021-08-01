likes_walks = True
is_barking = False
likes_treats = True

if likes_walks and is_barking:
    print("must be a dog")

if likes_walks or likes_treats:
    print("needs attention")

if likes_walks and not is_barking:
    print('ready for a walk')