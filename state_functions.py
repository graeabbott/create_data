import random

def compose(cur_t):
    if cur_t <=5:
        return 'compose', cur_t+1
    elif cur_t > 15:
        return 'browse', 0
    else:
        r = random.randint(1,10)
        # p_browse = 0.5, p_compose = 0.5
        if(r <=5):
            cur_t += 1
            return 'compose', cur_t
        else:
            return 'browse', 0

def browse(cur_t, not_browsed, time, user, last, browse_file):
    if cur_t%2 == 0:
        # browse new composition every 2 seconds
        end = len(not_browsed) - 1 
        if end == 0:
            #already browsed through everybody
            return last, 'compose', 0
        r = random.randint(0,end)
        browse_file.write(str(user) + ' ' + str(not_browsed[r]) + ' ' + str(time) + '\n')
        last = not_browsed[r]
        not_browsed.remove(last)
    else:
        browse_file.write(str(user) + ' ' + str(last) + ' ' + str(time) + '\n')
    #min time to browse is 5 sec
    if cur_t <= 5:
        return last,'browse', cur_t+1
    elif cur_t > 20:
        # past max browsing time, must go to mingle or compose
        r = random.randint(1,10)
        if r <= 9:
            return last, 'mingle', 0
        else:
            return last, 'compose', 0
    else:
        r = random.randint(1,10)
        if r <=3:
            return last, 'mingle', 0
        elif r == 10:
            return last, 'compose', 0
        else:
            return last, 'browse', cur_t+1

def mingle(cur_t, user, last_browsed, time, liked, like_file, mingle_file):
    p_like = 1 + (cur_t - 5) #increases the likelihood of liking depending on length of mingle
    r = random.randint(1,20)
    if r <= p_like:
        if last_browsed not in liked:
            liked.add(last_browsed)
            like_file.write(str(user) + ' ' + str(last_browsed) + ' ' + str(time) + '\n')
    mingle_file.write(str(user) + ' ' + str(last_browsed) + ' ' + str(time) + '\n')
    if cur_t <= 5:
        return 'mingle', cur_t+1
    elif cur_t > 20:
        return 'browse', 0
    else:
        r = random.randint(1,10)
        if r <=6:
            return 'mingle', cur_t+1
        else:
            return 'browse', 0