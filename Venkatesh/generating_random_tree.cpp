#include<iostream>
#include<cstdlib>

#include<cmath>
using namespace std;

int main(){
    int n;cin >> n; //number of nodes
    int adj_mat[n+1][n+1];
    for(int i = 0;i <= n;i++){
       for(int j = 0;j <= n;j++){
          adj_mat[i][j] = -1;
       }
    }

    for(int i = 1;i <= n;i++){
        int random = (rand()%n)+1;
        for(int j = 1;j <= random;j++){
            if((j != i)&&(adj_mat[i][j] == -1)){
                for(int k = 1;k <= n;k++){
                  if(adj_mat[i][k] != -1){
                      if(adj_mat[k][j] != -1){
                        adj_mat[i][j] = max((int)ceil(sqrt((adj_mat[i][k]*adj_mat[i][k]) + (adj_mat[k][j]*adj_mat[k][j]))),adj_mat[i][j]);    
                      }
                      else{
                        adj_mat[i][j] = max(rand()%n,adj_mat[i][j]);
                      }
                  }
                  else{
                      adj_mat[i][j] = max(rand()%n,adj_mat[i][j]);
                  }  
                }
            }
            adj_mat[j][i] = adj_mat[i][j];    
        }
    }

    for(int i = 0;i <= n;i++){
        for(int j = 0;j <= n;j++){
             cout << adj_mat[i][j] << " ";
        }
        cout << endl;
    } 
    return 0;
}