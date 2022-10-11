class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        mon = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mS = dS = mE = dE = 0 
        if int(arriveAlice[:2]) > int(arriveBob[:2]):
            mS = int(arriveAlice[:2])
            dS = int(arriveAlice[3:])
        elif int(arriveAlice[:2]) < int(arriveBob[:2]):
            mS = int(arriveBob[:2])
            dS = int(arriveBob[3:])
        else:
            mS = int(arriveBob[:2])
            dS = int(arriveAlice[3:]) if int(arriveAlice[3:]) >= int(arriveBob[3:]) else int(arriveBob[3:])
            
        
        if int(leaveAlice[:2]) < int(leaveBob[:2]):
            mE = int(leaveAlice[:2])
            dE = int(leaveAlice[3:])
        elif int(leaveAlice[:2]) > int(leaveBob[:2]):
            mE = int(leaveBob[:2])
            dE = int(leaveBob[3:])
        else:
            mE = int(leaveBob[:2])
            dE = int(leaveAlice[3:]) if int(leaveAlice[3:]) <= int(leaveBob[3:]) else int(leaveBob[3:])
        
        print(mS,dS,mE,dE)
        ans = 0
        for i in range(mS,mE+1):
            if mS == mE:
                if dE > dS:
                    ans += dE - dS + 1
                elif dE == dS:
                    ans += 1
            elif i == mS:
                ans += mon[i] - dS + 1
            elif i == mE:
                ans += dE
            else:
                ans += mon[i]
        return ans