from twython import TwythonStreamer

C_K = "************************************"
C_S = "************************************************"
A_T = "****************************************************"
A_S = "****************************************"

tweetcount = 0
def increment():
    global tweetcount
    tweetcount = tweetcount+1

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        text = 'text'
        for text in data:
            increment()
            print(tweetcount)
            break
        if tweetcount == 3:
            print("Ian G. Harris is popular!")
            
stream = MyStreamer(C_K, C_S, A_T, A_S)
stream.statuses.filter(track="Ian G. Harris")
