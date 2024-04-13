#include <iostream>
#include <string>
#include <map>
using namespace std;


void preorder(char node, map<char, pair <char, char>> m) {//preorder
	cout << node; //���� ����� ������ ���
	if (m[node].first != '.') { //���� �ڽ��� �ִٸ�
		preorder(m[node].first, m);
	}
	if (m[node].second != '.') { //������ �ڽ��� �ִٸ�
		preorder(m[node].second, m);
	}
}
void inorder(char node, map<char, pair <char, char>> m) {//inorder
	if (m[node].first != '.') { //���� �ڽ��� �ִٸ�
		inorder(m[node].first,m);
	}
	cout << node; //���� ����� ������ ���
	if (m[node].second != '.') { //������ �ڽ��� �ִٸ�
		inorder(m[node].second,m);
	}
}
void postorder(char node, map<char, pair <char, char>> m) { //postorder
	if (m[node].first != '.') { //���� �ڽ��� �ִٸ�
		postorder(m[node].first,m);
	}
	if (m[node].second != '.') { //������ �ڽ��� �ִٸ�
		postorder(m[node].second,m);
	}
	cout << node; //���� ����� ������ ���
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
