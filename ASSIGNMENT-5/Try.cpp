#include <bits/stdc++.h>
#include "TreeIndex.h"
using namespace std;


// intialze the static variable
VectorDataset TreeIndex::Space = VectorDataset(0);
int main()
{
    // declare 5 datavectors of size 10 having values between 0 to 1 don't use random do it explicityly
    DataVector data1(10);
    DataVector data2(10);
    DataVector data3(10);
    DataVector data4(10);
    DataVector data5(10);
    data1.AssignVector({0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1});
    data2.AssignVector({0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 0.1});
    data3.AssignVector({0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 0.1, 0.2});
    data4.AssignVector({0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 0.1, 0.2, 0.3});
    data5.AssignVector({0.5, 0.6, 0.7, 0.8, 0.9, 1, 0.1, 0.2, 0.3, 0.4});
    // add all datavector to static member using static assigndataset function
    VectorDataset Dataset(5);
    Dataset.dataset[0]=data1;
    Dataset.dataset[1]=data2;
    Dataset.dataset[2]=data3;
    Dataset.dataset[3]=data4;
    Dataset.dataset[4]=data5;
    TreeIndex::AssignDataset(Dataset);
    cout<<Dataset.getDataset().size()<<endl;
    cout<<TreeIndex::GetDataset().getDataset().size()<<endl;
    // make kd tree
    RPTreeIndex kdTreeIndex = RPTreeIndex::GetInstance();
    kdTreeIndex.AssignIndexes();
    RPTreeIndex *tree = kdTreeIndex.MakeTree();
    // print kd tree
    cout<<"Tree Construceted";
    tree->printRPTreeIndex();
}