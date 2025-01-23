#include <iostream>

using namespace std;

int main()
{
	int a1, a2, a3;
	cin >> a1 >> a2 >> a3;

	if ((2 * a2 + 4 * a3) <= (2 * a1 + 2 * a3) and (2 * a2 + 4 * a3) <= (4 * a1 + 2 * a2))
		cout << (2 * a2 + 4 * a3) <<endl;
	else if((2 * a1 + 2 * a3)<= (2 * a2 + 4 * a3)  and (2 * a1 + 2 * a3) <= (4 * a1 + 2 * a2)) 
		cout<<(2 * a1 + 2 * a3)<<endl;
	else cout<<(4 * a1 + 2 * a2)<<endl;

	return 0;
}
