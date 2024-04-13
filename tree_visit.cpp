#include <iostream>
#include <string>
#include <map>
using namespace std;


void preorder(char node, map<char, pair <char, char>> m) {//preorder
	cout << node; //현재 노드의 데이터 출력
	if (m[node].first != '.') { //왼쪽 자식이 있다면
		preorder(m[node].first, m);
	}
	if (m[node].second != '.') { //오른쪽 자식이 있다면
		preorder(m[node].second, m);
	}
}
void inorder(char node, map<char, pair <char, char>> m) {//inorder
	if (m[node].first != '.') { //왼쪽 자식이 있다면
		inorder(m[node].first,m);
	}
	cout << node; //현재 노드의 데이터 출력
	if (m[node].second != '.') { //오른쪽 자식이 있다면
		inorder(m[node].second,m);
	}
}
void postorder(char node, map<char, pair <char, char>> m) { //postorder
	if (m[node].first != '.') { //왼쪽 자식이 있다면
		postorder(m[node].first,m);
	}
	if (m[node].second != '.') { //오른쪽 자식이 있다면
		postorder(m[node].second,m);
	}
	cout << node; //현재 노드의 데이터 출력
}
int main() {
	int total_number = 0;
	cin >> total_number;
	map<char, pair <char,char>> tree;

	for (int i = 0; i < total_number; i++)
	{
		char parent, left, right;
		cin >> parent >> left >> right;
		tree[parent] = make_pair(left, right);
	}

	//pre-order
	preorder('A', tree);
	cout << endl;
	//in-order
	inorder('A', tree);
	cout << endl;

	//post-order
	postorder('A', tree);
	cout << endl;

}
