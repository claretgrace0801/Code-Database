#include<iostream>

using namespace std;

void merge(int array[],int l, int r);
void mergeSort(int array[], int l, int r);
void printArray(int array[], int len);

int main()
{
    int array[100];
    int n;
    cin>>n;
    for(int i = 0; i<n;i++)
    {
        cin>>array[i];
    }
    mergeSort(array,0,n-1);
    printArray(array, n);
}

void merge(int array[],int l, int r)
{
    int mid = l + (r-l)/2;

    int i = l,j=mid+1,k=0;
    int sortedArray[r-l+10];

    while(i<=mid && j<=r)
    {
        if(array[i] < array[j])
        {
            sortedArray[k++] = array[i++];
        }
        else
        {
            sortedArray[k++] = array[j++];
        }
    }

    while(i<=mid)
    {
        sortedArray[k++] = array[i++];
    }
    while(j<=r)
    {
        sortedArray[k++] = array[j++];
    }

    for(k=0,i=l;i<=r;)
    {
        array[i++] = sortedArray[k++];
    }
}

void mergeSort(int array[], int l, int r)
{
    if(l==r)
    {
        return;
    }
    int mid  = l + (r-l)/2;

    mergeSort(array,l,mid);
    mergeSort(array,mid+1,r);
    merge(array,l,r);
    return;
}

void printArray(int array[], int len)
{
    for(int i = 0; i<len;i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<endl;
}