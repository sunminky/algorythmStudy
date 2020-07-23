def cases(arr,cnt,str):
    if cnt == 0:
        print(str.strip())  #좌우 공백 없애기
        return
    for i,e in enumerate(arr):
        cases(arr[i+1:],cnt-1,str+" "+e)    #처음부터 뒤로 가면서 숫자를 조합해나감

store = []
while True:
    inputarr = input()
    inputNum, *nums = inputarr.split()
    if int(inputNum) == 0:
        break
    store.append(nums)

for i,e in enumerate(store):
    cases(e,6,"")
    print()