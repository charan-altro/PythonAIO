'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given 'n' scores. Store them in a list and find the score of the runner-up.
The first line contains . The second line contains an array A[]  of  integers each separated by a space.'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(set(arr))
    x.sort(reverse=True)
    print(x[1])
