#include <bits/stdc++.h>
using namespace std;
class Team{
    public:
    int ID = 0;
    int GD = 0;//Goal Difference = Goal score - Goal conced
    int PTS = 0;//Point (win = 3, draw = 1, lose = 0)

    //Constructor
    Team(int x, int y, int z) : ID(x), GD(y), PTS(z) {}
   
};

class Scoreboard{
public:
    vector<Team> T;
    int numberOfTeams = 0;
    
    Scoreboard(int n){
        numberOfTeams = n;
        for(int i=0;i<n;i++){
            Team x(i,0,0);
            T.push_back(x);
        
        }
    }

    void match(int ID1, int ID2,int G1,int G2){
        int posid1,posid2 = 0;
        for (int i = 0; i < numberOfTeams; i++){   
            if (T[i].ID == ID1){
                posid1 = i;
            }
            if (T[i].ID == ID2){
                posid2 = i;
            }
        }

        if (G1 > G2) {
            T[posid1].PTS += 3;
            T[posid1].GD += G1 - G2;
            T[posid2].GD -= G1 - G2;
        } else if (G2 > G1){
            T[posid2].PTS += 3;
            T[posid2].GD += G2 - G1;
            T[posid1].GD -= G2 - G1;
        } else {
            T[posid1].PTS += 1;
            T[posid2].PTS += 1;
        }

        for (int i = numberOfTeams-1; i >= 0 ; i--){
            for (int j = 1; j <= i; j++){
                if (T[j-1].PTS < T[j].PTS){
                    Team temp(T[j-1].ID,T[j-1].GD,T[j-1].PTS);
                    T[j-1] = T[j];
                    T[j] = temp;
                }else if(T[j-1].PTS == T[j].PTS){
                    if (T[j-1].GD < T[j].GD){
                        Team temp(T[j-1].ID,T[j-1].GD,T[j-1].PTS);
                        T[j-1] = T[j];
                        T[j] = temp;
                    }else if( T[j-1].GD == T[j].GD && (T[j-1].ID > T[j].ID)){
                        Team temp(T[j-1].ID,T[j-1].GD,T[j-1].PTS);
                        T[j-1] = T[j];
                        T[j] = temp;
                    }     
                }
            }  
        }
    } 

    void showTeamAtRank(int i){
        cout << T[i-1].ID << " ";
        cout << T[i-1].PTS << " ";
        cout << T[i-1].GD << endl;
    }
    
};