import time
start = time.time()

def swap(p1,p2):
    temp = p1
    p1 = p2
    p2 = temp
    return p1,p2



batsmen = [1,1,1,0,0,0,0,0,0,0,0,0,0]

score = 0
balls = 0
playerno1 = 1
playerno2 = 2
wickets = 0
scores = {1:0}
n = int(input())
l = list(map(str,input().split(',')))
k = int(input())
for i in range(len(l)):
    if(l[i] in ['Nb','Wd']):
        score+=1
        #scores[playerno1] += int(l[i])
       # print(score,l[i])
    
    elif(l[i] in ['1','2','3','4','6','W','0']):
        balls += 1
        
        if( l[i] in ['1','2','3','4','6','0']):
            score += int(l[i])
            #print(score,l[i],'a')
            if(playerno1 in scores):
                scores[playerno1] += int(l[i])
            else:
                scores[playerno1] = int(l[i])
                
            if(l[i] in ['1','3']):
                playerno1 , playerno2 = swap(playerno1,playerno2)
                batsmen[playerno1] = 1
                batsmen[playerno2] =1

        elif(l[i]== 'W'):
            if(i==0):
                wickets += 1
                #scores[playerno1] = score
                playerno1 = max(playerno1,playerno2)+1
                batsmen[playerno1] = 1
                
               
            else:
                j = i-1
                flag = 0
                while(l[j] == 'Nb' or l[j] == 'Wd'):
                   if(l[j] == 'Nb'):
                       #print(j)
                       flag = 1
                       break
                   j = j-1
                   

                if(flag == 0):
                    wickets += 1
                    if(playerno1 not in scores):
                        scores[playerno1] = 0
                   # print(i)
                    #scores[playerno1] = score
                

                    playerno1 = max(playerno1,playerno2)+1
                    batsmen[playerno1] = 1
            
    if(balls == 6):
        balls = 0
        #print(scores[playerno1],scores[playerno2])
        playerno1 , playerno2 = swap(playerno1,playerno2)
if(k>11 ):
    
    print(score)
elif(k in scores and batsmen[k] != 0):
    print(scores[k])
else:
    print(-1)



