from collections import defaultdict
def main():
    total_node_number=int(input())
    tree=defaultdict(list)
    for i in range(total_node_number):
        parent_node,left_node,right_node=input().split()
        tree[parent_node].append(left_node)
        tree[parent_node].append(right_node)
    global preorder_list
    global inorder_list
    global postorder_list
    preorder_list=list()
    inorder_list=list()
    postorder_list=list()
    preorder(tree,'A')
    print(preorder_list)
    inorder(tree,'A')
    print(inorder_list)
    postorder(tree,'A')
    print(postorder_list)
    print(tree)

def preorder(tree,node):
    preorder_list.append(node)
    if tree[node][0]!=".":
        preorder(tree,tree[node][0])
    if tree[node][1]!=".":
        preorder(tree,tree[node][1])

def inorder(tree,node):
    if tree[node][0]!=".":
        inorder(tree,tree[node][0])
    inorder_list.append(node)
    if tree[node][1]!=".":
        inorder(tree,tree[node][1])
def postorder(tree,node):
    if tree[node][0]!=".":
        postorder(tree,tree[node][0])
    if tree[node][1]!=".":
        postorder(tree,tree[node][1])
    postorder_list.append(node)


if __name__=="__main__":
    main()
