class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        ans = []
        for i in grid:
            for ele in i:
                ans.append(ele)
        print(ans)
        ans.sort()
        print(ans)
        answer = []
        for i in range(len(ans)-1):
            if ans[i]==ans[i+1]:
                answer.append(ans[i])
        for i in range(1,len(ans)+1):
            if i not in ans:
                answer.append(i)
        return answer
        