#include <bits/stdc++.h>
using namespace std;



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    string course;
    int result = 0;
    int curr_result = 0;
    
    vector<int> key = {};
    map<int,vector<string>> all_course = {};
    map<int,string>::iterator it;
    for(int i = 0; i < n; i++){
        vector<string> stu_course = {};
        key.push_back(i);
        for(int j = 0; j < 5; j++){
            cin >> course;
            stu_course.push_back(course);
        }
        sort(stu_course.begin(),stu_course.end());
        all_course[key[i]] = stu_course;
    }

    map<vector<string>, int> course_co;
    for (const auto& pair : all_course) {
        course_co[pair.second]++;
    }

    int max_co = 0;
    for (const auto& pair : course_co) 
        max_co = max(max_co, pair.second);
    

    if (max_co == 1)
        cout << n;
    else
        cout << max_co;
    

    return 0;

}
