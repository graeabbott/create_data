# Driver program to create sample data 
from state_functions import compose, browse, mingle


def main():
    sqn_file = open('sequence.txt', 'a') # file to write cmb sequence to
    browse_file = open('browse.txt', 'a') # file to write browsing interactions to
    like_file = open('like.txt', 'a') # file to write like interactions to
    mingle_file = open('mingle.txt', 'a') # file to write mingle interactions to
    #modified_file = open('modify.txt', 'a') # file to write modified interactions to

    #loop to generate data for 100 users
    for i in range(0,100):
        cur_t = 0 # amount of time that has been spent in current state
        cur_state = "compose" # current state, everyone starts in compose
        liked = set() # set holding ppl whose compositions you have liked
        not_browsed = [] # list of ids for people the current user hasn't browsed
        last_browsed = ''
        for x in range(0,100):
            not_browsed.append(x)
        not_browsed.remove(i)
        # loop used to generate 600 seconds of data, each user is uniquely identified by i
        for j in range(0,600):
            if cur_state == "compose":
                cur_state, cur_t = compose(cur_t)
            elif cur_state == "browse":
                last_browsed, cur_state, cur_t = browse(cur_t, not_browsed, j, i, last_browsed, browse_file)
            else:
                cur_state, cur_t = mingle(cur_t, i, last_browsed, j, liked, like_file, mingle_file)
            sqn_file.write(cur_state[0])
            if j < 599:
                sqn_file.write(',')
        sqn_file.write('\n')

if __name__ == '__main__':
    main()
