/*
Programming Challenges
Problem 1.6 The 3n+1 Problem
Solution
*/

#include <iostream>
#include <vector>
using namespace std;

int i = 0, j = 0, mc = 1;

int main() {
  scanf("%d %d", &i, &j);
  for (; i < j; i++) {
    int num = i, cycle = 1;
    while (num > 1) {
      if ((num % 2) == 0) {
        num = num / 2;
      } else {
        num = (num * 3) + 1;
      }
      cycle++;
    }
    mc = max(mc, cycle);
  }
  cout << mc;
}
